from application_logging import MyLogger, logger
from cement.core import foundation
from application_controller_base import BaseController


class MyApp(foundation.CementApp):
    """Default application"""
    class Meta:
        label = "application"
        base_controller = BaseController
        log_handler = logger
        debug = False
