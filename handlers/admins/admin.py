"""
В дальнейшем буду переделывать данную часть бота, просто нынешний функционал для меня достаточен.
In the future, I will redo this part of the bot, just the current functionality is sufficient for me.
"""
from loader import dp
from aiogram import types
from filters import AdminId
from States.state_advertising import State_Advertising
from aiogram.dispatcher import FSMContext
from keyboards.inline.admin_ikb import mail
from aiogram.types import CallbackQuery
from Data.database.db import DataBase
db = DataBase()


@dp.message_handler(AdminId(), text='Реклама 🎥')
async def admin_advertising(message: types.Message):
    await message.answer(text='Введите текст рекламы')
    await State_Advertising.text.set()


@dp.message_handler(AdminId(), state=State_Advertising.text)
async def step_1(message: types.Message, state: FSMContext):
    m_text = message.text
    await state.update_data(text=m_text)
    await message.answer(text='Хотите ли добавить фото?', reply_markup=mail)
    await State_Advertising.state_1.set()


@dp.callback_query_handler(state=State_Advertising.state_1)
async def state_(call: CallbackQuery, state: FSMContext):
    answer = call.data
    if answer == 'yes':
        await call.message.answer(text='Пришлите фото')
        await State_Advertising.photo.set()
    elif answer == 'no':
        data = await state.get_data()
        text = f'Отправить: \n{data.get("text")}'
        await call.message.answer(text=text)
        text = data.get('text')
        id_list = await db.len_user_id()
        for user_id in id_list:
            await dp.bot.send_message(chat_id=user_id[0], text=text)
            await state.finish()


@dp.message_handler(state=State_Advertising.photo, content_types=types.ContentType.PHOTO)
async def photo_(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)
    data = await state.get_data()
    photo = data.get('photo')
    text = data.get('text')
    id_list = await db.len_user_id()
    i = 0
    for user_id in id_list:
        await dp.bot.send_photo(chat_id=user_id[0], photo=photo, caption=text)
        i += 1
    await message.answer(text=f'Сообщение доставлено:\n{i=}')
    await state.finish()


@dp.message_handler(AdminId(), text='Статистика 📊')
async def admin_advertising(message: types.Message):
    """Sends a message with the count of users"""
    id_list = await db.len_user_id()
    text = f"В данный момент {len(id_list)} пользователей бота"
    await message.answer(text=text)
