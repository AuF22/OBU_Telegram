from .common_knowledge import Common_CallBack_Handler
from aiogram.types import CallbackQuery
from loader import dp
# Вызываем инилизацию класса
# Call class initialization
parent_class = Common_CallBack_Handler()


@dp.callback_query_handler()
async def all_callback_handler(call: CallbackQuery):
    if call.data == 'chart_game':
        parent_class.chart()
        await call.message.edit_text(text=parent_class.start_text, reply_markup=parent_class.keyboard)
    elif call.data == 'Верно2':
        parent_class.chart()
        await call.message.edit_text(text=parent_class.right_text, reply_markup=parent_class.keyboard)
    elif call.data == 'Неверно2':
        await call.answer(text=parent_class.last_true_answer, show_alert=True)
        parent_class.chart()
        await call.message.edit_text(text=parent_class.wrong_text, reply_markup=parent_class.keyboard)
    elif call.data == 'wiring':
        parent_class.wiring()
        await call.message.edit_text(text=parent_class.start_text, reply_markup=parent_class.keyboard)
    elif call.data == 'Верно1':
        parent_class.wiring()
        await call.message.edit_text(text=parent_class.right_text, reply_markup=parent_class.keyboard)
    elif call.data == 'Неверно1':
        await call.answer(text=parent_class.last_true_answer, show_alert=True)
        parent_class.wiring()
        await call.message.edit_text(text=parent_class.wrong_text, reply_markup=parent_class.keyboard)
