import json
import time
import pytest


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    now = time.time()
    print('\n-----------------')
    print('Окончание теста : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))


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


# Манкипатчнутый requests.get перемещенный в фикстуру
@pytest.fixture()
def mock_response_requests_get(monkeypatch):
    """
    Любые аргументы могут быть переданы в mock_get()
    и она всегда будет возвращать мокнутый объект,
    который имеет единственный метод json().
    """
    def mock_get(*args, **kwargs):
        return MockResponseJson()

    monkeypatch.setattr("requests.get", mock_get)



