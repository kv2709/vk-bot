# -*- coding: utf-8 -*-

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from weather_request import WeatherGetter
from setup import *
import logging.config


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
        self.event_log = logging.getLogger('event')
        self.error_log = logging.getLogger('error_bot')
        self.message_send_exec_code = None
        self.user_info = None
        self.user_id = None
        self.event = None
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


                                    }

    def cmd_start(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Nom')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        message_from_bot = f"Уважаемый(ая) {first_last_name}. " \
                           f"Вас привествует Бот сообщества <Бото-ферма>. Мой Бот умеет отвечать эхом " \
                           f"на произвольное входящее сообщение, а так же на пересылаемое Вами сообщение " \
                           f"из другого диалога с Вашим комментарием. Из полезной функциональности Бот умеет " \
                           f" показывать прогноз погоды в Бийске и Новосибирске на сегодня и на пять дней"

        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)

        self.event_log.info(msg=f"Пользователь {first_last_name} запустил новый сеанс бота"
                                f"Отправка сообщения завершена с кодом "
                                f"{self.message_send_exec_code}")

    def no_command(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Gen')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        message_from_bot = f"Эхо-ответ бота на входящее сообщение " \
                           f"<{self.event.object.message['text']}> от {first_last_name}"
        if len(self.event.object.message['fwd_messages']) > 0:
            user_id_reply = abs(self.event.object.message['fwd_messages'][0]['from_id'])
            user_info_reply = self.vk_api_get.users.get(user_id=user_id_reply, name_case='Gen')
            first_last_name_reply = f"{user_info_reply[0]['first_name']} {user_info_reply[0]['last_name']}"
            message_from_bot += f", переславшего сообщение <{self.event.object.message['fwd_messages'][0]['text']}> " \
                                f"от {first_last_name_reply}"
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)
        self.event_log.info(msg=f"Выдан эхо-ответ на входящее от "
                                f"{first_last_name} "
                                f"Отправка сообщения завершена с кодом "
                                f"{self.message_send_exec_code}")

    def cmd_menu_road_forecast(self):
        message_from_bot = "Загружено дорожное меню"
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD_ROAD)

    def cmd_return_main_menu(self):
        message_from_bot = "Загружено основное меню"
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_biysk_novosibirsk_road_weather_now(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Gen')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        message_from_bot = self.weather.get_current_weather_for_city_list(NOVOSIBIRSK_ID,
                                                                          CHEREPANOVO_ID,
                                                                          TALMENKA_ID,
                                                                          NOVOALTAYSK_ID,
                                                                          NALOBIKHA_ID,
                                                                          TROITSKOYE_ID,
                                                                          BIYSK_ID,
                                                                          )
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD_ROAD)
        self.event_log.info(msg=f"Выдана погода по трассе Нск-Бск для "
                                f"{first_last_name} "
                                f"Отправка сообщения завершена с кодом "
                                f"{self.message_send_exec_code}")

    def cmd_biysk_kosh_agach_road_weather_now(self):
        self.user_info = self.vk_api_get.users.get(user_id=self.user_id, name_case='Gen')
        first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
        message_from_bot = 'Функция в разработке'
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD_ROAD)
        self.event_log.info(msg=f"Функция в разработке: погода по трассе Бск-Кош-Агач для "
                                f"{first_last_name} "
                                f"Отправка сообщения завершена с кодом "
                                f"{self.message_send_exec_code}")

    def cmd_biysk_weather_now(self):
        message_from_bot = self.weather.get_current_weather(city_id=BIYSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_biysk_weather_forecast(self):
        message_from_bot = self.weather.get_forecast(city_id=BIYSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_novosibirsk_weather_now(self):
        message_from_bot = self.weather.get_current_weather(city_id=NOVOSIBIRSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def cmd_novosibirsk_weather_forecast(self):
        message_from_bot = self.weather.get_forecast(city_id=NOVOSIBIRSK_ID)
        self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
                                                                    peer_id=self.user_id,
                                                                    message=message_from_bot,
                                                                    keyboard=KEY_BOARD)

    def run(self):
        """
        Основной метод класса получающий события от лонгпуллера и вызывающий метод
        self.on_event для их обработки
        """

        for event in self.vk_bot_pollster.listen():
            try:
                if event.type == VkBotEventType.MESSAGE_NEW:
                    self.on_event_from_dict(event=event)
            except Exception as err:
                self.error_log.error(f'Исключение в обработчике событий: {err} тип события {event.type}')

    def on_event_from_dict(self, event=None):
        self.event = event
        command_event = self.event.object.message['text']
        if command_event not in CMD_LST:
            command_event = CMD_NO_COMMAND
        self.user_id = self.event.object.message['from_id']
        self.execute_command_dict[command_event]()

    # def on_event(self, event=None):
    #     """
    #     Обработчик событий. Реализован стартовый ответ на команду <Начать> с выводом приветствия
    #     пользоваетля и постановкой клавиатуры с четырьмя кнопками, один эхо-ответ на произвольное
    #     сообщение от пользователя и четыре обработчика для прогнозов погоды, для которых поставлены кнопки
    #     :param event: событие, которое обрабатывает метод
    #
    #     """
    #
    #     if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_START:
    #         user_id = event.object.message['from_id']
    #         self.user_info = self.vk_api_get.users.get(user_id=user_id, name_case='Nom')
    #         first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
    #         message_from_bot = f"Уважаемый(ая) {first_last_name}. " \
    #                            f"Вас привествует Бот сообщества <Бото-ферма>. Мой Бот умеет отвечать эхом " \
    #                            f"на произвольное входящее сообщение, а так же на пересылаемое Вами сообщение " \
    #                            f"из другого диалога с Вашим комментарием. Из полезной функциональности Бот умеет " \
    #                            f" показывать прогноз погоды в Бийске и Новосибирске на сегодня и на пять дней"
    #
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=user_id,
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #
    #         self.event_log.info(msg=f"Пользователь {first_last_name} запустил новый сеанс бота"
    #                                 f"Отправка сообщения завершена с кодом "
    #                                 f"{self.message_send_exec_code}")
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_MENU_ROAD_FORECAST:
    #         message_from_bot = "Загружено дорожное меню"
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD_ROAD)
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_RETURN_MAIN_MENU:
    #         message_from_bot = "Загружено основное меню"
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == \
    #             CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW:
    #         user_id = event.object.message['from_id']
    #         self.user_info = self.vk_api_get.users.get(user_id=user_id, name_case='Gen')
    #         first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
    #         message_from_bot = self.weather.get_current_weather_for_city_list(NOVOSIBIRSK_ID,
    #                                                                           CHEREPANOVO_ID,
    #                                                                           TALMENKA_ID,
    #                                                                           NOVOALTAYSK_ID,
    #                                                                           NALOBIKHA_ID,
    #                                                                           TROITSKOYE_ID,
    #                                                                           BIYSK_ID,
    #                                                                           )
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD_ROAD)
    #         self.event_log.info(msg=f"Выдана погода по трассе Нск-Бск для "
    #                                 f"{first_last_name} "
    #                                 f"Отправка сообщения завершена с кодом "
    #                                 f"{self.message_send_exec_code}")
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == \
    #             CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW:
    #         user_id = event.object.message['from_id']
    #         self.user_info = self.vk_api_get.users.get(user_id=user_id, name_case='Gen')
    #         first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
    #         message_from_bot = 'Функция в разработке'
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD_ROAD)
    #         self.event_log.info(msg=f"Функция в разработке: погода по трассе Бск-Кош-Агач для "
    #                                 f"{first_last_name} "
    #                                 f"Отправка сообщения завершена с кодом "
    #                                 f"{self.message_send_exec_code}")
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_BIYSK_WEATHER_NOW:
    #         message_from_bot = self.weather.get_current_weather(city_id=BIYSK_ID)
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_BIYSK_WEATHER_FORECAST:
    #         message_from_bot = self.weather.get_forecast(city_id=BIYSK_ID)
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_NOVOSIBIRSK_WEATHER_NOW:
    #         message_from_bot = self.weather.get_current_weather(city_id=NOVOSIBIRSK_ID)
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW and \
    #             event.object.message['text'] == CMD_NOVOSIBIRSK_WEATHER_FORECAST:
    #         message_from_bot = self.weather.get_forecast(city_id=NOVOSIBIRSK_ID)
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=event.object.message['from_id'],
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #
    #     elif event.type == VkBotEventType.MESSAGE_NEW:
    #         user_id = event.object.message['from_id']
    #         self.user_info = self.vk_api_get.users.get(user_id=user_id, name_case='Gen')
    #         first_last_name = f"{self.user_info[0]['first_name']} {self.user_info[0]['last_name']}"
    #         message_from_bot = f"Эхо-ответ бота на входящее сообщение " \
    #                            f"<{event.object.message['text']}> от {first_last_name}"
    #         if len(event.object.message['fwd_messages']) > 0:
    #             user_id_reply = abs(event.object.message['fwd_messages'][0]['from_id'])
    #             user_info_reply = self.vk_api_get.users.get(user_id=user_id_reply, name_case='Gen')
    #             first_last_name_reply = f"{user_info_reply[0]['first_name']} {user_info_reply[0]['last_name']}"
    #             message_from_bot += f", переславшего сообщение <{event.object.message['fwd_messages'][0]['text']}> " \
    #                                 f"от {first_last_name_reply}"
    #         self.message_send_exec_code = self.vk_api_get.messages.send(random_id=get_random_id(),
    #                                                                     peer_id=user_id,
    #                                                                     message=message_from_bot,
    #                                                                     keyboard=KEY_BOARD)
    #         self.event_log.info(msg=f"Выдан эхо-ответ на входящее от "
    #                                 f"{first_last_name} "
    #                                 f"Отправка сообщения завершена с кодом "
    #                                 f"{self.message_send_exec_code}")
    #
    #     else:
    #         pass


if __name__ == '__main__':
    logging.config.dictConfig(log_config)
    bot_log = logging.getLogger('bot')
    bot = VKBot()
    bot_log.info(f'Запуск Бота {bot}')
    bot.run()
