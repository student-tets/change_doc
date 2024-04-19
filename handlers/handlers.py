import logging
from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command

# настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# @dp.message()
async def process_start_command(message: types.Message):
    """Приветствие"""
    await message.answer("Привет!\nНапиши что-нибудь")
    logging.info(f'user {message.from_user.id} starts bot')


# @dp.message()
async def echo_command(message: types.Message):
    """Эхо-ответ"""
    await message.answer(message.text)
    logging.info(f'bot echos message from user {message.from_user.id}')

def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(process_start_command, Command(commands=['start']))
    router.message.register(echo_command)
