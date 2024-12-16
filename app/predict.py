import joblib
from app.zones import TaxiZoneFinder
from app.distance import calculate_distance
from app.weather import get_current_weather
from datetime import datetime

def load_model(model_path: str):
    model = joblib.load(model_path)
    return model

def predict_eta(model, input_data):
    pu_lat = input_data.pu_lat
    pu_lng = input_data.pu_lng
    do_lat = input_data.do_lat
    do_lng = input_data.do_lng

    trip_distance = calculate_distance(pu_lat=pu_lat,
                                       pu_lng=pu_lng,
                                       do_lat=do_lat,
                                       do_lng=do_lng)

    taxi_zone_data_path = "../data/taxi_zone_lookup.csv"
    taxi_zone_finder = TaxiZoneFinder(taxi_zone_data_path)
    pu_zone = taxi_zone_finder.get_zone_info(lat=pu_lat, lng=pu_lng)
    pu_zone_id = pu_zone['zone_id']
    do_zone = taxi_zone_finder.get_zone_info(lat=do_lat, lng=do_lng)
    do_zone_id = do_zone['zone_id']

    now = datetime.now()
    curr_weekday = now.weekday()
    curr_hour = now.hour
    curr_minute = now.minute

    pu_rain_status = get_current_weather(lat=pu_lat, lng=pu_lng)
    do_rain_status = get_current_weather(lat=do_lat, lng=do_lng)
    if (pu_rain_status or do_rain_status):
        rain = 1
    else:
        rain = 0

    pu_zone_name = pu_zone['zone_name']
    do_zone_name = do_zone['zone_name']
    if ("Airport" in pu_zone_name or "Airport" in do_zone_name):
        enter_airport = 1
    else:
        enter_airport = 0

    features = [
        trip_distance,
        pu_zone_id,
        do_zone_id,
        curr_weekday,
        curr_hour,
        curr_minute,
        rain,
        enter_airport
    ]
    
    prediction = model.predict([features])
    
    return prediction[0]