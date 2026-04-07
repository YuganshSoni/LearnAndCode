
class BaseDomainException(Exception):
    status_code = 400
    error_code = "DOMAIN_ERROR"

    def __init__(self, message: str = None):
        super().__init__(message or "A domain error occurred.")

class DeviceLockedException(BaseDomainException):
    status_code = 403
    error_code = "DEVICE_LOCKED"

class InsufficientBalanceException(BaseDomainException):
    status_code = 400
    error_code = "INSUFFICIENT_FUNDS"

class NetworkConnectionException(BaseDomainException):
    status_code = 503
    error_code = "NETWORK_UNAVAILABLE"

class InvalidDeviceException(BaseDomainException):
    status_code = 403
    error_code = "INVALID_DEVICE"

class CardNotFoundException(BaseDomainException):
    status_code = 404
    error_code = "CARD_NOT_FOUND"