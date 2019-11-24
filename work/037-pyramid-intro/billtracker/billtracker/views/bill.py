# -*- coding: utf-8 -*-

"""Defines bill view functions for the billtracker app."""

from typing import Optional, Dict

from pyramid.httpexceptions import HTTPNotFound
from pyramid.request import Request
from pyramid.view import view_config

from billtracker.data import repository
from billtracker.data.models.users import User
from billtracker.data.models.bill import Bill


@view_config(
    route_name="bill_detail",
    renderer="../templates/bill_detail.pt",
    request_method="GET",
)
def bill_detail_get(request: Request) -> Dict:
    """Render home template with given project name."""
    # noqa: DAR101, DAR201
    user_id: int = 1
    user: Optional[User] = repository.get_user_by_id(user_id)

    try:
        bill_id: int = int(request.matchdict.get("bill_id"))
    except ValueError:
        raise HTTPNotFound()
    else:
        bill: Optional[Bill] = repository.get_bill_by_id(bill_id)
        if bill is None:
            raise HTTPNotFound()

    return {
        "bill": bill,
        "user": user,
        "error": "",
    }
