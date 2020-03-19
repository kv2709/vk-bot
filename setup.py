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
CMD_RETURN_MAIN_MENU = "Вернуться в основное меню"
CMD_SIGN_UP_FOR_CONFERENCE = 'Запись на конференцию'

CMD_LST = [CMD_NO_COMMAND,
           CMD_START,
           CMD_BIYSK_WEATHER_NOW,
           CMD_BIYSK_WEATHER_FORECAST,
           CMD_NOVOSIBIRSK_WEATHER_NOW,
           CMD_NOVOSIBIRSK_WEATHER_FORECAST,
           CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW,
           CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW,
           CMD_MENU_ROAD_FORECAST,
           CMD_RETURN_MAIN_MENU,
           CMD_SIGN_UP_FOR_CONFERENCE]

NOVOSIBIRSK_ID = 1496747
CHEREPANOVO_ID = 1508161
TALMENKA_ID = 1490266
NOVOALTAYSK_ID = 1497173
NALOBIKHA_ID = 1498027
TROITSKOYE_ID = 1489209
BIYSK_ID = 1510018

GROUP_ID = 190385197

INTENTS = [
    {
        "name": "Дата проведения",
        "token": ("когда", "сколько", "дат", "как скоро", "время"),
        "scenario": None,
        "answer": "Конференция проводится 15 апреля, регитсрация начнется в 10 утра",
    },
    {
        "name": "Место проведения",
        "token": ("где", "мест", "локация", "адрес"),
        "scenario": None,
        "answer": "Конференция пройдет в павильоне 18г в Экспоцентре",
    },
    {
        "name": "Регистрация",
        "token": ("регистр", "добав", "включ", "запис"),
        "scenario": "registration",
        "answer": None,
    },
]
SCENARIO = {
    "registration": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "Чтобы зарегистрироваться, введите Ваше имя. Оно будет прописано на бэйджике",
                "failure_text": "Имя должно состоять из 3-30 букв и дефиса! Поробуйте еще раз",
                "handler": "handle_name",
                "next_step": "step2"
            },
            "step2": {
                "text": "Введите e-mail. Мы отправим на него все данные",
                "failure_text": "Во введенном адресе ошибка! Попробуйте еще раз",
                "handler": "handle_email",
                "next_step": "step3"
            },
            "step3": {
                "text": "Спасибо за регистрацию {name}! Мы отправим на Ваш e-mail {email} билет, распечатайте его",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
        }
    }
}

DEFAULT_ANSWER = "Не знаю как Вам ответить. " \
                 "Могу сказать когда и где пройдет конференция, " \
                 "а также зарегистрировать Вас. Просто спросите"

# Списки для работы тестов написаны в этом модуле из-за удобства
# близкого просмотра исходных структур INTENTS и SCENARIO
REG_CONF_INTENTS_LST_INPUT = [
    "Привет",
    "Когда будет проходить конференция",
    "А где она будет проходить",
    "Лабуда-лабуда",
]

REG_CONF_INTENTS_LST_ANSWER = [
    DEFAULT_ANSWER,
    INTENTS[0]["answer"],
    INTENTS[1]["answer"],
    DEFAULT_ANSWER,
]

REG_CONF_SCENARIO_LST_INPUT = [
    ("Зарегистрируй меня", None, None, None),
    ("КЮ", "registration", "step1", None),
    ("Юрий-Киреев", "registration", "step1", None),
    ("kv.gmail.com", "registration", "step2", None),
    ("kv2709@gmail.com", "registration", "step2", {"name": "Юрий-Киреев"}),
    ("Лабуда", None, None, None)
]

REG_CONF_SCENARIO_LST_ANSWER = [
    SCENARIO["registration"]["steps"]["step1"]["text"],
    SCENARIO["registration"]["steps"]["step1"]["failure_text"],
    SCENARIO["registration"]["steps"]["step2"]["text"],
    SCENARIO["registration"]["steps"]["step2"]["failure_text"],
    SCENARIO["registration"]["steps"]["step3"]["text"].format(name="Юрий-Киреев", email="kv2709@gmail.com"),
    DEFAULT_ANSWER,
]
# ------------------ конец струтур данных для тестов ------------------------

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
          {"action": {"type": "text",
                      "label": CMD_SIGN_UP_FOR_CONFERENCE
                      },
           "color": "primary"
           },
          ]
     ]
     }
)

KEY_BOARD_RETURN_MAIN_MENU = json.dumps(
    {"one_time": False,
     'buttons': [
         [{"action": {"type": "text",
                      "label": CMD_RETURN_MAIN_MENU
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
