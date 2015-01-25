import codecs
import os
import re

from application_logging import logger

class Parser:
    """Iterate through files and search for function/method calls"""

    def __init__(self):
        pass

    def run(self):
        logger.info("Info test")
        logger.warn("Warning")

