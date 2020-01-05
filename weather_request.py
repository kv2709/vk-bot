import datetime
import requests
from setup import APP_ID

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"


class WeatherGetter:
    """
    Класс выдачи текущей погоды и пятидневного прогноза по любому городу
    от сервиса openweathermap.org
    """
    def __init__(self):
        """
        Инициализация класса. Токен доступа к АПИ openweathermap.org получается
        из переменной окружения Heroku, определен в модуле setup
        """
        self.app_id = APP_ID
        self.weather_url = WEATHER_URL
        self.forecast_url = FORECAST_URL
        self.month_lst = ['января', 'февраля', 'марта', 'аплеля', 'мая', 'июня',
                          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        self.month_count_day_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def get_wind_direction(wind_deg=0):
        """
        Статический метод класса, для преобразования направления ветра,
        получаемое в градусах от АПИ в символьную нотацию сторон горизонта
        :param wind_deg: направление ветра в градусах
        :return: строка в символьной нотации из w_direct
        """
        w_direct = [' С', 'СВ', ' В', 'ЮВ', ' Ю', 'ЮЗ', ' З', 'СЗ']
        direct_str = ''
        for i in range(0, 8):
            step = 45.
            min_deg = i * step - 45 / 2.
            max_deg = i * step + 45 / 2.
            if i == 0 and wind_deg > 360 - 45 / 2.:
                wind_deg = wind_deg - 360
            if min_deg <= wind_deg <= max_deg:
                direct_str = w_direct[i]
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
            res = requests.get(self.weather_url, params={'id': city_id,
                                                         'units': 'metric',
                                                         'lang': 'ru',
                                                         'APPID': self.app_id})
            data = res.json()
            now_dt = datetime.datetime.utcfromtimestamp(data['dt']) + datetime.timedelta(hours=7)
            now_str = f"{str(now_dt.day)} {self.month_lst[now_dt.month - 1]} {str(now_dt.year)} года " \
                      f"{str(now_dt.hour).zfill(2)}:{str(now_dt.minute).zfill(2)}"

            weather_str = now_str + f"\n темп: {str(round(data['main']['temp'], 1))}C  " \
                                    f"ветер: {str(round(data['wind']['speed'], 1))}м/с " \
                                    f"{self.get_wind_direction(data['wind']['deg'])} \n " \
                                    f"{data['weather'][0]['description']}"

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
            res = requests.get(FORECAST_URL, params={'id': city_id,
                                                     'units': 'metric',
                                                     'lang': 'ru',
                                                     'APPID': self.app_id})
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
                    weather_str += f"\n {day_local} {self.month_lst[month_local_num - 1]} {year_str} года\n{'-'*40}\n"
                weather_str += f"{time_local}:00  {str(round(i['main']['temp'], 1))}C " \
                               f"{str(round(i['wind']['speed'], 1))}м/с {self.get_wind_direction(i['wind']['deg'])} " \
                               f"{i['weather'][0]['description']}\n"

        except Exception as e:
            weather_str = "Exception: " + str(e)
        return weather_str
