# -*- coding: utf-8 -*-

"""Defines home view functions for the billtracker app."""

from typing import Optional, Dict

from pyramid.view import view_config

from billtracker.data import repository
from billtracker.data.models.users import User


@view_config(route_name="home", renderer="../templates/home.pt")
def home(request) -> Dict:
    """Render home template with given project name."""
    # noqa: DAR101, DAR201
    user_id: int = 1
    user: Optional[User] = repository.get_user_by_id(user_id)

    return {
        "user": user,
    }
