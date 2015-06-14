from behave import *


use_step_matcher("re")

@given("initializedb script populate data")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("I should single model as a JSON object")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert context.response.get('one') == 1
