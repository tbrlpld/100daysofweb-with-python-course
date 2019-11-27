# -*- coding: utf-8 -*-

"""Defines authentication view for login / logout."""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember

from Heath.models import user


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    """Verify and save user's login information."""
    # Redirect logged in users to their home.
    if request.user is not None:
        return HTTPFound(location="/home")

    # Set forwarding url
    next_url = request.params.get("next", request.referrer)
    if not next_url or next_url.endswith("/login"):
        next_url = "/home"

    login_email = ""
    message = ""
    if "form-submit" in request.params:
        login_email = request.params["login"]
        password = request.params["password"]
        user_obj = user.get_by_email(
            session=request.dbsession,
            email=login_email,
        )
        if user_obj is not None and user_obj.check_password(password):
            headers = remember(request, user_obj.id_)
            return HTTPFound(location=next_url, headers=headers)
        else:
            message = "Login failed."

    return {
        "login": login_email,
        "message": message,
        "url": request.route_url("login"),
        "next_url": next_url,
    }
