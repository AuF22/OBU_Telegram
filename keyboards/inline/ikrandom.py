import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Knowledge_keyboard:
    """
    Генерирует клавиатуру
    Generates a keyboard
    """
    def __init__(self, values: list, true_value: str, g: object = 2) -> None:
        self.ikb_game = None
        self.values = values
        self.true_value = true_value
        self.g = g

        def validation(verifiable: str) -> str:
            if verifiable == self.true_value:
                return f'Верно{str(self.g)}'
            elif verifiable != self.true_value:
                return f'Неверно{str(self.g)}'
            else:
                return 'Ошибка'

        def remove(val: list) -> list:
            random_answer = random.choice(val)
            val.remove(random_answer)
            answer = [random_answer, validation(random_answer)]
            return answer

        self.a = remove(values)
        self.b = remove(values)
        self.c = remove(values)
        self.d = remove(values)

    def ikb(self, inline_mode: str):
        a, b, c, d = None, None, None, None

        if inline_mode == 'wiring':
            a = 'a'
            b = 'b'
            c = 'c'
            d = 'd'
        elif inline_mode == 'chart':
            a = self.a[0]
            b = self.b[0]
            c = self.c[0]
            d = self.d[0]
        else:
            print('Ошибка')
            
        self.ikb_game = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(text=a, callback_data=self.a[1]),
                                                     InlineKeyboardButton(text=b,callback_data=self.b[1])
                                                 ],
                                                 [
                                                     InlineKeyboardButton(text=c, callback_data=self.c[1]),
                                                     InlineKeyboardButton(text=d, callback_data=self.d[1])
                                                 ]
                                             ])
