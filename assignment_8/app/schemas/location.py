from pydantic import BaseModel

class LocationResponse(BaseModel):
    latitude: float
    longitude: float
    formatted_address: str