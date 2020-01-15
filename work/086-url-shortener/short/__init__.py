import os

from flask import Flask, request, redirect, abort, jsonify

from short.db import DynamoTable

app = Flask(__name__)


# @app.route("/")
# def hello():
#     host = request.host_url
#     return f"Hello from Lambda! You requested me at: {host}"


@app.route("/create", methods=["POST"])
def create():
    table = DynamoTable()
    long_url = request.form.get("long_url")
    if not long_url:
        abort(400)
    dbresponse = table.save_long_url(long_url)
    dbresponse["short"] = os.path.join(request.host_url, dbresponse["short"])
    return jsonify(dbresponse)


@app.route("/<shortlink>")
def redirect_to_long(shortlink):
    table = DynamoTable()
    long_url = table.get_long_from_short(shortlink)
    if not long_url:
        abort(404)
    return redirect(long_url)
