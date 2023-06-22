import logging

from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_API_TOKEN, OPENAI_API_TOKEN

from bot.additions.chat_setting import ChatSetting
from bot.additions.openai_request import OpenaiRequest

from bot.handlers.commands_handlers_for_admin import CommandsHandlersForAdmin
from bot.handlers.commands_handlers import MessageHandlersCommands
from bot.handlers.message_handlers import MessageHandlers

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    openai_request = OpenaiRequest(token=OPENAI_API_TOKEN)
    bot = Bot(token=BOT_API_TOKEN)
    dp = Dispatcher(bot)

    chat_setting = ChatSetting()

    commands_handlers = MessageHandlersCommands(dp, bot, chat_setting, openai_request)
    commands_handlers_for_admin = CommandsHandlersForAdmin(dp, bot, chat_setting)
    message_handlers = MessageHandlers(dp, bot, chat_setting)

    dp.register_message_handler(commands_handlers.send_info, commands=['info'])
    dp.register_message_handler(commands_handlers.send_welcome, commands=['start', 'help'])
    dp.register_message_handler(commands_handlers.send_request_in_openai, commands=['request'])
    dp.register_message_handler(commands_handlers.send_generate_image, commands=['generate_image'])
    dp.register_message_handler(commands_handlers.send_participant_notifications, commands=['pingAll'])
    dp.register_message_handler(commands_handlers.send_administration_notifications, commands=['pingAdmins'])

    dp.register_message_handler(commands_handlers_for_admin.send_help, commands=['helpAdmin'])
    dp.register_message_handler(commands_handlers_for_admin.send_chat_message, commands=['notifyChat'])
    dp.register_message_handler(commands_handlers_for_admin.set_permission_to_notify_users, commands=['setNotify'])

    dp.register_message_handler(message_handlers.echo)

    executor.start_polling(dp, skip_updates=True)
