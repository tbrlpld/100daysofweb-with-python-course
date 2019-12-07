# -*- coding: utf-8 -*-

"""Run the simple two factor auth app."""

from api import api
from views import *  # noqa: F401, F403, WPS347


def main() -> None:
    """Run app server."""
    api.run()


if __name__ == "__main__":
    main()
