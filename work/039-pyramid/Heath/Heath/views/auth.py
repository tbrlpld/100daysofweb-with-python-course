# -*- coding: utf-8 -*-

"""Defines authentication view for login / logout."""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from Heath.models import user


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    """Verify and save user's login information."""
    # Redirect logged in users to their home.
    if request.user is not None:
        raise HTTPFound(location="/home")

    # Set forwarding url
    next_url = request.params.get("next", request.referrer)
    if not next_url or next_url == "/login":
        next_url = "/home"

    message = ""
    login = ""
    if "form.submitted" in reqeust.params:
        login = request.params["login"]
        password = request.params["password"]
        user = user.get_by_email(login)

    return {'user': user}

