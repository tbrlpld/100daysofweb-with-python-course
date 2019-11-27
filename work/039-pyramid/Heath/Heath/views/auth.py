# -*- coding: utf-8 -*-

"""Defines authentication view for login / logout."""

from pyramid.view import view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget

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


@view_config(route_name="logout")
def logout(request):
    """Log the currently logged in user out."""
    headers = forget(request)
    next_url = request.route_url("landing")
    return HTTPFound(location=next_url, headers=headers)


@forbidden_view_config()
def forbidden_view(request):
    """Redirect when a resource is not to be available."""
    if request.user is not None:
        # Logged-in users are redirected to their home.
        next_url = request.route_url("home")
    else:
        # Not logged-in users are redirected to the login page.
        # The url they where forbidden from seeing is passed as next parameter.
        next_url = request.route_url("login", _query={"next": request.url})
    return HTTPFound(location=next_url)
