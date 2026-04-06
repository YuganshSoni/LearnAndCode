
class ATMService:

    def __init__(self):
        pass

    def withdraw_money(self, card_number: str, amount: float, device_id : str = "DEV1") -> float:
        handle = self._get_handle(device_id)
        self._validate_device(handle)

        record = self._retrieve_device_record(handle)
        self._validate_device_status(record)
        self._validate_network(record)
        self._validate_balance(account_id, amount)

        self._dispense_cash(handle, amount)

    def _get_handle(self, device_id: str) -> str:
        pass

    def _validate_device(self, handle: str) -> None:
        pass

    def _retrieve_device_record(self, handle: str) -> str:
        pass

    def _validate_device_status(self, record: str) -> None:
        pass

    def _validate_network(self, record: str) -> None:
        pass

    def _validate_balance(self, account_id: str, amount: float) -> None:
        pass

    def _dispense_cash(self, handle: str, amount: float) -> None:
        pass