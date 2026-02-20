from data.dto.message_dto import MessageModel
from utils.unit_of_work import IUnitOfWork


class MessageService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_message(self, message: MessageModel):
        async with self.uow:
            await self.uow.messages.add_one(message.to_db_dict())
            await self.uow.commit()

    async def get_chat_history(self, user_id: int) -> str:
        async with self.uow:
            messages = await self.uow.messages.get_all_messages(user_id)

            messages = [MessageModel.model_validate(message) for message in messages]

        if messages:
            converted_messages = [
                message.text_format
                for message in messages
            ]
            return "".join(converted_messages)

        return ""

    async def clear_chat_history(self, user_id: int):
        async with self.uow:
            await self.uow.messages.delete_all_messages(user_id)
            await self.uow.commit()
