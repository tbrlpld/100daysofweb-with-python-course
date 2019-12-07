# -*- coding: utf-8 -*-

"""Simple responder app for an API with a landing page."""

from api import api
from data import db
from views.home import *
from views.endpoints import *


def main():
    db.global_init()
    api.run()


if __name__ == "__main__":
    main()
