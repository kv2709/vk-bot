# -*- coding: utf-8 -*-
import sys
import os
import pytest
from vk_api.bot_longpoll import *
from vk_api.vk_api import *


WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
URL_API_DB_USER_REGISTRATION = "https://db-for-logging-vkbot.herokuapp.com/api/user_registration/"
URL_API_DB_USER_STATE = "https://db-for-logging-vkbot.herokuapp.com/api/user_state/"
URL_API_DB_LOGGING_BOT = "https://db-for-logging-vkbot.herokuapp.com/api/log/"
URL_API_GENERATE_AVATAR = "https://api.adorable.io/avatars/220/kv2709@gmail.com"


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Авто-фикстура: Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\nПродолжительнотсь выполения теста : {:0.3} секунд'.format(delta))


# ======================@pytest.fixture() def mock_response_requests_get(monkeypatch):=========================

# -----------------------------------------------------------------------------
def data_forecast_json_from_string():
    json_forecast_string = """
    {"cod": "200", "message": 0, "cnt": 40, "list": [{"dt": 1584716400, "main": {"temp": -2.14, "feels_like": -7.14, "temp_min": -2.14, "temp_max": -2.14, "pressure": 1018, "sea_level": 1018, "grnd_level": 994, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 94}, "wind": {"speed": 3.4, "deg": 229}, "sys": {"pod": "n"}, "dt_txt": "2020-03-20 15:00:00"}, {"dt": 1584727200, "main": {"temp": -4.65, "feels_like": -8.43, "temp_min": -4.65, "temp_max": -4.65, "pressure": 1016, "sea_level": 1016, "grnd_level": 993, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04n"}], "clouds": {"all": 68}, "wind": {"speed": 1.31, "deg": 219}, "sys": {"pod": "n"}, "dt_txt": "2020-03-20 18:00:00"}, {"dt": 1584738000, "main": {"temp": -5.18, "feels_like": -8.55, "temp_min": -5.18, "temp_max": -5.18, "pressure": 1015, "sea_level": 1015, "grnd_level": 992, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 801, "main": "Clouds", "description": "небольшая облачность", "icon": "02n"}], "clouds": {"all": 18}, "wind": {"speed": 0.67, "deg": 112}, "sys": {"pod": "n"}, "dt_txt": "2020-03-20 21:00:00"}, {"dt": 1584748800, "main": {"temp": -4.75, "feels_like": -9.11, "temp_min": -4.75, "temp_max": -4.75, "pressure": 1016, "sea_level": 1016, "grnd_level": 992, "humidity": 82, "temp_kf": 0}, "weather": [{"id": 802, "main": "Clouds", "description": "переменная облачность", "icon": "03n"}], "clouds": {"all": 50}, "wind": {"speed": 2.17, "deg": 133}, "sys": {"pod": "n"}, "dt_txt": "2020-03-21 00:00:00"}, {"dt": 1584759600, "main": {"temp": -0.45, "feels_like": -4.15, "temp_min": -0.45, "temp_max": -0.45, "pressure": 1014, "sea_level": 1014, "grnd_level": 991, "humidity": 83, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 89}, "wind": {"speed": 1.88, "deg": 135}, "sys": {"pod": "d"}, "dt_txt": "2020-03-21 03:00:00"}, {"dt": 1584770400, "main": {"temp": 0.85, "feels_like": -1.86, "temp_min": 0.85, "temp_max": 0.85, "pressure": 1013, "sea_level": 1013, "grnd_level": 990, "humidity": 100, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 88}, "wind": {"speed": 1.22, "deg": 115}, "sys": {"pod": "d"}, "dt_txt": "2020-03-21 06:00:00"}, {"dt": 1584781200, "main": {"temp": 1.35, "feels_like": -1.29, "temp_min": 1.35, "temp_max": 1.35, "pressure": 1011, "sea_level": 1011, "grnd_level": 988, "humidity": 100, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 98}, "wind": {"speed": 1.23, "deg": 97}, "sys": {"pod": "d"}, "dt_txt": "2020-03-21 09:00:00"}, {"dt": 1584792000, "main": {"temp": 0.43, "feels_like": -3.27, "temp_min": 0.43, "temp_max": 0.43, "pressure": 1010, "sea_level": 1010, "grnd_level": 988, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 98}, "wind": {"speed": 1.94, "deg": 98}, "sys": {"pod": "d"}, "dt_txt": "2020-03-21 12:00:00"}, {"dt": 1584802800, "main": {"temp": -0.89, "feels_like": -5.42, "temp_min": -0.89, "temp_max": -0.89, "pressure": 1010, "sea_level": 1010, "grnd_level": 986, "humidity": 77, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 100}, "wind": {"speed": 2.84, "deg": 112}, "sys": {"pod": "n"}, "dt_txt": "2020-03-21 15:00:00"}, {"dt": 1584813600, "main": {"temp": 0.25, "feels_like": -3.14, "temp_min": 0.25, "temp_max": 0.25, "pressure": 1009, "sea_level": 1009, "grnd_level": 985, "humidity": 78, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 100}, "wind": {"speed": 1.41, "deg": 168}, "sys": {"pod": "n"}, "dt_txt": "2020-03-21 18:00:00"}, {"dt": 1584824400, "main": {"temp": 1.71, "feels_like": -1.62, "temp_min": 1.71, "temp_max": 1.71, "pressure": 1009, "sea_level": 1009, "grnd_level": 985, "humidity": 83, "temp_kf": 0}, "weather": [{"id": 500, "main": "Rain", "description": "небольшой дождь", "icon": "10n"}], "clouds": {"all": 100}, "wind": {"speed": 1.75, "deg": 192}, "rain": {"3h": 0.13}, "sys": {"pod": "n"}, "dt_txt": "2020-03-21 21:00:00"}, {"dt": 1584835200, "main": {"temp": 1.88, "feels_like": -2.38, "temp_min": 1.88, "temp_max": 1.88, "pressure": 1009, "sea_level": 1009, "grnd_level": 986, "humidity": 79, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 100}, "wind": {"speed": 2.97, "deg": 197}, "sys": {"pod": "n"}, "dt_txt": "2020-03-22 00:00:00"}, {"dt": 1584846000, "main": {"temp": 2.72, "feels_like": -2.16, "temp_min": 2.72, "temp_max": 2.72, "pressure": 1009, "sea_level": 1009, "grnd_level": 987, "humidity": 91, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 4.44, "deg": 213}, "sys": {"pod": "d"}, "dt_txt": "2020-03-22 03:00:00"}, {"dt": 1584856800, "main": {"temp": 3.85, "feels_like": -1.97, "temp_min": 3.85, "temp_max": 3.85, "pressure": 1010, "sea_level": 1010, "grnd_level": 988, "humidity": 99, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 6.35, "deg": 244}, "sys": {"pod": "d"}, "dt_txt": "2020-03-22 06:00:00"}, {"dt": 1584867600, "main": {"temp": 3.87, "feels_like": -4.14, "temp_min": 3.87, "temp_max": 3.87, "pressure": 1012, "sea_level": 1012, "grnd_level": 989, "humidity": 79, "temp_kf": 0}, "weather": [{"id": 500, "main": "Rain", "description": "небольшой дождь", "icon": "10d"}], "clouds": {"all": 100}, "wind": {"speed": 8.72, "deg": 238}, "rain": {"3h": 0.44}, "sys": {"pod": "d"}, "dt_txt": "2020-03-22 09:00:00"}, {"dt": 1584878400, "main": {"temp": 2.22, "feels_like": -6.56, "temp_min": 2.22, "temp_max": 2.22, "pressure": 1016, "sea_level": 1016, "grnd_level": 993, "humidity": 67, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04d"}], "clouds": {"all": 70}, "wind": {"speed": 9.09, "deg": 245}, "sys": {"pod": "d"}, "dt_txt": "2020-03-22 12:00:00"}, {"dt": 1584889200, "main": {"temp": 0.23, "feels_like": -8.46, "temp_min": 0.23, "temp_max": 0.23, "pressure": 1021, "sea_level": 1021, "grnd_level": 996, "humidity": 75, "temp_kf": 0}, "weather": [{"id": 801, "main": "Clouds", "description": "небольшая облачность", "icon": "02n"}], "clouds": {"all": 12}, "wind": {"speed": 8.89, "deg": 248}, "sys": {"pod": "n"}, "dt_txt": "2020-03-22 15:00:00"}, {"dt": 1584900000, "main": {"temp": -2.15, "feels_like": -10.37, "temp_min": -2.15, "temp_max": -2.15, "pressure": 1025, "sea_level": 1025, "grnd_level": 1000, "humidity": 79, "temp_kf": 0}, "weather": [{"id": 600, "main": "Snow", "description": "небольшой снег", "icon": "13n"}], "clouds": {"all": 56}, "wind": {"speed": 7.97, "deg": 271}, "snow": {"3h": 0.19}, "sys": {"pod": "n"}, "dt_txt": "2020-03-22 18:00:00"}, {"dt": 1584910800, "main": {"temp": -4.05, "feels_like": -9.79, "temp_min": -4.05, "temp_max": -4.05, "pressure": 1028, "sea_level": 1028, "grnd_level": 1003, "humidity": 82, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 85}, "wind": {"speed": 4.24, "deg": 266}, "sys": {"pod": "n"}, "dt_txt": "2020-03-22 21:00:00"}, {"dt": 1584921600, "main": {"temp": -4.55, "feels_like": -8.9, "temp_min": -4.55, "temp_max": -4.55, "pressure": 1029, "sea_level": 1029, "grnd_level": 1004, "humidity": 86, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04n"}], "clouds": {"all": 84}, "wind": {"speed": 2.27, "deg": 272}, "sys": {"pod": "n"}, "dt_txt": "2020-03-23 00:00:00"}, {"dt": 1584932400, "main": {"temp": -3.45, "feels_like": -8.23, "temp_min": -3.45, "temp_max": -3.45, "pressure": 1029, "sea_level": 1029, "grnd_level": 1005, "humidity": 79, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 2.88, "deg": 288}, "sys": {"pod": "d"}, "dt_txt": "2020-03-23 03:00:00"}, {"dt": 1584943200, "main": {"temp": -2.25, "feels_like": -6.28, "temp_min": -2.25, "temp_max": -2.25, "pressure": 1029, "sea_level": 1029, "grnd_level": 1004, "humidity": 75, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 1.87, "deg": 306}, "sys": {"pod": "d"}, "dt_txt": "2020-03-23 06:00:00"}, {"dt": 1584954000, "main": {"temp": -1.74, "feels_like": -5.7, "temp_min": -1.74, "temp_max": -1.74, "pressure": 1028, "sea_level": 1028, "grnd_level": 1004, "humidity": 77, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 1.9, "deg": 358}, "sys": {"pod": "d"}, "dt_txt": "2020-03-23 09:00:00"}, {"dt": 1584964800, "main": {"temp": -2.84, "feels_like": -6.62, "temp_min": -2.84, "temp_max": -2.84, "pressure": 1028, "sea_level": 1028, "grnd_level": 1004, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 600, "main": "Snow", "description": "небольшой снег", "icon": "13d"}], "clouds": {"all": 100}, "wind": {"speed": 1.56, "deg": 58}, "snow": {"3h": 0.13}, "sys": {"pod": "d"}, "dt_txt": "2020-03-23 12:00:00"}, {"dt": 1584975600, "main": {"temp": -4.74, "feels_like": -9.53, "temp_min": -4.74, "temp_max": -4.74, "pressure": 1029, "sea_level": 1029, "grnd_level": 1004, "humidity": 83, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 97}, "wind": {"speed": 2.81, "deg": 52}, "sys": {"pod": "n"}, "dt_txt": "2020-03-23 15:00:00"}, {"dt": 1584986400, "main": {"temp": -6.61, "feels_like": -11.94, "temp_min": -6.61, "temp_max": -6.61, "pressure": 1029, "sea_level": 1029, "grnd_level": 1005, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04n"}], "clouds": {"all": 67}, "wind": {"speed": 3.31, "deg": 33}, "sys": {"pod": "n"}, "dt_txt": "2020-03-23 18:00:00"}, {"dt": 1584997200, "main": {"temp": -7.67, "feels_like": -12.93, "temp_min": -7.67, "temp_max": -7.67, "pressure": 1029, "sea_level": 1029, "grnd_level": 1005, "humidity": 78, "temp_kf": 0}, "weather": [{"id": 802, "main": "Clouds", "description": "переменная облачность", "icon": "03n"}], "clouds": {"all": 41}, "wind": {"speed": 3.06, "deg": 30}, "sys": {"pod": "n"}, "dt_txt": "2020-03-23 21:00:00"}, {"dt": 1585008000, "main": {"temp": -8.39, "feels_like": -13.55, "temp_min": -8.39, "temp_max": -8.39, "pressure": 1030, "sea_level": 1030, "grnd_level": 1005, "humidity": 77, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04n"}], "clouds": {"all": 67}, "wind": {"speed": 2.83, "deg": 14}, "sys": {"pod": "n"}, "dt_txt": "2020-03-24 00:00:00"}, {"dt": 1585018800, "main": {"temp": -7.08, "feels_like": -12.48, "temp_min": -7.08, "temp_max": -7.08, "pressure": 1030, "sea_level": 1030, "grnd_level": 1006, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04d"}], "clouds": {"all": 78}, "wind": {"speed": 3.35, "deg": 27}, "sys": {"pod": "d"}, "dt_txt": "2020-03-24 03:00:00"}, {"dt": 1585029600, "main": {"temp": -5.05, "feels_like": -10.85, "temp_min": -5.05, "temp_max": -5.05, "pressure": 1030, "sea_level": 1030, "grnd_level": 1006, "humidity": 68, "temp_kf": 0}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04d"}], "clouds": {"all": 68}, "wind": {"speed": 3.91, "deg": 22}, "sys": {"pod": "d"}, "dt_txt": "2020-03-24 06:00:00"}, {"dt": 1585040400, "main": {"temp": -4.63, "feels_like": -10.52, "temp_min": -4.63, "temp_max": -4.63, "pressure": 1030, "sea_level": 1030, "grnd_level": 1006, "humidity": 64, "temp_kf": 0}, "weather": [{"id": 800, "main": "Clear", "description": "ясно", "icon": "01d"}], "clouds": {"all": 2}, "wind": {"speed": 4.01, "deg": 15}, "sys": {"pod": "d"}, "dt_txt": "2020-03-24 09:00:00"}, {"dt": 1585051200, "main": {"temp": -5.89, "feels_like": -11.18, "temp_min": -5.89, "temp_max": -5.89, "pressure": 1030, "sea_level": 1030, "grnd_level": 1006, "humidity": 67, "temp_kf": 0}, "weather": [{"id": 800, "main": "Clear", "description": "ясно", "icon": "01d"}], "clouds": {"all": 1}, "wind": {"speed": 3.09, "deg": 4}, "sys": {"pod": "d"}, "dt_txt": "2020-03-24 12:00:00"}, {"dt": 1585062000, "main": {"temp": -7.09, "feels_like": -11.73, "temp_min": -7.09, "temp_max": -7.09, "pressure": 1032, "sea_level": 1032, "grnd_level": 1008, "humidity": 73, "temp_kf": 0}, "weather": [{"id": 800, "main": "Clear", "description": "ясно", "icon": "01n"}], "clouds": {"all": 0}, "wind": {"speed": 2.15, "deg": 355}, "sys": {"pod": "n"}, "dt_txt": "2020-03-24 15:00:00"}, {"dt": 1585072800, "main": {"temp": -8.31, "feels_like": -12.73, "temp_min": -8.31, "temp_max": -8.31, "pressure": 1032, "sea_level": 1032, "grnd_level": 1008, "humidity": 80, "temp_kf": 0}, "weather": [{"id": 800, "main": "Clear", "description": "ясно", "icon": "01n"}], "clouds": {"all": 0}, "wind": {"speed": 1.83, "deg": 7}, "sys": {"pod": "n"}, "dt_txt": "2020-03-24 18:00:00"}, {"dt": 1585083600, "main": {"temp": -8.8, "feels_like": -12.49, "temp_min": -8.8, "temp_max": -8.8, "pressure": 1033, "sea_level": 1033, "grnd_level": 1008, "humidity": 82, "temp_kf": 0}, "weather": [{"id": 800, "main": "Clear", "description": "ясно", "icon": "01n"}], "clouds": {"all": 6}, "wind": {"speed": 0.77, "deg": 27}, "sys": {"pod": "n"}, "dt_txt": "2020-03-24 21:00:00"}, {"dt": 1585094400, "main": {"temp": -8.6, "feels_like": -12.96, "temp_min": -8.6, "temp_max": -8.6, "pressure": 1034, "sea_level": 1034, "grnd_level": 1009, "humidity": 84, "temp_kf": 0}, "weather": [{"id": 802, "main": "Clouds", "description": "переменная облачность", "icon": "03n"}], "clouds": {"all": 47}, "wind": {"speed": 1.78, "deg": 188}, "sys": {"pod": "n"}, "dt_txt": "2020-03-25 00:00:00"}, {"dt": 1585105200, "main": {"temp": -6.22, "feels_like": -12.12, "temp_min": -6.22, "temp_max": -6.22, "pressure": 1033, "sea_level": 1033, "grnd_level": 1009, "humidity": 67, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 3.93, "deg": 245}, "sys": {"pod": "d"}, "dt_txt": "2020-03-25 03:00:00"}, {"dt": 1585116000, "main": {"temp": -3.85, "feels_like": -10.93, "temp_min": -3.85, "temp_max": -3.85, "pressure": 1033, "sea_level": 1033, "grnd_level": 1009, "humidity": 48, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 5.44, "deg": 245}, "sys": {"pod": "d"}, "dt_txt": "2020-03-25 06:00:00"}, {"dt": 1585126800, "main": {"temp": -2.15, "feels_like": -9.49, "temp_min": -2.15, "temp_max": -2.15, "pressure": 1033, "sea_level": 1033, "grnd_level": 1009, "humidity": 51, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 6.02, "deg": 254}, "sys": {"pod": "d"}, "dt_txt": "2020-03-25 09:00:00"}, {"dt": 1585137600, "main": {"temp": -2.55, "feels_like": -8.93, "temp_min": -2.55, "temp_max": -2.55, "pressure": 1034, "sea_level": 1034, "grnd_level": 1009, "humidity": 63, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}], "clouds": {"all": 100}, "wind": {"speed": 4.91, "deg": 262}, "sys": {"pod": "d"}, "dt_txt": "2020-03-25 12:00:00"}], "city": {"id": 1510018, "name": "Бийск", "coord": {"lat": 52.5364, "lon": 85.2072}, "country": "RU", "timezone": 25200, "sunrise": 1584663690, "sunset": 1584707501}}
    """
    return json.loads(json_forecast_string)


