from fastapi import APIRouter

from app.api.v1.endpoints.atm import atm_router

router = APIRouter(prefix="/v1")

router.include_router(atm_router, prefix="/atm", tags=["atm"])
