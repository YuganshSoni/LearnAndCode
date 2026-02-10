from exceptions.wallet_exception import InSufficientBalanceException
from services.wallet_service import Wallet

class Customer:
    def __init__(self, first_name : str, last_name : str, wallet : Wallet):
        self.first_name = first_name
        self.last_name = last_name
        self.my_wallet = wallet

    def pay_bill(self, amount_to_pay:int):
        self.my_wallet.withdraw(amount_to_pay)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
