import os
from fastapi import FastAPI, HTTPException
from app.schemas import ETARequest, ETAResponse
from app.predict import load_model, predict_eta

app = FastAPI()

model_path = "../model/xgboost_model.joblib"
if not os.path.isabs(model_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, model_path)
model = load_model(model_path)

@app.post("/predict", response_model=ETAResponse)
async def get_eta(request: ETARequest):
    try:
        eta = predict_eta(model, request)
        return {"estimated_duration": eta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))