from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_game = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text='Знание плана счетов', callback_data='chart_game')],
                                    [InlineKeyboardButton(text='Знание проводок', callback_data='wiring')]
                                ])
