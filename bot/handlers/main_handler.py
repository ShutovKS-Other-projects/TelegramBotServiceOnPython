import re

from aiogram import types

import bot.handlers.commands.commands_dictionary as commands_dictionary
from bot.config import CHAT_ID, ADMIN_ID


async def handler_text(message: types.Message):
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


def check_where_the_message_is_from(message: types.Message):
    return message.chat.id == CHAT_ID \
        or message.from_user.id == ADMIN_ID
