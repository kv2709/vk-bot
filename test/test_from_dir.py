# -*- coding: utf-8 -*-
from weather_request import WeatherGetter
import pytest


def test_object():
    pytest.skip("skipping this test")
    wg = WeatherGetter()
    assert str(type(wg)) == "<class 'weather_request.WeatherGetter'>"


def test_sending_list_cities():

    wg = WeatherGetter()
    lst_city = wg.get_current_weather_for_city_list(1496747, 1508161,
                                                    1490266, 1497173,
                                                    1498027, 1489209,
                                                    1510018)
    assert lst_city == [1496747, 1508161, 1490266, 1497173,
                        1498027, 1489209, 1510018]


"""
{
coord: {
lon: 85.21,
lat: 52.54
},
weather: [
{
id: 601,
main: "Snow",
description: "снег",
icon: "13d"
}
],
base: "model",
main: {
temp: -3.86,
feels_like: -13.82,
temp_min: -3.86,
temp_max: -3.86,
pressure: 1014,
humidity: 91,
sea_level: 1014,
grnd_level: 990
},
wind: {
speed: 10.48,
deg: 255
},
snow: {
3h: 1.75
},
clouds: {
all: 100
},
dt: 1579424679,
sys: {
country: "RU",
sunrise: 1579400374,
sunset: 1579430355
},
timezone: 25200,
id: 1510018,
name: "Бийск",
cod: 200
}
"""

