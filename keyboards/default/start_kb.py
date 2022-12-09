from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = [
    [
        KeyboardButton(text='🎓Проверка знаний')
    ],
    [
        KeyboardButton(text='ℹ️Информация')
    ],
    [
        KeyboardButton(text='Реклама 🎥'),
        KeyboardButton(text='Статистика 📊')
    ]
]


start_kb = ReplyKeyboardMarkup(row_width=2,
                               keyboard=keyboard[:-1],
                               resize_keyboard=True
                               )

admin_kb = ReplyKeyboardMarkup(row_width=2,
                               keyboard=keyboard,
                               resize_keyboard=True
                               )
