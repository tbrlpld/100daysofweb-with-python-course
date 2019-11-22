# -*- coding: utf8 -*-

"""Defines components and functions for the user interface."""

import sys

from typing import Dict, Callable, Tuple


def loop():
    """Run main loop for the user interface."""
    print(" INVENTORY MANAGEMENT ".center(80, "*"))

    while True:
        prompt_function_select()


def prompt_function_select():
    """Prompt user to select interactive function. Execute function."""
    FUNCTIONS: Dict[str, Tuple(str, Callable)] = {
        "x": ("e(x)it program", end_program),
    }
    options_string: str = ""
    for key in FUNCTIONS:
        options_string = "{0}, ".format(FUNCTIONS[key][0])
    options_string = options_string[:-2]

    user_input: str = input("Select option: {0}\n>>> ".format(options_string))
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
