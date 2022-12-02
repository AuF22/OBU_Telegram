from loader import dp
from keyboards.inline.random_ikb import ikb_random
from aiogram.types import CallbackQuery
from .game_config import random_values
import random


@dp.callback_query_handler(text='chart_game')
async def game(call: CallbackQuery):

    all_list = random_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)

    text = f"""
{all_list.get(true_key)}
"""
    ikb = ikb_random(values, true_key)
    print(ikb)
    await call.message.edit_text(text=text, reply_markup=ikb)


@dp.callback_query_handler(text='Верно')
async def game(call: CallbackQuery):

    all_list = random_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)

    text = f"""
Молодец, все правильно !!!
{all_list.get(true_key)}
"""

    await call.message.edit_text(text=text, reply_markup=ikb_random(values, true_key))


@dp.callback_query_handler(text='Неверно')
async def game(call: CallbackQuery):

    all_list = random_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)


    text = f"""
Ответ был неправильный, попробуй еще
{all_list.get(true_key)}
"""

    await call.message.edit_text(text=text, reply_markup=ikb_random(values, true_key))

