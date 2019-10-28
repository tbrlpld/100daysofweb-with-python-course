# -*- coding: utf-8 -*-

"""Simple API to return user information."""

import datetime
import json
from http import HTTPStatus

from apistar import App, Route, types, validators
from apistar.http import JSONResponse


# -----------------------------------------------------------------------------
# Getting the mock data. The global is only used to fake a DB connection.
def _get_data(data_file="users.json") -> dict:
    with open(data_file, mode="r") as data_file_obj:
        user_list = json.load(data_file_obj)
        return {user["userid"]: user for user in user_list}


users = _get_data()
VALID_TIMEZONES = list({user["timezone"] for user in users.values()})


# -----------------------------------------------------------------------------
ERROR_USER_NOT_FOUND = {"error": "User not found."}

# -----------------------------------------------------------------------------
class User(types.Type):
    """Simple User class."""

    userid = validators.Integer(minimum=1, allow_null=True)
    userhash = validators.String(min_length=32, max_length=32)
    username = validators.String(max_length=50)
    fullname = validators.String(max_length=100)
    joined = validators.Date(allow_null=True)
    timezone = validators.String(enum=VALID_TIMEZONES)


# -----------------------------------------------------------------------------
def get_users() -> JSONResponse:
    """Return list of all users."""
    list_of_user_objs = [User(user) for user in users.values()]
    return JSONResponse(list_of_user_objs, HTTPStatus.OK)


def get_user(userid: int) -> JSONResponse:
    """Return user by id."""
    user = users.get(userid)
    if not user:
        return JSONResponse(ERROR_USER_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return JSONResponse(User(user), HTTPStatus.OK)


def create_user(new_user: User) -> JSONResponse:
    """Create new user in persistent storage."""
    new_userid = len(users) + 1
    new_user.userid = new_userid
    new_user.joined = datetime.date.today()
    users[new_userid] = new_user
    return JSONResponse(users[new_userid], HTTPStatus.CREATED)


# -----------------------------------------------------------------------------
routes = [
    Route("/", method="get", handler=get_users),
    Route("/{userid}", method="get", handler=get_user),
    Route("/", method="post", handler=create_user),
]

app = App(routes=routes)
if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5000
    app.serve(SERVER_IP, SERVER_PORT, debug=True)
