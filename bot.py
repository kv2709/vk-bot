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
        print(f"From BOT==self.vk_api_obj=={self.vk_api_obj}")
        self.vk_bot_pollster = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk_api_obj, group_id=GROUP_ID)
        print(f"From BOT==self.vk_bot_pollster=={self.vk_bot_pollster}")
        print(f"From BOT==self.vk_bot_pollster.listen()=={self.vk_bot_pollster.listen()}")
        self.vk_api_get = self.vk_api_obj.get_api()
        print(f"From BOT==self.vk_api_get=={self.vk_api_get}")
        self.weather = WeatherGetter()
        # bsk_str = self.weather.get_current_weather(city_id=NOVOSIBIRSK_ID)
        # print(f"From BOT!!!!!!!!!!!!!!!!{bsk_str}")
        logging.config.dictConfig(log_config)
        self.event_log = logging.getLogger('event')
        self.error_log = logging.getLogger('error_bot')

    def run(self):
        """
        Основной метод класса получающий события от лонгпуллера и вызывающий метод
        self.on_event для их обработки
        """

        for event in self.vk_bot_pollster.listen():
            try:
                self.on_event(event=event)
            except Exception as err:
                self.error_log.error(f'Исключение в обработчике событий: {err} listen {self.vk_bot_pollster.listen()}')
                print(err)

    def on_event(self, event=None):
        """
        Обработчик событий. Реализован стартовый ответ на команду <Начать> с выводом приветствия
        пользоваетля и постановкой клавиатуры с четырьмя кнопками, один эхо-ответ на произвольное
        сообщение от пользователя и четыре обработчика для прогнозов погоды, для которых поставлены кнопки
        :param event: событие, которое обрабатывает метод

        """
        user_id = event.object.message['from_id']
        print(user_id)
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_START:
            print(self.vk_api_get.users.get(user_id=user_id))

            user_info = self.vk_api_get.users.get(user_id=user_id)
            message_from_bot = f"Уважаемый {user_info[0]['first_name']} {user_info[0]['last_name']}. " \
                               f"Вас привествует Бот сообщества <Бото-ферма>. Мой Бот умеет отвечать эхом " \
                               f"на произвольное входящее сообщение, а так же на пересылаемое Вами сообщение " \
                               f"из другого диалога с Вашим комментарием. Из полезной функциональности Бот умеет " \
                               f" показывать прогноз погоды в Бийске и Новосибирске на сегодня и на пять дней"
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=user_id,
                                          message=message_from_bot, keyboard=KEY_BOARD)

            self.event_log.info(msg=f"Пользователь {user_info[0]['first_name']} {user_info[0]['last_name']}"
                                    f" запустил сеанс бота")

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_MENU_ROAD_FORECAST:
            message_from_bot = "Загружено дорожное меню"
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot, keyboard=KEY_BOARD_ROAD)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_RETURN_MAIN_MENU:
            message_from_bot = "Загружено основное меню"
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot, keyboard=KEY_BOARD)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == \
                CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW:
            user_info = self.vk_api_get.users.get(user_id=user_id, name_case='Gen')
            message_from_bot = self.weather.get_current_weather_for_city_list(NOVOSIBIRSK_ID,
                                                                              CHEREPANOVO_ID,
                                                                              TALMENKA_ID,
                                                                              NOVOALTAYSK_ID,
                                                                              NALOBIKHA_ID,
                                                                              TROITSKOYE_ID,
                                                                              BIYSK_ID,
                                                                              )
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot)
            self.event_log.info(msg=f"Выдана погода по трассе Нск-Бск для "
                                    f"{user_info[0]['first_name']} {user_info[0]['last_name']}")

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_BIYSK_WEATHER_NOW:
            message_from_bot = self.weather.get_current_weather(city_id=BIYSK_ID)
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_BIYSK_WEATHER_FORECAST:
            message_from_bot = self.weather.get_forecast(city_id=BIYSK_ID)
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_NOVOSIBIRSK_WEATHER_NOW:
            message_from_bot = self.weather.get_current_weather(city_id=NOVOSIBIRSK_ID)
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.message['text'] == CMD_NOVOSIBIRSK_WEATHER_FORECAST:
            message_from_bot = self.weather.get_forecast(city_id=NOVOSIBIRSK_ID)
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=event.object.message['from_id'],
                                          message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW:
            user_info = self.vk_api_get.users.get(user_id=user_id, name_case='Gen')
            user_name = f"{user_info[0]['first_name']} {user_info[0]['last_name']}"
            message_from_bot = f"Эхо-ответ бота на входящее сообщение <{event.object.message['text']}> от {user_name}"
            if len(event.object.message['fwd_messages']) > 0:
                user_id_reply = abs(event.object.message['fwd_messages'][0]['from_id'])
                user_info_reply = self.vk_api_get.users.get(user_id=user_id_reply, name_case='Gen')
                user_name_reply = f"{user_info_reply[0]['first_name']} {user_info_reply[0]['last_name']}"
                message_from_bot += f", переславшего сообщение <{event.object.message['fwd_messages'][0]['text']}> " \
                                    f"от {user_name_reply}"
            self.vk_api_get.messages.send(random_id=get_random_id(), peer_id=user_id, message=message_from_bot)
            self.event_log.info(msg=f"Выдан эхо-ответ на входящее от "
                                    f"{user_info[0]['first_name']} {user_info[0]['last_name']}")


if __name__ == '__main__':
    logging.config.dictConfig(log_config)
    bot_log = logging.getLogger('bot')
    bot = VKBot()
    bot_log.info(f'Запуск Бота {bot}')
    bot.run()
