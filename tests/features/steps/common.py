from behave import *

use_step_matcher("re")


@then("I should get an empty result")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    try:
        result = context.result
    except AttributeError:
        assert False, 'no result attirbute'
    assert result in [[], None]
