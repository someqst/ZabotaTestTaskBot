from aiogram import Router, F
from aiogram.types import Message

from data.dto.message_dto import MessageModel
from services.services_factory import ServicesFactory
from loader import bot


router = Router()


@router.message(F.text)
async def request_to_ai(message: Message, services: ServicesFactory):
    chat_history = await services.message.get_chat_history(message.from_user.id)

    await bot.send_chat_action(message.from_user.id, "typing")

    ai_response = await services.ai.make_ai_request(message.text, chat_history)

    chat_message = MessageModel(
        user_id=message.from_user.id, message_text=message.text, answer_text=ai_response
    )
    await services.message.add_message(chat_message)

    if len(ai_response) < 4096:
        return await message.answer(ai_response)

    for i in range(0, len(ai_response), 4096):
        await message.answer(ai_response[i:i+4096])
