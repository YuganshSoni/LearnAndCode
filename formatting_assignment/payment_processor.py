from services.notification_service import NotificationService
from common.models import PaymentRecord, PaymentRequest, PaymentResult
from exceptions.payment_exception import PaymentException, InvalidPaymentDetailsException
from common.constants import MAX_PAYMENT_RETRIES, MIN_PAYMENT_AMOUNT, MAX_PAYMENT_AMOUNT
from datetime import datetime
import logging

class PaymentProcessor:
    MIN_AMOUNT = MIN_PAYMENT_AMOUNT
    MAX_AMOUNT = MAX_PAYMENT_AMOUNT
    MAX_RETRIES = MAX_PAYMENT_RETRIES
    PAYMENT_SUCCESSFUL = "Payment Successful"
    PAYMENT_FAILED = "Payment Failed"

    def __init__(self, logger : logging.Logger, notifier_service : NotificationService):
        self.logger = logger
        self.notifier_service = notifier_service
        self.history :  dict[str, PaymentRecord] = {}

    def process_payment(self, payment_request : PaymentRequest)->PaymentResult:
        payment_attempts = 0
        self._validate_payment_request(payment_request)
        while(payment_attempts<PaymentProcessor.MAX_RETRIES):
            try:
                self._execute_payment_request(payment_request)
                self._save_payment_request_details(payment_request)
                self._notify_payment_success(payment_request)
                return PaymentResult(
                        success = True,
                        message = PaymentProcessor.PAYMENT_SUCCESSFUL,
                        transaction_id = self._generate_id()
                    )
            except PaymentException:
                payment_attempts+=1
                self.logger.info("Payment Request Failed")
                self.logger.info(f"Retrying attempt : {payment_attempts}")
        
        return PaymentResult(
            success = False,
            message = PaymentProcessor.PAYMENT_FAILED,
            transaction_id = None
        )

    def _validate_payment_request(self, payment_request : PaymentRequest):
        if payment_request.customer_id is None or payment_request.customer_id == "":
            raise InvalidPaymentDetailsException
        
        if (
            payment_request.amount is None
            or payment_request.amount < PaymentProcessor.MIN_AMOUNT
            or payment_request.amount > PaymentProcessor.MAX_AMOUNT
        ):
            raise InvalidPaymentDetailsException
        
    def _execute_payment_request(self, payment_request : PaymentRequest):
        self.logger.log(f"Executing payment of : {payment_request.amount}")        

    def _save_payment_request_details(self, payment_request : PaymentRequest)->None:
        payment_id = self._generate_id()
        self.history[payment_id] = PaymentRecord(
            customer_id = payment_request.customer_id,
            amount = payment_request.amount,
            timestamp = datetime.utcnow()
        )

    def _notify_payment_success(self, payment_request : PaymentRequest):
        notification_message = f"Payment of amount {payment_request.amount} is successfull"
        self.notifier_service.send_notification(payment_request.customer_id, notification_message)

    def _generate_id(self):
        return f"TXN-{int(datetime.utcnow().timestamp() * 1000)}"