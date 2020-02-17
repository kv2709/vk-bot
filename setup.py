# -*- coding: utf-8 -*-

import random
import json
import os

TOKEN_API = os.environ.get('TOKEN_API_HEROKU')
APP_ID = os.environ.get('TOKEN_WEATHER_HEROKU')
# TOKEN_API = "test"
# APP_ID = "test"


CMD_START = 'Начать'
CMD_BIYSK_WEATHER_NOW = "Погода в Бийске сегодня"
CMD_BIYSK_WEATHER_FORECAST = "Прогноз по Бийску на 5дн"
CMD_NOVOSIBIRSK_WEATHER_NOW = "Погода в Нов-ске сегодня"
CMD_NOVOSIBIRSK_WEATHER_FORECAST = "Прогноз по Нов-ску на 5дн"
CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW = "Погода на трассе Бск-Нск"
CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW = "Погода на трассе Бск-ЧТ"
CMD_MENU_ROAD_FORECAST = "Меню погоды по Чуйскому тракту"
CMD_RETURN_MAIN_MENU = "Вернутся в основное меню"


NOVOSIBIRSK_ID = 1496747
CHEREPANOVO_ID = 1508161
TALMENKA_ID = 1490266
NOVOALTAYSK_ID = 1497173
NALOBIKHA_ID = 1498027
TROITSKOYE_ID = 1489209
BIYSK_ID = 1510018

GROUP_ID = 190385197

KEY_BOARD = json.dumps(
                 {"one_time": False,
                  'buttons': [
                              [{"action": {"type": "text",
                                           "label": CMD_BIYSK_WEATHER_NOW
                                           },
                                "color": "primary"
                                },
                               {"action": {"type": "text",
                                           "label": CMD_BIYSK_WEATHER_FORECAST
                                           },
                                "color": "primary"
                                },
                               ],
                              [{"action": {"type": "text",
                                           "label": CMD_NOVOSIBIRSK_WEATHER_NOW
                                           },
                                "color": "primary"
                                },
                               {"action": {"type": "text",
                                           "label": CMD_NOVOSIBIRSK_WEATHER_FORECAST
                                           },
                                "color": "primary"
                                },
                               ],
                              [{"action": {"type": "text",
                                           "label": CMD_MENU_ROAD_FORECAST
                                           },
                                "color": "primary"
                                },
                               ]
                              ]
                  }
                       )

KEY_BOARD_ROAD = json.dumps(
                 {"one_time": False,
                  'buttons': [
                              [{"action": {"type": "text",
                                           "label": CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW
                                           },
                                "color": "primary"
                                },
                               {"action": {"type": "text",
                                          "label": CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW
                                           },
                               "color": "primary"
                                },
                               ],
                              [{"action": {"type": "text",
                                           "label": CMD_RETURN_MAIN_MENU
                                           },
                                "color": "primary"
                                },
                               ]
                              ]
                  }
                       )

KEY_BOARD_EMPTY = json.dumps({"buttons": [],
                              "one_time": True}
                             )


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])


log_config = {
    "version": 1,
    "formatters": {
        "event_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "bot_formatter": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "error_bot_formatter": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    },
    "handlers": {
        "event_handler": {
            "class": "logging.FileHandler",
            "formatter": "event_formatter",
            "filename": "event.log",
            "encoding": "UTF-8",
        },
        "bot_handler": {
            "class": "logging.FileHandler",
            "formatter": "bot_formatter",
            "filename": "bot.log",
            "encoding": "UTF-8",
        },
        "error_bot_handler": {
            "class": "logging.FileHandler",
            "formatter": "error_bot_formatter",
            "filename": "error_bot.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "event": {
            "handlers": ["event_handler"],
            "level": "DEBUG",
        },
        "bot": {
            "handlers": ["bot_handler"],
            "level": "INFO",
        },
        "error_bot": {
            "handlers": ["error_bot_handler"],
            "level": "ERROR",
        },
    },
}


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
  'object': {'message': {'date': 1578040300, 
                         'from_id': 77209884, 
                         'id': 143, 
                         'out': 0, 
                         'peer_id': 77209884, 
                         'text': 'Начать', 
                         'conversation_message_id': 133, 
                         'fwd_messages': [], 
                         'important': False, 
                         'random_id': 0, 
                         'attachments': [], 
                         'payload': '{"command":"start"}', 
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
  'event_id': 'ac2e1a246bc6df35aa61a84b87fc47c3f67072d1'
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
             'is_hidden': False
             }, 
  'group_id': 190385197, 
  'event_id': 'c45f49d7dbdfc2e72d99d7e7d320e49722120543'
 }

VkBotEventType.MESSAGE_REPLY 
 class 'vk_api.bot_longpoll.VkBotMessageEvent'
 {'type': 'message_reply', 
  'object': {'date': 1578033195, 
             'from_id': -190385197, 
             'id': 132, 
             'out': 1, 
             'peer_id': 77209884, 
             'text': 'Ответ бота на VkBotEventType.MESSAGE_NEW <тест сообщения> от Юрия Киреева', 
             'conversation_message_id': 122, 
             'fwd_messages': [], 
             'important': False, 
             'random_id': 1602631776, 
             'attachments': [], 
             'is_hidden': False
             }, 
  'group_id': 190385197, 
  'event_id': 'a4a69ef41abea2b198ad4139aeb7b877461d8659'
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
