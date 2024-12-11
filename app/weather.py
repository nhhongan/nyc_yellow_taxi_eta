import requests
from app.config import API_KEY
from app.zones import get_zone_coordinates

def get_current_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_weather_data_for_zones(pickup_zone, dropoff_zone):
    pickup_coords = get_zone_coordinates(pickup_zone)
    dropoff_coords = get_zone_coordinates(dropoff_zone)

    if any(coord is None for coord in pickup_coords):
        raise ValueError(f"Coordinates for pickup zone '{pickup_zone}' not found.")
    
    if any(coord is None for coord in dropoff_coords):
        raise ValueError(f"Coordinates for dropoff zone '{dropoff_zone}' not found.")

    pickup_weather = get_current_weather(*pickup_coords)
    dropoff_weather = get_current_weather(*dropoff_coords)
    
    return {
        "pickup_weather": pickup_weather,
        "dropoff_weather": dropoff_weather
    }