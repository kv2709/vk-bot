# -*- coding: utf-8 -*-

import datetime
import requests
from setup import APP_ID

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

MONTH_LST = ['января', 'февраля', 'марта', 'аплеля', 'мая', 'июня',
             'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
WIND_DIRECT = [' С', 'СВ', ' В', 'ЮВ', ' Ю', 'ЮЗ', ' З', 'СЗ']


class WeatherGetter:
    """
    Класс выдачи текущей погоды и пятидневного прогноза по любому городу
    от сервиса openweathermap.org
    """
    @staticmethod
    def get_wind_direction(wind_deg=0):
        """
        Статический метод класса, для преобразования направления ветра,
        получаемое в градусах от АПИ в символьную нотацию сторон горизонта
        :param wind_deg: направление ветра в градусах
        :return: строка в символьной нотации из w_direct
        """
        direct_str = ''
        step = 45.
        half_step = 22.5
        rest_sector = 360 - half_step

        for i in range(8):
            min_deg = i * step - half_step
            max_deg = i * step + half_step
            if i == 0 and wind_deg > rest_sector:
                wind_deg = wind_deg - 360
            if min_deg <= wind_deg <= max_deg:
                direct_str = WIND_DIRECT[i]
                break
        return direct_str

    def get_current_weather(self, city_id=0):
        """
        Метод, отдающий строку текущей погоды по коду города
        :param city_id: код города
        :return: строка текущей погоды (дата, температура, направление ветра и
        состояние(облачность, осадки))
        """
        try:
            res = requests.get(url=WEATHER_URL, params={'id': city_id,
                                                        'units': 'metric',
                                                        'lang': 'ru',
                                                        'APPID': APP_ID})

            data = res.json()
            now_dt = datetime.datetime.utcfromtimestamp(data['dt']) + datetime.timedelta(hours=7)
            now_str = f"{data['name']}\n" \
                      f"{str(now_dt.day)} {MONTH_LST[now_dt.month - 1]} {str(now_dt.year)} года " \
                      f"{str(now_dt.hour).zfill(2)}:{str(now_dt.minute).zfill(2)}"

            weather_str = now_str + f"\nтемп: {str(round(data['main']['temp'], 1))}C " \
                                    f"ветер: {str(round(data['wind']['speed'], 1))}м/с " \
                                    f"{self.get_wind_direction(data['wind']['deg'])}\n" \
                                    f"{data['weather'][0]['description']}\n"

        except Exception as e:
            weather_str = "Exception: " + str(e)

        return weather_str

    def get_forecast(self, city_id=0):
        """
        Метод, отдающий строку прогноза погоды на пять дней по коду города
        :param city_id: код города
        :return: строка прогноза погоды (дата, затем с трех часовым интервалом время,
        температура, направление ветра и состояние(облачность, осадки))
        """
        weather_str = ""
        try:
            res = requests.get(url=FORECAST_URL, params={'id': city_id,
                                                         'units': 'metric',
                                                         'lang': 'ru',
                                                         'APPID': APP_ID})
            data = res.json()
            count_cycle = 0
            for i in data['list']:
                count_cycle += 1
                dt_local = datetime.datetime.utcfromtimestamp(i['dt']) + datetime.timedelta(hours=7)
                dt_local_str = dt_local.strftime("%Y-%m-%d %H:%M:%S")
                year_str = dt_local_str[0:4]
                month_local_num = int(dt_local_str[5:7])
                day_local = dt_local_str[8:10]
                time_local = dt_local_str[11:13]

                if count_cycle == 1 or (int(time_local) in [0, 1]):
                    weather_str += f"\n {day_local} {MONTH_LST[month_local_num - 1]} {year_str} года\n{'-'*40}\n"
                weather_str += f"{time_local}:00  {str(round(i['main']['temp'], 1))}C " \
                               f"{str(round(i['wind']['speed'], 1))}м/с {self.get_wind_direction(i['wind']['deg'])} " \
                               f"{i['weather'][0]['description']}\n"

        except Exception as e:
            weather_str = "Exception: " + str(e)
        return weather_str

    def get_current_weather_for_city_list(self, *args):
        weather_str = ""
        for arg in args:
            weather_str += f"{self.get_current_weather(city_id=arg)}{'-'*50}\n"
        return weather_str
