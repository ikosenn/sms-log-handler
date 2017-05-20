SMS Log handler
----------------
|Travis| |Codecov|

This is a python sms handler. The idea is to quickly alert the developer that
something has gone horribly wrong with their application. This only serves as a
means of alerting, for comprehensive traceback you can configure something like
Sentry_ or use python's SMTPHandler_ to get email alerts.


Requirements
~~~~~~~~~~~~

- Python 3.4+

The handler has not been tested using python27. Feel free to open a pull request
if you need support for this version


Installation
~~~~~~~~~~~~

.. code-block:: bash

    pip install sms-log-handler


Python
~~~~~~~

The following details how this handler can be configured to run on Python.
The implementation below is specific to AfricasTalking Provider

.. code-block:: python

    import logging

    LOGGER = logging.getLogger(__name__)
    provider_config =  {
        'provider_class': 'sms_log_handler.providers.africastalking.AfricasTalkingProvider',
        'provider_key': '<your-username>',
        'provider_secret': '<your-api-key>',
        'provider_send_to': ['+25472XXXXXXX', ]
    }
    handler = SMSHandler(provider_config)
    LOGGER.addHandler(handler)

    try:
        raise KeyError()
    except:
        LOGGER.error('Duplicate records found in the user model', exc_info=True)


Django
~~~~~~

To use the logger in django configure your LOGGING to include the ``SMSHandler``
as part of you handlers.


.. code-block:: python

    # settings.py

    LOGGING = {
        'version': 1,
        'handlers': {
            'smshandler': {
                'level': 'ERROR',
                'class': 'sms_log_handler.sms_handler.SMSHandler',
                'provider_config': {
                    'provider_key': '<your-username>',
                    'provider_secret': '<your-api-key>',
                    'provider_send_to': ['+25472XXXXXXX']
                }
            },
        },
        'loggers': {
            'django': {
                'handlers': ['smshandler'],
                'propagate': True,
                'level': 'ERROR',
            },
        }
    }


.. _Sentry: https://sentry.io/welcome/
.. _SMTPHandler: https://docs.python.org/3.6/library/logging.handlers.html#smtphandler
.. |Travis| image:: https://travis-ci.org/ikosenn/sms-log-handler.svg?branch=master

.. |Codecov| image:: https://codecov.io/gh/ikosenn/sms-log-handler/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/ikosenn/sms-log-handler
