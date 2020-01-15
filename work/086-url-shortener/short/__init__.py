from flask import Flask, request, redirect, abort, jsonify

from short.db import DynamoTable

app = Flask(__name__)


@app.route("/")
def hello():
    host = request.host
    return f"Hello from Lambda! You requested me at: {host}"


# @app.route("/x")
# def exmple():
#     return redirect("http://example.com")


@app.route("/create", methods=["POST"])
def create():
    table = DynamoTable()
    long_url = request.form.get("long_url")
    if not long_url:
        abort(400)
    response = table.save_long_url(long_url)
    return jsonify(response)


@app.route("/<shortlink>")
def redirect_to_long(shortlink):
    table = DynamoTable()
    long_url = table.get_long_from_short(shortlink)
    if not long_url:
        abort(404)
    return redirect(long_url)
