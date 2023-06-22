import base64

from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatMemberOwner, ChatMemberAdministrator

from bot.config import ADMIN_ID

from bot.additions.chat_setting import ChatSetting
from bot.additions.members import members_in_chat
from bot.additions.openai_request import OpenaiRequest


class MessageHandlersCommands:
    def __init__(self, dp: Dispatcher, bot: Bot, chat_setting: ChatSetting, openai_request: OpenaiRequest):
        self.__dp = dp
        self.__chat_setting = chat_setting
        self.__bot = bot
        self.__openai_request = openai_request

    async def send_welcome(self, message: types.Message):
        await message.reply("Список команд:\n"
                            "/pingAll - уведомить всех участников\n"
                            "/pingAdmins - уведомить всех администраторов\n"
                            "/request (Текст) - запросить информацию у OpenAI"
                            "/generate_image (Текст) - сгенерировать изображение по тексту\n")

    async def send_participant_notifications(self, message: types.Message):
        if self.__chat_setting.is_notifications or message.from_user.id == ADMIN_ID:
            text = ''

            members = members_in_chat.copy()
            members.remove(message.from_user.id)

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
        if self.ChatSetting.is_notifications:
            text += 'Уведомления участников включены'
        else:
            text += 'Уведомления участников выключены'

        await message.reply(text)

    async def send_request_in_openai(self, message: types.Message):

        if message.text.replace('/request', '').strip() == '':
            await message.reply('Запрос не может быть пустым')
            return

        def message_from_user(text: str):
            return {"role": "user", "content": text}

        def message_from_assistant(text: str):
            return {"role": "assistant", "content": text}

        text_temp = message.text.replace('/request', '')
        messages = [message_from_user(text_temp)]

        message_temp = message
        while message_temp.reply_to_message:
            message_temp = message_temp.reply_to_message
            if message_temp.from_user.id == self.__bot.id and message_temp.reply_to_message is not None and message_temp.reply_to_message.text.startswith(
                    '/request'):
                messages.append(message_from_assistant(message_temp.text))
            elif message_temp.text.startswith('/request'):
                text_temp = message_temp.text.replace('/request', '')
                messages.append(message_from_user(text_temp))

        messages.reverse()
        response = self.__openai_request.request_text(messages)
        await message.reply(response)

    async def send_generate_image(self, message: types.Message):
        if message.text.replace('/generate_image', '').strip() == '':
            await message.reply('Запрос не может быть пустым')
            return

        prompt = message.text.replace('/generate_image', '').strip()
        image = self.__openai_request.request_image(prompt)
        if image is None:
            await message.reply('Не удалось сгенерировать изображение')
            return

        image_bytes = bytes(image, 'utf-8')
        image_decoded = base64.decodebytes(image_bytes)
        await message.reply_photo(image_decoded)
