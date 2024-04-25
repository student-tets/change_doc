__all__ = [
    "commands_for_bot",
]

from aiogram import types

bot_commands = (
    ("help", "Справка по боту"),
    # TODO ("status", "Показать статус пользователя"),
)

commands_for_bot = []
for cmd in bot_commands:
    commands_for_bot.append(types.BotCommand(command=cmd[0], description=cmd[1]))
