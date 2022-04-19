import logging
from create_bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
from handlers import weather

logging.basicConfig(level=logging.INFO)


async def on_startup(__):
    print('Бот онлайн')

client.register_handlers_client(dp)
other.register_handlers_other(dp)
# weather.register_handlers_weather(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    