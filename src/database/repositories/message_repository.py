from sqlalchemy import Sequence, delete, select

from database.repositories.base import BaseRepository
from database.models import Message


class MessageRepository(BaseRepository):
    model = Message

    async def get_all_messages(self, user_id: int) -> Sequence[Message]:
        stmt = (
            select(Message)
            .where(Message.user_id == user_id)
            .order_by(Message.created_at.desc())
            .limit(30)
        )
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def delete_all_messages(self, user_id: int):
        """
        Можно было добавить тему, чтобы был "статус сообщений"
        Не удалять их, а изменять статус на "удалено"
        Возможно, для аналитической работы чтобы данные оставались
        Но в тз не было, так что пока будет так
        """
        stmt = delete(Message).where(Message.user_id == user_id)
        await self.session.execute(stmt)
