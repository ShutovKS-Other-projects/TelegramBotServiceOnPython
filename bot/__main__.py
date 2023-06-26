import logging

from aiogram import Bot, Dispatcher, executor, types

from bot import config, main_handler

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo(message: types.Message):
    await main_handler.handler_text(message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
