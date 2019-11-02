# -*- coding: utf-8 -*-

"""Routes for the simple flask demo app."""

# Standard Library Imports
from datetime import datetime

# Thrid-Party Imports
from flask import render_template

# First-Party Imports
# Flask is already imported in the __init__.py
from program import app  # This is in the __init__.py
# Now I have the app


@app.route("/")
@app.route("/index")
def index():
    today = datetime.today()
    return render_template("index.html.j2", today=today)


@app.route("/100days")
def route100days():
    return render_template("100days.html.j2")
