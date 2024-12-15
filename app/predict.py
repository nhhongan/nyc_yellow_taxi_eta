import joblib

def load_model(model_path: str):
    model = joblib.load(model_path)
    return model

def predict_eta(model, input_data):
    features = [
        input_data.trip_distance,
        input_data.pu_zone_id,
        input_data.do_zone_id,
        input_data.pickup_weekday,
        input_data.pickup_hour,
        input_data.pickup_minute,
        input_data.rain,
        input_data.enter_airport
    ]
    
    prediction = model.predict([features])
    
    return prediction[0]