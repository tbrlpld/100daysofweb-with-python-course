# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

from data.generate import add_iventory
from db.session import Session
from ui import main as ui_main


def main() -> None:
    """Run main program function."""
    setup_db()

    add_iventory()

    # TODO: Create user interface
    ui_main.loop()


def setup_db() -> None:
    """Set up database."""
    Session.init_db()


if __name__ == "__main__":
    main()
