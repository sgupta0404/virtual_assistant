# Fetches weather information from OpenWeatherMap API.

import requests
from config import WEATHER_API_KEY
from response import speak

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()
    if response["cod"] == 200: # 200=ok
        temp = response["main"]["temp"] - 273.15  # Kelvin to Celsius
        description = response["weather"][0]["description"]
        speak(f"The current temperature is {temp:.2f}°C with {description}.")
    else:
        speak("Sorry, I couldn't retrieve the weather information.")
