# -*- coding: utf8 -*-

"""Defines components and functions for the user interface."""

import sys

from typing import Dict, Callable


def loop():
    """Run main loop for the user interface."""
    print(" INVENTORY MANAGEMENT ".center(80, "*"))

    while True:
        prompt_function_select()


def prompt_function_select():
    """Prompt user to select interactive function. Execute function."""
    FUNCTIONS: Dict[str, Callable] = {
        "x": end_program,
    }

    user_input: str = input("Select option: e(x)it program\n>>> ")
    if user_input not in FUNCTIONS.keys():
        print("'{0}' is not a valid option.\n".format(user_input))
        return
    else:
        selected_function = FUNCTIONS[user_input]
        selected_function()


def end_program():
    """Leave the program."""
    print(" LEAVING INVENTORY MANAGEMENT ".center(80, "*"))
    sys.exit(0)
