# -*- coding: utf-8 -*-

"""Define package wide components."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"

db = SQLAlchemy(app)

from awesome import routes  # noqa: F401
