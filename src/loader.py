from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from data.config import settings


dp = Dispatcher(storage=MemoryStorage())
bot = Bot(
    token=settings.BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(parse_mode="MarkDown"),
)
