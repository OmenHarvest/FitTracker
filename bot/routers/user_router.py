from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command, CommandStart

from aiogram.enums import ParseMode

from services.language_service import lng_service

user_handler = Router()

@user_handler.message(CommandStart())
async def cmd_start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="🇺🇲", callback_data="eng"),
        InlineKeyboardButton(text="🇷🇺", callback_data="rus")
    )
    await message.answer(lng_service.t(message.from_user.language_code, "choose_language"), reply_markup=builder.as_markup())

@user_handler.message(Command("about"))
async def about_bot(message: Message):
    await message.answer(lng_service.t(message.from_user.language_code, "about_bot"), parse_mode=ParseMode.MARKDOWN_V2)

@user_handler.message(Command("settime"))
async def set_report_time(message: Message):
    await message.answer("test")

@user_handler.message(Command("setnorm"))
async def set_nutrion_norm_for_user(message: Message):
    await message.answer("test_norm")
