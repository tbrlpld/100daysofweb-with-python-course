# -*- coding: utf-8 -*-

"""Defines components and functions for the user interface."""

import sys
from typing import Dict, Callable, Tuple, List

from data import services
from models.parts import StockPart


def loop():
    """Run main loop for the user interface."""
    print(" INVENTORY MANAGEMENT ".center(80, "*"))

    while True:
        prompt_function_select()


def prompt_function_select() -> None:
    """Prompt user to select interactive function. Execute function."""
    FUNCTIONS: Dict[str, Tuple[str, Callable]] = {
        "a": ("(a)dd part", add_part),
        "l": ("(l)ist inventory", list_inventory),
        "x": ("e(x)it program", end_program),
    }

    options: List[str] = [opt[0] for opt in FUNCTIONS.values()]
    options_string: str = ", ".join(options)

    user_input: str = input(
        "\nSelect option: {0}\n>>> ".format(options_string),
    )
    if user_input not in FUNCTIONS.keys():
        print("'{0}' is not a valid option.\n".format(user_input))
        return
    else:
        selected_function: Callable = FUNCTIONS[user_input][1]
        selected_function()


def list_inventory() -> None:
    """Print parts in inventory."""
    inventory: List[StockPart] = services.get_inventory()
    inventory_strings: List[str] = [str(i) for i in inventory]
    output: str = "\n".join(inventory_strings)
    print(output)


def add_part() -> None:
    """Get user input for new part."""
    part_name: str = input("Name for new part:\n>>> ")
    part_count_str: str = input("Count of new part in inventory:\n>>> ")

    try:
        part_count: int = int(part_count_str)
    except ValueError:
        print("Count can only be integer!")
        return

    services.create_new_stock_part(name=part_name, count=part_count)


def end_program():
    """Leave the program."""
    print(" LEAVING INVENTORY MANAGEMENT ".center(80, "*"))
    sys.exit(0)
