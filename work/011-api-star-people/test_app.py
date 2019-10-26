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
