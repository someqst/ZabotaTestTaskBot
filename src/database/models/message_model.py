from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String, Text

from database.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, index=True)
    message_text: Mapped[str] = mapped_column(String(4096))
    answer_text: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
