from dotenv import load_dotenv
import os

import requests

load_dotenv()  # reads .env file
api_key = os.getenv("OPENWEATHER_API_KEY") # gets api_key

def get_weather(city):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url) # sends HTTP requests
    if response.status_code == 200: # success
        return response.json() # convert response to json
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")