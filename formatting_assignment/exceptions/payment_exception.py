class PaymentException(Exception):
    def __init__(self, message:str = "Payment request failed"):
        self.message = message

    def __str__(self):
        return f"{self.message}."
    
class InvalidPaymentDetailsException(Exception):
    def __init__(self, message:str = "Payment request failed Invalid details"):
        self.message = message

    def __str__(self):
        return f"{self.message}."