from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from behave import *
from hamcrest import assert_that, equal_to, has_key, all_of, has_entries


use_step_matcher("parse")


@given("an app request has valid keys")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@given("an app request has some bad key\(s\)")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@given("app registration data")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    context.post_data = context.table


@when("I post it to the app registration url")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("I get an APIKey and a SecretKey in a response")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    for response in context.responses:
        body = json.loads(response.body.decode('utf-8'))
        has_keys = all_of(has_key('APIKey'), has_key('SecretKey'))
        assert_that(body, has_keys)


@then("the request is {authenticated}")
def step_impl(context, authenticated):
    """
    :type context behave.runner.Context
    :type authenticated str
    """
    pass


@given("registration data")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@when("I post it to user registration url")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then("I get a user token in a response")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@given(u'an app request has some bad key(s)')
def step_impl(context):
    pass


@given(u'the request has {sometoken} in the header')
def step_impl(context, sometoken):
    """
    :type context behave.runner.Context
    """
    pass


@then(u'the response has "{somestatus}"')
def step_impl(context, somestatus):
    """
    :type context behave.runner.Context
    """
    pass


@given(u'a request with a valid username/email and a password')
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then(u'the response should contain a token')
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then(u'a token is valid')
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@given(u'a request with invalid username/email and password')
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@then(u'the response should have "{status}" status')
def step_impl(context, status):
    """
    :type context behave.runner.Context
    """
    pass


@step("the request has \{sometoken\} in the header")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    pass


@step("I should get same data in a response when I open a registered app url")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    context.request_kwargs = {'api_key': 'apikey'}
    context.execute_steps(
        """When I open a "{where}" url""".format(where='userappresource')
    )
    expected = {
        'APIKey': 'apikey',
        'SecretKey': 'secretkey'
    }

    assert_that(context.response.json, has_entries(expected))
