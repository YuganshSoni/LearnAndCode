from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from common.api.exceptions import BaseAPIException

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(BaseAPIException)
    async def base_api_exception_handler(request: Request, exc: BaseAPIException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.message,
                "code": exc.code,
                "details": exc.details or {}
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        # We could log the error here
        return JSONResponse(
            status_code=500,
            content={
                "detail": "An unexpected error occurred.",
                "code": "INTERNAL_SERVER_ERROR"
            },
        )

    app.include_router(api_router, prefix="/api")
    return app


app = create_app()