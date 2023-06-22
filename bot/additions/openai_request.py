import openai


class OpenaiRequest:

    def __init__(self, token: str):
        openai.api_key = token

    def request(self, messages: list[dict[str, str]]):
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        return reply
