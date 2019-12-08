# -*- coding: utf-8 -*-

"""Run the simple two factor auth app."""

from api import api
from db import dbengine
from models.base import Base
from models.user import User
from views import *  # noqa: F401, F403, WPS347


def main() -> None:
    """Run app server."""
    # Create DB tables
    Base.metadata.create_all(dbengine)
    api.run()


if __name__ == "__main__":
    main()