"""
{
cod: "200",
message: 0,
cnt: 40,
list: [
{
dt: 1579435200,
main: {
temp: -5,
feels_like: -14.14,
temp_min: -5,
temp_max: -5,
pressure: 1015,
sea_level: 1015,
grnd_level: 991,
humidity: 85,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 9.03,
deg: 253
},
snow: {
3h: 0.25
},
sys: {
pod: "n"
},
dt_txt: "2020-01-19 12:00:00"
},
{
dt: 1579446000,
main: {
temp: -5.49,
feels_like: -14.09,
temp_min: -5.49,
temp_max: -5.49,
pressure: 1017,
sea_level: 1017,
grnd_level: 993,
humidity: 93,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 8.35,
deg: 259
},
snow: {
3h: 0.44
},
sys: {
pod: "n"
},
dt_txt: "2020-01-19 15:00:00"
},
{
dt: 1579456800,
main: {
temp: -7.13,
feels_like: -14.41,
temp_min: -7.13,
temp_max: -7.13,
pressure: 1019,
sea_level: 1019,
grnd_level: 994,
humidity: 93,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 6.26,
deg: 267
},
snow: {
3h: 0.5
},
sys: {
pod: "n"
},
dt_txt: "2020-01-19 18:00:00"
},
{
dt: 1579467600,
main: {
temp: -10.7,
feels_like: -17.06,
temp_min: -10.7,
temp_max: -10.7,
pressure: 1022,
sea_level: 1022,
grnd_level: 997,
humidity: 93,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 4.56,
deg: 270
},
snow: {
3h: 0.13
},
sys: {
pod: "n"
},
dt_txt: "2020-01-19 21:00:00"
},
{
dt: 1579478400,
main: {
temp: -16.48,
feels_like: -22.43,
temp_min: -16.48,
temp_max: -16.48,
pressure: 1026,
sea_level: 1026,
grnd_level: 1000,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 97
},
wind: {
speed: 3.55,
deg: 265
},
snow: {
3h: 0.06
},
sys: {
pod: "n"
},
dt_txt: "2020-01-20 00:00:00"
},
{
dt: 1579489200,
main: {
temp: -20.08,
feels_like: -25.55,
temp_min: -20.08,
temp_max: -20.08,
pressure: 1027,
sea_level: 1027,
grnd_level: 1001,
humidity: 98,
temp_kf: 0
},
weather: [
{
id: 803,
main: "Clouds",
description: "облачно с прояснениями",
icon: "04d"
}
],
clouds: {
all: 65
},
wind: {
speed: 2.67,
deg: 272
},
sys: {
pod: "d"
},
dt_txt: "2020-01-20 03:00:00"
},
{
dt: 1579500000,
main: {
temp: -16.86,
feels_like: -21.96,
temp_min: -16.86,
temp_max: -16.86,
pressure: 1028,
sea_level: 1028,
grnd_level: 1003,
humidity: 94,
temp_kf: 0
},
weather: [
{
id: 803,
main: "Clouds",
description: "облачно с прояснениями",
icon: "04d"
}
],
clouds: {
all: 81
},
wind: {
speed: 2.3,
deg: 250
},
sys: {
pod: "d"
},
dt_txt: "2020-01-20 06:00:00"
},
{
dt: 1579510800,
main: {
temp: -16.57,
feels_like: -21.56,
temp_min: -16.57,
temp_max: -16.57,
pressure: 1028,
sea_level: 1028,
grnd_level: 1002,
humidity: 95,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04d"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.16,
deg: 232
},
sys: {
pod: "d"
},
dt_txt: "2020-01-20 09:00:00"
},
{
dt: 1579521600,
main: {
temp: -21.23,
feels_like: -26.05,
temp_min: -21.23,
temp_max: -21.23,
pressure: 1029,
sea_level: 1029,
grnd_level: 1003,
humidity: 99,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 1.7,
deg: 236
},
sys: {
pod: "n"
},
dt_txt: "2020-01-20 12:00:00"
},
{
dt: 1579532400,
main: {
temp: -22.48,
feels_like: -26.73,
temp_min: -22.48,
temp_max: -22.48,
pressure: 1028,
sea_level: 1028,
grnd_level: 1002,
humidity: 99,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 0.83,
deg: 236
},
sys: {
pod: "n"
},
dt_txt: "2020-01-20 15:00:00"
},
{
dt: 1579543200,
main: {
temp: -21.77,
feels_like: -25.84,
temp_min: -21.77,
temp_max: -21.77,
pressure: 1027,
sea_level: 1027,
grnd_level: 1001,
humidity: 98,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 0.59,
deg: 124
},
sys: {
pod: "n"
},
dt_txt: "2020-01-20 18:00:00"
},
{
dt: 1579554000,
main: {
temp: -19.05,
feels_like: -23.79,
temp_min: -19.05,
temp_max: -19.05,
pressure: 1025,
sea_level: 1025,
grnd_level: 1000,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 1.67,
deg: 110
},
sys: {
pod: "n"
},
dt_txt: "2020-01-20 21:00:00"
},
{
dt: 1579564800,
main: {
temp: -16.15,
feels_like: -21.22,
temp_min: -16.15,
temp_max: -16.15,
pressure: 1023,
sea_level: 1023,
grnd_level: 997,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.31,
deg: 88
},
snow: {
3h: 0.25
},
sys: {
pod: "n"
},
dt_txt: "2020-01-21 00:00:00"
},
{
dt: 1579575600,
main: {
temp: -12.95,
feels_like: -18.03,
temp_min: -12.95,
temp_max: -12.95,
pressure: 1020,
sea_level: 1020,
grnd_level: 995,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.56,
deg: 96
},
snow: {
3h: 0.56
},
sys: {
pod: "d"
},
dt_txt: "2020-01-21 03:00:00"
},
{
dt: 1579586400,
main: {
temp: -9.32,
feels_like: -13.64,
temp_min: -9.32,
temp_max: -9.32,
pressure: 1019,
sea_level: 1019,
grnd_level: 994,
humidity: 94,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 1.79,
deg: 115
},
snow: {
3h: 0.94
},
sys: {
pod: "d"
},
dt_txt: "2020-01-21 06:00:00"
},
{
dt: 1579597200,
main: {
temp: -7.69,
feels_like: -11.9,
temp_min: -7.69,
temp_max: -7.69,
pressure: 1017,
sea_level: 1017,
grnd_level: 993,
humidity: 95,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 1.84,
deg: 139
},
snow: {
3h: 1.13
},
sys: {
pod: "d"
},
dt_txt: "2020-01-21 09:00:00"
},
{
dt: 1579608000,
main: {
temp: -7.5,
feels_like: -12.06,
temp_min: -7.5,
temp_max: -7.5,
pressure: 1018,
sea_level: 1018,
grnd_level: 994,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.37,
deg: 158
},
snow: {
3h: 1.19
},
sys: {
pod: "n"
},
dt_txt: "2020-01-21 12:00:00"
},
{
dt: 1579618800,
main: {
temp: -6.04,
feels_like: -10.96,
temp_min: -6.04,
temp_max: -6.04,
pressure: 1019,
sea_level: 1019,
grnd_level: 994,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.07,
deg: 193
},
snow: {
3h: 1.31
},
sys: {
pod: "n"
},
dt_txt: "2020-01-21 15:00:00"
},
{
dt: 1579629600,
main: {
temp: -5.72,
feels_like: -10.11,
temp_min: -5.72,
temp_max: -5.72,
pressure: 1020,
sea_level: 1020,
grnd_level: 995,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.36,
deg: 217
},
snow: {
3h: 1.19
},
sys: {
pod: "n"
},
dt_txt: "2020-01-21 18:00:00"
},
{
dt: 1579640400,
main: {
temp: -7.71,
feels_like: -12.16,
temp_min: -7.71,
temp_max: -7.71,
pressure: 1020,
sea_level: 1020,
grnd_level: 996,
humidity: 95,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.18,
deg: 247
},
snow: {
3h: 0.56
},
sys: {
pod: "n"
},
dt_txt: "2020-01-21 21:00:00"
},
{
dt: 1579651200,
main: {
temp: -9.18,
feels_like: -13.45,
temp_min: -9.18,
temp_max: -9.18,
pressure: 1021,
sea_level: 1021,
grnd_level: 997,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 1.77,
deg: 233
},
snow: {
3h: 0.25
},
sys: {
pod: "n"
},
dt_txt: "2020-01-22 00:00:00"
},
{
dt: 1579662000,
main: {
temp: -8.9,
feels_like: -12.63,
temp_min: -8.9,
temp_max: -8.9,
pressure: 1021,
sea_level: 1021,
grnd_level: 997,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 1.03,
deg: 138
},
snow: {
3h: 0.5
},
sys: {
pod: "d"
},
dt_txt: "2020-01-22 03:00:00"
},
{
dt: 1579672800,
main: {
temp: -6.38,
feels_like: -11.54,
temp_min: -6.38,
temp_max: -6.38,
pressure: 1020,
sea_level: 1020,
grnd_level: 996,
humidity: 94,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.34,
deg: 115
},
snow: {
3h: 0.5
},
sys: {
pod: "d"
},
dt_txt: "2020-01-22 06:00:00"
},
{
dt: 1579683600,
main: {
temp: -5.07,
feels_like: -9.49,
temp_min: -5.07,
temp_max: -5.07,
pressure: 1019,
sea_level: 1019,
grnd_level: 996,
humidity: 94,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.46,
deg: 153
},
snow: {
3h: 0.44
},
sys: {
pod: "d"
},
dt_txt: "2020-01-22 09:00:00"
},
{
dt: 1579694400,
main: {
temp: -5.59,
feels_like: -10.04,
temp_min: -5.59,
temp_max: -5.59,
pressure: 1020,
sea_level: 1020,
grnd_level: 996,
humidity: 96,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.47,
deg: 185
},
snow: {
3h: 1.44
},
sys: {
pod: "n"
},
dt_txt: "2020-01-22 12:00:00"
},
{
dt: 1579705200,
main: {
temp: -4.85,
feels_like: -12.04,
temp_min: -4.85,
temp_max: -4.85,
pressure: 1021,
sea_level: 1021,
grnd_level: 997,
humidity: 93,
temp_kf: 0
},
weather: [
{
id: 601,
main: "Snow",
description: "снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 6.43,
deg: 235
},
snow: {
3h: 2
},
sys: {
pod: "n"
},
dt_txt: "2020-01-22 15:00:00"
},
{
dt: 1579716000,
main: {
temp: -5.86,
feels_like: -11.26,
temp_min: -5.86,
temp_max: -5.86,
pressure: 1022,
sea_level: 1022,
grnd_level: 998,
humidity: 88,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13n"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.64,
deg: 223
},
snow: {
3h: 0.19
},
sys: {
pod: "n"
},
dt_txt: "2020-01-22 18:00:00"
},
{
dt: 1579726800,
main: {
temp: -8.83,
feels_like: -13.82,
temp_min: -8.83,
temp_max: -8.83,
pressure: 1022,
sea_level: 1022,
grnd_level: 998,
humidity: 86,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.68,
deg: 171
},
sys: {
pod: "n"
},
dt_txt: "2020-01-22 21:00:00"
},
{
dt: 1579737600,
main: {
temp: -7.72,
feels_like: -12.72,
temp_min: -7.72,
temp_max: -7.72,
pressure: 1021,
sea_level: 1021,
grnd_level: 997,
humidity: 82,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.75,
deg: 153
},
sys: {
pod: "n"
},
dt_txt: "2020-01-23 00:00:00"
},
{
dt: 1579748400,
main: {
temp: -7.35,
feels_like: -11.98,
temp_min: -7.35,
temp_max: -7.35,
pressure: 1020,
sea_level: 1020,
grnd_level: 996,
humidity: 80,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04d"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.23,
deg: 172
},
sys: {
pod: "d"
},
dt_txt: "2020-01-23 03:00:00"
},
{
dt: 1579759200,
main: {
temp: -3.21,
feels_like: -7.78,
temp_min: -3.21,
temp_max: -3.21,
pressure: 1018,
sea_level: 1018,
grnd_level: 995,
humidity: 77,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04d"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.56,
deg: 190
},
sys: {
pod: "d"
},
dt_txt: "2020-01-23 06:00:00"
},
{
dt: 1579770000,
main: {
temp: -1.63,
feels_like: -5.97,
temp_min: -1.63,
temp_max: -1.63,
pressure: 1017,
sea_level: 1017,
grnd_level: 994,
humidity: 81,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04d"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.56,
deg: 183
},
sys: {
pod: "d"
},
dt_txt: "2020-01-23 09:00:00"
},
{
dt: 1579780800,
main: {
temp: -2.29,
feels_like: -7.42,
temp_min: -2.29,
temp_max: -2.29,
pressure: 1017,
sea_level: 1017,
grnd_level: 994,
humidity: 81,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.59,
deg: 218
},
sys: {
pod: "n"
},
dt_txt: "2020-01-23 12:00:00"
},
{
dt: 1579791600,
main: {
temp: -3.13,
feels_like: -7.82,
temp_min: -3.13,
temp_max: -3.13,
pressure: 1017,
sea_level: 1017,
grnd_level: 994,
humidity: 83,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 2.88,
deg: 202
},
sys: {
pod: "n"
},
dt_txt: "2020-01-23 15:00:00"
},
{
dt: 1579802400,
main: {
temp: -4.08,
feels_like: -9.46,
temp_min: -4.08,
temp_max: -4.08,
pressure: 1017,
sea_level: 1017,
grnd_level: 994,
humidity: 79,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.66,
deg: 207
},
sys: {
pod: "n"
},
dt_txt: "2020-01-23 18:00:00"
},
{
dt: 1579813200,
main: {
temp: -4.24,
feels_like: -9.58,
temp_min: -4.24,
temp_max: -4.24,
pressure: 1017,
sea_level: 1017,
grnd_level: 994,
humidity: 78,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.55,
deg: 208
},
sys: {
pod: "n"
},
dt_txt: "2020-01-23 21:00:00"
},
{
dt: 1579824000,
main: {
temp: -3.41,
feels_like: -8.58,
temp_min: -3.41,
temp_max: -3.41,
pressure: 1017,
sea_level: 1017,
grnd_level: 994,
humidity: 80,
temp_kf: 0
},
weather: [
{
id: 804,
main: "Clouds",
description: "пасмурно",
icon: "04n"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.46,
deg: 203
},
sys: {
pod: "n"
},
dt_txt: "2020-01-24 00:00:00"
},
{
dt: 1579834800,
main: {
temp: -2.52,
feels_like: -7.7,
temp_min: -2.52,
temp_max: -2.52,
pressure: 1017,
sea_level: 1017,
grnd_level: 993,
humidity: 84,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.7,
deg: 204
},
snow: {
3h: 0.13
},
sys: {
pod: "d"
},
dt_txt: "2020-01-24 03:00:00"
},
{
dt: 1579845600,
main: {
temp: 0,
feels_like: -6.19,
temp_min: 0,
temp_max: 0,
pressure: 1018,
sea_level: 1018,
grnd_level: 994,
humidity: 86,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 5.6,
deg: 226
},
snow: {
3h: 0.44
},
sys: {
pod: "d"
},
dt_txt: "2020-01-24 06:00:00"
},
{
dt: 1579856400,
main: {
temp: 0.52,
feels_like: -3.77,
temp_min: 0.52,
temp_max: 0.52,
pressure: 1018,
sea_level: 1018,
grnd_level: 994,
humidity: 88,
temp_kf: 0
},
weather: [
{
id: 600,
main: "Snow",
description: "небольшой снег",
icon: "13d"
}
],
clouds: {
all: 100
},
wind: {
speed: 3.04,
deg: 225
},
snow: {
3h: 0.31
},
sys: {
pod: "d"
},
dt_txt: "2020-01-24 09:00:00"
}
],
city: {
id: 1510018,
name: "Бийск",
coord: {
lat: 52.5364,
lon: 85.2072
},
country: "RU",
population: 215430,
timezone: 25200,
sunrise: 1579400374,
sunset: 1579430357
}
}
"""