# -*- coding: utf-8 -*-

"""Routes for the simple flask demo app."""

# Standard Library Imports
from datetime import datetime

# Thrid-Party Imports
from flask import render_template
import requests

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


def get_chuck_norris_joke():
    """Get a random Chuck Norris joke from the API."""
    response = requests.get("https://api.chucknorris.io/jokes/random")
    json_data = response.json()
    return json_data["value"]


@app.route("/chuck")
def chuck():
    joke = get_chuck_norris_joke()
    return render_template("chuck.html.j2", joke=joke)


def get_beers_ordered_by_ibu():
    brewerydb_url = "https://sandbox-api.brewerydb.com/v2/"
    endpoint = "beers/?order=ibu&sort=DESC&withBreweries=Y"
    sandbox_api_key = "cb1ce0c7f124fd5dd98f2a57d19120c4"
    response = requests.get(
        brewerydb_url
        + endpoint
        + "&key="
        + sandbox_api_key,
    )
    return response.json()["data"]


@app.route("/beer")
def beer():
    beer_data = get_beers_ordered_by_ibu()
    return render_template("beers.html.j2", beers=beer_data)


@app.route("/pokemon", methods=["POST", "GET"])
def pokemon():
    return render_template("pokemon.html.j2")
