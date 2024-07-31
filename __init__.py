import os

from aiogram import Bot
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
bot = Bot(os.getenv("BOT_TOKEN"))
owned = os.getenv("OWNED_ID")
