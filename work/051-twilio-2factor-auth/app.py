# -*- coding: utf-8 -*-

"""Run the simple two factor auth  app."""


import responder


api = responder.API()

@api.route("/")
def index(_: responder.Request, resp: responder.Response) -> None:
    """Render index page."""
    resp.text = "Welcome!"


def main() -> None:
    """Run app server."""
    api.run()


if __name__ == "__main__":
    main()
