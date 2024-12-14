import pickle

def load_model(model_path: str):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

def predict_eta(model, input_data):
    # Prepare and reshape input data for prediction
    # Example assuming input_data is of ETARequest type which is a Pydantic model
    features = [
        input_data.pickup_id,
        input_data.dropoff_id,
        input_data.pickup_time,
        input_data.is_rain,
        input_data.is_airport
        # Collect other features
    ]
    
    # Model prediction
    prediction = model.predict([features])
    
    return prediction[0]  # Assuming single prediction