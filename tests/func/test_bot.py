# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bot.py находясь в текущем каталоге func

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


def test_create_bot_from_my_bot_class(mock_obj_vk_api,
                                      mock_long_poll,
                                      mock_vk_api_get,
                                      mock_response_requests_get,
                                      mock_users_info,
                                      ):
    bot = VKBot()
    print(f"From test==bot.vk_api_obj.get_api()=={bot.vk_api_obj.get_api}")

    event = None
    print(f"From test==bot.vk_bot_pollster.listen=={bot.vk_bot_pollster.listen}")
    for event in bot.vk_bot_pollster.listen(cmd=CMD_START):
        # print(event.object)
        bot.on_event(event=event)
    assert event.object['message']['text'] == 'Начать'


# @pytest.mark.parametrize(argnames="cmd", argvalues=CMD_LST)
# def test_run_bot_from_my_bot_class(cmd, mock_vk_api, mock_long_poll):
#     bot = VkBotTest(mock_vk_api=mock_vk_api, mock_long_poll=mock_long_poll)
#     event = None
#     for event in bot.vk_bot_pollster.listen(cmd=cmd):
#         bot.on_event(event=event)
#     assert event.object['message']['text'] == CMD_LST_revers.pop()

