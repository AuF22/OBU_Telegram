from aiogram import Dispatcher
from .admin_filter import AdminId


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminId)