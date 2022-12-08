"""
Описание команд
Description of commands
"""
from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('help', 'Инструкция по применению'),
        types.BotCommand('menu', 'Главное меню')
    ])
