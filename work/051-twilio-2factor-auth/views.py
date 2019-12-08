# -*- coding: utf-8 -*-

"""Define views and routes for the auth app."""

import responder
from sqlalchemy.exc import IntegrityError

from api import api
from db import Session
from models.user import User


@api.route("/")
def index(_: responder.Request, resp: responder.Response) -> None:
    """Render index page."""
    # noqa: DAR101, E800
    signup_url = api.url_for("signup")
    # print(api.jinja_values_base())
    resp.html = api.template("index.html.j2", api=api)


@api.route("/signup")
async def signup(req: responder.Request, resp: responder.Response) -> None:
    """Show signup page on get and handle signup data on post."""
    # noqa: DAR101, E800

    errors = {}
    user = User()

    if req.method == "post":
        post_data = await req.media()

        user.username = post_data["username"]
        user.password = post_data["password"]
        user.phone_number = post_data["password"]

        dbsession = Session()
        dbsession.add(user)

        try:
            dbsession.commit()
        except IntegrityError:
            errors["username"] = "Username exists already!"

        if not errors:
            api.redirect(resp, location=api.url_for("index"))

    resp.html = api.template(
        "signup.html.j2",
        api=api,
        errors=errors,
        user=user,
    )
