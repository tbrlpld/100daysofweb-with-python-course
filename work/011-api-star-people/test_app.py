# -*- coding: utf-8 -*-

"""Tests for user API."""

from http import HTTPStatus
#
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
    assert first_user["id"] == 1
    assert first_user["username"] == "hyurikov0"
    last_user = users[-1]
    assert last_user["id"] == 1000
    assert last_user["username"] == "bokeevanrr"
