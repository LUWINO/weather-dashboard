from dotenv import load_dotenv
import os

import requests

load_dotenv()  # reads .env file
api_key = os.getenv("OPENWEATHER_API_KEY") # gets api_key

def get_weather(city):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url) # sends HTTP requests
    if response.status_code == 200:
        return response.json() # returns JSON data
    elif response.status_code == 404:
        raise ValueError("City not found. Please check the city name and try again.")
    elif response.status_code == 401:
        raise ValueError("Invalid API key. Please check your API key and try again.")
    else:
        raise RuntimeError(f"Something went wrong: {response.status_code}")
        
    