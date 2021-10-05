from pyowm.owm import OWM
from pyowm.utils import config as cfg
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
print(get_weather('Ярославль')[0])

ask_weather_at_place()