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
        "timezone": "Europe/Stockholm",
    }
    response = client.post("/", data=new_user_data)
    assert response.status_code == HTTPStatus.CREATED
    new_user = response.json()
    assert new_user["userid"] == 1001
    assert new_user["username"] == new_user_data["username"]
    assert new_user["userhash"] == new_user_data["userhash"]
    assert new_user["fullname"] == new_user_data["fullname"]

    new_user_count = len(client.get("/").json())
    assert new_user_count == initial_user_count + 1
    assert new_user_count == 1001
    response = client.get("/1001")
    assert response.status_code == HTTPStatus.OK
    persistent_user = response.json()
    assert persistent_user["username"] == new_user_data["username"]
    assert persistent_user["userhash"] == new_user_data["userhash"]
    assert persistent_user["fullname"] == new_user_data["fullname"]


def test_create_new_user_with_no_data():
    """Create new user without passing data."""
    empty_data = {}
    response = client.post("/", data=empty_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    error_data = response.json()
    assert "May not be null." in error_data


def test_create_new_user_with_wrong_data():
    """Create new user with passing wrong data."""
    wrong_data = {"somekey": "somevalue"}
    response = client.post("/", data=wrong_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    error_data = response.json()
    assert 'The \"userhash\" field is required.' in error_data["userhash"]
    assert 'The \"username\" field is required.' in error_data["username"]
    assert 'The \"fullname\" field is required.' in error_data["fullname"]
    assert 'The \"timezone\" field is required.' in error_data["timezone"]


def test_create_new_user_with_invalid_data():
    """Create new user with invalid data."""
    invalid_data = {
        "userhash": "123",
        "username": "x" * 51,
        "fullname": "A" * 101,
        "timezone": "Moon/City",
    }
    response = client.post("/", data=invalid_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    error_data = response.json()
    assert "Must have at least 32 characters." in error_data["userhash"]
    assert "Must have no more than 50 characters." in error_data["username"]
    assert "Must have no more than 100 characters." in error_data["fullname"]
    assert "Must be one of" in error_data["timezone"]


def test_update_user():
    """Test update user."""
    response = client.get("/1")
    assert response.status_code == HTTPStatus.OK
    initial_user_data = response.json()
    assert initial_user_data["username"] == "hyurikov0"

    new_user_data = {
        "userhash": "12345678901234567890123456789012",
        "username": "newuser",
        "fullname": "Some Body",
        "timezone": "Europe/Stockholm",
    }
    response = client.put("/1", data=new_user_data)
    assert response.status_code == HTTPStatus.OK
    returned_user_data = response.json()
    assert returned_user_data["userid"] == initial_user_data["userid"]
    assert returned_user_data["username"] == new_user_data["username"]

    response = client.get("/1")
    assert response.status_code == HTTPStatus.OK
    persistent_user_data = response.json()
    assert persistent_user_data["username"] == new_user_data["username"]
    assert persistent_user_data["joined"] == initial_user_data["joined"]


def test_update_user_not_found():
    """Test updating not existing user."""
    new_user_data = {
        "userhash": "12345678901234567890123456789012",
        "username": "newuser",
        "fullname": "Some Body",
        "timezone": "Europe/Stockholm",
    }
    response = client.put("/11111", data=new_user_data)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user_with_no_data():
    """Update user without passing data."""
    empty_data = {}
    response = client.put("/1", data=empty_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    error_data = response.json()
    assert "May not be null." in error_data


def test_update_user_with_wrong_data():
    """Update user with passing  wrong data."""
    wrong_data = {"somekey": "somevalue"}
    response = client.put("/1", data=wrong_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    error_data = response.json()
    assert 'The \"userhash\" field is required.' in error_data["userhash"]
    assert 'The \"username\" field is required.' in error_data["username"]
    assert 'The \"fullname\" field is required.' in error_data["fullname"]
    assert 'The \"timezone\" field is required.' in error_data["timezone"]


def test_update_user_with_invalid_data():
    """Update new user with invalid data."""
    invalid_data = {
        "userhash": "123",
        "username": "x" * 51,
        "fullname": "A" * 101,
        "timezone": "Moon/City",
    }
    response = client.put("/1", data=invalid_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    error_data = response.json()
    assert "Must have at least 32 characters." in error_data["userhash"]
    assert "Must have no more than 50 characters." in error_data["username"]
    assert "Must have no more than 100 characters." in error_data["fullname"]
    assert "Must be one of" in error_data["timezone"]


def test_delete_user():
    """Test deletion of user."""
    # Get initial number of users
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    initial_user_count = len(response.json())

    response = client.delete("/1")
    assert response.status_code == HTTPStatus.NO_CONTENT
    assert response.json() == {}

    # Check persitence of deletion
    response = client.get("/1")
    assert response.status_code == HTTPStatus.NOT_FOUND
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == initial_user_count - 1


def test_delete_user_not_found():
    """Test deletion of not existing user."""
    response = client.delete("/111111")
    assert response.status_code == HTTPStatus.NOT_FOUND
