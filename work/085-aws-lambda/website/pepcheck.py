import os
import json

from flask import Flask, request, render_template, abort, Response
import requests


app = Flask(__name__)
API_GATEWAY = os.getenv("API_GATEWAY")


@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    peperrors = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        response = requests.post(
            API_GATEWAY,
            data=json.dumps({"code": code}),
        )
        response_data = response.json()

        err = response_data.get("errorType")
        if err:
            msg = response_data.get("errorMessage")
            abort(Response(
                f"The code processing API raised an {err} exception: {msg}",
                status=400,
            ))
        peperrors = response_data.get("body", "")

    return render_template(
        "index.jinja2",
        code=code,
        peperrors=peperrors,
    )
