from aiogram import Router

from handlers.user.commands import start, help
from utils.middleware.services_middleware import ServiceMiddleware


def handle_commands_router() -> Router:
    '''
    Мидлварь можно было и глобально кинуть, но это не очень
    хорошая практика для расширяемости
    '''
    router = Router()
    router.message.outer_middleware(ServiceMiddleware())
    router.include_routers(start.router, help.router)

    return router
