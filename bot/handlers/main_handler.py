import re

from aiogram import types

import bot.config as config
import bot.handlers.commands_dictionary as commands_dictionary


async def echo_handler_text(message: types.Message):
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
    return message.chat.id == config.CHAT_ID \
        or message.from_user.id == config.ADMIN_ID
