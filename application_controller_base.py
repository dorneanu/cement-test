from application_logging import MyLogger
from cement.core import controller


class BaseController(controller.CementBaseController):

    class Meta:
        label = 'base'
        description = "application"
        config_defaults = dict(
            debug = False,
            foo='bar', some_other_option='my default value',
        )

        arguments = [
            (['-f', '--foo'], dict(action='store')),
        ]

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        self.app.log.error("Test error")
        self.app.log.info("Test info")
