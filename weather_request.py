import datetime
import requests

APPID = "11e15b9843605c694e86fee262a52d86"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"
month_lst = ['января', 'февраля', 'марта', 'аплеля', 'мая', 'июня',
             'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
month_count_day_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_wind_direction(deg):
    w_direct = [' С', 'СВ', ' В', 'ЮВ', ' Ю', 'ЮЗ', ' З', 'СЗ']
    direct_str = ''
    for i in range(0, 8):
        step = 45.
        min_deg = i * step - 45 / 2.
        max_deg = i * step + 45 / 2.
        if i == 0 and deg > 360 - 45 / 2.:
            deg = deg - 360
        if min_deg <= deg <= max_deg:
            direct_str = w_direct[i]
            break
    return direct_str


def request_current_weather(city_id):
    try:
        res = requests.get(WEATHER_URL, params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
        data = res.json()
        now_dt = datetime.datetime.utcfromtimestamp(data['dt']) + datetime.timedelta(hours=7)
        now_str = str(now_dt.day) + " " + month_lst[now_dt.month - 1] + " " + str(now_dt.year) + " года " + \
                  '{:0>2}'.format(str(now_dt.hour)) + ":" + '{:0>2}'.format(str(now_dt.minute)) + " "

        weather_str = now_str + '\n' + 'темп: ' + str(data['main']['temp']) + 'C  ветер: ' + \
                      str(data['wind']['speed']) + 'м/с ' + \
                      get_wind_direction(data['wind']['deg']) + '\n' + \
                      data['weather'][0]['description']
    except Exception as e:
        weather_str = "Exception: " + str(e)
    return weather_str


def request_forecast(city_id):
    weather_str = ""
    try:
        res = requests.get(FORECAST_URL, params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
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
                weather_str += '\n' + day_local + " " + month_lst[month_local_num - 1] + ' ' + year_str + ' года' \
                               + '\n' + '{:-^40}'.format('') + '\n'
            weather_str += time_local + \
                           ":00" + '{0:+3.0f}'.format(i['main']['temp']) + \
                           'C ' + '{0:2.0f}'.format(i['wind']['speed']) + \
                           "м/с " + get_wind_direction(i['wind']['deg']) + " " + \
                           i['weather'][0]['description'] + '\n'

    except Exception as e:
        weather_str = "Exception: " + str(e)
    return weather_str
