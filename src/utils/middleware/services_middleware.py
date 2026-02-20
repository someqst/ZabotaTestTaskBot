from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable

from services.services_factory import ServicesFactory


class ServiceMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ):
        data["services"] = ServicesFactory()
        return await handler(event, data)
