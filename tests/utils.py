# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


_URL_NAMES_MAP = {
    'app registration': 'collection_userappresource'
}


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
