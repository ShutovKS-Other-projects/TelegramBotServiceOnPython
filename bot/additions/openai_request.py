import openai


class OpenaiRequest:

    def __init__(self, token: str):
        openai.api_key = token

    def request_text(self, messages: list[dict[str, str]]):
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = chat.choices[0].message.content
        return response

    def request_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json")
        if response:
            image = response['data'][0]['b64_json']
            return image
        else:
            return None
