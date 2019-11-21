# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

from db.session import Session


def main():
    """Run main program function."""
    setup_db()
    session = Session.create()


def setup_db():
    """Set up database."""
    Session.init_db()


if __name__ == "__main__":
    main()