class MockResponseJsonForecast:
    """
    Класс, подменяющий возвращение значения метода requests.get()
    """
    @staticmethod
    def json():
        """
        Подмена json() метода для возврата им тестового словаря с данными погоды
        :return: словарь с макетными данными
        """
        return data_forecast_json_from_string()


# -----------------------------------------------------------------------------
def data_weather_json_from_string():
    json_weather_string = """{"coord": {"lon": 85.21, "lat": 52.54},
                              "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04d"}],
                              "base": "model",
                              "main": {"temp": -3.02, "feels_like": -8.35, "temp_min": -3.02, "temp_max": -3.02,
                                       "pressure": 1018, "humidity": 81, "sea_level": 1018, "grnd_level": 994},
                              "wind": {"speed": 3.76, "deg": 245},
                              "clouds": {"all": 100},
                              "dt": 1580207283,
                              "sys": {"country": "RU", "sunrise": 1580177303, "sunset": 1580208915},
                              "timezone": 25200,
                              "id": 1510018,
                              "name": "Бийск",
                              "cod": 200}"""
    return json.loads(json_weather_string)


class MockResponseJson:
    """
    Класс, подменяющий возвращение значения метода requests.get()
    """
    @staticmethod
    def json():
        """
        Подмена json() метода для возврата им тестового словаря с данными погоды
        :return: словарь с макетными данными
        """

        return data_weather_json_from_string()


