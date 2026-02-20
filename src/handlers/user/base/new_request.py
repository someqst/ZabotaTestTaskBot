from aiogram import Router, F
from aiogram.types import Message

from services.services_factory import ServicesFactory


router = Router()


@router.message(F.text == "Новый запрос")
async def help_cmd(message: Message, services: ServicesFactory):
    await services.message.clear_chat_history(message.from_user.id)
    await message.answer("Чат очищен!")
