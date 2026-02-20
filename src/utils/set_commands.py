from aiogram.client.bot import BotCommand

from loader import bot


async def set_bot_commands():
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Очистить диалог 🧹"),
            BotCommand(command="help", description="Помощь ℹ️"),
        ]
    )
