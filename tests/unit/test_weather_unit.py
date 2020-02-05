# -*- coding: utf-8 -*-

# Запуск тестов командой pytest -v -k test_weather_unit.py находясь в текущем каталоге
from weather_request import WeatherGetter
import pytest

WIND_DIRECT_TEST = [' С', 'СВ', ' В', 'ЮВ', ' Ю', 'ЮЗ', ' З', 'СЗ']

wg = WeatherGetter()


def test_object():
    assert str(type(wg)) == "<class 'weather_request.WeatherGetter'>"


@pytest.mark.parametrize(argnames="wind_deg", argvalues=[315, 270, 225, 180, 135, 90, 45, 0])
def test_wind_direct(wind_deg):
    direct = wg.get_wind_direction(wind_deg=wind_deg)
    assert WIND_DIRECT_TEST.pop() == direct


def test_get_current_weather(mock_response_requests_get):
    weather_str = wg.get_current_weather(1)
    assert weather_str == "Бийск\n28 января 2020 года 17:28\nтемп: -3.0C ветер: 3.8м/с ЮЗ\nпасмурно\n"


def test_get_current_weather_for_city_list(mock_response_requests_get):
    weather_str = wg.get_current_weather_for_city_list(1, 2, 3)
    assert weather_str == f"Бийск\n28 января 2020 года 17:28\nтемп: -3.0C ветер: 3.8м/с ЮЗ\nпасмурно\n{'-'*50}\n" \
                          f"Бийск\n28 января 2020 года 17:28\nтемп: -3.0C ветер: 3.8м/с ЮЗ\nпасмурно\n{'-'*50}\n" \
                          f"Бийск\n28 января 2020 года 17:28\nтемп: -3.0C ветер: 3.8м/с ЮЗ\nпасмурно\n{'-'*50}\n"

