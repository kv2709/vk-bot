from setup import *

WIND_DIRECT_TEST = [' С', 'СВ', ' В', 'ЮВ', ' Ю', 'ЮЗ', ' З', 'СЗ']

EXPECT_ANSWER_WEATHER_STR = "Бийск\n" \
                            "28 января 2020 года 17:28\n" \
                            "темп: -3.0C ветер: 3.8м/с ЮЗ\n" \
                            "пасмурно\n"
EXPECT_ANSWER_WEATHER_STR_FOR_CITY_LIST = EXPECT_ANSWER_WEATHER_STR + f"{'-'*50}\n"
EXPECT_ANSWER_FORECAST_STR = "\n 20 марта 2020 года\n" \
                                "----------------------------------------\n" \
                                "22:00  -2.1C 3.4м/с ЮЗ пасмурно\n\n" \
                                " 21 марта 2020 года\n" \
                                "----------------------------------------\n" \
                                "01:00  -4.7C 1.3м/с ЮЗ облачно с прояснениями\n" \
                                "04:00  -5.2C 0.7м/с  В небольшая облачность\n" \
                                "07:00  -4.8C 2.2м/с ЮВ переменная облачность\n" \
                                "10:00  -0.5C 1.9м/с ЮВ пасмурно\n" \
                                "13:00  0.8C 1.2м/с ЮВ пасмурно\n" \
                                "16:00  1.4C 1.2м/с  В пасмурно\n" \
                                "19:00  0.4C 1.9м/с  В пасмурно\n" \
                                "22:00  -0.9C 2.8м/с  В пасмурно\n\n" \
                                " 22 марта 2020 года\n" \
                                "----------------------------------------\n" \
                                "01:00  0.2C 1.4м/с  Ю пасмурно\n" \
                                "04:00  1.7C 1.8м/с  Ю небольшой дождь\n" \
                                "07:00  1.9C 3.0м/с  Ю пасмурно\n" \
                                "10:00  2.7C 4.4м/с ЮЗ пасмурно\n" \
                                "13:00  3.9C 6.3м/с ЮЗ пасмурно\n" \
                                "16:00  3.9C 8.7м/с ЮЗ небольшой дождь\n" \
                                "19:00  2.2C 9.1м/с ЮЗ облачно с прояснениями\n" \
                                "22:00  0.2C 8.9м/с  З небольшая облачность\n\n" \
                                " 23 марта 2020 года\n" \
                                "----------------------------------------\n" \
                                "01:00  -2.1C 8.0м/с  З небольшой снег\n" \
                                "04:00  -4.0C 4.2м/с  З пасмурно\n" \
                                "07:00  -4.5C 2.3м/с  З облачно с прояснениями\n" \
                                "10:00  -3.5C 2.9м/с  З пасмурно\n" \
                                "13:00  -2.2C 1.9м/с СЗ пасмурно\n" \
                                "16:00  -1.7C 1.9м/с  С пасмурно\n" \
                                "19:00  -2.8C 1.6м/с СВ небольшой снег\n" \
                                "22:00  -4.7C 2.8м/с СВ пасмурно\n\n" \
                                " 24 марта 2020 года\n" \
                                "----------------------------------------\n" \
                                "01:00  -6.6C 3.3м/с СВ облачно с прояснениями\n" \
                                "04:00  -7.7C 3.1м/с СВ переменная облачность\n" \
                                "07:00  -8.4C 2.8м/с  С облачно с прояснениями\n" \
                                "10:00  -7.1C 3.4м/с СВ облачно с прояснениями\n" \
                                "13:00  -5.0C 3.9м/с  С облачно с прояснениями\n" \
                                "16:00  -4.6C 4.0м/с  С ясно\n" \
                                "19:00  -5.9C 3.1м/с  С ясно\n" \
                                "22:00  -7.1C 2.1м/с  С ясно\n\n" \
                                " 25 марта 2020 года\n" \
                                "----------------------------------------\n" \
                                "01:00  -8.3C 1.8м/с  С ясно\n" \
                                "04:00  -8.8C 0.8м/с СВ ясно\n" \
                                "07:00  -8.6C 1.8м/с  Ю переменная облачность\n" \
                                "10:00  -6.2C 3.9м/с ЮЗ пасмурно\n" \
                                "13:00  -3.9C 5.4м/с ЮЗ пасмурно\n" \
                                "16:00  -2.1C 6.0м/с  З пасмурно\n" \
                                "19:00  -2.5C 4.9м/с  З пасмурно\n"

