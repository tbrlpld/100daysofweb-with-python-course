# -*- coding: utf-8 -*-

"""Define routes and views for the app."""

from flask import render_template, request, flash

from awesome import app, db
from awesome.models import User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create-user", methods=["GET", "POST"])
def create_user() -> str:
    """Create user in db or show form."""
    if request.method == "POST":
        add_user_to_db(
            username=request.form["username"],
            password=request.form["password"],
        )
        flash("User {u} created.".format(u=request.form["username"]))
    return render_template("create-user.html")


def add_user_to_db(username, password) -> None:
    """Create a user in the database."""
    user = User(
        username=username,
        password=password,
    )
    db.session.add(user)
    db.session.commit()


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    """Log in the user or show form."""
    if request.method == "POST":
        pass
    return render_template("login.html")
