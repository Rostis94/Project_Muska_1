from pyowm.owm import OWM
import Secrets

owm = OWM(Secrets.open_weather_api_key)
w_manager = owm.weather_manager()

observation = w_manager.weather_at_place('Moscow,RU')
w = observation.weather
t = w.temperature('celsius')
print(t['temp'])
