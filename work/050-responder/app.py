# -*- coding: utf-8 -*-

"""Simple responder app for an API with a landing page."""

import responder

api = responder.API()


def main():
    api.run()


@api.route("/")
def index(_, response: responder.Response) -> None:
    response.html = api.template("/index.html", recreator="Tibor")


if __name__ == "__main__":
    main()
