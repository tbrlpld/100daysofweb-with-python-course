# -*- coding: utf-8 -*-

"""Defines UI functions to manage parts in stock."""

from typing import Dict, Union, Tuple

from data import services


def main() -> None:
    """Manage parts."""
    part_id: Union[None, int] = prompt_for_part_id()
    if part_id is None:
        return None

    operation: Union[None, Tuple[str, str]] = promt_for_operation()
    if operation is None:
        return None
    operation_sign, operation_verb = operation

    change_count: Union[None, int] = prompt_for_change_count(
        verb=operation_verb,
    )
    if change_count is None:
        return None

    if operation_sign == "+":
        services.increase_count_of_stock_part(
            part_id=part_id,
            increase=change_count,
        )
    elif operation_sign == "-":
        services.reduce_count_of_stock_part(
            part_id=part_id,
            reduction=change_count,
        )


def prompt_for_part_id() -> Union[None, int]:
    """Prompt user for part id."""
    part_id_str: str = input("Id of part to manage: \n>>> ")

    id_issue: bool = False
    try:
        part_id: int = int(part_id_str)
    except ValueError:
        id_issue = True
    else:  # noqa: WPS513
        if part_id not in services.get_part_ids_from_inventory():
            id_issue = True
    if id_issue:
        print("Id '{0}' not available!".format(part_id_str))
        return None
    return part_id


def promt_for_operation() -> Union[None, Tuple[str, str]]:
    """Prompt user to select operation."""
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

    return (operation, available_operations[operation]["verb"])


def prompt_for_change_count(verb: str) -> Union[None, int]:
    """Prompt user for change count."""
    change_count_str: str = input("{0} count by:\n>>> ".format(
        str(verb).capitalize(),
    ))
    try:
        change_count: int = int(change_count_str)
    except ValueError:
        print("Count has to be integer!")
        return None

    return change_count
