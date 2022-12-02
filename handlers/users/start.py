from loader import dp
from aiogram import types
from keyboards.default.start_kb import start_kb
from keyboards.inline.chart_game import ikb_game


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text='Справочник по ОБУ,  помогу чем смогу', reply_markup=start_kb)


@dp.message_handler(text='🧮Счета')
async def chart(message: types.Message):
    await message.answer(text='Давай проверим твои знания плана счетов', reply_markup=ikb_game)

