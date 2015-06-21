import json
from behave import *
from behave import model
from hamcrest import assert_that, equal_to, is_


from tests.utils import reverse


use_step_matcher("parse")


@when("the request was sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Http Unauthorized error should not be returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Http Unauthorized error should be returned")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("a request from {someuser} for any url")
def step_impl(context, someuser):
    """
    :type context: behave.runner.Context
    :type someuser: str
    """
    pass


@step('the response has "{somestatus:d}" status')
def step_impl(context, somestatus):
    """
    :type context: behave.runner.Context
    :type somestatus: int
    """
    if not context.responses:
        assert False, 'No response'
    for response in context.responses:
        assert_that(response.status_code, equal_to(somestatus))


@then('I should get a "{warning}" warning with a "{status:d}" status')
def step_impl(context, warning, status):
    """
    :type context: behave.runner.Context
    :type status: int
    """
    pass


@when("I open main index url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = reverse(context.mapper, 'hello')
    response = context.test_app.get(url, status=200)
    context.response = response.json


@when('I post "{what}" to the "{where}" url')
def step_impl(context, what, where):
    url = reverse(context.mapper, where)
    context.responses = []
    if isinstance(context.post_data, model.Table):
        for data in context.post_data:
            context.responses.append(
                context.test_app.post(url, data)
            )
    else:
        context.responses.append(
            context.test_app.post(url, context.post_data)
        )



