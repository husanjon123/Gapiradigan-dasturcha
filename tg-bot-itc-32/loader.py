import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN
from filters import IsAdmin

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
bot.admins = list(map(int, os.getenv("ADMIN_IDS").split(",")))


dp.filters_factory.bind(IsAdmin)
