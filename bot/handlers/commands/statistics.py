from aiogram import types

from bot.data_base.db import StatisticsTable


async def help(message: types.Message):
    await message.reply("Список команд:\n"
                        "/help - это сообщение\n"
                        "/stat - статистика о вас\n"
                        "/stat (id) - статистика пользователя\n"
                        "/statAll - статистика всех\n")


async def get_stat_by_id(message: types.Message):
    user_id = message.text.replace('/stat', '').strip()
    if user_id == '':
        await get_stat(message)
    else:
        stat = StatisticsTable.get_stat(user_id)
        if stat is None:
            await message.reply('Статистика о пользователе отсутствует')
        else:
            await message.reply(f'Статистика о пользователе:\n'
                                f'Сообщений: {stat[1]}\n'
                                f'Картинок: {stat[2]}\n'
                                f'Стикеров: {stat[3]}')


async def get_stat(message: types.Message):
    stat = StatisticsTable.get_stat(message.from_user.id)
    if stat is None:
        await message.reply('Статистика о вас отсутствует')
    else:
        await message.reply(f'Статистика о вас:\n'
                            f'Сообщений: {stat[1]}\n'
                            f'Картинок: {stat[2]}\n'
                            f'Стикеров: {stat[3]}')


async def get_stat_all(message: types.Message):
    stats = StatisticsTable.get_all_stats()

    if stats is None or stats == []:
        await message.reply('Статистика отсутствует')
    else:
        text = 'Пользователь | Сообщений | Картинок | Стикеров\n'
        for stat in stats:
            text += f'{stat[0]} | {stat[1]} | {stat[2]} | {stat[3]}\n'

        await message.reply(text)
