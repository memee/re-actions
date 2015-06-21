import json
from behave import *
from behave import model
from hamcrest import assert_that, equal_to, is_


use_step_matcher("parse")


_URL_NAMES_MAP = {
    'app registration': 'collection_userapp'
}


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


def reverse(routes_mapper, view_name, **kwargs):
    """Returns url path for view name

    It acts similar to django reverse and differently than Pyramid
    `request.route_url` which return full/absolute url

    :param routes_mapper:
        RoutesMapper instance acquired from application instance
    :param view_name:
        Name of view registered with `@view_config`
    :return:
        Url path
    :rtype:
        str
    """
    # if there's url configured in url names map, use that
    view_name = _URL_NAMES_MAP.get(view_name, view_name)
    route = routes_mapper.get_route(view_name)

    if not route:
        msg = 'Route {} is not configured for this app'.format(view_name)
        raise LookupError(msg)
    return route.generate(kwargs)
