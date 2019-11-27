# -*- coding: utf-8 -*-.

"""Defines the authentication for the app."""

from typing import Optional

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.request import Request

from Heath.models import user


class HeathAuthenticationPolicy(AuthTktAuthenticationPolicy):
    """Authentication features and policy for Heath app."""

    def authenticated_user(self, request):
        """Return id of authenticated user from request."""
        user = request.user
        if user is not None:
            return user.id


def get_user(request: Request) -> Optional[user.User]:
    """
    Return user from database if available.

    The user id in the request has to be treated as unauthenticated, because
    this is based on external information. The id from the request it looked up
    in the database. I the id exists, that user object is returned. None is
    returned if the user is not found.
    """
    user_id = request.unauthenticated_userid
    session = request.dbsession
    if user_id is not None:
        return user.get_by_id(session, user_id)
    return None


def includeme(config):
    """
    Not sure what this does.

    I guess it is called some where and then what I am defining in here is
    added to the app configuration. Guess this happens when the app is created.

    I do not know how the configuration can be retrieved (outside of functions
    that are called by the config it self...
    """
    settings = config.get_settings()
    authn_policy = HeathAuthenticationPolicy(
        settings["auth.secret"],
        hashalg="sha512",  # I don't think this is actually applied somewhere.
    )

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, "user", reify=True)
