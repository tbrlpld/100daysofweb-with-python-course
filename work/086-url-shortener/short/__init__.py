from urllib.parse import urljoin

from flask import Flask, request, redirect, abort, jsonify, render_template, url_for

from short.db import DynamoTable

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_form():
    return render_template(
        "shorten_form.jinja2",
    )


@app.route("/", methods=["POST"])
def post_form():
    dbresponse = process_post_request(request)
    return render_template(
        "short_display.jinja2",
        **dbresponse,
    )


@app.route("/apidoc")
def apidoc():
    host_url = request.host_url
    create_endpoint = urljoin(host_url, url_for("create"))
    return render_template(
        "apidoc.jinja2",
        host_url=host_url,
        create_endpoint=create_endpoint,
    )


@app.route("/create", methods=["POST"])
def create():
    dbresponse = process_post_request(request)
    return jsonify(dbresponse)


def process_post_request(request):
    """Convert post request into dbresponse."""
    table = DynamoTable()
    long_url = request.form.get("long_url")
    if not long_url:
        abort(400)
    dbresponse = table.save_long_url(long_url)
    dbresponse["short"] = urljoin(request.host_url, dbresponse["short"])
    return dbresponse


@app.route("/<shortlink>")
def redirect_to_long(shortlink):
    table = DynamoTable()
    long_url = table.get_long_from_short(shortlink)
    if not long_url:
        abort(404)
    return redirect(long_url)
