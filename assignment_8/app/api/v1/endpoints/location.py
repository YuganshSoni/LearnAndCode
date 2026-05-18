from fastapi import APIRouter, status, Query
from typing import List

from app.services.location import LocationService
from app.infra.location.location_iq_service import LocationIQService
from app.schemas.location import LocationResponse

class LocationAPI:
    def __init__(self):
        self.router = APIRouter()
        self.location_service = LocationService(LocationIQService())
        self._register_route()

    def _register_route(self):
        self.router.add_api_route(
            "/",
            self.get_geo_location,
            methods=["GET"],
            description="Get geo location coordinates for a given address",
            status_code=status.HTTP_200_OK,
            response_model=List[LocationResponse],
        )

    async def get_geo_location(self, user_location_query: str = Query(..., examples="Statue of Liberty, New York")):
        return await self.location_service.get_location_data(user_location_query)

location_api = LocationAPI()
location_router = location_api.router