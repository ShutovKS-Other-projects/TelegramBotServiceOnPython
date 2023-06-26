import re

from aiogram import types

import bot.handlers.commands.commands_dictionary as commands_dictionary
from bot.config import CHAT_ID, ADMIN_ID
from bot.handlers.observers import data_base


async def handler_text_commands(message: types.Message):
    if check_where_the_message_is_from(message) is False: return

    command = message.text.split()[0]

    if command[0] == '/':
        command = re.sub(r'(@\w+)', '', command)
        command = command.strip()
        print(command)

    if command in commands_dictionary.command_handlers:
        handlers = commands_dictionary.command_handlers[command]
        for handler in handlers:
            await handler(message)


async def handler_any(message: types.Message):
    if message.chat.id == CHAT_ID is False: return
    match message.content_type:
        case types.ContentTypes.NEW_CHAT_MEMBERS:
            await data_base.handler_new_chat_members(message)
        case types.ContentTypes.LEFT_CHAT_MEMBER:
            await data_base.handler_left_chat_member(message)

    await data_base.handler_message(message)


def check_where_the_message_is_from(message: types.Message):
    return message.chat.id == CHAT_ID \
        or message.from_user.id == ADMIN_ID
