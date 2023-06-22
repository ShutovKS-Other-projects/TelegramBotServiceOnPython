from aiogram import Bot, Dispatcher, types
from bot.config import ADMIN_ID, CHAT_ID
from bot.additions.chat_setting import ChatSetting


class CommandsHandlersForAdmin:
    def __init__(self, dp: Dispatcher, bot: Bot, chat_setting: ChatSetting):
        self.__dp = dp
        self.__chat_setting = chat_setting
        self.__bot = bot

    async def send_help(self, message: types.Message):
        if message.from_user.id == ADMIN_ID:
            await message.reply('Список команд:\n'
                                '/setNotify (True/False) - включить/выключить уведомления\n'
                                '/notifyChat (Текс) - отправить сообщение в главный чат')

    async def set_permission_to_notify_users(self, message: types.Message):
        print('set_permission_to_notify_users')
        input_str = message.text.replace('/setNotify', '').lower().strip()
        if input_str in ['true', '1', 'да']:
            self.__chat_setting.is_notifications = True
            await message.reply('Уведомления включены')
        elif input_str in ['false', '0', 'нет']:
            self.__chat_setting.is_notifications = False
            await message.reply('Уведомления выключены')

    async def send_chat_message(self, message: types.Message):
        text = message.text.replace('/notifyChat', '')
        # await self.__bot.send_message(chat_id=message.chat.id, text=text)
        await self.__bot.send_message(chat_id=CHAT_ID, text=text)
