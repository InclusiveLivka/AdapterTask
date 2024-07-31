import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.__init__ import setup_routers
from app.database.engine import intialize_db
from __init__ import bot

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Создание экземпляра бота
async def main():

    # Создание диспетчера
    dp = Dispatcher()
    logger.info("Dispatcher instance create")

    # Подключение роутеров
    setup_routers(dp)
    logger.info("Routers setup")

    # Запуск пуллинга

    try:
        await dp.start_polling(bot)
    finally:
        await Bot.session.close()


if __name__ == "__main__":
    logger.info("Starting bot")
    intialize_db()
    asyncio.run(main())
    logger.info("Bot finished")
