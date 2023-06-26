from aiogram import types
from aiogram.types import ChatMemberOwner, ChatMemberAdministrator

import bot.additions.chat_setting as chat_setting
from bot.config import ADMIN_ID
from bot.data_base.db import UserTable


async def help(message: types.Message):
    await message.reply("Список команд:\n"
                        "/helpCommands - это сообщение\n"
                        "/pingAll - уведомить всех участников\n"
                        "/pingAdmins - уведомить всех администраторов\n")


async def participant_notifications(message: types.Message):
    if chat_setting.is_notifications or message.from_user.id == ADMIN_ID:
        text = ''

        members_list = UserTable.get_all_user_id()
        if message.from_user.id in members_list:
            members_list.remove(message.from_user.id)

        if len(members_list) == 0:
            await message.reply('Участников нет')
            return

        for id_user in members_list:
            try:
                member = await message.chat.get_member(id_user)
                text += f'@{member.user.username}, '
            except:
                print(f'Пользователь {id_user} не найден в чате {message.chat.title}')

        text = f'Пользователь @{message.from_user.username} запросил созвать всех\n' \
               'Участники:\n' + text

        await message.reply(text)


async def administration_notifications(message: types.Message):
    if chat_setting.is_notifications or message.from_user.id == ADMIN_ID:
        text = ''

        admins: list[ChatMemberOwner | ChatMemberAdministrator] = await message.chat.get_administrators()

        if admins is not None:
            text = 'Администраторов нет'
        else:
            for admin in admins:  # type: ChatMemberOwner | ChatMemberAdministrator
                if message.from_user.id == admin.user.id: continue
                text += f'@{admin.user.username}, '

            text = f'Пользователь @{message.from_user.username} запросил уведомление всех администраторов\n' \
                   'Администраторы:\n' + text

        await message.reply(text)
