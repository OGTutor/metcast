import pyowm

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from colorama import init
from colorama import Fore, Back, Style

owm = OWM('')
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'en' 

print( Fore.BLACK )
print( Back.RED )
print("Greetings!")
print("Interested in the weather?")
print("Don't know how to dress on this beautiful day?")
print("Not a problem!")

print( Back.GREEN )
place = input("What city/country are you interested in? ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']
temp2 = w.temperature('celsius')['temp_max']
temp3 = w.temperature('celsius')['temp_min']
wind = w.wind()['speed']
humidity = w.humidity

print( Back.RED )
print( "In the city of " + place + " now " + w.detailed_status )
print( Back.YELLOW )
print( 'The temperature is now around ' + str(temp) + '°')
print( 'The maximum temperature during the day is around ' + str(temp2) + '°')
print( 'The minimum temperature during the day is around ' + str(temp3) + '°')
print( Back.RED )
print( 'Wind speed about ' + str(wind) + ' km/h')
print( 'Humidity ' + str(humidity) + '%')

if temp < 10:
	print( 'It`s really cold now, dress like a tank!!!' )
elif temp < 20:
	print( 'It`s cold, dress warm!!' )
else:
	print( 'Warmly, dress as you please!' )
