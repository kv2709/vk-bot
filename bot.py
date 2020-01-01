# -*- coding: utf-8 -*-

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from setup import TOKEN_API, GROUP_ID, get_random_id


class VKBot:
    def __init__(self, token='', group_id=0):
        self.token = token
        self.group_id = group_id
        self.vk_api_obj = vk_api.VkApi(token=self.token)
        self.vk_bot_pollster = VkBotLongPoll(vk=self.vk_api_obj, group_id=self.group_id)
        self.vk_api = self.vk_api_obj.get_api()

    def run(self):
        for event in self.vk_bot_pollster.listen():
            try:
                self.on_event(event=event)
            except Exception as err:
                print(err)

    def on_event(self, event=None):
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.type, '\n', event)
            user_id = event.obj.message['from_id']
            user_info = self.vk_api.users.get(user_id=user_id, name_case='Gen')
            user_name = f"{user_info[0]['first_name']} {user_info[0]['last_name']}"
            print(f"Новое сообщение {event.obj.message['text']} от {user_name}")
            message_from_bot = f"Ответ бота на входящее сообщение <{event.obj.message['text']}> от {user_name}"
            if len(event.obj.message['fwd_messages']) > 0:
                user_id_reply = event.obj.message['fwd_messages'][0]['from_id']
                user_info_reply = self.vk_api.users.get(user_id=user_id_reply, name_case='Gen')
                user_name_reply = f"{user_info_reply[0]['first_name']} {user_info_reply[0]['last_name']}"
                message_from_bot += f", переславшего сообщение <{event.obj.message['fwd_messages'][0]['text']}> от {user_name_reply}"
            self.vk_api.messages.send(random_id=get_random_id(), peer_id=user_id, message=message_from_bot)
        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print(event.type, '\n', event)
        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print(event.type, '\n', event)
        else:
            print(event.type, '\n', event)


if __name__ == '__main__':
    bot = VKBot(token=TOKEN_API, group_id=GROUP_ID)
    bot.run()
