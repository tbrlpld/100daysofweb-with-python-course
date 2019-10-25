# -*- coding: utf-8 -*-

"""Simple car data API."""

import json

from apistar import App, Route
from apistar.http import JSONResponse


def _load_car_data():
    with open("car_data.json") as car_data_file:
        car_data = json.load(car_data_file)[:12]
    return {car["id"]: car for car in car_data}


# Global variable acts as a stand in for an actual database connection.
cars = _load_car_data()

STATUS_OK = 200
STATUS_NOT_FOUND = 404


def get_cars() -> JSONResponse:
    """Return all cars as in a sorted list."""
    key_value_list = cars.items()
    sorted_key_value_list = sorted(key_value_list)
    list_of_car_dicts = [car[1] for car in sorted_key_value_list]
    return JSONResponse(list_of_car_dicts, STATUS_OK)


routes = [
    Route("/", method="get", handler=get_cars),
]

app = App(routes=routes)

if __name__ == "__main__":
    SERVER_PORT = 5000
    SERVER_IP = "127.0.0.1"
    app.serve(SERVER_IP, SERVER_PORT, debug=True)
