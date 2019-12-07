# -*- coding: utf-8 -*-

"""Run the simple two factor auth  app."""


import responder


api = responder.API()


@api.route("/")
def index(_: responder.Request, resp: responder.Response) -> None:
    """Render index page."""
    # noqa: DAR101, E800
    resp.html = api.template("index.html.j2")


def main() -> None:
    """Run app server."""
    api.run()


if __name__ == "__main__":
    main()
