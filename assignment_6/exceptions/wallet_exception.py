
class InSufficientBalanceException(Exception):
    def __init__(self, message : str ="Not enough balance in wallet"):
        super().__init__(message)