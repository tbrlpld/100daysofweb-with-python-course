# -*- coding: utf-8 -*-

"""Defines account view."""

from typing import Optional, List, Dict

from pyramid.httpexceptions import HTTPForbidden
from pyramid.request import Request
from pyramid.view import view_config
from sqlalchemy.orm import Session

from Heath.models.account import Account, get_account_by_id


@view_config(route_name='account', renderer='../templates/account.jinja2')
def account(request: Request) -> Dict:
    """Return dictionary account information."""
    # Get account
    account_id: int = request.matchdict.get("account_id")
    account_obj: Optional[Account] = get_account_by_id(
        session=request.dbsession,
        account_id=account_id,
    )
    # Check access

    # Get records

    return {
        "account": account_obj,
    }
