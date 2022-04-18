from unicodedata import name
from aiogram import types
from aiogram.utils import executor
from create_bot import dp, bot
from pyowm import OWM
from pyowm.utils import config
import datetime as dtm


from handlers.other import message_filter
# from pyowm.utils.config import get_default_config
# from pyowm.utils import timestamps
# language = "ru"

# config_dict = get_default_config()
config_dict = config.get_default_config_for_subscription_type('professional')
config_dict['language'] = 'ru' 

owm = OWM('127934e41dc5667bf248c54d9435ea1a', config_dict)
mgr = owm.weather_manager()

# async def answer_user_bot(data):
#     pass

# async def parse_weather_data(data):
#     pass

# async def get_weather(location):
#     pass

# async def get_message(data):
#     return data['message']['text']


# one_call = mgr.one_call(lat=52.5244, lon=13.4105)

# place = input("Введите город/страну: ")
# place = "Grodno"

# forecast = mgr.forecast_at_place(place, 'daily')

# observation = mgr.weather_at_place('Grodno')
# w = observation.weather

# current_temp = w.temperature
# @dp.message_handler(commands = ["city"])
# 

@dp.message_handler(commands=['Погода']) #content_types= ['text'])
async def weather(message: types.Message):
    await bot.send_message(message.from_user.id, "Город?")

#   mgr.run_once(dtm.datetime.now(), context=update.effective_chat.id)
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    try:
        observation = mgr.weather_at_place(str(message.text))
        w = observation.weather
        a = w.detailed_status
        b = w.wind() 
        c = ("Температура на градуснике: " + str(w.temperature('celsius')['temp']) + "°С" + "\nПо ощущению: " + str(w.temperature('celsius')['feels_like']) + "°С")
        d = (w.temperature('celsius')['feels_like'])
        e = w.rain
        f = w.clouds

        # current_temp = w.temperature ('celsius')["temp"]

        # await message.answer (w.detailed_status, w.wind, w.humidity, parse_mode=True) 
        # await bot.send_message(message_filter, message.text)
        # await message.answer (w.detailed_status)         # 'clouds'
        # w.detailed_status
        # w.wind()                  # {'speed': 4.6, 'deg': 330}

        # await message.answer (w.humidity)                # 87
        # w.humidity
        # await message.answer ("Температура на градуснике: " + str(w.temperature('celsius')['temp']) + "°С" + "\nПо ощущению: " + str(w.temperature('celsius')['feels_like']) + "°С")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0, 'feels_like': 1.43}
        # await message.answer("<u>egbegb</u> " + str(w.temperature('celsius')['temp']))

        if d < 18 and \
            d >= 12:
            d = ("Стоять чисто в труханах прохладно, что-нибудь накинь ")
        elif d < 12 and \
            d >= 5:
            d = ("Пощади свои суставы, время утепляться")
        elif d < 5 and \
            d >= 0:
            d = ("Не вздумай ехать в семейниках, бубенцы звинеть будут. Одевайся тепло и тёплые перчатки не забудь")
        elif d < 0 and \
            d >= -10:
            d = ("Ходят слухи, что в такую погоду не катают, но не мы. Тёплые одёжки и перчатки ждут. Про голову и ноги не забывай, голова в тепле и бахилы на ногах (если ты в контактах катаешь)")
        elif d < -10:
            d = ("Холодно, противно, местами снег, время катнуть. ТОЛЬКО ТЁПЛЫЕ ОДЁЖКИ! Коня потом не забудь почистить, после покатухи")
        else:
            d = ("Температура шикарная, катай хоть в том, в чём мать родила")

        # await message.answer (w.rain)                    # {}
        # await message.answer (w.heat_index)              # None
        # await message.answer (w.clouds)                  # 75
        await message.answer(str(a) + "\n" + str(b) + "\n" + c + "\n" + str(d) + "\n" + str(e) + "\n" + str(f))
    except:
        await message.reply("Ты что мне тут вводишь?")
# answer = forecast.will_be_clear_at(timestamps.tomorrow())

# print(a)

# await bot.send_message(message.from_user.id, message.answer)

if __name__ == "__main__":
    executor.start_polling(dp)