from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot('5242216537:AAH5ZKYln4DllV-k8h5NlAnL54ThjZ9QTIE', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
