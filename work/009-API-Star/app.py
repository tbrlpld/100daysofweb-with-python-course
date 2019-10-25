# -*- coding: utf-8 -*-

"""Simple car data API."""

import json

from apistar import App, Route, types, validators
from apistar.http import JSONResponse


def _load_car_data():
    with open("car_data.json") as car_data_file:
        car_data = json.load(car_data_file)
    return {car["id"]: car for car in car_data}


# Global variable acts as a stand in for an actual database connection.
cars = _load_car_data()

# Response status codes.
STATUS_OK = 200
STATUS_CREATED = 201
STATUS_FORBIDDEN = 403
STATUS_NOT_FOUND = 404

# Error messages
ERROR_CAR_NOT_FOUND = {"error", "Car not found."}
ERROR_CAR_EXISTS = {"error": "Car already exists."}

# Creating set of valid make names.
VALID_MAKES = list({car["make"] for car in cars.values()})


class Car(types.Type):
    """Simple Car class."""

    # allow_null required to assign id manually.
    id = validators.Integer(allow_null=True)
    make = validators.String(enum=VALID_MAKES)
    model = validators.String(min_length=1, max_length=50)
    year = validators.Integer(minimum=1900, maximum=2050)
    vin = validators.String(max_length=50, default="")


def _car_exists(car: Car) -> bool:
    """Check if car already exists in storage."""
    for existing_car in cars.values():
        found = (
            existing_car["make"] == car.make
            and existing_car["model"] == car.model
            and existing_car["year"] == car.year
        )
        if found:
            return True
    return False


def get_cars() -> JSONResponse:
    """Return all cars as in a sorted list."""
    key_value_list = cars.items()
    sorted_key_value_list = sorted(key_value_list)
    list_of_car_objs = [Car(car[1]) for car in sorted_key_value_list]
    return JSONResponse(list_of_car_objs, STATUS_OK)


def create_car(car: Car) -> JSONResponse:
    """Create car in 'presistent' storage."""
    # Generating increased id. This is not concurrency proof and would usually
    # happen in the DB automatically.
    new_car_id = len(cars) + 1
    # Adding generated id to car object (passed in from request)
    car.id = new_car_id
    # Error if car is duplicate
    if _car_exists(car):
        return JSONResponse(ERROR_CAR_EXISTS, STATUS_FORBIDDEN)
    # Saving the car in the storage variable
    cars[car.id] = car
    return JSONResponse(car, STATUS_CREATED)


def get_car(car_id: int) -> JSONResponse:
    """Return car with given id."""
    car = cars.get(car_id)
    if not car:
        return JSONResponse(ERROR_CAR_NOT_FOUND, STATUS_NOT_FOUND)
    return JSONResponse(Car(car), STATUS_OK)


def update_car(car_id: int, car: Car) -> JSONResponse:
    """Update stored car with new data."""
    if not car_id in cars:
        return JSONResponse(ERROR_CAR_NOT_FOUND, STATUS_NOT_FOUND)
    car_obj = Car(car)
    car_obj.id = car_id
    cars[car_id] = car_obj
    return JSONResponse(car_obj)


routes = [
    Route("/", method="get", handler=get_cars),
    Route("/", method="post", handler=create_car),
    Route("/{car_id}", method="get", handler=get_car),
    Route("/update/{car_id}", method="put", handler=update_car),
]

app = App(routes=routes)

if __name__ == "__main__":
    SERVER_PORT = 5000
    SERVER_IP = "127.0.0.1"
    app.serve(SERVER_IP, SERVER_PORT, debug=True)
