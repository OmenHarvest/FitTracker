import asyncio
from aiogram import Bot, Dispatcher
import logging

from startup_properties import TOKEN_API

from routers import admin_router, user_router

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
dispath = Dispatcher()

dispath.include_routers(admin_router.admin_router, user_router.user_handler)

async def main():
    await dispath.start_polling(bot);

if __name__ == "__main__":
    asyncio.run(main())