# -*- coding: utf-8 -*-

"""Defines the security functionality for the app."""

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


from billtracker.data import repository


class MyAuthenticationPolicy(AuthTktAuthenticationPolicy):
    """Defines the auth policy for the app."""

    def authenticated_user(self, request):
        """Return id of authenticated user from request."""
        user = request.user
        if user is not None:
            return user.id


def get_user(request):
    """Return User object from database with given id."""
    user_id = request.unauthenticated_userid
    if user_id is not None:
        user = repository.get_user_by_id(user_id)
        return user


def includeme(config):
    settings = config.get_settings()
    authn_policy = MyAuthenticationPolicy(
        settings["auth.secret"],
        hashalg="sha512",
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, "user", reify=True)

