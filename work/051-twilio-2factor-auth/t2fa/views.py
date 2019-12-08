# -*- coding: utf-8 -*-

"""Define views and routes for the auth app."""

import os
from random import random

import responder
from sqlalchemy.exc import IntegrityError
from twilio.rest import Client


from t2fa.api import api
from t2fa.db import Session
from t2fa.models.user import User


@api.route("/")
def index(_: responder.Request, resp: responder.Response) -> None:
    """Render index page."""
    # noqa: DAR101, E800

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
        user.phone_number = post_data["phone"]

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


@api.route("/login")
async def login(req: responder.Request, resp: responder.Response) -> None:
    """Show login page on get and handle login data on post."""
    # noqa: DAR101, E800

    errors = {}
    user = User()

    if req.method == "post":
        post_data = await req.media()

        dbsession = Session()

        user = dbsession.query(User).filter(
            User.username == post_data["username"],
        ).first()

        # Check password
        if post_data["password"] == user.password:
            # redirect to login confirm
            resp.session["username"] = user.username
            resp.session["identiy_confirmed"] = False
            api.redirect(resp, location=api.url_for("confirm_login"))
            return None
        else:
            errors["password"] = "Wrong password!"

    resp.html = api.template(
        "login.html.j2",
        api=api,
        errors=errors,
        user=user,
    )


def send_code_to_number(phone_number: str) -> str:
    """Send code to user per sms and return the code."""

    twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
    twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    client = Client(twilio_account_sid, twilio_auth_token)

    code = str(int(random() * 100000))

    print(phone_number)

    client.messages.create(
        to=phone_number,
        from_=twilio_phone_number,
        body="Here is login code: {0}".format(code),
    )

    return code


@api.route("/login/confirm")
async def confirm_login(req: responder.Request, resp: responder.Response) -> None:
    """Confirm the login via text code."""

    errors = {}

    username_from_session = req.session["username"]

    dbsession = Session()
    user = dbsession.query(User).filter(
        User.username == username_from_session,
    ).first()

    if req.method == "post":
        post_data = await req.media()
        posted_code = post_data["code"]
        session_code = req.session["code"]
        if posted_code == session_code:
            # User is verified
            resp.session["identiy_confirmed"] = True
            api.redirect(resp, location=api.url_for("home"))
            return None
        else:
            errors["code"] = "Code not confirmed. Try again."

    code = send_code_to_number(user.phone_number)
    resp.session["code"] = code

    resp.html = api.template(
        "login_confirm.html.j2",
        api=api,
        errors=errors,
    )


@api.route("/home")
async def home(req: responder.Request, resp: responder.Response) -> None:
    """Show user home."""
    if not resp.session["identiy_confirmed"]:
        api.redirect(resp, location=api.url_for("index"))
        return None

    username_from_session = req.session["username"]

    dbsession = Session()
    user = dbsession.query(User).filter(
        User.username == username_from_session,
    ).first()

    resp.text = "Logged in {0}".format(user.username)
