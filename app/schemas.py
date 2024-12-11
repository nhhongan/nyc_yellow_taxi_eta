from pydantic import BaseModel, validator
from datetime import datetime

class ETARequest(BaseModel):
    # Define the features your model expects here
    pickup_time: datetime
    pickup_zone: str
    dropoff_zone: str
    # Add more features as per your model’s requirements

    @validator('pickup_time')
    def check_pickup_time(cls, value):
        if value < datetime.now():
            raise ValueError("Pickup time cannot be in the past")
        return value

class ETAResponse(BaseModel):
    estimated_time: float