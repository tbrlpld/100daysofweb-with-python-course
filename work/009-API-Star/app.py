# -*- coding: utf-8 -*-

"""Simple car data API."""

import json
from pprint import pprint

from apistar import App, Route


def _load_car_data():
    with open("car_data.json") as car_data_file:
        car_data = json.load(car_data_file)
    return {car["id"]: car for car in car_data}


cars = _load_car_data()


def dummy():
    return "hello world!"


routes = [
    Route("/", method="get", handler=dummy),
]

app = App(routes=routes)

if __name__ == "__main__":
    SERVER_PORT = 5000
    SERVER_IP = "127.0.0.1"
    app.serve(SERVER_IP, SERVER_PORT, debug=True)
