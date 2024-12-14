from fastapi import FastAPI, HTTPException
from app.schemas import ETARequest, ETAResponse
from app.predict import load_model, predict_eta

app = FastAPI()

model = load_model("model/pipeline.pickle")

@app.post("/predict", response_model=ETAResponse)
async def get_eta(request: ETARequest):
    try:
        eta = predict_eta(model, request)
        return {"estimated_time": eta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))