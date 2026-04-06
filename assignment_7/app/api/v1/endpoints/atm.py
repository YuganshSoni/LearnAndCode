from fastapi import APIRouter
from pydantic import BaseModel
from app.services.atm import ATMService

from common.api.exceptions import InvalidDeviceException
from common.api.exceptions import NetworkConnectionException
from common.api.exceptions import DeviceLockedException
from common.api.exceptions import InsufficientBalanceException

class WithdrawRequest(BaseModel):
    card_number: str
    amount: float

class WithdrawResponse(BaseModel):
    success: bool
    message: str
    balance: float

class AtmAPI:
    def __init__(self):
        self.router = APIRouter(prefix="/atm", tags=["atm"])
        self._register_routes()
        self.atm_service : ATMService = ATMService()

    def _register_routes(self):
        self.router.add_api_route(
            "/withdraw",
            self.withdraw_money,
            methods=["POST"],
            description="Endpoint to withdraw money from atm",
            response_model=WithdrawResponse
        )

    def withdraw_money(self, request: WithdrawRequest) -> WithdrawResponse:
            self.atm_service.withdraw_money(request.card_number, request.amount)
            return WithdrawResponse(
                success=True,
                message="Withdrawal successful",
                balance=self.atm_service.get_balance(request.card_number)
            )

atm_api = AtmAPI()
atm_router = atm_api.router