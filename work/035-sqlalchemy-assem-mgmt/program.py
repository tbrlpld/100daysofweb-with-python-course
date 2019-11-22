# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

from data.generate import add_iventory
from data.services import create_new_stock_part, get_inventory
from db.session import Session
import ui


def main() -> None:
    """Run main program function."""
    setup_db()
    # TODO: Add some data
    add_iventory()
    # TODO: Add functionality to interact and modify data
    create_new_stock_part(name="Hole", count=10)
    # TODO: Create user interface
    ui.loop()


def setup_db() -> None:
    """Set up database."""
    Session.init_db()


if __name__ == "__main__":
    main()
