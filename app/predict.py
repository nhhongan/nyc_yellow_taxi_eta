import joblib
from zones import TaxiZoneFinder
from distance import calculate_distance
from datetime import datetime

def load_model(model_path: str):
    model = joblib.load(model_path)
    return model

def predict_eta(model, input_data):
    init_input = {
        'pu_lat': input_data.pu_lat,
        'pu_lng': input_data.pu_lng,
        'do_lat': input_data.do_lat,
        'do_lng': input_data.do_lng    
    }

    trip_distance = calculate_distance(pu_lat=init_input['pu_lat'],
                                       pu_lng=init_input['pu_lng'],
                                       do_lat=init_input['do_lat'],
                                       do_lng=init_input['do_lng'])

    taxi_zone_data_path = "../data/taxi_zone_lookup.csv"
    taxi_zone_finder = TaxiZoneFinder(taxi_zone_data_path)
    pu_zone = taxi_zone_finder.get_zone_id(lat=init_input['pu_lat'], lng=init_input['pu_lng'])
    pu_zone_id = pu_zone['zone_id']
    pu_zone = taxi_zone_finder.get_zone_id(lat=init_input['pu_lat'], lng=init_input['pu_lng'])
    do_zone = taxi_zone_finder.get_zone_id(lat=init_input['do_lat'], lng=init_input['do_lng'])
    do_zone_id = do_zone['zone_id']

    now = datetime.now()
    curr_weekday = now.weekday()
    curr_hour = now.hour
    curr_minute = now.minute



    features = [
        trip_distance,
        pu_zone_id,
        do_zone_id,
        curr_weekday,
        curr_hour,
        curr_minute,
        input_data.rain,
        input_data.enter_airport
    ]
    
    prediction = model.predict([features])
    
    return prediction[0]