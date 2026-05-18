from fastapi import APIRouter, status
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    message: str


class HealthAPI:
    def __init__(self):
        self.router = APIRouter()
        self._register_route()

    def _register_route(self):
        self.router.add_api_route(
            "/",
            self.health_check,
            methods=["GET"],
            description="Health check",
            response_model=HealthResponse,
            status_code=status.HTTP_200_OK,
        )
        
    def health_check(self):
        return HealthResponse(
            status="ok",
            message="Health check"
        )

health_api = HealthAPI()
health_router = health_api.router
