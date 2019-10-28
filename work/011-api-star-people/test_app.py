# -*- coding: utf-8 -*-

"""Tests for user API."""

from http import HTTPStatus

import pytest
from apistar import test
#
from app import app

client = test.TestClient(app)


def test_get_users():
    """Test get all users."""
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    users = response.json()
    assert len(users) == 1000

    first_user = users[0]
    assert first_user["userid"] == 1
    assert first_user["username"] == "hyurikov0"
    last_user = users[-1]
    assert last_user["userid"] == 1000
    assert last_user["username"] == "bokeevanrr"


@pytest.mark.parametrize(("userid", "username"), [
    (1, "hyurikov0"),
    (1000, "bokeevanrr"),
])
def test_get_user(userid, username):
    """Test get of one user by its id."""
    response = client.get("/{0}".format(userid))
    assert response.status_code == HTTPStatus.OK
    assert response.json()["username"] == username


def test_get_user_notfound():
    """Test get user with id out of range."""
    response = client.get("/111111")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["error"] == "User not found."


def test_create_new_user():
    """Test creation of new user."""
    initial_user_count = len(client.get("/").json())
    assert initial_user_count == 1000

    new_user_data = {
        "userhash": "12345678901234567890123456789012",
        "username": "newuser",
        "fullname": "Some Body",
        "joined": "2019-10-27",
        "timezone": "Europe/Stockholm",
    }
    response = client.post("/", data=new_user_data)
    assert respone.status_code == HTTPStatus.CREATED

    assert len(client.get("/").json()) == initial_user_count + 1
    persistent_user = client.get("/1001")
    assert persistent_user["username"] == new_user_data["username"]
    assert persistent_user["fullname"] == new_user_data["fullname"]
    assert persistent_user["joined"] == new_user_data["joined"]


def test_create_new_user_with_no_data():
    """Create new user without passing any data."""
    empty_data = {}
    response = client.get("/", data=empty_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_new_user_with_invalid_data():
    """Create new user with invalid data."""
    invalid_data = {
        "userhash":"123",
        "username": "x" * 51,
        "fullname": "A" * 101,
        "joined": "2001-10-17",
        "timezone": "Moon/City",
    }
    response = client.get("/", data=invalid_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
