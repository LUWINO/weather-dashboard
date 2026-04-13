from weather.api import get_weather
from weather.display import show_weather
def main():
    user_input = input("Enter a city name to get the current weather: ")
    try:
        weather_data = get_weather(user_input) # fetch weather data
        show_weather(weather_data) # display weather data
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()