from aiogram import types

import bot.additions.chat_setting as chat_setting


async def help(message: types.Message):
    await message.reply("Список команд:\n"
                        "/help - это сообщение\n"
                        "/helpAll - все команды\n"
                        "/helpCommands - команды для участников\n"
                        "/helpAdmin - команды для администраторов\n"
                        "/helpOpenai - команды для работы с OpenAI\n"
                        "/helpStatistics - команды для работы со статистикой\n"
                        "/info - информация о боте\n")


async def info(message: types.Message):
    text = 'Информация о боте:\n'
    if chat_setting.is_notifications:
        text += 'Уведомления участников включены'
    else:
        text += 'Уведомления участников выключены'

    await message.reply(text)
