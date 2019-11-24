# -*- coding: utf-8 -*-

"""Defines bill view functions for the billtracker app."""

from typing import Optional, Dict, List

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPBadRequest,
    HTTPFound,
    HTTPForbidden,
)
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
    user = request.user

    bill = get_bill_or_client_error(
        bill_id=request.matchdict.get("bill_id"),
    )

    verfiy_user_access_to_bill(user, bill)

    return {
        "bill": bill,
        "user": user,
        "error": "",
    }


@view_config(
    route_name="bill_detail",
    renderer="../templates/bill_detail.pt",
    request_method="POST",
)
def bill_detail_post(request: Request) -> Dict:
    """Render home template with given project name."""
    # noqa: DAR101, DAR201
    user = request.user

    bill = get_bill_or_client_error(
        bill_id=request.matchdict.get("bill_id"),
    )

    verfiy_user_access_to_bill(user, bill)

    errors: List = []
    amount_str: str = request.POST.get("amount", "")
    try:
        amount: int = int(amount_str)
    except ValueError:
        errors.append("Amount has to be integer.")
    else:
        if amount < 0:
            errors.append("Amount has to larger than zero.")
        if amount > bill.open:
            errors.append("Amount should be small than open amount.")

    if errors:
        return {
            "bill": bill,
            "user": user,
            "error": " ".join(errors),
            "amount": amount_str,
        }

    repository.add_payment(amount=amount, bill_id=bill.id)
    raise HTTPFound(location="/bill/{0}".format(bill.id))


def get_bill_or_client_error(bill_id):
    try:
        bill_id: int = int(bill_id)
    except ValueError:
        raise HTTPBadRequest()
    else:
        bill: Optional[Bill] = repository.get_bill_by_id(bill_id)
        if bill is None:
            raise HTTPNotFound()
    return bill


def verfiy_user_access_to_bill(user, bill):
    """Raise HTTPForbidden if use has no access."""
    if user is None or user.id != bill.user.id:
        raise HTTPForbidden()
