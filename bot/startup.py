import asyncio
from aiogram import Bot, Dispatcher

from startup_properties import TOKEN_API

bot = Bot(TOKEN_API)
dispath = Dispatcher()

async def start_bot():
    await dispath.start_polling(bot);

if __name__ == "__name__":
    asyncio.run(start_bot())