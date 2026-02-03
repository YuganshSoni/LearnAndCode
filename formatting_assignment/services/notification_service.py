import uuid
class NotificationService:

    @staticmethod
    def send_notification(cls, customer_id : uuid , message:str):
        print(f"sending message to customer id : {customer_id}")