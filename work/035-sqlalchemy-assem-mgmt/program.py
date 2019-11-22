# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

from data.generate import add_iventory
from data.services import create_new_stock_part
from db.session import Session
from ui import loop


def main():
    """Run main program function."""
    setup_db()
    # TODO: Add some data
    add_iventory()
    # TODO: Add functionality to interact and modify data
    create_new_stock_part(name="Hole", count=10)

    # TODO: Create user interface
    loop()



def setup_db():
    """Set up database."""
    Session.init_db()


if __name__ == "__main__":
    main()
