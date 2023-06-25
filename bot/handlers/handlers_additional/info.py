from aiogram import types

import bot.additions.chat_setting as chat_setting


async def help(message: types.Message):
    await message.reply("Список команд:\n"
                        "/help - это сообщение\n"
                        # "/helpAdmin - команды для администраторов\n"
                        "/helpCommands - команды для участников\n"
                        "/helpOpenai - команды для работы с OpenAI\n"
                        "/helpAll - все команды\n"
                        "/info - информация о боте\n")


async def info(message: types.Message):
    text = 'Информация о боте:\n'
    if chat_setting.is_notifications:
        text += 'Уведомления участников включены'
    else:
        text += 'Уведомления участников выключены'

    await message.reply(text)
