from datetime import datetime

class PaymentRecord:
    customer_id : str
    amount : float
    timestamp : datetime

class PaymentRequest:
    customer_id : str
    amount : float

class PaymentResult:
    success : bool
    message : str
    transaction_id : str