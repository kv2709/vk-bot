# -*- coding: utf-8 -*-

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from weather_request import WeatherGetter
from setup import *
from bot import VKBot
import pytest
import vk_api


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
    @staticmethod
    def listen():
        while True:
            for event in event_list:
                yield event


@pytest.fixture()
def mock_long_poll(monkeypatch):
    def mock_listen(*args, **kwargs):
        return MockVkBotLongPoll()

    monkeypatch.setattr("vk_api.bot_longpoll.VkBotLongPoll", mock_listen)


class VkBotTest(VKBot):
    def __init__(self, mock_vk_api=None, mock_long_poll=None):
        super().__init__()
        self.vk_api_obj = vk_api.VkApi(token=TOKEN_API)
        self.vk_api_get = self.vk_api_obj.get_api()
        self.vk_bot_pollster = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk_api_obj, group_id=GROUP_ID)


def test_create_bot_from_my_bot_class(mock_vk_api, mock_long_poll):
    bot = VkBotTest(mock_vk_api=mock_vk_api, mock_long_poll=mock_long_poll)
    assert bot.vk_bot_pollster.listen() == "Listener"
    assert bot.vk_api_get == "VkApi"



# def test_run_bot(mock_vk_api, mock_long_poll):
#     vk_api_obj = vk_api.VkApi(token=TOKEN_API)
#     vk_api_get = vk_api_obj.get_api()
#     vk_bot_pollster = vk_api.bot_longpoll.VkBotLongPoll(vk=vk_api_obj, group_id=GROUP_ID)
#
#     assert vk_bot_pollster.listen() == "Listener"
#     assert vk_api_get == "VkApi"
