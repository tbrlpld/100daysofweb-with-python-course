# -*- coding: utf-8 -*-

"""Defines home view for a uer."""

from pyramid.httpexceptions import HTTPForbidden
from pyramid.view import view_config

from .. import models


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    """Return dictionary containing the user associated with the request."""
    user = request.user
    if user is None:
        raise HTTPForbidden()

    return {'user': user}
