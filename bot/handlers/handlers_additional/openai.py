import base64

from aiogram import Bot, types

import bot.additions.openai_request as openai_request
import bot.config as config

bot = Bot(token=config.BOT_API_TOKEN)


async def help(message: types.Message):
    await message.reply("Список команд:\n"
                        "/helpOpenai - это сообщение\n"
                        "/request (Текст) - запросить информацию у OpenAI\n"
                        "/generate_image (Текст) - сгенерировать изображение по тексту\n")


async def request_in_openai(message: types.Message):
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
        if message_temp.from_user.id == bot.id \
                and message_temp.reply_to_message is not None \
                and message_temp.reply_to_message.text.startswith('/request'):
            messages.append(message_from_assistant(message_temp.text))
        elif message_temp.text.startswith('/request'):
            text_temp = message_temp.text.replace('/request', '')
            messages.append(message_from_user(text_temp))

    messages.reverse()
    response = openai_request.request_text(messages)
    await message.reply(response)


async def generate_image(message: types.Message):
    if message.text.replace('/generate_image', '').strip() == '':
        await message.reply('Запрос не может быть пустым')
        return

    prompt = message.text.replace('/generate_image', '').strip()
    image = openai_request.request_image(prompt)
    if image is None:
        await message.reply('Не удалось сгенерировать изображение')
        return

    image_bytes = bytes(image, 'utf-8')
    image_decoded = base64.decodebytes(image_bytes)
    await message.reply_photo(image_decoded)
