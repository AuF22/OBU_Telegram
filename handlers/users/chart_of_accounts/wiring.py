from loader import dp
from keyboards.inline.random_ikb import ikb_random
from aiogram.types import CallbackQuery
from .game_config import wiring_all_values
import random


@dp.callback_query_handler(text='wiring')
async def game(call: CallbackQuery):

    all_list = wiring_all_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)

    text = f"""
Для начала начнем с этого:
{all_list.get(true_key).strip()}
"""
    ikb = ikb_random(values, true_key, g=1)
    await call.message.edit_text(text=text, reply_markup=ikb)


@dp.callback_query_handler(text='Верно1')
async def game(call: CallbackQuery):

    all_list = wiring_all_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)

    text = f"""
Молодец, все правильно !!!

{all_list.get(true_key).strip()}
"""

    await call.message.edit_text(text=text, reply_markup=ikb_random(values, true_key, g=1))


@dp.callback_query_handler(text='Неверно1')
async def game(call: CallbackQuery):

    all_list = wiring_all_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)

    text = f"""
Ответ был неправильный, попробуй еще

{all_list.get(true_key).strip()}
"""

    await call.message.edit_text(text=text, reply_markup=ikb_random(values, true_key, g=1))
