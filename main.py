# Этап 1

# Дополнительный гайд по aiogram https://mastergroosha.github.io/aiogram-3-guide/quickstart/
# Дополнительный гайд по асинхронному бэкенду https://habr.com/ru/companies/kts/articles/598575/
# Дополнительный гайд по логированию https://habr.com/ru/companies/wunderfund/articles/683880/

# Установить библиотеки и фреймворки aiogram==3.4
# pip install aiogram
# pip install python-dotenv

# Для сохранения текущих пакетов в проекте и их версий при переносе используйте файл requirements.txt
# pip freeze — внешние пакеты проекта
# pip freeze > requirements.txt — сохранить внешние пакеты в файл
# pip install -r requirements.txt —  загрузить пакеты из файла


# импорты
import asyncio  # библиотека для асинхронного программирования
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from handlers import register_message_handler


# асинхронный вызов функции - конкурентный вызов с ожиданием события для продолжения процесса выполнения
async def main():
    # создание экземпляров классов Bot и Dispatcher
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # функция для вызова хендлеров из пакета handlers
    register_message_handler(dp)

    await dp.start_polling(bot)


# запуск бота через long_polling
if __name__ == "__main__":
    asyncio.run(main())
