from loader import dp
from aiogram import types
from keyboards.default.start_kb import start_kb, admin_kb
from keyboards.inline.knowledge import ikb_game
from fuzzywuzzy import fuzz
from time import sleep
from aiogram.utils.markdown import hlink
from Data.database.db import DataBase
data = DataBase()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    from Data.config import admins_id

    user_id = str(message.from_user.id)
    name = str(message.from_user.first_name)
    username = str(message.from_user.username)
    user = await data.create_profile(user_id=user_id, name=name)
    if user is not None:
        for admin in admins_id:
            await dp.bot.send_message(chat_id=admin, text=f'{user}:\n{user_id=}\n{name=}\nusername=@{username}')

    text = f"""
Вы находитесь в стартовом меню
Для подробного ознакомления с ботом прошу ввести комманду : /help
    """

    if user_id in admins_id:
        await message.answer(text=text, reply_markup=admin_kb)
    else:
        await message.answer(text=text, reply_markup=start_kb)


@dp.message_handler(commands=['menu'])
async def start(message: types.Message):
    text = f"""
Вы находитесь в Главном меню
Отточите свои знания бух учета, или же поищите интересующую вас проводку
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
    """
    Как по мне эта самая основная функция бота, нахождение нужной информации из некоторого количества данных.
    Тут проходит несколько стадий сравнения текста и анализа ее составляющих.
    As for me, this is the most basic function of the bot, finding the necessary information from a certain amount of data.
    There are several stages of text comparison and analysis of its components.
    """
    from Data.data import accounting_entries
    answers = []

    msg = message.text
    # Ловит проводки в сообщении пользователя
    # Catches accounting entries in the user's message
    if 'дт' in msg.lower() or 'д-т' in msg.lower():
        from .chart_of_accounts.game_config import wiring_all_values
        import difflib
        entry_dict = wiring_all_values()
        for entry in entry_dict:
            matcher = difflib.SequenceMatcher(None, msg.lower(), entry.lower()).ratio()
            if matcher >= 0.86:
                answers.append(f'{entry_dict.get(entry)}\n{entry}')

    else:
        for account_entry in accounting_entries:
            coincidence = fuzz.partial_ratio(msg.lower(), str(account_entry).lower())
            if coincidence >= 90:
                answers.append(account_entry)
            else:
                continue

    if len(answers) == 0:
        text = f"Проводка: {msg} не найдено\nПопробуйте перефразировать"
        await message.answer(text=text)

    else:
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
