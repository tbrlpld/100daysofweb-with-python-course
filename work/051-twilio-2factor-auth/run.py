# -*- coding: utf-8 -*-

"""Run the simple two factor auth app."""

import sys

from t2fa.api import api
from t2fa.db import dbengine
from t2fa.models.base import Base
from t2fa.models.user import User
from t2fa.views import *  # noqa: F401, F403, WPS347


def main() -> None:
    """Run app server."""
    # Create DB tables
    Base.metadata.create_all(dbengine)
    api.run()


if __name__ == "__main__":
    main()
