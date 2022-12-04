from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

chart_kb = ReplyKeyboardMarkup(row_width=2,
                               keyboard=[
                                   [
                                       KeyboardButton(text='🔍Поиск'),
                                       KeyboardButton(text='🎲Игра')
                                   ],
                               ],
                               resize_keyboard=True)
