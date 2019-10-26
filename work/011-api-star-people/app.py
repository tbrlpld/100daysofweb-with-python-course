# -*- coding: utf-8 -*-

"""Simple API to return user information."""

from apistar import App, Route


def get_users():
    pass


routes = [
    Route("/", method="get", handler=get_users),
]

app = App(routes=routes)

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5000
    app.serve(SERVER_IP, SERVER_PORT, debug=True)
