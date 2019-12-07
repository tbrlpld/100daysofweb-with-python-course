# -*- coding: utf-8 -*-

"""Define views and routes for the auth app."""

import responder

from api import api


@api.route("/")
def index(_: responder.Request, resp: responder.Response) -> None:
    """Render index page."""
    # noqa: DAR101, E800
    resp.html = api.template("index.html.j2")
