from pydantic import BaseModel
from datetime import datetime

class ETARequest(BaseModel):
    pu_lat: float
    pu_lng: float
    do_lat: float
    do_lng: float

class ETAResponse(BaseModel):
    estimated_duration: float