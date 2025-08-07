import os
from dotenv import load_dotenv

load_dotenv()

INST_COOKIES = """
# put insta cookies here if needed
"""

YTUB_COOKIES = """
# put yt cookies here if needed
"""

API_ID = "24558120"
API_HASH = "85bd1a317c44733e6620ec82a7053fe9"
BOT_TOKEN = "7264260495:AAHXaiFmOoJ0KnymkeqaDTy0UpsJw1HINY8"
MONGO_DB = "mongodb+srv://sandeepkrbth64:NbPbc81D9Z7CXhLj@sandeepkr.5zk8q.mongodb.net/?retryWrites=true&w=majority&appName=Sandeepkr"
OWNER_ID = [6005294654]
DB_NAME = "telegram_downloader"
STRING = None
LOG_GROUP = -1002344616377
FORCE_SUB = -1002191173069
MASTER_KEY = "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq"
IV_KEY = "s7Yx5CpVmE3F"
YT_COOKIES = YTUB_COOKIES
INSTA_COOKIES = INST_COOKIES
FREEMIUM_LIMIT = 0
PREMIUM_LIMIT = 500
JOIN_LINK = "https://t.me/team_spy_pro"
ADMIN_CONTACT = "https://t.me/username_of_admin"

from pyrogram import Client

app = Client("bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN)

async def start_client():
    await app.start()
    print("Bot Started.")


