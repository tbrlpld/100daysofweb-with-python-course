# -*- coding: utf-8 -*-

"""Define movie API endpoint views."""

import responder

from api import api
from data import db


# Search movies
# GET /api/search/{keyword}
@api.route("/api/search/{keyword}")
def search_by_keyword(_, response: responder.Response, keyword: str) -> None:
    movies = db.search_keyword(keyword)

    # Limit returns. Why ever... The limit seems arbitrary.
    max_returns = 10
    if len(movies) > max_returns:
        movies = movies[:max_returns]

    movie_dicts = [db.movie_to_dict(movie) for movie in movies]

    response.media = {
        "Searched": keyword,
        "Found": len(movie_dicts),
        "Results": movie_dicts,
    }


# Movies by director
# GET /api/director/{director_name}
@api.route("/api/director/{director_name}")
def search_by_director(
    _,
    response: responder.Response,
    director_name: str,
) -> None:

    movies = db.search_director(director_name)

    # Limit returns. Why ever... The limit seems arbitrary.
    max_returns = 10
    if len(movies) > max_returns:
        movies = movies[:max_returns]

    movie_dicts = [db.movie_to_dict(movie) for movie in movies]

    response.media = {
        "Searched": director_name,
        "Found": len(movie_dicts),
        "Results": movie_dicts,
    }


# Movie by IMDB code
# GET /api/movie/{imdb_number}
@api.route("/api/movie/{imdb_number}")
def search_by_imdb_number(
    _,
    response: responder.Response,
    imdb_number: str,
) -> None:
    movie = db.find_by_imdb(imdb_number)
    movie_dict = db.movie_to_dict(movie)
    response.media = movie_dict
