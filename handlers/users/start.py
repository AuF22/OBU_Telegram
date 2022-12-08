from loader import dp
from aiogram import types
from keyboards.default.start_kb import start_kb
from keyboards.inline.knowledge import ikb_game
from fuzzywuzzy import fuzz
from time import sleep
from aiogram.utils.markdown import hlink


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f"""
Вы находитесь в стартовом меню
Для подробного ознакомления с ботом прошу ввести комманду : /help
    """
    await message.answer(text=text, reply_markup=start_kb)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = f"""
Вы находитесь в Главном меню
Отточите свои знания бух учета, или же поищите интересуюшую вас проводку
    """
    await message.answer(text=text, reply_markup=start_kb)


@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    link = hlink('YouTube', 'https://www.youtube.com/@hypeel8713/videos')
    text = f"""
Данный бот предназначен для облегчения восприятия/изучения Бухгалтерского учета в Кыргызстане.
Вы можете оттачивать свои способности составления бухгалтерских проводок или же в знании рекомендуемого плана счетов КР.

Вы можете просто написать: "купили за наличный расчет"
и бот подготовит для вас готовые варианты данной операции
Если же вам нужно из проводки получить название хозяйственной операции, для более точного определения стоит писать:
Д-т: 1610
К-т: 3110

Еще для тех кто начал только изучать бухгалтерский учет я могу посоветовать вам {link} канал

Удачи вам в изучении мира бухгалтерии 😉
    """
    await message.answer(text=text, reply_markup=start_kb)


@dp.message_handler(text='🎓Проверка знаний')
async def chart(message: types.Message):
    await message.answer(text='Насколько же ты уверен(а) в своих знаниях ?!', reply_markup=ikb_game)


@dp.message_handler(text='ℹ️Информация')
async def info(message: types.Message):
    await message.answer(text="""Данный бот был создан выпускником БФЭТ
Группа: Бух 1-19""")


@dp.message_handler(content_types=['text'])
async def look_for_accounting_entries(message: types.Message):
    from Data.data import accounting_entries
    answers = []
    for account_entry in accounting_entries:
        coincidence = fuzz.partial_ratio(message.text, str(account_entry))
        if coincidence >= 90:
            answers.append(account_entry)
        else:
            continue

    if len(answers) == 0:
        text = f"К сожалению мы такой проводки не нашли:\n{message.text}"
        await message.answer(text=text)
    else:
        wiring = None
        if len(answers) == 1:
            wiring = 'проводка'
        elif len(answers) >= 5:
            wiring = 'проводок'
        else:
            wiring = 'проводки'

        await message.answer(text=f'Найдено всего {len(answers)} {wiring}')
        for answer in answers:
            await message.answer(text=answer)
            sleep(0.2)
        await message.answer('Это были все проводки')
