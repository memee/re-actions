from behave import *
from sqlalchemy import and_
import transaction

from reactions import models


use_step_matcher("re")


@then("I should single model as a JSON object")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert context.response.get('one') == 1


@then("I should have two model objects in the database")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    result = models.DBSession.query(models.MyModel).all()
    assert len(result) == 2


@when("I add a model object in this scenario")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    with transaction.manager:
        model2 = models.MyModel(name='two', value=2)
        models.DBSession.add(model2)


@when("I make a query for that model object")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    context.result = (
        models.DBSession
        .query(models.MyModel)
        .filter(and_(models.MyModel.name == 'two', models.MyModel.value == 1))
        .first()
    )


@given("a single model object in the database")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    with transaction.manager:
        model = models.MyModel(name='one', value=1)
        models.DBSession.add(model)
