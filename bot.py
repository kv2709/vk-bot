# -*- coding: utf-8 -*-
import sys

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from generate_ticket import generate_ticket
from weather_request import WeatherGetter
from setup import *
import logging.config
import handlers


class UserState:
    """
    Состояние пользователя внутри сценария
    """
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class VKBot:
    """
    Класс бота, обрабатывающий события, полученные в результате
    прослушивания ответов от сервера ВК на LongPoll запросы
    """

    def __init__(self):
        """
        Инициализация объекта класса
        TOKEN_API: Токен доступа к АПИ ВК, полученный из переменной окружения Heroku
                   Определен в модуле setup
        GROUP_ID: номер сообщества бота. Определен в модуле setup
        """
        self.vk_api_obj = vk_api.VkApi(token=TOKEN_API)
        self.vk_bot_pollster = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk_api_obj, group_id=GROUP_ID)
        self.vk_api_get = self.vk_api_obj.get_api()
        self.weather = WeatherGetter()
        logging.config.dictConfig(log_config)
        self.event_log_http = logging.getLogger('event_http')
        self.error_log = logging.getLogger('error_bot')
        self.message_from_bot = None
        self.message_send_exec_code = None
        self.log_send_status_code = None
        self.user_info = None
        self.user_id = None
        self.event = None
        self.status_bot_sing_up_conf = False
        self.user_states = dict()

        self.execute_command_dict = {
            CMD_NO_COMMAND: self.no_command,
            CMD_START: self.cmd_start,
            CMD_MENU_ROAD_FORECAST: self.cmd_menu_road_forecast,
            CMD_RETURN_MAIN_MENU: self.cmd_return_main_menu,
            CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW: self.cmd_biysk_novosibirsk_road_weather_now,
            CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW: self.cmd_biysk_kosh_agach_road_weather_now,
            CMD_BIYSK_WEATHER_NOW: self.cmd_biysk_weather_now,
            CMD_BIYSK_WEATHER_FORECAST: self.cmd_biysk_weather_forecast,
            CMD_NOVOSIBIRSK_WEATHER_NOW: self.cmd_novosibirsk_weather_now,
            CMD_NOVOSIBIRSK_WEATHER_FORECAST: self.cmd_novosibirsk_weather_forecast,
            CMD_SIGN_UP_FOR_CONFERENCE: self.cmd_sign_up_for_conference,
                                    }
        self.event_log_http.debug(msg=f"Произведен запуск бота {self.__class__}")

    def cmd_start(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Nom')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        self.message_from_bot = f"Уважаемый(ая) {first_last_name}. " \
                                f"Вас привествует Бот сообщества <Бото-ферма>. Мой Бот умеет отвечать эхом " \
                                f"на произвольное входящее сообщение, а так же на пересылаемое Вами сообщение " \
                                f"из другого диалога с Вашим комментарием. Из полезной функциональности Бот умеет " \
                                f" показывать прогноз погоды в Бийске и Новосибирске на сегодня и на пять дней"

        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD)

        self.log_send_status_code = self.event_log_http.handlers[0].status_code_request
        self.event_log_http.debug(msg=f"Пользователь {first_last_name} запустил новый сеанс бота. "
                                      f"Отправка сообщения завершена с кодом "
                                      f"{self.message_send_exec_code}")

    def no_command(self):
        if not self.status_bot_sing_up_conf:
            self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Gen')
            first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
            self.message_from_bot = f"Эхо-ответ бота на входящее сообщение " \
                                    f"<{self.event.object.message['text']}> от {first_last_name}"
            if len(self.event.object.message['fwd_messages']) > 0:
                user_id_reply = abs(self.event.object.message['fwd_messages'][0]['from_id'])
                user_info_reply = self.vk_api_get.users.get(user_id=user_id_reply, name_case='Gen')
                first_last_name_reply = f"{user_info_reply[0]['first_name']} {user_info_reply[0]['last_name']}"
                self.message_from_bot += f", переславшего сообщение " \
                                         f"<{self.event.object.message['fwd_messages'][0]['text']}> " \
                                         f"от {first_last_name_reply}"
            self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                        peer_id=self.user_id,
                                                                        message=self.message_from_bot,
                                                                        keyboard=KEY_BOARD)
            self.event_log_http.debug(msg=f"Выдан эхо-ответ на входящее "
                                          f"<{self.event.object.message['text']}> от "
                                          f"{first_last_name}. "
                                          f"Отправка сообщения завершена с кодом "
                                          f"{self.message_send_exec_code}")
            self.log_send_status_code = self.event_log_http.handlers[0].status_code_request
            if self.log_send_status_code != 200:
                self.error_log.error(msg=f"Запись лога в БД не произведена! Статус код {self.log_send_status_code}")
        else:
            self.cmd_sign_up_for_conference()

    def cmd_menu_road_forecast(self):
        self.message_from_bot = "Загружено дорожное меню"
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD_ROAD)

    def cmd_return_main_menu(self):
        self.status_bot_sing_up_conf = False
        self.message_from_bot = "Загружено основное меню"
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_biysk_novosibirsk_road_weather_now(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Gen')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        self.message_from_bot = self.weather.get_current_weather_for_city_list(NOVOSIBIRSK_ID,
                                                                               CHEREPANOVO_ID,
                                                                               TALMENKA_ID,
                                                                               NOVOALTAYSK_ID,
                                                                               NALOBIKHA_ID,
                                                                               TROITSKOYE_ID,
                                                                               BIYSK_ID,
                                                                               )
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD_ROAD)
        self.event_log_http.debug(msg=f"Выдана погода по трассе Нск-Бск для "
                                      f"{first_last_name}. "
                                      f"Отправка сообщения завершена с кодом "
                                      f"{self.message_send_exec_code}")

    def cmd_biysk_kosh_agach_road_weather_now(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Gen')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        self.message_from_bot = 'Функция в разработке'
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD_ROAD)
        self.event_log_http.debug(msg=f"Функция в разработке: погода по трассе Бск-Кош-Агач для "
                                      f"{first_last_name}. "
                                      f"Отправка сообщения завершена с кодом "
                                      f"{self.message_send_exec_code}")

    def cmd_biysk_weather_now(self):
        self.message_from_bot = self.weather.get_current_weather(city_id=BIYSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_biysk_weather_forecast(self):
        self.message_from_bot = self.weather.get_forecast(city_id=BIYSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_novosibirsk_weather_now(self):
        self.message_from_bot = self.weather.get_current_weather(city_id=NOVOSIBIRSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_novosibirsk_weather_forecast(self):
        self.message_from_bot = self.weather.get_forecast(city_id=NOVOSIBIRSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=self.message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_sign_up_for_conference(self):

        if not self.status_bot_sing_up_conf:
            self.status_bot_sing_up_conf = True
            self.message_from_bot = "Бот переключен в режим <Регистрация на конференцию>"
            self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                        peer_id=self.user_id,
                                                                        message=self.message_from_bot,
                                                                        keyboard=KEY_BOARD_RETURN_MAIN_MENU)
        else:
            text_from_user = self.event.object.message['text']
            # Получили текст от пользователя, знаем его self.user_id
            # пошли в базу за за поиском там записи для него и
            # если она найдена, то берем оттуда остальные значения для self.user_states[self.user_id]
            request_result = requests.get(url=URL_API_DB_USER_STATE + str(self.user_id))
            response = request_result.json()
            # заменяем if на проверку наличия в БД записи про этого user_id
            if "user_id" in response:
                self.user_states[self.user_id].scenario_name = response["scenario_name"]
                self.user_states[self.user_id].step_name = response["step_name"]
                self.user_states[self.user_id].context = response["context"]
                self.message_from_bot = self.continue_scenario(text=text_from_user)
            else:
                # search intent
                for intent in INTENTS:
                    if any(token in text_from_user.lower() for token in intent['token']):
                        # run intent
                        if intent['answer']:
                            self.message_from_bot = intent['answer']
                        else:
                            # не найдя ответа уходим в сценарий - запускаем новый сценарий, добавив в БД новую запись
                            self.message_from_bot = self.start_scenario(scenario_name=intent['scenario'])
                        break
                else:
                    self.message_from_bot = DEFAULT_ANSWER
            self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                        peer_id=self.user_id,
                                                                        message=self.message_from_bot,
                                                                        keyboard=KEY_BOARD_RETURN_MAIN_MENU)

    def start_scenario(self, scenario_name):
        scenario = SCENARIO[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        # Заносим в базу новую запись для данного user_id
        self.user_states[self.user_id] = UserState(scenario_name=scenario_name, step_name=first_step, context={})
        dict_for_send = {'user_id': str(self.user_id),
                         'scenario_name': self.user_states[self.user_id].scenario_name,
                         'step_name': self.user_states[self.user_id].step_name,
                         'context': self.user_states[self.user_id].context
                         }
        request_result = requests.post(url=URL_API_DB_USER_STATE,
                                       data=json.dumps(dict_for_send),
                                       headers={"Content-type": "application/json"})
        return text_to_send

    def continue_scenario(self, text):
        state = self.user_states[self.user_id]
        steps = SCENARIO[state.scenario_name]["steps"]
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                # swith next step
                state.step_name = step['next_step']
                # Обновляем запись user_state в базе
                dict_for_send = {'user_id': str(self.user_id),
                                 'scenario_name': self.user_states[self.user_id].scenario_name,
                                 'step_name': self.user_states[self.user_id].step_name,
                                 'context': self.user_states[self.user_id].context
                                 }
                request_result = requests.put(url=URL_API_DB_USER_STATE + str(self.user_id),
                                              data=json.dumps(dict_for_send),
                                              headers={"Content-type": "application/json"})
            else:
                # finish scenario
                self.event_log_http.info(msg="Зарегистрирован: {name} с адресом {email}".format(**state.context))

                dict_for_send = {"name": state.context["name"], "email": state.context["email"]}
                # Заносим запись о новом зарегистрированном пользователе в таблицу registrationuser
                request_result = requests.post(url=URL_API_DB_USER_REGISTRATION,
                                               data=json.dumps(dict_for_send),
                                               headers={"Content-type": "application/json"})
                print(request_result.json())

                self.user_states.pop(self.user_id)
                # Удаляем запись о пользователе из таблицы userstate
                request_result = requests.delete(url=URL_API_DB_USER_STATE + str(self.user_id))

                # Отправляем заполннный бланк билета
                # Отсюда на Хероку не работает generate_ticket и send_ticket_image
                tk_image = generate_ticket(name=state.context["name"],
                                           email=state.context["email"])

                print("tk_image====>>>", tk_image)
                self.send_ticket_image(ticket_image=tk_image)

        else:
            # retry current step
            text_to_send = step['failure_text'].format(**state.context)
        return text_to_send

    def send_ticket_image(self, ticket_image):
        upload_url = self.vk_api_get.photos.getMessagesUploadServer()['upload_url']
        print("upload_url====>>>", upload_url)
        upload_data = requests.post(url=upload_url, files={'photo': ('image.png', ticket_image, 'image/png')}).json()
        print("upload_data====>>>", upload_data)
        image_data = self.vk_api_get.photos.saveMessagesPhoto(**upload_data)
        owner_id = image_data[0]['owner_id']
        media_id = image_data[0]['id']
        attachment = f"photo{owner_id}_{media_id}"
        print("attachment====>>>", attachment)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    attachment=attachment,
                                                                    keyboard=KEY_BOARD_RETURN_MAIN_MENU)

    def run(self):
        """
        Основной метод класса получающий события от лонгпуллера и вызывающий метод
        self.on_event для их обработки
        """

        for self.event in self.vk_bot_pollster.listen():
            try:
                if self.event.type == VkBotEventType.MESSAGE_NEW:
                    self.on_event_from_dict()
            except Exception as err:
                self.error_log.error(f'Исключение в обработчике событий: {err} тип события {self.event.type}')

    def on_event_from_dict(self):
        self.user_id = self.event.object.message['from_id']
        command_event = self.event.object.message['text']
        if command_event in self.execute_command_dict:
            self.execute_command_dict[command_event]()
        else:
            self.no_command()


if __name__ == '__main__':
    bot = VKBot()
    bot.run()
