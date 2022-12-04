from loader import dp
from aiogram import types
from keyboards.default.start_kb import start_kb
from keyboards.inline.knowledge import ikb_game
from fuzzywuzzy import fuzz
from time import sleep


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text='Справочник по ОБУ,  помогу чем смогу', reply_markup=start_kb)


@dp.message_handler(text='🎓Проверка знаний')
async def chart(message: types.Message):
    await message.answer(text='Насколько же ты уверен(а) в своих знаниях ?!', reply_markup=ikb_game)


@dp.message_handler(content_types=['text'])
async def look_for_accounting_entries(message: types.Message):
    from Data.data import accounting_entries
    answers = []
    for account_entry in accounting_entries:
        coincidence = fuzz.partial_ratio(message.text, str(account_entry))
        if coincidence >= 75:
            answers.append(account_entry)
        else:
            continue

    if len(answers) == 0:
        text = f"К сожалению мы такой проводки не нашли:\n{message.text}"
        await message.answer(text=text)
    else:
        await message.answer(text=f'Найдено всего {len(answers)} проводок')
        for answer in answers:
            await message.answer(text=answer)
            sleep(0.2)
        await message.answer('Это были все проводки')
