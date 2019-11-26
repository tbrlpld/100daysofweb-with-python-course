# -*- coding: utf-8 -*-

"""Defines home view for a uer."""

from pyramid.view import view_config

from .. import models


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    """Return dictionary containing the user associated with the request."""
    # TODO: Actual make the returned user based on the login.
    user = models.user.get_by_email(
        session=request.dbsession,
        email="kyurlov1@symantec.com",
    )
    return {'user': user}
