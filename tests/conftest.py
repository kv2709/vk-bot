import json
import time
import pytest
from vk_api.bot_longpoll import *
from vk_api.vk_api import *


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Авто-фикстура: Отчет о времени начала и конца сессии"""
    yield
    now = time.time()
    print('\n-----------------')
    print('Окончание теста : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Авто-фикстура: Сообщает продолжительность теста после каждой функции."""
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


# Неиспользованные класс и фикстура для объекта vk_api.VkApi
# Реализация полной изоляции Бота от работы с внешними источниками данных
# Слишком сложна и малооправдана
class MockVkApi:
    @staticmethod
    def get_api():
        return "VkApi"


@pytest.fixture()
def mock_vk_api(monkeypatch):
    def mock_get_api(*args, **kwargs):
        return MockVkApi()

    monkeypatch.setattr("vk_api.VkApi", mock_get_api)


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
