from aiogram import BaseMiddleware
from typing import Dict, Any, Callable, Awaitable

from services.services_factory import ServicesFactory


service_factory = ServicesFactory()


class ServiceMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ):
        data["services"] = service_factory
        return await handler(event, data)
