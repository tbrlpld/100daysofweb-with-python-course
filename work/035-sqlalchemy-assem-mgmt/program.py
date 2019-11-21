# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

from db.session import Session
import generate_data


def main():
    """Run main program function."""
    setup_db()
    # TODO: Add some data
    generate_data.add_parts()
    # TODO: Add functionality to modify data


def setup_db():
    """Set up database."""
    Session.init_db()


if __name__ == "__main__":
    main()
