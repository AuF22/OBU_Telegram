from aiogram.dispatcher.filters.state import StatesGroup, State


class State_Advertising(StatesGroup):
    text = State()
    state_1 = State()
    photo = State()