def data_no_user_state_json_from_string():
    json_no_user_state_string = """{"key": "value"}"""
    return json.loads(json_no_user_state_string)


class MockResponseJsonNoUserState:
    @staticmethod
    def json():
        return data_no_user_state_json_from_string()


class MockResponseByteAvatar:

    def __init__(self):
        root_dir = sys.path.pop()
        abs_path_for_avatar_file = os.path.join(root_dir, 'files/avatar-test.png')
        with open(abs_path_for_avatar_file, 'rb') as avatar_file:
            self.content = avatar_file.read()
        sys.path.append(root_dir)
# -----------------------------------------------------------------------------
# Манкипатчнутый requests.get перемещенный в фикстуру
# Отдает json объект в зависимости от url для погоды, передаваемому ему при вызове


@pytest.fixture()
def mock_response_requests_get(monkeypatch):
    """
    Любые аргументы могут быть переданы в mock_get()
    и она всегда будет возвращать мокнутый объект,
    который имеет единственный метод json().
    """
    def mock_get(*args, **kwargs):

        if kwargs['url'] == WEATHER_URL:
            return MockResponseJson()
        elif kwargs['url'] == FORECAST_URL:
            return MockResponseJsonForecast()
        elif kwargs['url'] == URL_API_DB_USER_STATE + "77209884":
            return MockResponseJsonNoUserState()
        elif kwargs['url'] == URL_API_GENERATE_AVATAR:
            return MockResponseByteAvatar()

    monkeypatch.setattr("requests.get", mock_get)