CMD_LST = [
    CMD_NO_COMMAND,
    CMD_START,
    CMD_BIYSK_WEATHER_NOW,
    CMD_BIYSK_WEATHER_FORECAST,
    CMD_NOVOSIBIRSK_WEATHER_NOW,
    CMD_NOVOSIBIRSK_WEATHER_FORECAST,
    CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW,
    CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW,
    CMD_MENU_ROAD_FORECAST,
    CMD_RETURN_MAIN_MENU,
    CMD_SIGN_UP_FOR_CONFERENCE
]

CMD_START_ANSWER = "Уважаемый(ая) Urik Kireev. " \
                   "Вас привествует Бот сообщества <Бото-ферма>. Мой Бот умеет отвечать эхом " \
                   "на произвольное входящее сообщение, а так же на пересылаемое Вами сообщение " \
                   "из другого диалога с Вашим комментарием. Из полезной функциональности Бот умеет " \
                   " показывать прогноз погоды в Бийске и Новосибирске на сегодня и на пять дней"
CMD_NO_COMMAND_ANSWER = "Эхо-ответ бота на входящее сообщение <None> от Urik Kireev"
CMD_BIYSK_WEATHER_NOW_ANSWER = EXPECT_ANSWER_WEATHER_STR
CMD_BIYSK_WEATHER_FORECAST_ANSWER = EXPECT_ANSWER_FORECAST_STR
CMD_NOVOSIBIRSK_WEATHER_NOW_ANSWER = EXPECT_ANSWER_WEATHER_STR
CMD_NOVOSIBIRSK_WEATHER_FORECAST_ANSWER = EXPECT_ANSWER_FORECAST_STR
CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW_ANSWER = EXPECT_ANSWER_WEATHER_STR_FOR_CITY_LIST * 7
CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW_ANSWER = 'Функция в разработке'
CMD_MENU_ROAD_FORECAST_ANSWER = "Загружено дорожное меню"
CMD_RETURN_MAIN_MENU_ANSWER = "Загружено основное меню"
CMD_SIGN_UP_FOR_CONFERENCE_ANSWER = "Бот переключен в режим <Регистрация на конференцию>"

CMD_LST_ANSWER = [
    CMD_NO_COMMAND_ANSWER,
    CMD_START_ANSWER,
    CMD_BIYSK_WEATHER_NOW_ANSWER,
    CMD_BIYSK_WEATHER_FORECAST_ANSWER,
    CMD_NOVOSIBIRSK_WEATHER_NOW_ANSWER,
    CMD_NOVOSIBIRSK_WEATHER_FORECAST_ANSWER,
    CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW_ANSWER,
    CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW_ANSWER,
    CMD_MENU_ROAD_FORECAST_ANSWER,
    CMD_RETURN_MAIN_MENU_ANSWER,
    CMD_SIGN_UP_FOR_CONFERENCE_ANSWER
]

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
    ("Зарегистрируй меня", None, None, None, 0),
    ("КЮ", "registration", "step1", None, 1),
    ("Юрий-Киреев", "registration", "step1", None, 2),
    ("kv.gmail.com", "registration", "step2", None, 3),
    ("kv2709@gmail.com", "registration", "step2", {"name": "Юрий-Киреев"}, 4),
    ("Лабуда", None, None, None, 5)
]

REG_CONF_SCENARIO_LST_ANSWER = [
    SCENARIO["registration"]["steps"]["step1"]["text"],
    SCENARIO["registration"]["steps"]["step1"]["failure_text"],
    SCENARIO["registration"]["steps"]["step2"]["text"],
    SCENARIO["registration"]["steps"]["step2"]["failure_text"],
    SCENARIO["registration"]["steps"]["step3"]["text"].format(name="Юрий-Киреев", email="kv2709@gmail.com"),
    DEFAULT_ANSWER,
]

CMD_LST_revers = CMD_LST.copy()
CMD_LST_revers.reverse()

CMD_LST_ANSWER_revers = CMD_LST_ANSWER.copy()
CMD_LST_ANSWER_revers.reverse()

REG_CONF_INTENTS_LST_INPUT_revers = REG_CONF_INTENTS_LST_INPUT.copy()
REG_CONF_INTENTS_LST_INPUT_revers.reverse()

REG_CONF_INTENTS_LST_ANSWER_revers = REG_CONF_INTENTS_LST_ANSWER.copy()
REG_CONF_INTENTS_LST_ANSWER_revers.reverse()

REG_CONF_SCENARIO_LST_INPUT_revers = REG_CONF_SCENARIO_LST_INPUT.copy()
REG_CONF_SCENARIO_LST_INPUT_revers.reverse()

REG_CONF_SCENARIO_LST_ANSWER_revers = REG_CONF_SCENARIO_LST_ANSWER.copy()
REG_CONF_SCENARIO_LST_ANSWER_revers.reverse()
