from africastalking.AfricasTalkingGateway import AfricasTalkingGateway

from sms_log_handler.providers.base import SMSProviderBase


class AfricasTalkingProvider(SMSProviderBase):
    """
    AfricasTalking provider
    """

    def send(self, phone_numbers: str, message: str) -> None:
        """
        Handles sending of the error message to the provider phone numbers

        params:
            phone_numbers: An array of phonenumbers to sms
            message: This are the contents of the message that is being sent.

        """
        phone_numbers_csv = ','.join(phone_numbers)
        gateway = AfricasTalkingGateway(self.key, self.secret)
        gateway.sendMessage(phone_numbers_csv, message)
