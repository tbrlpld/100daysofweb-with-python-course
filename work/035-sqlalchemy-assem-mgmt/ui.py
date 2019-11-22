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
        "m": ("(m)anage parts", manage_parts),
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


def manage_parts() -> None:
    """Manage parts."""
    print(services.get_part_ids_from_inventory())
    part_id_str: str = input("Id of part to manage: \n>>> ")

    id_issue: bool = False
    try:
        part_id: int = int(part_id_str)
    except ValueError:
        id_issue = True
    else:
        if part_id not in services.get_part_ids_from_inventory():
            id_issue = True
    if id_issue:
        print("Id '{0}' not available!".format(part_id_str))
        return None

    available_operations: Dict[str, Dict[str, str]] = {
        "+": {
            "option": "(+) add parts to stock",
            "verb": "increase",
        },
        "-": {
            "option": "(-) remove parts from stock",
            "verb": "reduce",
        },
    }

    operation_options_str: str = ", ".join([
        operation["option"] for operation in available_operations.values()
    ])
    operation: str = input(
        "Pick operation: "
        + "{0}".format(operation_options_str)
        + "\n>>> ",
    )

    if operation not in available_operations.keys():
        print("Invalid operation!")
        return None

    change_count_str: str = input("{0} count by:\n>>> ".format(
        str(available_operations[operation]["verb"]).capitalize(),
    ))
    try:
        change_count: int = int(change_count_str)
    except ValueError:
        print("Count has to be integer!")
        return None

    if operation == "+":
        services.increase_count_of_stock_part(
            part_id=part_id,
            increase=change_count,
        )
    elif operation == "-":
        services.reduce_count_of_stock_part(
            part_id=part_id,
            reduction=change_count,
        )


def end_program():
    """Leave the program."""
    print(" LEAVING INVENTORY MANAGEMENT ".center(80, "*"))
    sys.exit(0)
