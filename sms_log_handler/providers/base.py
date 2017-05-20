class SMSProviderBase:
    """
    This is a base class that should be inherited by any new providers that
    are brought abroad. It providers a common interface
    """
    def __init__(self, key, secret):
        """
        Intialises the provider class

        params:
            key: This can be that client_id or username
                 depending on the provider
            secret: This can be the client_secret or api_key
        """
        self.key = key
        self.secret = secret

    def send(self, phone_numbers, message):
        """
        This method should ultimately send a text message. It needs to
        be implemented by classes that choose to inherit this class
        """
        raise NotImplemented('send() must be implemented')
