from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_game = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [InlineKeyboardButton(text='Старт', callback_data='chart_game')],
                                ])
