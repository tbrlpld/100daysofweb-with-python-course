# -*- coding: utf-8 -*-

"""Defines view functions for the billtracker app."""

from pyramid.view import view_config


@view_config(route_name="home", renderer="../templates/home.pt")
def home(request):
    """Render home template with given project name."""
    # noqa: DAR101, DAR201
    return {
        "project": "Bill Tracker",
        "items": [
            "item1",
            "item2",
            "item3",
            "item4",
        ],
    }
