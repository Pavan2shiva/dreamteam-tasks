import requests

API_KEY = "e12494a743dfe43fee4845e82a86da90"  

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Could not find weather for '{city}'.")
        return None

    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }
    return weather

def show_weather(info):
    if info:
        print(f"\nWeather in {info['city']}, {info['country']}:")
        print(f"Temperature: {info['temp']}°C")
        print(f"Humidity: {info['humidity']}%")
        print(f"Condition: {info['description']}\n")

def main():
    while True:
        city1 = input("Enter your city: ")
        weather1 = get_weather(city1)
        show_weather(weather1)

        city2 = input("Enter the city you want to visit: ")
        weather2 = get_weather(city2)
        show_weather(weather2)

        again = input("Do you want to check another place? (yes/no): ")
        if again.lower() != "yes":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()


from unittest.mock import patch
from weather_app import get_weather

@patch("weather_app.requests.get")
def test_get_weather_valid_city(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "London",
        "sys": {"country": "GB"},
        "main": {"temp": 20, "humidity": 65},
        "weather": [{"description": "clear sky"}]
    }


    result = get_weather("London")


    assert result["city"] == "London"
    assert result["country"] == "GB"
    assert result["temp"] == 20
    assert result["humidity"] == 65
    assert result["description"] == "clear sky"


@patch("weather_app.requests.get")
def test_get_weather_invalid_city(mock_get):

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {
        "message": "city not found"
    }

    result = get_weather("FakeCity123")

    
    assert result is None