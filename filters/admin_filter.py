from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from Data.config.config import admins_id


class AdminId(BoundFilter):
    """
    Проверяет user_id пользователя, есть ли он в списке админов
    Checks the user_id of the user, whether he is in the list of admins
    """
    async def check(self, message: types.Message):
        if str(message.from_user.id) in admins_id:
            return True
