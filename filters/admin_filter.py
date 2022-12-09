from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from Data.config.config import admins_id


class AdminId(BoundFilter):
    async def check(self, message: types.Message):
        if str(message.from_user.id) in admins_id:
            return True
