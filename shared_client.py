import os
from dotenv import load_dotenv

load_dotenv()

INST_COOKIES = """
# write your Instagram cookies here if needed
"""

YTUB_COOKIES = """
# write your YouTube cookies here if needed
"""

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))
MONGO_DB = os.getenv("MONGO_DB")
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None)
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002344616377"))
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002191173069"))
MASTER_KEY = os.getenv("MASTER_KEY")
IV_KEY = os.getenv("IV_KEY")
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/team_spy_pro")
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/its_sandeepkashyap")
