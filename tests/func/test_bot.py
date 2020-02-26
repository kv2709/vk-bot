# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bot.py находясь в текущем каталоге func

from setup import *
from bot import VKBot
import pytest

CMD_LST_revers = CMD_LST.copy()
CMD_LST_revers.reverse()


def test_create_bot_from_my_bot_class(mock_response_requests_get,
                                      mock_response_requests_post,
                                      mock_obj_vk_api,
                                      mock_long_poll,
                                      mock_vk_api_get,
                                      mock_users_get_messages_send,
                                      ):
    bot = VKBot()
    for bot.event in bot.vk_bot_pollster.listen(cmd=CMD_START):
        bot.on_event_from_dict()
    assert bot.event.object['message']['text'] == 'Начать'
    assert bot.user_info[0]['first_name'] == 'Urik'
    assert bot.message_send_exec_code == 600
    assert bot.log_send_status_code == 2000


def test_bot_for_no_command(mock_response_requests_get,
                            mock_response_requests_post,
                            mock_obj_vk_api,
                            mock_long_poll,
                            mock_vk_api_get,
                            mock_users_get_messages_send,
                            ):
    bot = VKBot()
    for bot.event in bot.vk_bot_pollster.listen(cmd=CMD_NO_COMMAND):
        bot.on_event_from_dict()
    assert bot.event.object['message']['text'] == CMD_NO_COMMAND
    assert bot.user_info[0]['first_name'] == 'Urik'
    assert bot.message_send_exec_code == 600
    assert bot.log_send_status_code == 2000


@pytest.mark.parametrize(argnames="cmd", argvalues=CMD_LST)
def test_run_bot_from_my_bot_class(cmd,
                                   mock_response_requests_get,
                                   mock_response_requests_post,
                                   mock_obj_vk_api,
                                   mock_long_poll,
                                   mock_vk_api_get,
                                   mock_users_get_messages_send,
                                   ):
    bot = VKBot()
    for bot.event in bot.vk_bot_pollster.listen(cmd=cmd):
        bot.on_event_from_dict()
    assert bot.event.object['message']['text'] == CMD_LST_revers.pop()
    assert bot.message_send_exec_code == 600
