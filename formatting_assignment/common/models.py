from datetime import datetime
import uuid

class PaymentRecord:
    customer_id : uuid
    amount : float
    timestamp : datetime

class PaymentRequest:
    customer_id : uuid
    amount : float

class PaymentResult:
    success : bool
    message : str
    transaction_id : uuid