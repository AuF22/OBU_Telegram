from aiogram import Dispatcher, Bot, types
from Data.config import API_KEY
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=API_KEY, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
