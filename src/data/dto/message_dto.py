from pydantic import BaseModel, ConfigDict


class MessageModel(BaseModel):
    user_id: int
    message_text: str
    answer_text: str | None = None

    model_config = ConfigDict(from_attributes=True)

    def to_db_dict(self) -> dict:
        return self.model_dump()
    
    @property
    def text_format(self):
        return f"Вопрос: {self.message_text}\nОтвет: {self.answer_text}\n\n"