import asyncio
import threading

from aiogram import types

from bot.data_base.db import StatisticsTable

message_stack_in_five_minutes: dict[int, dict[str, int]] = {}


async def update_statistics():
    while True:
        for user_id in message_stack_in_five_minutes:
            message_count = message_stack_in_five_minutes[user_id]['message_count']
            image_count = message_stack_in_five_minutes[user_id]['media_count']
            sticker_count = message_stack_in_five_minutes[user_id]['sticker_count']

            id: int = int(user_id)
            StatisticsTable.increase_stat(id, message_count, image_count, sticker_count)

        message_stack_in_five_minutes.clear()
        await asyncio.sleep(10)


async def init():
    await update_statistics()


def start_statistics_observer():
    print('Starting statistics observer...')
    asyncio.run(init())
    print('Statistics observer started!')


# Запуск потока для запуска асинхронного кода
thread = threading.Thread(target=start_statistics_observer)
thread.start()


async def handler_message(message: types.Message):
    if message.from_user.id not in message_stack_in_five_minutes:
        message_stack_in_five_minutes[message.from_user.id] = {
            'message_count': 0,
            'media_count': 0,
            'sticker_count': 0
        }

    message_stack_in_five_minutes[message.from_user.id]['message_count'] += 1

    if message.content_type == 'sticker':
        message_stack_in_five_minutes[message.from_user.id]['sticker_count'] += 1

    if message.content_type == 'photo' \
            or message.content_type == 'video' \
            or message.content_type == 'audio' \
            or message.content_type == 'document':
        message_stack_in_five_minutes[message.from_user.id]['media_count'] += 1


async def handler_new_chat_members(message: types.Message):
    UserTable.add_user(message.from_user.id)
    StatisticsTable.add_stat(message.from_user.id)


async def handler_left_chat_member(message: types.Message):
    StatisticsTable.delete_stat(message.from_user.id)
    UserTable.delete_user(message.from_user.id)
