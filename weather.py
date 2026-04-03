import requests
import os 
from dotenv import load_dotenv
load_dotenv()

weathers = os.getenv("WEATHER_KEY")
api_url = f"https://api.weatherapi.com/v1/current.json?key={weathers}&q=Canberra"



def get_weather():
    response = requests.get(api_url)
    data = response.json()
    weather = {"temp": data['current']["temp_c"], "humidity": data['current']["humidity"],"uv":data['current']["uv"]}
    return weather

