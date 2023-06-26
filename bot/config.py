import os

from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_API_TOKEN = os.getenv('BOT_TEST_API_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
CHAT_ID = int(os.getenv('CHAT_ID'))

# OpenAI
OPENAI_API_TOKEN = os.getenv('OPENAI_API_TOKEN')

# Database
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
