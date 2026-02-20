from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from services.services_factory import ServicesFactory


router = Router()


rpm = ReplyKeyboardBuilder()
rpm.button(text="Новый запрос")
rpm = rpm.as_markup(resize_keyboard=True)
# Эту штуку можно было вынести куда-нибудь, но поскольку клава одна, решил тут оставить.
# Понятно, что если расширять - практика так себе :)


@router.message(Command("start"))
async def start_cmd(message: Message, services: ServicesFactory):
    await services.message.clear_chat_history(message.from_user.id)
    await message.answer("Отправь сообщение!", reply_markup=rpm)
