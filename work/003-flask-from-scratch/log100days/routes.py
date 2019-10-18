import requests

from flask import render_template

from log100days import app


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("home.html.j2")


@app.route("/rules")
def rules():
    request = requests.get("https://raw.githubusercontent.com/tbrlpld/100-days-of-code/master/rules.md")
    return request.content


@app.route("/log")
def log():
    request = requests.get("https://raw.githubusercontent.com/tbrlpld/100-days-of-code/master/log.md")
    return request.content
