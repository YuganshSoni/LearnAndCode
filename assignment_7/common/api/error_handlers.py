from fastapi import Request
from fastapi.responses import JSONResponse
from common.api.exceptions import BaseDomainException

async def domain_exception_handler(request: Request, exc: BaseDomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error_type": exc.error_code,
            "message": str(exc)
        }
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error_type": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred."
        }
    )

def register_error_handlers(app):
    app.add_exception_handler(BaseDomainException, domain_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
