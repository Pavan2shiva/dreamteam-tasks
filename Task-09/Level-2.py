import requests
import folium


def get_user_location():
    """
    Fetch the user's current location using IP-based geolocation.

    Returns:
        dict: Dictionary containing latitude, longitude, city, region, and country.
    """
    response = requests.get("http://ip-api.com/json/")
    data = response.json()

    if data["status"] == "fail":
        raise Exception("Unable to fetch location from API.")

    return {
        "lat": data["lat"],
        "lon": data["lon"],
        "city": data["city"],
        "region": data["regionName"],
        "country": data["country"]
    }


def plot_location_on_map(location, filename="user_location.html"):
    """
    Plot the location on an interactive map and save it to an HTML file.

    Args:
        location (dict): User location containing lat, lon, city, region, country.
        filename (str): Output HTML filename.
    """
    user_map = folium.Map(location=[location["lat"], location["lon"]], zoom_start=12)

    folium.Marker(
        [location["lat"], location["lon"]],
        popup=f"{location['city']}, {location['region']}, {location['country']}",
        tooltip="You are here!"
    ).add_to(user_map)


    user_map.save(filename)
    print(f"Map generated and saved as '{filename}'.")


if __name__ == "__main__":
    try:
        loc = get_user_location()
        print(f" Current Location: {loc['city']}, {loc['region']}, {loc['country']}")
        plot_location_on_map(loc)
    except Exception as e:
        print(str(e))


import pytest
import os
import folium
from unittest.mock import patch
from location_map import get_user_location, plot_location_on_map



@patch("location_map.requests.get")
def test_get_user_location_success(mock_get):
    """Test successful response from IP API."""
    mock_get.return_value.json.return_value = {
        "status": "success",
        "lat": 37.7749,
        "lon": -122.4194,
        "city": "San Francisco",
        "regionName": "California",
        "country": "USA"
    }

    result = get_user_location()

    assert result["lat"] == 37.7749
    assert result["lon"] == -122.4194
    assert result["city"] == "San Francisco"
    assert result["region"] == "California"
    assert result["country"] == "USA"


@patch("location_map.requests.get")
def test_get_user_location_failure(mock_get):
    """Test API failure response."""
    mock_get.return_value.json.return_value = {
        "status": "fail"
    }

    with pytest.raises(Exception, match="Unable to fetch location"):
        get_user_location()


def test_plot_location_on_map_creates_file(tmp_path):
    """Test map creation and output HTML file."""
    location = {
        "lat": 37.7749,
        "lon": -122.4194,
        "city": "San Francisco",
        "region": "California",
        "country": "USA"
    }

    file_path = tmp_path / "map_test.html"
    plot_location_on_map(location, filename=str(file_path))

    assert file_path.exists()
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "San Francisco" in content
        assert "<html" in content.lower()