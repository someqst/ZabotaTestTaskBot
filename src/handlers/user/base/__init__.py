from aiogram import Router

from handlers.user.base import message, new_request
from utils.middleware.services_middleware import ServiceMiddleware


def handle_base_router() -> Router:
    '''
    Мидлварь можно было и глобально кинуть, но это не очень
    хорошая практика для расширяемости
    '''
    router = Router()
    router.message.outer_middleware(ServiceMiddleware())
    router.include_routers(new_request.router, message.router)

    return router
