import os
import logging
import logging.config
import tempfile
from cement.core.log import CementLogHandler
from cement.ext.ext_logging import LoggingLogHandler

class MyLogger(LoggingLogHandler):
    class Meta:
        console_format = '[%(levelname)-10s] %(message)s'
        debug_format = '%(asctime)s (%(levelname)s) %(namespace)s : %(message)s'

        config_section = 'log'
        label = 'my application'
