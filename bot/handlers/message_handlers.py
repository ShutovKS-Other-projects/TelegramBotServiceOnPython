from aiogram import Bot, Dispatcher, types
from bot.additions.chat_setting import ChatSetting


class MessageHandlers:
    def __init__(self, dp: Dispatcher, bot: Bot, chat_setting: ChatSetting):
        self.__dp = dp
        self.__chat_setting = chat_setting
        self.__bot = bot

    async def echo(self, message: types.Message):
        if self.__chat_setting.is_notifications:
            await message.reply(message.text)
