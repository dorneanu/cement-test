from cement.core import controller
from cement.core.controller import CementBaseController
from parser import Parser

class ParserController(CementBaseController):
    """Parse sth"""

    class Meta:
        label = 'parser'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Parser controller"

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        # Create new parser
        parser = Parser()
        parser.run()
