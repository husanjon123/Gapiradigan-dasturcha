from aiogram.types import Message

from loader import dp
from filters import IsAdmin
from keyboards import admin_commands_list_keyboard


@dp.message_handler(IsAdmin(), commands=['start'], commands_prefix="/!")
async def start(message: Message):
    await message.answer("Привет, админ! Выбери команду", reply_markup=admin_commands_list_keyboard)
