from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart

user_handler = Router()

@user_handler.message(CommandStart())
async def cmd_start():
    pass
