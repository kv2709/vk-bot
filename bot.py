# -*- coding: utf-8 -*-

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from setup import TOKEN_API, GROUP_ID, KEY_BOARD, get_random_id
from weather_request import WeatherGetter


class VKBot:
    def __init__(self, token='', group_id=0):
        self.token = token
        self.group_id = group_id
        self.vk_api_obj = vk_api.VkApi(token=self.token)
        self.vk_bot_pollster = VkBotLongPoll(vk=self.vk_api_obj, group_id=self.group_id)
        self.vk_api = self.vk_api_obj.get_api()
        self.weather = WeatherGetter()

    def run(self):
        for event in self.vk_bot_pollster.listen():
            try:
                self.on_event(event=event)
            except Exception as err:
                print(err)

    def on_event(self, event=None):
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Начать':
            user_id = event.obj.message['from_id']
            user_info = self.vk_api.users.get(user_id=user_id)
            message_from_bot = f"Уважаемый {user_info[0]['first_name']} {user_info[0]['last_name']}. " \
                               f"Вас привествует Бот сообщества <Бото-ферма>. Мой Бот умеет отвечать эхом " \
                               f"на произвольное входящее сообщение, а так же на пересылаемое Вами сообщение " \
                               f"из другого диалога с Вашим комментарием. Из полезной функциональности Бот умеет " \
                               f" показывать прогноз погоды в Бийске и Новосибирске на сегодня и на пять дней"
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=user_id, message=message_from_bot, keyboard=KEY_BOARD)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == "Погода в Бийске сегодня":
            message_from_bot = self.weather.get_current_weather(city_id=1510018)
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=event.obj.message['from_id'], message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == "Прогноз по Бийску на 5дн":
            message_from_bot = self.weather.get_forecast(city_id=1510018)
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=event.obj.message['from_id'], message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == "Погода в Нов-ске сегодня":
            message_from_bot = self.weather.get_current_weather(city_id=1496747)
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=event.obj.message['from_id'], message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == "Прогноз по Нов-ску на 5дн":
            message_from_bot = self.weather.get_forecast(city_id=1496747)
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=event.obj.message['from_id'], message=message_from_bot)

        elif event.type == VkBotEventType.MESSAGE_NEW:
            # print(event.type, '\n', event)
            user_id = event.obj.message['from_id']
            user_info = self.vk_api.users.get(user_id=user_id, name_case='Gen')
            user_name = f"{user_info[0]['first_name']} {user_info[0]['last_name']}"
            # print(f"VkBotEventType.MESSAGE_NEW {event.obj.message['text']} от {user_name}")
            message_from_bot = f"Ответ бота на VkBotEventType.MESSAGE_NEW <{event.obj.message['text']}> от {user_name}"
            if len(event.obj.message['fwd_messages']) > 0:
                user_id_reply = abs(event.obj.message['fwd_messages'][0]['from_id'])
                user_info_reply = self.vk_api.users.get(user_id=user_id_reply, name_case='Gen')
                user_name_reply = f"{user_info_reply[0]['first_name']} {user_info_reply[0]['last_name']}"
                # print(f"fwd_messages {event.obj.message['fwd_messages'][0]['text']}> от {user_name_reply}")
                message_from_bot += f", переславшего сообщение <{event.obj.message['fwd_messages'][0]['text']}> от {user_name_reply}"
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=user_id, message=message_from_bot)
        # elif event.type == VkBotEventType.MESSAGE_REPLY:
        #     print(event.type, '\n', event)
        #     user_id = event.object['peer_id']
        #     user_info = self.vk_api.users.get(user_id=user_id, name_case='Gen')
        #     user_name = f"{user_info[0]['first_name']} {user_info[0]['last_name']}"
        #     print(f"VkBotEventType.MESSAGE_REPLY Бот отправил сообщение {event.object['text']} для {user_name}")
        # elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
        #     print(event.type, '\n', event)
        # else:
        #     print('Another Event ', event.type, '\n', event)


if __name__ == '__main__':
    bot = VKBot(token=TOKEN_API, group_id=GROUP_ID)
    bot.run()
