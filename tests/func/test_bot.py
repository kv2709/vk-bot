# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bot.py находясь в текущем каталоге func

from setup import *
from bot import VKBot
import pytest

CMD_LST = [None,
           CMD_START,
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
                  CMD_START,
                  None]


def test_create_bot_from_my_bot_class(mock_response_requests_get,
                                      mock_obj_vk_api,
                                      mock_long_poll,
                                      mock_vk_api_get,
                                      mock_users_get_messages_send,
                                      ):
    bot = VKBot()
    event = None
    for event in bot.vk_bot_pollster.listen(cmd=CMD_START):
        bot.on_event(event=event)
    assert event.object['message']['text'] == 'Начать'
    assert bot.user_info[0]['first_name'] == 'Urik'
    assert bot.message_send_exec_code == 600


@pytest.mark.parametrize(argnames="cmd", argvalues=CMD_LST)
def test_run_bot_from_my_bot_class(cmd,
                                   mock_response_requests_get,
                                   mock_obj_vk_api,
                                   mock_long_poll,
                                   mock_vk_api_get,
                                   mock_users_get_messages_send,
                                   ):
    bot = VKBot()
    event = None
    for event in bot.vk_bot_pollster.listen(cmd=cmd):
        bot.on_event(event=event)
    assert event.object['message']['text'] == CMD_LST_revers.pop()
    assert bot.message_send_exec_code == 600
