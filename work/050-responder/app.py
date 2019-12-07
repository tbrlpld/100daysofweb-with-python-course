# -*- coding: utf-8 -*-

"""Simple responder app for an API with a landing page."""

import responder

from data import db


api = responder.API()
db.global_init()


def main():
    api.run()


@api.route("/")
def index(_, response: responder.Response) -> None:
    response.html = api.template("/index.html", recreator="Tibor")


# Search movies
# GET /api/search/{keyword}
@api.route("/api/search/{keyword}")
def search_by_keyword(_, response: responder.Response, keyword: str) -> None:
    response.media = {"searched": keyword}


# Movies by director
# GET /api/director/{director_name}
@api.route("/api/director/{director_name}")
def search_by_director(_, response: responder.Response, director_name: str) -> None:
    response.media = {"searched": director_name}


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


# Top 10 Movies (by IMDB score)
# GET /api/movie/top
@api.route("/api/movie/top")
def top_movies(_, response: responder.Response) -> None:
    response.media = {"searched": "Top 10 Movies"}


# All genres
# GET /api/movie/genre/all
@api.route("/api/movie/genre/all")
def all_genres(_, response: responder.Response) -> None:
    response.media = {"Genres": "All"}


# Top movies for a given genres
# GET /api/movie/genre/{genre}
@api.route("/api/movie/genre/{genre}")
def search_by_genre(_, response: responder.Response, genre: str) -> None:
    response.media = {"searched": genre}


if __name__ == "__main__":
    main()
