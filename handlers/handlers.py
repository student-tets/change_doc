__all__ = [
    "register_message_handler",
]


import logging
from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from db import async_session_maker, User
from .keyboards import keyboard_continue


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


async def status_command(message: types.Message):
    """Информация о пользователе"""

    async with async_session_maker() as session:
        session: AsyncSession
        query = select(User).where(User.user_id == message.from_user.id)
        result = await session.execute(query)
        user = result.scalar()
        await message.reply(f"User ID: {user.user_id}\nUser name: {user.username}")
        logging.info(f"user {message.from_user.id} is asking for status")

    await message.reply("Хотите ли вы продолжить?", reply_markup=keyboard_continue)


def register_message_handler(router: Router):
    """Маршрутизация"""
    router.message.register(help_command, Command(commands=["start", "help"]))
    router.message.register(status_command, Command(commands=["status"]))
