from aiogram import types

import bot.additions.chat_setting as chat_setting
import bot.config as config


async def help(message: types.Message):
    if check_for_administrator_access(message) is False: return
    await message.reply('Список команд:\n'
                        '/helpAdmin - это сообщение\n'
                        '/setNotify (True/False) - включить/выключить уведомления\n'
                        '/notifyChat (Текс) - отправить сообщение в главный чат')


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
    await message.bot.send_message(chat_id=config.CHAT_ID, text=text)
    # await message.bot.send_message(chat_id=message.chat.id, text=text)


def check_for_administrator_access(message: types.Message):
    return message.from_user.id == config.ADMIN_ID
