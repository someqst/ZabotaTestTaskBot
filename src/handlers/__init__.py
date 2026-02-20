from aiogram import Router

from handlers.user.commands import handle_commands_router
from handlers.user.base import handle_base_router


def handle_routers() -> Router:
    router = Router()
    router.include_routers(
        handle_commands_router(),
        handle_base_router()
    )

    return router
