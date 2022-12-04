import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ikb_random(values: list, true_value: str, g=2) -> InlineKeyboardMarkup:

    def validation(verifiable: str) -> str:
        if verifiable == true_value:
            return f'Верно{str(g)}'
        elif verifiable != true_value:
            return f'Неверно{str(g)}'
        else:
            return 'Ошибка'

    def remove(val: list) -> list:
        random_answer = random.choice(val)
        val.remove(random_answer)
        answer = [random_answer, validation(random_answer)]
        return answer

    x = remove(values)
    y = remove(values)
    z = remove(values)
    g = remove(values)

    ikb_game = InlineKeyboardMarkup(row_width=2,

                                    inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text=x[0], callback_data=x[1]),
                                                InlineKeyboardButton(text=y[0], callback_data=y[1])
                                            ],
                                            [
                                                InlineKeyboardButton(text=z[0], callback_data=z[1]),
                                                InlineKeyboardButton(text=g[0], callback_data=g[1])
                                            ]
                                        ]
                                    )

    return ikb_game
