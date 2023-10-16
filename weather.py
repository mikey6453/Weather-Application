import requests  # query the internet
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# 15:40

# grabs the data from my .env file and loads it into variable api_key
load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


def getLatLon(city_name, state_code, country_code, API_key):
    response = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def getWeather(lat, lon, API_key):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=int(response.get('main').get('temp'))
    )

    return data


def main(city_name, state_name, country_name):
    lat, lon = getLatLon(city_name, state_name, country_name, api_key)
    weather_data = getWeather(lat, lon, api_key)
    return weather_data



if __name__ == "__main__":
    lat, lon = getLatLon('Burke', 'VA', 'US', api_key)
    print(getWeather(lat, lon, api_key))