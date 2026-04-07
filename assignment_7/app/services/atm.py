from app.handlers.device_handler import DeviceHandler

class ATMService:
    def __init__(self, device_handler: DeviceHandler):
        self.device_handler = device_handler

    def withdraw_money(self, card_number: str, amount: float, device_id: str = "DEV_1") -> None:
        handle = self.device_handler.get_handler(device_id)
        self.device_handler.is_validate_handler(handle)
        self.device_handler.is_validate_card(card_number)

        record = self.device_handler.retrieve_device_record(handle)
        self.device_handler.is_device_active(record)
        self.device_handler.is_network_available(record)
        self.device_handler.is_balance_sufficient(card_number, amount)

        self._dispense_cash(handle, amount)
        self.device_handler.update_balance(card_number, amount)

    def _dispense_cash(self, handle: str, amount: float) -> None:
        print(f"DEBUG: [Device {handle}] Dispensing ${amount} in cash...")