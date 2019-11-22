# -*- coding: utf-8 -*-

"""Define UI functions to mange inventory as a whole."""

from typing import List

from models.parts import StockPart
from data import services


def display() -> None:
    """Print parts in inventory."""
    inventory: List[StockPart] = services.get_inventory()
    inventory_strings: List[str] = [str(i) for i in inventory]
    output: str = "\n".join(inventory_strings)
    print(output)


def add_part() -> None:
    """Get user input for new part."""
    part_name: str = input("Name for new part:\n>>> ")
    if not part_name:
        print("Part name can not be empty!")
        return None

    part_count_str: str = input("Count of new part in inventory:\n>>> ")
    try:
        part_count: int = int(part_count_str)
    except ValueError:
        print("Count can only be integer!")
        return None

    services.create_new_stock_part(name=part_name, count=part_count)
