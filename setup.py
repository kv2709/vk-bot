# -*- coding: utf-8 -*-
# heroku ps:scale worker=1
import random

TOKEN_API = '329cff0dfbb52cda1f3f64a65d9a08cba6313e424121bc94347b4765dc8f65cbdc0dce00d17bd60379ea5'
GROUP_ID = 190385197


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])

"""
VkBotEventType.MESSAGE_TYPING_STATE 
 class 'vk_api.bot_longpoll.VkBotEvent'
 {'type': 'message_typing_state', 
  'object': {'state': 'typing', 
             'from_id': 77209884, 
             'to_id': -190385197
             }, 
  'group_id': 190385197, 
  'event_id': '0f5de9b1aac5acb5e1365ad387890c2ed24efd77'
  }
  
VkBotEventType.MESSAGE_NEW 
 class 'vk_api.bot_longpoll.VkBotMessageEvent'
 {'type': 'message_new', 
  'object': {'message': {'date': 1577855040, 
                         'from_id': 77209884, 
                         'id': 75, 
                         'out': 0, 
                         'peer_id': 77209884, 
                         'text': 'Проверка бота', 
                         'conversation_message_id': 75, 
                         'fwd_messages': [], 
                         'important': False, 
                         'random_id': 0, 
                         'attachments': [], 
                         'is_hidden': False
                         }, 
             'client_info': {'button_actions': ['text', 
                                                'vkpay', 
                                                'open_app', 
                                                'location', 
                                                'open_link'
                                                ], 
                             'keyboard': True, 
                             'inline_keyboard': True, 
                             'lang_id': 0
                             }
             }, 
  'group_id': 190385197, 
  'event_id': 'fe6c51bb2c55b921431fc0fee81f872a11095246'
 }
Новое сообщение Проверка бота от Юрия Киреева



VkBotEventType.MESSAGE_REPLY 
 class 'vk_api.bot_longpoll.VkBotMessageEvent'
 {'type': 'message_reply', 
  'object': {'date': 1577855041, 
             'from_id': -190385197, 
             'id': 76, 
             'out': 1, 
             'peer_id': 77209884, 
             'text': 'Ответ бота на входящее сообщение <Проверка бота от Юрия Киреева>', 
             'conversation_message_id': 76, 
             'fwd_messages': [], 
             'important': False, 
             'random_id': 1486284936, 
             'attachments': [], 
             'is_hidden': False}, 
             'group_id': 190385197, 
             'event_id': 'c45f49d7dbdfc2e72d99d7e7d320e49722120543'
             }



VkBotEventType.MESSAGE_MESSAGE_REPLY 
 class 'vk_api.bot_longpoll.VkBotMessageEvent'
 {'type': 'message_new', 
  'object': {'message': {'date': 1577815585, 
                         'from_id': 77209884, 
                         'id': 43, 
                         'out': 0, 
                         'peer_id': 77209884, 
                         'text': '', 
                         'conversation_message_id': 43, 
                         'fwd_messages': [{'date': 1490793686, 
                                          'from_id': 88625640, 
                                          'text': 'спасибо)', 
                                          'attachments': [], 
                                          'conversation_message_id': 9
                                          }], 
                         'important': False, 
                         'random_id': 0, 
                         'attachments': [], 
                         'is_hidden': False
                         }, 
             'client_info': {'button_actions': ['text', 
                                               'vkpay', 
                                               'open_app', 
                                               'location', 
                                               'open_link'
                                               ], 
                            'keyboard': True, 
                            'inline_keyboard': True, 
                            'lang_id': 0
                            }
            }, 
   'group_id': 190385197, 
   'event_id': '2ad42ccc5d34d70fe742b3f395aa64475307fe17'
  }
"""