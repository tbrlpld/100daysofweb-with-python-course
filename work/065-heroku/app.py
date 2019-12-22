# -*- coding: utf-8 -*-

"""Super simple flask app to deploy on Heroku as an example."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
