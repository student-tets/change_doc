import logging
from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session_maker, User


# настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def help_command(message: types.Message):
    """справочная команда, регистрация пользователя"""

    async with async_session_maker() as session:
        session: AsyncSession
        query = select(User).where(User.user_id == message.from_user.id)
        user_exit = await session.execute(query)

        if user_exit.scalars().all():
            await message.reply("Ты есть!")
            logging.info(f"user {message.from_user.id} asks for help")

        else:
            new_user = {
                "user_id": message.from_user.id,
                "username": message.from_user.username
            }
            stmt = insert(User).values(**new_user)
            await session.execute(stmt)
            await session.commit()
            await message.reply("Теперь ты есть!")
            logging.info(f"register new user: {message.from_user.id}")


# @dp.message()
async def echo_command(message: types.Message):
    """Эхо-ответ"""
    await message.answer(message.text)
    logging.info(f'bot echos message from user {message.from_user.id}')

def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(process_start_command, Command(commands=["start", "help"]))
    router.message.register(echo_command)
