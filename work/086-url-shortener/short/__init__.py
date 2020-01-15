from flask import Flask, redirect, abort

from short.db import DynamoTable

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Lambda!"


@app.route("/x")
def exmple():
    return redirect("http://example.com")


@app.route("/<shortlink>")
def redirect_to_long(shortlink):
    table = DynamoTable()
    long_url = table.get_long_from_short(shortlink)
    if not long_url:
        abort(404)
    return redirect(long_url)
