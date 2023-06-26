from aiogram import types

import bot.additions.chat_setting as chat_setting
from bot.config import CHAT_ID, ADMIN_ID
from bot.data_base.db import UserTable, StatisticsTable


async def help(message: types.Message):
    if check_for_administrator_access(message) is False: return
    await message.reply('Список команд:\n'
                        '/helpAdmin - это сообщение\n'
                        '/setNotify (True/False) - включить/выключить уведомления\n'
                        '/notifyChat (Текс) - отправить сообщение в главный чат\n'
                        '/addUser - добавить пользователя в таблицу\n'
                        '/deleteUser - удалить пользователя из таблицы\n'
                        '/getUsers - получить список пользователей\n')


async def set_permission_to_notify_users(message: types.Message):
    if check_for_administrator_access(message) is False: return
    input_str = message.text.replace('/setNotify', '').lower().strip()
    if input_str in ['true', '1', 'да']:
        chat_setting.is_notifications = True
        await message.reply('Уведомления включены')
    elif input_str in ['false', '0', 'нет']:
        chat_setting.is_notifications = False
        await message.reply('Уведомления выключены')


async def send_chat_message(message: types.Message):
    if check_for_administrator_access(message) is False: return

    text = message.text.replace('/notifyChat', '')
    await message.bot.send_message(chat_id=CHAT_ID, text=text)
    # await message.bot.send_message(chat_id=message.chat.id, text=text)


async def add_user_in_user_table(message: types.Message):
    if check_for_administrator_access(message) is False: return




async def delete_user_in_user_table(message: types.Message):
    if check_for_administrator_access(message) is False: return
    StatisticsTable.delete_stat(message.from_user.id)
    UserTable.delete_user(message.from_user.id)


def check_for_administrator_access(message: types.Message):
    return message.from_user.id == ADMIN_ID
