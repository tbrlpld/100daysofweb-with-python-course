# -*- conding: utf-8 -*-

"""App entry point."""

import os

from pyramid.config import Configurator

from billtracker.bin.load_base_data import load_starter_data
from billtracker.data.db_session import DbSession


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")
        config.include(".routes")
        config.include(".security")
        config.scan()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_dir, "db/billtracker.sqlite3")
    DbSession.global_init(db_file)
    load_starter_data()
    return config.make_wsgi_app()
