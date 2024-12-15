import requests
import os
from dotenv import load_dotenv
load_dotenv()

def calculate_distance(pu_lat, pu_lng, do_lat, do_lng):
    MAP_API_KEY = os.getenv('MAP_API_KEY')
    url = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={pu_lat},{pu_lng}&destinations={do_lat},{do_lng}&key={MAP_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        resp = response.json()
        distance_m = resp['rows'][0]['elements'][0]['distance']['value']
        distance_mile = distance_m / 1609.344
        return distance_mile
    else:
        response.raise_for_status()

def main():
    pu_lat, pu_lng = 40.67480990612672, -73.75067754192816
    do_lat, do_lng = 40.681709702980726, -73.73780293884953
    resp = calculate_distance(pu_lat=pu_lat, pu_lng=pu_lng, do_lat=do_lat, do_lng=do_lng)
    
    print(resp)

if __name__ == "__main__":
    main()
