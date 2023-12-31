import openai
import bot.config as config

openai.api_key = config.OPENAI_API_TOKEN


def request_text(messages: list[dict[str, str]]):
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response = chat.choices[0].message.content
    return response


def request_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
        response_format="b64_json")
    if response:
        image = response['data'][0]['b64_json']
        return image
    else:
        return None
