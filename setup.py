# -*- coding: utf-8 -*-

import random
import os
import json
import logging
import time
import requests


TOKEN_API = os.environ.get('TOKEN_API_HEROKU')
APP_ID = os.environ.get('TOKEN_WEATHER_HEROKU')

CMD_NO_COMMAND = None
CMD_START = 'Начать'
CMD_BIYSK_WEATHER_NOW = "Погода в Бийске сегодня"
CMD_BIYSK_WEATHER_FORECAST = "Прогноз по Бийску на 5дн"
CMD_NOVOSIBIRSK_WEATHER_NOW = "Погода в Нов-ске сегодня"
CMD_NOVOSIBIRSK_WEATHER_FORECAST = "Прогноз по Нов-ску на 5дн"
CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW = "Погода на трассе Бск-Нск"
CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW = "Погода на трассе Бск-ЧТ"
CMD_MENU_ROAD_FORECAST = "Меню погоды по Чуйскому тракту"
CMD_RETURN_MAIN_MENU = "Вернутся в основное меню"

CMD_LST = [CMD_NO_COMMAND,
           CMD_START,
           CMD_BIYSK_WEATHER_NOW,
           CMD_BIYSK_WEATHER_FORECAST,
           CMD_NOVOSIBIRSK_WEATHER_NOW,
           CMD_NOVOSIBIRSK_WEATHER_FORECAST,
           CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW,
           CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW,
           CMD_MENU_ROAD_FORECAST,
           CMD_RETURN_MAIN_MENU]


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


class HTTPHandlerDB(logging.Handler):

    def __init__(self):
        super().__init__()
        self.content_request = None
        self.status_code_request = None

    def emit(self, record):
        date_fmt = '%d-%m-%Y %H:%M:%S'
        time_created_log = time.strftime(date_fmt, time.localtime(record.created))
        url = 'https://db-for-logging-vkbot.herokuapp.com/api/log/'
        dict_for_send = {'time_created': time_created_log,
                         'logger_name': record.name,
                         'level_name': record.levelname,
                         'file_name': record.filename,
                         'func_name': record.funcName,
                         'line_number': str(record.lineno),
                         'msg': record.msg}
        request_result = requests.post(url=url,
                                       data=json.dumps(dict_for_send),
                                       headers={"Content-type": "application/json"})
        self.content_request = request_result.content
        self.status_code_request = request_result.status_code
        return self.content_request


log_config = {
    "version": 1,
    "formatters": {
        "event_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "bot_formatter": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "error_bot_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    },
    "handlers": {
        "event_http_handler": {
            "class": "setup.HTTPHandlerDB",
        },
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
        "event_http": {
            "handlers": ["event_http_handler"],
            "level": "DEBUG",
        },
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
