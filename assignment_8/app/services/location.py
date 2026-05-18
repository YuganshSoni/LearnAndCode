from app.domain.interfaces.geo_location import LocationProvider
from common.api.exceptions import ValidationError

class LocationService:

    def __init__(self, location_provider : LocationProvider):
        self.location_provider = location_provider

    async def get_location_data(self, location: str):
        if not location or not location.strip():
            raise ValidationError("Location name cannot be empty or whitespace.")
            
        return await self.location_provider.get_coordinates(location.strip())