from services.notification_service import NotificationService
from common.models import PaymentRecord, PaymentRequest, PaymentResult
from exceptions.payment_exception import PaymentException, InvalidPaymentDetailsException
from common.constants import MAX_PAYMENT_RETRIES, MIN_PAYMENT_AMOUNT, MAX_PAYMENT_AMOUNT
from datetime import datetime

class PaymentProcessor:
    MIN_AMOUNT = MIN_PAYMENT_AMOUNT
    MAX_AMOUNT = MAX_PAYMENT_AMOUNT
    MAX_RETRIES = MAX_PAYMENT_RETRIES
    PAYMENT_SUCCESSFULL = "Payment Successfull"
    PAYMENT_FAILED = "Payment Failed"


    def __init__(self, logger : Logger, notifier_service : NotificationService):
        self.logger = logger
        self.notifier_service = notifier_service
        self.history :  dict[str, PaymentRecord] = {}

    def validate_payment_request(self, payment_request : PaymentRequest):
        if payment_request.customer_id is None or payment_request.customer_id == "":
            raise InvalidPaymentDetailsException
        
        if (
            payment_request.amount is None
            or payment_request.amount < PaymentProcessor.MIN_AMOUNT
            or payment_request.amount > PaymentProcessor.MAX_PAYMENT_AMOUNT
        ):
            raise InvalidPaymentDetailsException
        
    def execute_payment_request(self, payment_request : PaymentRequest):
        self.logger.log("Executing payment of : ", payment_request.amount)        

    def save_payment_request_details(self, payment_request : PaymentRequest):
        payment_id = self.generate_id()
        self.history[payment_id]
        #create new record (where and how)??    

    def notify_payment_success(self, payment_request : PaymentRequest):
        notification_message = f"Payment of amount {payment_request.amount} is successfull"
        self.notifier_service.send_notification(payment_request.customer_id, notification_message)

    def generate_id(self):
        return f"TXN-{datetime.now()}"

    def process_payment(self, payment_request : PaymentRequest)->PaymentResult:
        payment_attempts = 0
        self.validate_payment_request(payment_request)
        while(payment_attempts<PaymentProcessor.MAX_RETRIES):
            try:
                self.execute_payment_request(payment_request)
                self.save_payment_request_details(payment_request)
                self.notify_payment_success(payment_request)
                return PaymentResult(PaymentProcessor.PAYMENT_SUCCESSFULL)
            except PaymentException:
                self.logger.info("Payment Request Failed")
                self.logger.info(f"Retrying attempt : {payment_attempts}")
                payment_attempts+=1
        
        return PaymentResult(PaymentProcessor.PAYMENT_FAILED)