# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bot.py
from vk_api.bot_longpoll import VkBotLongPoll
from setup import *
from bot import VKBot
import vk_api
import pytest

CMD_LST = [CMD_START,
           CMD_BIYSK_WEATHER_NOW,
           CMD_BIYSK_WEATHER_FORECAST,
           CMD_NOVOSIBIRSK_WEATHER_NOW,
           CMD_NOVOSIBIRSK_WEATHER_FORECAST,
           CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW,
           CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW,
           CMD_MENU_ROAD_FORECAST,
           CMD_RETURN_MAIN_MENU]

CMD_LST_revers = [CMD_RETURN_MAIN_MENU,
                  CMD_MENU_ROAD_FORECAST,
                  CMD_BIYSK_KOSH_AGACH_ROAD_WEATHER_NOW,
                  CMD_BIYSK_NOVOSIBIRSK_ROAD_WEATHER_NOW,
                  CMD_NOVOSIBIRSK_WEATHER_FORECAST,
                  CMD_NOVOSIBIRSK_WEATHER_NOW,
                  CMD_BIYSK_WEATHER_FORECAST,
                  CMD_BIYSK_WEATHER_NOW,
                  CMD_START]


class VkBotTest(VKBot):
    def __init__(self, mock_vk_api=None, mock_long_poll=None):
        super().__init__()
        self.vk_api_obj = vk_api.VkApi(token=TOKEN_API)
        self.vk_bot_pollster = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk_api_obj, group_id=GROUP_ID)


def test_create_bot_from_my_bot_class(mock_vk_api, mock_long_poll):
    bot = VkBotTest(mock_vk_api=mock_vk_api, mock_long_poll=mock_long_poll)
    event = None
    for event in bot.vk_bot_pollster.listen(cmd=CMD_START):
        continue
    assert event.object['message']['text'] == 'Начать'


@pytest.mark.parametrize(argnames="cmd", argvalues=CMD_LST)
def test_run_bot_from_my_bot_class(cmd, mock_vk_api, mock_long_poll):
    bot = VkBotTest(mock_vk_api=mock_vk_api, mock_long_poll=mock_long_poll)
    event = None
    for event in bot.vk_bot_pollster.listen(cmd=cmd):
        bot.on_event(event=event)
    assert event.object['message']['text'] == CMD_LST_revers.pop()

# self.vk_api_get = self.vk_api_obj.get_api()
# assert bot.vk_api_get == "VkApi"
