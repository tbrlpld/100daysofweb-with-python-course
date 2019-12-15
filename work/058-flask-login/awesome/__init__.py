# -*- coding: utf-8 -*-

"""Define package wide components."""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.secret_key = os.urandom(32)

db = SQLAlchemy(app)


from awesome import routes  # noqa: F401
from awesome import models  # noqa: F401
