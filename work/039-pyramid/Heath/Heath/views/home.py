# -*- coding: utf-8 -*-

"""Defines home view for a uer."""

from typing import Optional, List

from pyramid.httpexceptions import HTTPForbidden
from pyramid.request import Request
from pyramid.view import view_config

from Heath.models.user import User
from Heath.models.account import Account, get_accounts_by_user


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request: Request):
    """Return dictionary containing the user associated with the request."""
    user: Optional[User] = request.user
    if user is None:
        raise HTTPForbidden()

    accounts: List[Account] = get_accounts_by_user(
        session=request.dbsession,
        user=user,
    )

    return {
        "user": user,
        "accounts": accounts,
    }
