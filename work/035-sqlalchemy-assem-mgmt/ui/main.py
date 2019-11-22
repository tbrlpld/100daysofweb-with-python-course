# -*- coding: utf-8 -*-

"""Defines components and functions for the user interface."""

import sys
from typing import Dict, Callable, Tuple, List

from ui import manage_parts, inventory


def loop():
    """Run main loop for the user interface."""
    print(" INVENTORY MANAGEMENT ".center(80, "*"))

    while True:
        prompt_function_select()


def prompt_function_select() -> None:
    """Prompt user to select interactive function. Execute function."""
    FUNCTIONS: Dict[str, Tuple[str, Callable]] = {
        "a": ("(a)dd part", inventory.add_part),
        "l": ("(l)ist inventory", inventory.display),
        "m": ("(m)anage parts", manage_parts.main),
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


def end_program():
    """Leave the program."""
    print(" LEAVING INVENTORY MANAGEMENT ".center(80, "*"))
    sys.exit(0)
