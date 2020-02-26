# -*- coding: utf-8 -*-
import pytest
from vk_api.bot_longpoll import *
from vk_api.vk_api import *


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Авто-фикстура: Сообщает продолжительность теста после каждой функции."""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\nПродолжительнотсь выполения теста : {:0.3} секунд'.format(delta))


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


# ------------------------------------------------------------------------
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
