# -*- coding: utf-8 -*-

"""Tests for the cars API app."""

from apistar import test
#
from app import app, STATUS_OK

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
        "id":1,
        "make":"BMW",
        "model":"3 Series",
        "year":1998,
        "vin":"JH4CU2F60AC794232",
    }
    assert cars[0] == expected_first_car
