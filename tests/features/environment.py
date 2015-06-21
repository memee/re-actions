from pyramid import testing
from pyramid.paster import get_appsettings
from pyramid.request import Request
from sqlalchemy import orm
from webtest import TestApp

from reactions import (
    main,
    models
)

# based on https://gist.github.com/inklesspen/4504383


def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".
    context.config.setup_logging()

    context.settings = get_appsettings('development.ini')
    context.test_app = TestApp(main({}, **context.settings))
    context.engine = models.DBSession.bind

    # create all tables
    models.Base.metadata.create_all(context.engine)

    context.Session = orm.sessionmaker()


def before_scenario(context, scenario):
    connection = context.engine.connect()
    context.transaction = connection.begin()

    # https://github.com/Pylons/webtest/issues/5#issuecomment-44995932
    models.DBSession.remove()

    models.DBSession.configure(bind=connection)
    context.session = context.Session(bind=connection)
    models.Base.session = context.session

    context.pyramid_config = testing.setUp()
    context.request = Request.blank('/')
    context.request.registry = context.test_app.app.registry
    context.mapper = context.test_app.app.routes_mapper


def after_scenario(context, scenario):
    testing.tearDown()
    context.transaction.rollback()
    context.session.close()
    models.DBSession.remove()


def after_all(context):
    models.Base.metadata.drop_all(context.engine)
