from ast import Constant
from asyncio import constants
from email.message import Message
from lib2to3.pgen2 import token
from aiogram import Bot, Dispatcher, types, Dispatcher
import py
from create_bot import dp, bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram import types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
# from handlers import weather

# from aiogram.utils import executor
from pyowm import OWM
from pyowm.utils import config
# import datetime as dtm



config_dict = config.get_default_config_for_subscription_type('professional')
config_dict['language'] = 'ru' 

owm = OWM('127934e41dc5667bf248c54d9435ea1a', config_dict)
mgr = owm.weather_manager()

help_button = KeyboardButton('/Помощь')
vk_button = KeyboardButton('/ВК')
weather_button = KeyboardButton('/Погода')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(help_button)
help_kb = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(vk_button)\
    .add(weather_button)\
    .add(help_button)


# Функция команды старт
@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer('Привет! Я буду следить за порядком в чате Три Версты \
и предоставлять полезную информацию!', reply_markup=help_kb, )
    await message.delete()


# Функция команды хелп
@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    try:
        await bot.send_message(message.from_user.id, """
    Вот список моих команд:
/Помощь - Помощь
/ВК - Наша группа ВК
/Погода - Текущая погода и прогноз
""", reply_markup=help_kb)
        await message.delete()
    except:
        await message.answer('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/penis_mudilaBot')           
        await message.delete()


# Функция команды вк
@dp.message_handler(commands=['vk'])
async def vk_group(message:types.Message):
    await bot.send_message(message.from_user.id, """Наша группа ВК:
https://vk.com/kubok_tri_versty
""", reply_markup=(help_kb))
    await message.delete()

# @dp.message_handler(commands=['Погода']) #content_types= ['text'])
# async def weather(message: types.Message):
#     await bot.send_message(message.from_user.id, "Город?")

# Тут по идее будешь встраивать погоду
# @dp.message_handler(commands=['Погода'])
# # async def get_weather(location):
# #     # bot = constants.WEATHER_URL.format(city=location,
# #     #                                 token=Constant.WEATHER_TOKEN)
# # # @dp.message_handler(commands = ["Город"])

# async def Weather(message:types.Message):
#     # await message.reply("Город? ")
#     bot.send_message(message.from_user.id, "Город?")
    # bot.register_next_step_handler(message, city_name)
    # await bot.send_message(message.from_user.id, Weather, reply_markup=(help_kb))
    # await message.delete()
# async def city(message):
#     bot.send_message(message.from_user.id, "Город?")
#     bot.register_next_step_handler(message, city_name)
# async def city_name(message):
#     global name
#     name = message.text



# class FSMWeather(StatesGroup):
#     city = State()


# @dp.message_handler(commands=['Погода'], state=None)
# async def gorod_start(message:types.Message):
#     await FSMWeather.city.set()
#     await message.reply('Город?')


# @dp.message_handler(content_types=['text'], state=FSMWeather.city)
# async def gorod_input(message:types.Message, state:FSMContext):
#     async with state.proxy() as data: # Эта строчка открывает словарь data, то есть ее можно прописывать несколько раз, и под каждой что то делать с тем что получили от пользователя
#         data['city'] = message.text
#     await message.reply('Я понял, ты живешь в ' + data['city']) # Вместо этого получается мы сунем в погоду город
#     await state.finish()

# Приветствие новеньких
# @dp.message_handler(content_types=['new_chat_members'])
async def user_joined(message:types.Message):
    await message.answer(message.from_user.first_name + ', добро пожаловать в чат!\
Я буду следить за порядком в чате Три Версты \
и предоставлять полезную информацию!\n\
Чтобы увидеть список моих команд нажми кнопку /Помощь', reply_markup=(start_kb))


# Прощание с покинувшими чат
# @dp.message_handler(content_types=['left_chat_member'])
async def user_left(message:types.Message):
    await message.answer(message.from_user.first_name + ', мы будем по тебе скучать!')
    await bot.send_message(message.from_user.first_name + ', мы будем по тебе скучать!')


# Регистрация хендлеров для последующего импорта в tri_verstyBot.py
def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['Помощь'])
    dp.register_message_handler(vk_group, commands=['ВК'])
    # dp.register_message_handler(gorod_start, commands=['Погода'])
    dp.register_message_handler(user_joined, content_types=['new_chat_members'])
    dp.register_message_handler(user_left, content_types=['left_chat_member'])
