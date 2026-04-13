from unittest.mock import patch, Mock
from weather.api import get_weather

def test_get_weather_returns_data():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'name': 'London',
        'main': {
            'temp': 15,
            'feels_like': 13,
            'humidity': 80},
            'weather': [{'description': 'partly cloudy'}],
            'wind': {'speed': 5}
    
    }

    with patch('weather.api.requests.get', return_value=mock_response):
        result = get_weather('London')
        assert result['name'] == 'London'
        assert result['main']['temp'] == 15
        assert result['main']['feels_like'] == 13
        assert result['main']['humidity'] == 80
        assert result['weather'][0]['description'] == 'partly cloudy'
        assert result['wind']['speed'] == 5


def test_get_weather_raises_error_on_city_not_found():
    mock_response = Mock()
    mock_response.status_code = 404

    with patch('weather.api.requests.get', return_value=mock_response):
        try:
            get_weather('InvalidCity')
        except ValueError as e:
            assert str(e) == "City not found. Please check the city name and try again."