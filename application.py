from application_main import MyApp
from application_controller_second import ParserController
from cement.core import handler

# Add application
app = MyApp()

try:
    # Setup application
    app.setup()

    # Register controler
    handler.register(ParserController)

    # Run it
    app.run()

finally:
    # close app
    app.close()
