from services.paperboy_service import Paperboy
from services.wallet_service import Wallet
from services.customer_service import Customer


if __name__ == "__main__":

    # Code for testing functionality
    INITIAL_WALLET_AMOUNT = 100
    DUE_AMOUNT = 90

    wallet = Wallet(INITIAL_WALLET_AMOUNT)
    customer = Customer("james", "bond", wallet=wallet)
    paper_boy_raj = Paperboy()
    paper_boy_raj.collect_payment(customer, due_amount=DUE_AMOUNT)

    print(f"amount left in wallet of {customer.first_name} is : {wallet.get_wallet_balance()}")
