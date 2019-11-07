# -*- coding: utf-8 -*-

"""Synchronous program as example that can be turned into a async program."""

# Standard Library Imports
from datetime import datetime
from random import random
import time


def main():
    """Run program."""
    t0 = datetime.now()
    print("Starting the app. Start time: {0}".format(t0))

    data = []
    generate_data(20, data)
    processing_data(20, data)

    dt = datetime.now() - t0
    print("Finished run. Run time: {0:.2f} s".format(dt.total_seconds()))


def generate_data(num: int, data: list):
    """Generate data in the passed in (mutable) list."""
    for index in range(1, num + 1):
        value = index * index
        data.append((value, datetime.now()))

        print("+++ Generated Data: {0}".format(value), flush=True)
        time.sleep(random() + 0.5)  # noqa: S311


def processing_data(num: int, data: list):
    """Process data in the (mutable) list."""
    processed = 0
    while processed < num:
        item = data.pop(0)
        value = item[0]
        creation_time = item[1]
        tunaround_time = datetime.now() - creation_time
        processed += 1

        print("--- Processing Data: {0} --- Turnaround time: {1}".format(
            value,
            tunaround_time,
        ))

        time.sleep(0.5)


if __name__ == "__main__":
    main()
