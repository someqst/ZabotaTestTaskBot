import asyncio
from logging import getLogger

from aiogram.types.error_event import ErrorEvent

from handlers import handle_routers
from loader import bot, dp
from data.config import settings
from utils.logs import setup_logging
from utils.set_commands import set_bot_commands


logger = getLogger("testTaskBot." + __name__)


@dp.error()
async def error_handling(error: ErrorEvent):
    if message := error.update.message:
        chat_id = message.from_user.id
    else:
        chat_id = error.update.callback_query.from_user.id

    logger.error("Ошибка в хендлере ошибок", exc_info=True)

    await bot.send_message(
        chat_id, "Произошла ошибка. Нажмите /start и повторите попытку."
    )
    return True


async def main():
    dp.include_routers(handle_routers())
    setup_logging(debug_console=settings.DEBUG)
    await set_bot_commands()

    if settings.DEBUG:
        await bot.send_message(539937958, "Старт")
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
