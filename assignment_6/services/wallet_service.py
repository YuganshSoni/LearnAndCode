from exceptions.wallet_exception import InSufficientBalanceException

class Wallet:
    def __init__(self, balance : int):
        self.balance = balance
        self.MINIMUM_AMOUNT = 10

    def withdraw(self, amount_to_withdraw : int):
        if amount_to_withdraw <= self.balance:
            self.balance -= amount_to_withdraw
        else:
            raise InSufficientBalanceException()

    def get_wallet_balance(self):
        return self.balance

    def set_balance(self, new_balance : int):
            self.balance = new_balance

