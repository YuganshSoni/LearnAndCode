from services.customer_service import Customer
from exceptions.wallet_exception import InSufficientBalanceException

class Paperboy:

    def collect_payment(self, customer : Customer, due_amount: int):
        try:
            customer.pay_bill(due_amount)
            print("Payment Successful")
        except InSufficientBalanceException:
            print("Insufficient Balance in wallet")
