import logging
import datetime

from .utils import import_from_string


class SMSHandler(logging.Handler):
    def __init__(self, provider_config):
        """
        Initializes the SMSHandler

        params:
            provider_config: The provider configurations.
                             {
                                provider_key: <key_id>
                                provider_secret: <secret_key>
                                provider_send_to: [<an array of phone numbers>]
                             }
        """
        logging.Handler.__init__(self)
        self.provider_class_str = provider_config.get(
            'provider_class',
            'sms_log_handler.providers.africastalking.AfricasTalkingProvider')
        self.provider_class = import_from_string(self.provider_class_str)
        self.key = provider_config.get('provider_key', '')
        self.secret = provider_config.get('provider_secret', '')
        self.phone_numbers = provider_config.get('provider_send_to', [])

    def emit(self, record):
        """
        Sends the message
        """
        to_send = self._construct_message(record)
        sms_provider = self.provider_class(self.key, self.secret)
        sms_provider.send(self.phone_numbers, to_send)

    def _construct_message(self, record):
        """
        Contruct and format the mesage to be sent.

        i.e
        MODULE: sms_log_handler.sms_handler

        LEVEL: ERROR

        TIME: 21, May 2017 10:54

        MESSAGE: Duplicate records found in the user model
        """
        msg = (
            'MODULE: {module_path}\n\nLEVEL: {level}\n\nTIME: {time}\n\n'
            'MESSAGE: {msg}')
        date_time = datetime.datetime.fromtimestamp(record.created)
        date_time = date_time.strftime('%d, %b %Y %H:%M')
        formatted_msg = msg.format(
            level=record.levelname, time=date_time, msg=record.getMessage(),
            module_path=record.name, line_no=record.lineno)
        return formatted_msg
