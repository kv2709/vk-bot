# -*- coding: utf-8 -*-
# Запуск тестов командой pytest -v -k test_bot.py находясь в текущем каталоге func

from bot import VKBot, UserState
import pytest
from tests.test_const import *


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
    assert bot.user_info[0]['last_name'] == 'Kireev'
    assert bot.message_from_bot == CMD_START_ANSWER
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
    assert bot.user_info[0]['last_name'] == 'Kireev'
    assert bot.message_from_bot == CMD_NO_COMMAND_ANSWER
    assert bot.message_send_exec_code == 600
    assert bot.log_send_status_code == 2000


@pytest.mark.parametrize(argnames="cmd", argvalues=CMD_LST)
def test_bot_for_list_commands(cmd,
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
    assert bot.message_from_bot == CMD_LST_ANSWER_revers.pop()
    assert bot.message_send_exec_code == 600


def test_bot_for_select_registration_conference(mock_response_requests_get,
                                                mock_response_requests_post,
                                                mock_obj_vk_api,
                                                mock_long_poll,
                                                mock_vk_api_get,
                                                mock_users_get_messages_send,
                                                ):
    bot = VKBot()
    for bot.event in bot.vk_bot_pollster.listen(cmd=CMD_SIGN_UP_FOR_CONFERENCE):
        bot.on_event_from_dict()
    assert bot.event.object['message']['text'] == CMD_SIGN_UP_FOR_CONFERENCE
    assert bot.status_bot_sing_up_conf
    assert bot.message_from_bot == "Бот переключен в режим <Регистрация на конференцию>"
    assert bot.message_send_exec_code == 600


@pytest.mark.parametrize(argnames="cmd", argvalues=REG_CONF_INTENTS_LST_INPUT)
def test_bot_for_intents_registration_conference(cmd,
                                                 mock_response_requests_get,
                                                 mock_response_requests_post,
                                                 mock_obj_vk_api,
                                                 mock_long_poll,
                                                 mock_vk_api_get,
                                                 mock_users_get_messages_send,
                                                 ):
    bot = VKBot()
    for bot.event in bot.vk_bot_pollster.listen(cmd=cmd):
        bot.status_bot_sing_up_conf = True
        bot.on_event_from_dict()
    assert bot.event.object['message']['text'] == REG_CONF_INTENTS_LST_INPUT_revers.pop()
    assert bot.message_from_bot == REG_CONF_INTENTS_LST_ANSWER_revers.pop()
    assert bot.message_send_exec_code == 600


@pytest.mark.parametrize(argnames=("cmd", "scenario_name", "step_name", "context"),
                         argvalues=REG_CONF_SCENARIO_LST_INPUT)
def test_bot_for_scenario_registration_conference(cmd, scenario_name, step_name, context,
                                                  mock_response_requests_get,
                                                  mock_response_requests_post,
                                                  mock_obj_vk_api,
                                                  mock_long_poll,
                                                  mock_vk_api_get,
                                                  mock_users_get_messages_send,
                                                  ):
    bot = VKBot()
    for bot.event in bot.vk_bot_pollster.listen(cmd=cmd):
        bot.status_bot_sing_up_conf = True
        if scenario_name:
            bot.user_states[77209884] = UserState(scenario_name=scenario_name, step_name=step_name, context=context)
        bot.on_event_from_dict()
    assert bot.event.object['message']['text'] == REG_CONF_SCENARIO_LST_INPUT_revers.pop()[0]
    assert bot.message_from_bot == REG_CONF_SCENARIO_LST_ANSWER_revers.pop()
    assert bot.message_send_exec_code == 600
