from application_logging import MyLogger
from cement.core import foundation
from application_controller_base import BaseController


class MyApp(foundation.CementApp):
    """Default application"""
    class Meta:
        label = "application"
        base_controller = BaseController
        log_handler = MyLogger
        debug = False


# Add application
application = MyApp()

# Add logger
log = application.log
