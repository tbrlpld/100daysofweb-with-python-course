# -*- coding: utf-8 -*-

"""Synchronous program as example that can be turned into a async program."""

# Standard Library Imports
import asyncio
from datetime import datetime
from random import random


def main():
    """Run program."""
    t0 = datetime.now()
    print("Starting the app. Start time: {0}".format(t0))

    data = asyncio.Queue()

    loop = asyncio.get_event_loop()
    task_generate = loop.create_task(generate_data(20, data))
    # task_generate_2 = loop.create_task(generate_data(20, data))
    task_processing = loop.create_task(processing_data(20, data))
    gathered_tasks = asyncio.gather(
        task_generate,
        # task_generate_2,
        task_processing,
    )
    loop.run_until_complete(gathered_tasks)

    dt = datetime.now() - t0
    print("Finished run. Run time: {0:.2f} s".format(dt.total_seconds()))


async def generate_data(num: int, data: list):
    """Generate data in the passed in (mutable) list."""
    for index in range(1, num + 1):
        value = index * index
        await data.put((value, datetime.now()))

        print("+++ Generated Data: {0}".format(value), flush=True)
        await asyncio.sleep(random() + 0.5)


async def processing_data(num: int, data: list):
    """Process data in the (mutable) list."""
    processed = 0
    while processed < num:
        item = await data.get()
        value = item[0]
        creation_time = item[1]
        tunaround_time = datetime.now() - creation_time
        processed += 1

        print("--- Processing Data: {0} --- Turnaround time: {1}".format(
            value,
            tunaround_time,
        ))

        await asyncio.sleep(0.5)


if __name__ == "__main__":
    main()
