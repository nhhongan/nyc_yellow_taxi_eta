import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_current_weather(lat, lng):
    API_KEY = os.getenv('API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def main():
    lat, lng = 10.773646162021558, 106.70045957927135
    resp = get_current_weather(lat, lng)
    
    print(resp)

if __name__ == "__main__":
    main()