import asyncio
import os
import sys
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

dp = Dispatcher()


@dp.message(Command("start"))
async def handle_start(message: Message):
    await message.answer("Я бот вайс!!")


async def main():

    token = os.getenv("BOT_TOKEN_TG")

    if not token:
        logging.critical("FATAL: Environment variable 'BOT_TOKEN_TG' is missing or empty!")
        sys.exit(1)
    bot = Bot(token=token)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
