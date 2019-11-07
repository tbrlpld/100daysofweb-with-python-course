# -*- coding: utf-8 -*-

"""Synchronous program as example that can be turned into a async program."""

import time
from datetime import datetime
from random import random


def main():
    """Run program."""
    t0 = datetime.now()
    print("Starting the app. Start time: {0}".format(t0))

    data = []
    generate_data(10, data)

    dt = datetime.now() - t0
    print("Finished run. Run time: {0}".format(dt))


def generate_data(num: int, data: list):
    """Generate data in the passed in (mutable) list."""
    for index in range(1, num + 1):
        value = index * index
        data.append((value, datetime.now()))

        print("+++ Generated Data: {0}".format(value), flush=True)
        time.sleep(random() + 0.5)  # noqa: S311


if __name__ == "__main__":
    main()
