from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(row_width=2,
                               keyboard=[
                                   [
                                       KeyboardButton(text='🧮Счета'),
                                       KeyboardButton(text='📝Проводки')
                                   ],
                                   [
                                       KeyboardButton(text='🎓Термины'),
                                       KeyboardButton(text='ℹ️Информация')
                                   ]
                               ],
                               resize_keyboard=True)
