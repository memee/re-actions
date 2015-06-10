from behave import *

use_step_matcher("parse")


@when("the request was sent")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("Http Unauthorized error should not be returned")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("Http Unauthorized error should be returned")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@given("a request from {someuser} for any url")
def step_impl(context, someuser):
    """
    :type context behave.runner.Context
    :type someuser str
    """
    pass


@step("the response has {somestatus:d}")
def step_impl(context, somestatus):
    """
    :type context behave.runner.Context
    :type somestatus int
    """
    pass


@then('I should get a warning with a "{status}" status')
def step_impl(context, status):
    """
    :type context behave.runner.Context
    """
    pass
