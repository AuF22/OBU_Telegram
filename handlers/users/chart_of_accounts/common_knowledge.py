"""
Часть кода отвечающая за подготовку вариантов и составления тестов
Part of the code responsible for preparing options and compiling tests
"""
from .game_config import chart_all_values, wiring_all_values
import random
from keyboards.inline.ikrandom import Knowledge_keyboard
from Data.data import praises


class Common_CallBack_Handler:
    def __init__(self) -> None:
        self.all_dict_chart = chart_all_values()
        self.all_dict_wiring = wiring_all_values()
        self.next_text = 'Следующий вопрос:\n'
        self.last_true_answer = None
        self.keyboard = None
        self.right_text = None
        self.start_text = None
        self.wrong_text = None

    def chart(self):
        """
        Подготавливает опции для плана счетов
        Prepares parameters for the chart of accounts
        """
        all_list = self.all_dict_chart
        values = random.choices(list(all_list), k=4)
        true_key = random.choice(values)
        ikb = Knowledge_keyboard(values=values, g=2, true_value=true_key)
        praise = random.choice(praises)

        self.start_text = f"Для начала начнем со следущего счета:\n{all_list.get(true_key).strip()}"
        self.right_text = f"✅ {praise} Все верно\n{self.next_text}{all_list.get(true_key).strip()}"
        self.wrong_text = f"❌ Ответ был неверным\n{self.next_text}{all_list.get(true_key).strip()}"

        ikb.ikb('chart')
        self.keyboard = ikb.ikb_game

        self.last_true_answer = f'Верный ответ:\n{all_list.get(true_key).strip()}:\n{true_key}'

    def wiring(self):
        """
        Подготавливает опции для бухгалтерских проводок
        Prepares parameters for accounting entries
        """
        all_list = self.all_dict_wiring
        values = random.choices(list(all_list), k=4)
        true_key = random.choice(values)

        ikb = Knowledge_keyboard(values=values, g=1, true_value=true_key)
        answer_options = f'Варианты ответов:\n\
a)\n{ikb.a[0]}\n\
b)\n{ikb.b[0]}\n\
c)\n{ikb.c[0]}\n\
d)\n{ikb.d[0]}'
        praise = random.choice(praises)

        self.start_text = f"Для начала начнем со следущей проводки:\n\
        {all_list.get(true_key).strip()}\n{answer_options}"
        self.right_text = f"✅ {praise} Все верно\n{self.next_text}{all_list.get(true_key).strip()}\n{answer_options}"
        self.wrong_text = f"❌ Ответ был неверным\n{self.next_text}{all_list.get(true_key).strip()}\n{answer_options}"

        ikb.ikb('wiring')
        self.keyboard = ikb.ikb_game

        self.last_true_answer = f'Верный ответ:\n{all_list.get(true_key).strip()}:\n{true_key}'
        