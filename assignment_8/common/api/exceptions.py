from typing import Any, Dict, Optional

class BaseAPIException(Exception):
    def __init__(
        self, 
        message: str, 
        status_code: int = 500, 
        code: str = "INTERNAL_SERVER_ERROR", 
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.code = code
        self.details = details
        super().__init__(self.message)

class ExternalServiceError(BaseAPIException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            message=message, 
            status_code=502, 
            code="EXTERNAL_SERVICE_ERROR", 
            details=details
        )

class ValidationError(BaseAPIException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            message=message, 
            status_code=400, 
            code="VALIDATION_ERROR", 
            details=details
        )

class ResourceNotFoundError(BaseAPIException):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            message=message, 
            status_code=404, 
            code="RESOURCE_NOT_FOUND", 
            details=details
        )
