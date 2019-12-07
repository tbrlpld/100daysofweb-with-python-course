# -*- coding: utf-8 -*-

"""Define views and routes for the auth app."""

import responder

from api import api


@api.route("/")
def index(_: responder.Request, resp: responder.Response) -> None:
    """Render index page."""
    # noqa: DAR101, E800
    signup_url = api.url_for("signup")
    # print(api.jinja_values_base())
    resp.html = api.template("index.html.j2", api=api)


@api.route("/signup")
def signup(req: responder.Request, resp: responder.Response) -> None:
    """Show signup page on get and handle signup data on post."""
    # noqa: DAR101, E800

    if req.method == "post":
        api.redirect(resp, location=api.url_for("index"))

    resp.html = api.template("signup.html.j2", api=api)
