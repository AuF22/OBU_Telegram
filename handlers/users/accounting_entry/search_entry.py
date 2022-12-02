from loader import dp
from aiogram import types


@dp.message_handler(text='🔍Поиск')
async def search(message: types.Message):
    await message.answer(text='Поиск2')