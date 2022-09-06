import asyncio

from aiogram import Bot, Dispatcher, executor
from data.config import token


bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp, send_to_admin,f

    executor.start_polling(dp, on_startup=f)
