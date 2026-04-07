from common.api.exceptions import (
    InvalidDeviceException,
    DeviceLockedException,
    NetworkConnectionException,
    InsufficientBalanceException,
    CardNotFoundException
)

class DeviceHandler:
    def __init__(self):
        self.device_id = ["DEV_1"]
        self._balances = {
            "1234-5678": 1000.0,
            "8765-4321": 50.0
        }

    def get_handler(self, device_id: str) -> str:
        return device_id if device_id in self.device_id else "INVALID"

    def is_validate_handler(self, handle: str) -> bool:
        if handle == "INVALID":
            raise InvalidDeviceException("Device is invalid.")
        return True

    def is_validate_card(self, card_number: str) -> bool:
        if card_number not in self._balances:
            raise CardNotFoundException(f"Credit card {card_number} was not found in our records.")
        return True

    def retrieve_device_record(self, handle: str) -> dict:
        return {
            "id": handle,
            "status": "ACTIVE",
            "network_available": True
        }

    def is_device_active(self, record: dict) -> bool:
        if record.get("status") == "SUSPENDED":
            raise DeviceLockedException("This ATM is currently suspended for maintenance.")
        return True

    def is_network_available(self, record: dict) -> bool:
        if not record.get("network_available"):
            raise NetworkConnectionException("ATM lost connection to the banking network.")
        return True

    def is_balance_sufficient(self, card_number: str, amount: float) -> bool:
        balance = self.get_balance(card_number)
        if balance < amount:
            raise InsufficientBalanceException(
                f"Insufficient funds. You attempted to withdraw ${amount} but only have ${balance}."
            )
        return True

    def get_balance(self, card_number: str) -> float:
        return self._balances.get(card_number, 0.0)

    def update_balance(self, card_number: str, amount: float) -> bool:
        if card_number in self._balances:
            self._balances[card_number] -= amount
            return True
        return False