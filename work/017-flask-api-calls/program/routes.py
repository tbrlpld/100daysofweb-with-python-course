# -*- coding: utf-8 -*-

"""Routes for the simple flask demo app."""

# Standard Library Imports
from datetime import datetime
from http import HTTPStatus

# Thrid-Party Imports
from flask import render_template, request
import requests

# First-Party Imports
from program import app


@app.route("/")
@app.route("/index")
def index():
    """Render simple index template."""
    today = datetime.today()
    return render_template("index.html.j2", today=today)


@app.route("/100days")
def route100days():
    """Render a simple second page that is different from the index."""
    return render_template("100days.html.j2")


def get_chuck_norris_joke():
    """Get a random Chuck Norris joke from the API."""
    response = requests.get("https://api.chucknorris.io/jokes/random")
    json_data = response.json()
    return json_data["value"]


@app.route("/chuck")
def chuck():
    """Render template that displays a random Chuck Norris joke."""
    joke = get_chuck_norris_joke()
    return render_template("chuck.html.j2", joke=joke)


def get_beers_ordered_by_ibu():
    """Return beer data sorted by descending IBU."""
    response = requests.get(
        "https://sandbox-api.brewerydb.com/v2/"
        + "beers/?order=ibu&sort=DESC&withBreweries=Y"
        + "&key=cb1ce0c7f124fd5dd98f2a57d19120c4",
    )
    full_beer_data = response.json()["data"]
    reduced_beer_data = []
    for beer in full_beer_data:
        new_beer = {}
        new_beer["name"] = beer["nameDisplay"]
        new_beer["brewery"] = beer["breweries"][0]["nameShortDisplay"]
        new_beer["ibu"] = beer["ibu"]
        reduced_beer_data.append(new_beer)
    return reduced_beer_data


@app.route("/beer")
def beer():
    """Render template to show beers sorted by IBU."""
    beer_data = get_beers_ordered_by_ibu()
    return render_template("beers.html.j2", beers=beer_data)


def get_pokemon_of_color(color):
    """Get names of Pokemon with a certain color."""
    color_url = "https://pokeapi.co/api/v2/pokemon-color/{0}".format(
        color.lower(),
    )
    response = requests.get(color_url)
    if response.status_code == HTTPStatus.OK:
        response_data = response.json()
        species = response_data.get("pokemon_species")
        return [specie["name"] for specie in species if species]
    return []


def get_forms_of_pokemon_species(species):
    """Get possible forms for given species."""
    form_url = "https://pokeapi.co/api/v2/pokemon-species/{0}".format(
        species.lower(),
    )
    response = requests.get(form_url)
    forms = []
    if response.status_code == HTTPStatus.OK:
        response_data = response.json()
        for variety in response_data["varieties"]:
            poke_form_name = variety["pokemon"]["name"]
            if poke_form_name.lower() != species.lower():
                forms.append(poke_form_name)
    return forms


@app.route("/pokemon", methods=["POST", "GET"])
def pokemon():
    """Render template showing Pokemon by color according to user input."""
    # TODO: Add form, nature and habitat to displayed table.
    color = request.form.get("pokecolor")
    pokemon_of_color = []
    pokemon_with_data = []
    if color:
        pokemon_of_color = get_pokemon_of_color(color)
        # This is not a good implementation, because after getting the Pokemon
        # with a certain color, now I need to get each species to extract the
        # forms.
        for poke in pokemon_of_color:
            print("Extending Species: {0}".format(poke))
            extended_poke = {}
            extended_poke["name"] = poke
            extended_poke["forms"] = get_forms_of_pokemon_species(species=poke)
            pokemon_with_data.append(extended_poke)
    return render_template("pokemon.html.j2", pokemon=pokemon_with_data)
