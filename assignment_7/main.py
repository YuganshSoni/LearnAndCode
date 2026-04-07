from fastapi import FastAPI
from app.api.v1.api import router as api_router
from common.api.error_handlers import register_error_handlers

def create_app():
    fastapi_app = FastAPI(title="ATM Application", version="1.0.0")
    fastapi_app.include_router(api_router)
    register_error_handlers(fastapi_app)
    return fastapi_app

app = create_app()