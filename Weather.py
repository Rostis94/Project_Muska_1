from pyowm.owm import OWM
from pyowm.utils import config as cfg
from datetime import datetime
from telebot import TeleBot
import Secrets

config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM(Secrets.open_weather_api_key, config)
w_manager = owm.weather_manager()


def get_weather(place):
    try:
        observation = w_manager.weather_at_place(place)
        w = observation.weather
        t = w.temperature('celsius')
        return (f'В городе {place} температура {t["temp"]:.0f}°С', True)
    except:
        return (f'Не удалось найти город {place}', False)


def ask_weather_at_place():
    success = False
    while not success:
        place = input('В каком городе?\n')
        message, success = get_weather(place)
        print(message)
    print()
    print()


# Извлекаем нулевой элемент кортежа
# print(get_weather('Ярославль')[0])
# ask_weather_at_place()

bot = TeleBot(Secrets.telegram_bot_api_key)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Привет!\n" +
        "Напиши мне название города и я скажу тебе какая там температура")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    place = message.text
    print(f'{datetime.now():%H:%M:%S} чат {message.chat.id} пользователь {message.from_user.first_name} сообщение: {message.text}')
    bot.send_message(message.chat.id, get_weather(place)[0])


bot.polling()
# в случае ошибки добавить аргумент (none_stop = True)

# https://core.telegram.org/bots/api#available-types
