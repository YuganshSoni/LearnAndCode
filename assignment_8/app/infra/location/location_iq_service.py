import httpx
from app.domain.interfaces.geo_location import LocationProvider
from app.core.config import settings
from common.api.exceptions import ExternalServiceError

class LocationIQService(LocationProvider):
    def __init__(self):
        self.api_key = settings.LOCATION_IQ_API_KEY
        self.base_url = settings.LOCATION_IQ_BASE_URL
        self.client = httpx.AsyncClient(timeout=5.0)

    async def get_coordinates(self, location: str) -> list:
        try:
            params = {
                "key": self.api_key,
                "q": location,
                "format": "json",
                "addressdetails": 1
            }
            response = await self.client.get(self.base_url, params=params)
            
            if response.status_code == 404:
                return []
                
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data:
                results.append({
                    "formatted_address": item.get("display_name"),
                    "latitude": float(item.get("lat")),
                    "longitude": float(item.get("lon")),
                })
            
            return results

        except httpx.HTTPStatusError as e:
            raise ExternalServiceError(
                message=f"LocationIQ API error: {response.status_code}",
                details={"response_text": response.text}
            ) from e
        except Exception as e:
            raise ExternalServiceError(
                message=f"Error fetching location from LocationIQ: {str(e)}"
            ) from e
