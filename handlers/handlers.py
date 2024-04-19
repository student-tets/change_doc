from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command


# @dp.message()
async def process_start_command(message: types.Message):
    """Приветствие"""
    await message.answer("Привет!\nНапиши что-нибудь")


# @dp.message()
async def echo_command(message: types.Message):
    """Эхо-ответ"""
    await message.answer(message.text)


def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(process_start_command, Command(commands=['start']))
    router.message.register(echo_command)
