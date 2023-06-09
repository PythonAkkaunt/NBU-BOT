from aiogram import executor

from handlers.users.users import register_users_py
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    register_users_py(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
