# -*- coding: utf-8 -*-

"""Defines bill view functions for the billtracker app."""

from typing import Optional, Dict, List

from pyramid.httpexceptions import HTTPNotFound, HTTPFound
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


@view_config(
    route_name="bill_detail",
    renderer="../templates/bill_detail.pt",
    request_method="POST",
)
def bill_detail_post(request: Request) -> Dict:
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
