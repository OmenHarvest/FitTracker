import asyncio
from aiogram import Bot, Dispatcher

from startup_properties import TOKEN_API

from routers import admin_router, user_router

bot = Bot(TOKEN_API)
dispath = Dispatcher()

dispath.include_routers(admin_router.admin_router, user_router.user_handler)

async def start_bot():
    await dispath.start_polling(bot);

if __name__ == "__name__":
    asyncio.run(start_bot())