# ======================@pytest.fixture() def mock_response_requests_get(monkeypatch):=========================


# ==================@pytest.fixture() def mock_response_requests_get_for_registration(monkeypatch)=============


def data_json_from_string_for_user_state_step1():
    json_user_state = """{"user_id" : "77209884", 
                          "scenario_name": "registration", 
                          "step_name": "step1", 
                          "context": {}
                          }"""
    return json.loads(json_user_state)


class MockResponseJsonForRegistrationStep1:
    @staticmethod
    def json():
        return data_json_from_string_for_user_state_step1()


def data_json_from_string_for_user_state_step2():
    json_user_state = """{"user_id" : "77209884", 
                          "scenario_name": "registration", 
                          "step_name": "step2", 
                          "context": {"name": "Юрий-Киреев"}
                          }"""
    return json.loads(json_user_state)


class MockResponseJsonForRegistrationStep2:

    @staticmethod
    def json():
        return data_json_from_string_for_user_state_step2()


# Манкипатчнутый requests.get перемещенный в фикстуру
# Отдает json объект в зависимости от url для user_state, передаваемому ему при вызове
@pytest.fixture()
def mock_response_requests_get_for_registration(monkeypatch, number_call):
    """
    Любые аргументы могут быть переданы в mock_get()
    и она всегда будет возвращать мокнутый объект,
    который имеет единственный метод json().
    """
    def mock_get(*args, **kwargs):

        if kwargs['url'] == URL_API_DB_USER_STATE + "77209884":
            if number_call == 0 or number_call == 5:
                return MockResponseJsonNoUserState()
            elif number_call == 1 or number_call == 2:
                return MockResponseJsonForRegistrationStep1()
            elif number_call == 3 or number_call == 4:
                return MockResponseJsonForRegistrationStep2()
        elif kwargs['url'] == WEATHER_URL:
            return MockResponseJson()
        elif kwargs['url'] == FORECAST_URL:
            return MockResponseJsonForecast()
        elif kwargs['url'] == URL_API_DB_USER_STATE + "77209884":
            return MockResponseJsonNoUserState()
        elif kwargs['url'] == URL_API_GENERATE_AVATAR:
            return MockResponseByteAvatar()
    monkeypatch.setattr("requests.get", mock_get)
