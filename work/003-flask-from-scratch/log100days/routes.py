from flask import render_template

from log100days import app


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("home.html.j2")
