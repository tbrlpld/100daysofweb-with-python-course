# -*- coding: utf-8 -*-

"""Define routes and views for the app."""

from typing import Union

from flask import (
    flash,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    logout_user,
    current_user,
)
from werkzeug.wrappers import Response  # for typing
from sqlalchemy.exc import IntegrityError

from awesome import app, db
from awesome.models import User


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route("/")
def index() -> str:
    """Return simple index page."""
    return render_template("index.html.j2")


@app.route("/signup", methods=["GET", "POST"])
def signup() -> str:
    """Create user in db or show form."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            add_user_to_db(
                username=username,
                password=password,
            )
        except IntegrityError:
            flash("Username '{username}' not available.".format(
                username=username,
            ))
        else:
            flash("User {u} created.".format(u=request.form["username"]))
    return render_template("signup.html.j2")


def add_user_to_db(username, password) -> None:
    """Create a user in the database."""
    user = User(
        username=username,
        password=password,  # Hashing is done in the ORM automatically.
    )
    db.session.add(user)
    db.session.commit()


@app.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response]:
    """Log in the user or show form."""
    # Only anonymous users can see the login.
    # Other users are already logged in.
    if not current_user.is_anonymous:
        # Logged in users are redirected
        return redirect(url_for("members_only"))
    if request.method == "POST":
        # Get user
        user = User.query.filter_by(username=request.form["username"]).first()
        if user:
            # Check password
            if user.verify_password(request.form["password"]):
                # Log user in
                login_user(user)
                # Redirect to member site
                flash("Login successful.")
                return redirect(url_for("members_only"))
        # In case of issue, create a message
        flash("Username or password not correct!")
    return render_template("login.html.j2")


@login_manager.user_loader
def load_user(user_id):
    """Load user from db."""
    return User.query.get(int(user_id))


@app.route("/logout")
@login_required
def logout() -> Response:
    """Log the currently logged in user out."""
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("index"))


@app.route("/members-only")
@login_required
def members_only():
    """Return view for logged in users."""
    return render_template("members-only.html.j2")
