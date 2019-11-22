# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

from data.generate import add_iventory
from db.session import Session


def main():
    """Run main program function."""
    setup_db()
    # TODO: Add some data
    add_iventory()
    # TODO: Add functionality to interact and modify data


def setup_db():
    """Set up database."""
    Session.init_db()


if __name__ == "__main__":
    main()
