from openai import AsyncClient

from data.config import settings

openai_client = AsyncClient(api_key=settings.OPENAI_TOKEN.get_secret_value())


class AIService:
    def __init__(self):
        self.client = openai_client

    async def make_ai_request(self, message_text: str, chat_history: str) -> str:
        """
        Тут можно было completions api использовать, но это скоро будет устаревшая тема
        так же, как и с assistants api произошло в пользу responses api
        """
        response = await self.client.responses.create(
            model="gpt-4.1-nano",
            instructions="Ты дружелюбный помощник. Используй MarkDown. Для выделений используй *",
            input=f"История чата: {chat_history}\n\nСообщение: {message_text}",
            previous_response_id=None,  # Тут я мог просто в бд сохранять его, но решил блеснуть, было бы слишком просто :D
            store=None,  # Сюда можно vector_store подгрузить с данными
        )

        return response.output_text