# ==================@pytest.fixture() def mock_response_requests_get_for_registration(monkeypatch)=============


class MockResponseContentForRequestsPutUserSate:
    """
    Класс, подменяющий возвращение значения метода requests.put()
    через свой атрибут content
    """
    content = {"code_error": "Update_user_state_record_from_pytest"}
    status_code = 2000


@pytest.fixture()
def mock_response_requests_put(monkeypatch):
    """
    Фикстура mock_put() будет возвращать мокнутый объект,
    который имеет единственным атрибутом content
    """
    def mock_put(*args, **kwargs):
        return MockResponseContentForRequestsPutUserSate()

    monkeypatch.setattr("requests.put", mock_put)


class MockResponseContentForRequestsDeleteUserSate:
    """
    Класс, подменяющий возвращение значения метода requests.put()
    через свой атрибут content
    """
    content = {"code_error": "Delete_user_state_record_from_pytest"}
    status_code = 2000


@pytest.fixture()
def mock_response_requests_delete(monkeypatch):
    """
    Фикстура mock_delete() будет возвращать мокнутый объект,
    который имеет единственным атрибутом content
    """
    def mock_delete(*args, **kwargs):
        return MockResponseContentForRequestsDeleteUserSate()

    monkeypatch.setattr("requests.delete", mock_delete)


