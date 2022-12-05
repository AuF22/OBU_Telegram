from loader import dp
from aiogram.types import CallbackQuery
from .game_config import wiring_all_values
import random
from keyboards.inline.ikrandom import Knowledge_keyboard


@dp.callback_query_handler(text='wiring')
async def game(call: CallbackQuery):

    all_list = wiring_all_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)

    ikb = Knowledge_keyboard(values=values, g=1, true_value=true_key)

    text = f"""
Для начала начнем с этого:
{all_list.get(true_key).strip()}
a) 
{ikb.a[0]} 
b) 
{ikb.b[0]}
c) 
{ikb.c[0]}
d) 
{ikb.d[0]}
"""
    # ikb = ikb_random(values, true_key, g=1, row_width=1)
    ikb.ikb('wiring')
    await call.message.edit_text(text=text, reply_markup=ikb.ikb_game)


@dp.callback_query_handler(text='Верно1')
async def game(call: CallbackQuery):

    all_list = wiring_all_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)
    ikb = Knowledge_keyboard(values=values, g=1, true_value=true_key)
    text = f"""
✅ Молодец, все правильно !!!

{all_list.get(true_key).strip()}
a) 
{ikb.a[0]} 
b) 
{ikb.b[0]}
c) 
{ikb.c[0]}
d) 
{ikb.d[0]}
"""
    ikb.ikb('wiring')
    await call.message.edit_text(text=text, reply_markup=ikb.ikb_game)


@dp.callback_query_handler(text='Неверно1')
async def game(call: CallbackQuery):

    all_list = wiring_all_values()
    values = random.choices(list(all_list), k=4)
    true_key = random.choice(values)
    ikb = Knowledge_keyboard(values=values, g=1, true_value=true_key)

    text = f"""
❌ Ответ был неправильный, попробуй еще

{all_list.get(true_key).strip()}
a) 
{ikb.a[0]} 
b) 
{ikb.b[0]}
c) 
{ikb.c[0]}
d) 
{ikb.d[0]}
"""
    ikb.ikb('wiring')
    await call.message.edit_text(text=text, reply_markup=ikb.ikb_game)
