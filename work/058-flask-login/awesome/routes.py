# -*- coding: utf-8 -*-

"""Define routes and views for the app."""

from flask import render_template

from awesome import app


@app.route("/")
def index():
    return render_template("index.html")
