import logging

from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_API_TOKEN
from bot.additions.chat_setting import ChatSetting
from bot.handlers.commands_handlers_for_admin import CommandsHandlersForAdmin
from bot.handlers.commands_handlers import MessageHandlersCommands
from bot.handlers.message_handlers import MessageHandlers

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_API_TOKEN)
    dp = Dispatcher(bot)

    chat_setting = ChatSetting()

    commands_handlers = MessageHandlersCommands(dp, bot, chat_setting)
    commands_handlers_for_admin = CommandsHandlersForAdmin(dp, bot, chat_setting)
    message_handlers = MessageHandlers(dp, bot, chat_setting)

    dp.register_message_handler(commands_handlers.send_welcome, commands=['start', 'help'])
    dp.register_message_handler(commands_handlers.send_info, commands=['info'])
    dp.register_message_handler(commands_handlers.send_participant_notifications, commands=['pingAll'])
    dp.register_message_handler(commands_handlers.send_administration_notifications, commands=['pingAdmins'])

    dp.register_message_handler(commands_handlers_for_admin.send_help, commands=['helpAdmin'])
    dp.register_message_handler(commands_handlers_for_admin.echo)

    dp.register_message_handler(message_handlers.echo)

    executor.start_polling(dp, skip_updates=True)
