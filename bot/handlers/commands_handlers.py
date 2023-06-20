from aiogram import Bot, Dispatcher, types
from bot.config import ADMIN_ID
from bot.additions.chat_setting import ChatSetting
from bot.additions.members import members_in_chat
from typing import List
from aiogram.types import ChatMemberOwner, ChatMemberAdministrator


class MessageHandlersCommands:
    def __init__(self, dp: Dispatcher, bot: Bot, chat_setting: ChatSetting):
        self.__dp = dp
        self.__chat_setting = chat_setting
        self.__bot = bot

    async def send_welcome(self, message: types.Message):
        await message.reply("Список команд:\n"
                            "/pingAll - уведомить всех участников\n"
                            "/pingAdmins - уведомить всех администраторов\n")

    async def send_participant_notifications(self, message: types.Message):
        if self.__chat_setting.is_notifications or message.from_user.id == ADMIN_ID:
            text = ''

            members = members_in_chat.items()
            members: List[tuple[int, str]] = list(members)
            members.remove((message.from_user.id, members_in_chat[message.from_user.id]))

            for id_user, name_user in members:
                try:
                    member = await self.__bot.get_chat_member(message.chat.id, id_user)
                    text += f'@{member.user.username}, '
                except:
                    print(f'Пользователь {name_user} не найден в чате {message.chat.title}')

            if text == '':
                text = 'Участники из списка не найдены'
            else:
                text = f'Пользователь @{message.from_user.username} запросил уведомление всех участников\n' \
                       'Участники:\n' + text

            await message.reply(text)

    async def send_administration_notifications(self, message: types.Message):
        if self.__chat_setting.is_notifications or message.from_user.id == ADMIN_ID:
            text = ''

            admins: list[ChatMemberOwner | ChatMemberAdministrator] = await self.__bot.get_chat_administrators(
                message.chat.id)

            if admins is not None:
                text = 'Администраторов нет'
            else:
                for admin in admins:  # type: ChatMemberOwner | ChatMemberAdministrator
                    if message.from_user.id == admin.user.id: continue
                    text += f'@{admin.user.username}, '

                text = f'Пользователь @{message.from_user.username} запросил уведомление всех администраторов\n' \
                       'Администраторы:\n' + text

            await message.reply(text)

    async def send_info(self, message: types.Message):
        text = 'Информация о боте:\n'
        if ChatSetting.is_notifications:
            text += 'Уведомления участников включены'
        else:
            text += 'Уведомления участников выключены'

        await message.reply(text)