# ============================================================================
class MockResponseContent:
    """
    Класс, подменяющий возвращение значения метода requests.post()
    через свой атрибут content
    """
    content = {"code_error": "Created_new_log_record_from_pytest"}
    status_code = 2000


@pytest.fixture()
def mock_response_requests_post(monkeypatch):
    """
    Фикстура mock_post() будет возвращать мокнутый объект,
    который имеет единственным атрибутом content
    """
    def mock_post(*args, **kwargs):
        return MockResponseContent()

    monkeypatch.setattr("requests.post", mock_post)


# ------------------------------------------------------------------------
class MockVkBotLongPoll:
    """
    Класс, подменяющий возвращение значения объестом vk_api.bot_longpoll.VkBotLongPoll
    реализован метод listen()
    """

    @staticmethod
    def listen(cmd=None):
        event = VkBotEvent
        event.type = VkBotEventType.MESSAGE_NEW
        event.group_id = 190385197
        object_dict = {'object': {'message': {'date': 1578040300,
                                              'from_id': 77209884,
                                              'id': 143,
                                              'out': 0,
                                              'peer_id': 77209884,
                                              'text': cmd,
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
                                  }
                       }
        event.object = DotDict(object_dict['object'])
        yield event


@pytest.fixture()
def mock_long_poll(monkeypatch):
    def mock_listen(*args, **kwargs):
        return MockVkBotLongPoll()

    monkeypatch.setattr("vk_api.bot_longpoll.VkBotLongPoll", mock_listen)


# ------------------------------------------------------------------------
class MockObjVkApi:
    @staticmethod
    def obj_api():
        return None


@pytest.fixture()
def mock_obj_vk_api(monkeypatch):
    def mock_obj(*args, **kwargs):
        return MockObjVkApi()

    monkeypatch.setattr("vk_api.vk_api.VkApi", mock_obj)


# ------------------------------------------------------------------------
class MockVkApi:
    @staticmethod
    def get_api():
        return None


@pytest.fixture()
def mock_vk_api_get(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockVkApi()

    monkeypatch.setattr("vk_api.VkApi.get_api", mock_get)
# -------------------------------------------------------------------------------


class SendTicketImage:
    status_code = 2000


@pytest.fixture()
def mock_send_ticket_image_fixture(monkeypatch):
    def mock_send_ticket_image(*args, **kwargs):
        return SendTicketImage()

    monkeypatch.setattr("bot.VKBot.send_ticket_image", mock_send_ticket_image)


class GetClass:
    """
    Класс, создающий возможность создаваемому полю
    переменной этого класса иметь входой параметр user_id и name_case
    и возвращать значение value, переданное при создании
    переменной экземпляра этого класса
    """
    def __init__(self, value):
        self.value = value

    def __call__(self, user_id, name_case):
        return self.value


class SendClass:

    def __init__(self, value):
        self.value = value

    def __call__(self, random_id, peer_id, message, keyboard):
        return self.value


def get_add(user_info):
    """
    Декоратор с входным параметром, внутри которого декорируемой функции
    добавляется поле(атрибут), который должен принимать входное значение,
    а эта функция при ее вызове возвращать переданное в декоратор значение
    :param user_info:
    :return value:
    """
    def wrapper(users_func):
        users_func.get = GetClass(user_info)
        return users_func
    return wrapper


def send_add(code_exec):
    def wrapper(users_func):
        users_func.send = SendClass(code_exec)
        return users_func
    return wrapper


class MockUserGetMessagesSend:

    @staticmethod
    @get_add([{'first_name': 'Urik', 'last_name': 'Kireev'}, ])
    def users():
        return None

    @staticmethod
    @send_add(600)
    def messages():
        return None


@pytest.fixture()
def mock_users_get_messages_send(monkeypatch):
    def users_get_messages_send(*args, **kwargs):
        return MockUserGetMessagesSend()

    monkeypatch.setattr("vk_api.VkApi.get_api", users_get_messages_send)
