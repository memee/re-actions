from pyramid.paster import get_appsettings
from reactions import main
from webtest import TestApp


def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()
    context.settings = get_appsettings('development.ini')
    context.app = TestApp(main({}, **context.settings))
