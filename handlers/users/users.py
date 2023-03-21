from aiogram import Dispatcher
from aiogram.types import *

# from loader import dp
from database.connections import add_user



async def bot_start(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    await add_user(user_id, user_name)
    await message.answer(f"Привет, {message.from_user.full_name}!")


def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])


