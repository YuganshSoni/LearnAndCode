from fastapi import APIRouter

from app.api.v1.endpoints.health import health_router
from app.api.v1.endpoints.location import location_router

api_router = APIRouter(prefix="/v1", tags=["v1"])

api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(location_router, prefix="/geo-location", tags=["Location"])