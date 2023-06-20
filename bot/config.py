import os
from dotenv import load_dotenv

load_dotenv()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
CHAT_ID = int(os.getenv('CHAT_ID'))
