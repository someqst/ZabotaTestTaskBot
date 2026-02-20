from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


router = Router()


@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("Команда помощи")
