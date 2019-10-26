# -*- coding: utf-8 -*-

"""Tests for the cars API app."""

import pytest
from apistar import test
#
from app import STATUS_CREATED, STATUS_NOT_FOUND, STATUS_OK, app

client = test.TestClient(app)


def test_get_cars():
    """Test get list of cars."""
    response = client.get("/")
    assert response.status_code == STATUS_OK

    cars = response.json()
    assert len(cars) == 1000
    # first id should be 1
    assert cars[0]["id"] == 1
    # last id should be 1000
    assert cars[-1]["id"] == 1000

    expected_first_car = {
        "id": 1,
        "make": "BMW",
        "model": "3 Series",
        "year": 1998,
        "vin": "JH4CU2F60AC794232",
    }
    assert cars[0] == expected_first_car


def test_get_car_invalid_id():
    """Test get of car with invalid id."""
    response = client.get("/11111")
    assert response.status_code == STATUS_NOT_FOUND


@pytest.mark.parametrize(
    ("car_id, expected_car"), [
        (1, {
            "id": 1,
            "make": "BMW",
            "model": "3 Series",
            "year": 1998,
            "vin": "JH4CU2F60AC794232",
        }),
        (10, {
            "id": 10,
            "make": "Mitsubishi",
            "model": "Eclipse",
            "year": 2007,
            "vin": "WAULFAFH3AN549756",
        }),
        (1000, {
            "id": 1000,
            "make": "Lexus",
            "model": "IS",
            "year": 2001,
            "vin": "WA1CMBFP8EA251118",
        }),
    ],
)
def test_get_car_valid_id(car_id, expected_car):
    """Test get of car with valid ids."""
    response = client.get("/{0}".format(car_id))
    assert response.status_code == STATUS_OK
    assert response.json() == expected_car


def test_create_car_bad_data():
    """Test creation of car with data that violates the validation."""
    car_data = {
        "make": "BMWNotValid",  # must be in existing makes
        "model": "longname" * 10,  # must not be longer than 50
        "year": 2051,  # must be between 1900 and 2050
    }
    response = client.post("/", data=car_data)
    # These responses are automatically generated by apistar.
    status_bad_request = 400
    assert response.status_code == status_bad_request
    error_messages = response.json()
    assert "Must be one of" in error_messages["make"]
    assert "Must have no more than 50 characters." in error_messages["model"]
    assert "Must be less than or equal to 2050." in error_messages["year"]


def test_create_car_valid_data():
    """Test creation of car with valid data."""
    initial_number_of_cars = len(client.get("/").json())

    car_data = {
        "make": "BMW",
        "model": "3 Series New",
        "year": 2019,
        "vin": "abc",
    }
    response = client.post("/", data=car_data)
    assert response.status_code == STATUS_CREATED

    assert len(client.get("/").json()) == initial_number_of_cars + 1


def test_update_car_invalid_id():
    """Test update of car with invalid id."""
    car_data = {
        "id": 1,
        "make": "BMW",
        "model": "3 Series",
        "year": 1998,
        "vin": "JH4CU2F60AC794232",
    }
    response = client.put("/11111", data=car_data)
    assert response.status_code == STATUS_NOT_FOUND


def test_update_car_bad_data():
    """Test update of car with data that violates the validation."""
    car_data = {
        "id": 1,
        "make": "BMWNotValid",  # must be in existing makes
        "model": "longname" * 10,  # must not be longer than 50
        "year": 2051,  # must be between 1900 and 2050
        "vin": "JH4CU2F60AC794232",
    }
    response = client.put("/1", data=car_data)
    # These responses are automatically generated by apistar.
    status_bad_request = 400
    assert response.status_code == status_bad_request
    error_messages = response.json()
    assert "Must be one of" in error_messages["make"]
    assert "Must have no more than 50 characters." in error_messages["model"]
    assert "Must be less than or equal to 2050." in error_messages["year"]


def test_update_car_valid_id():
    """Test update of car with invalid id."""
    car_data = {
        "id": 1,
        "make": "BMW",
        "model": "3 Series New",
        "year": 2019,
        "vin": "JH4CU2F60AC794232",
    }
    response = client.put("/1", data=car_data)
    assert response.status_code == STATUS_OK
    assert response.json() == car_data

    # Checking data persistence with get
    response = client.get("/1")
    assert response.json() == car_data
