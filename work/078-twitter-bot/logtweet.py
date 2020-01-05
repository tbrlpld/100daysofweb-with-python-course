# -*- coding: utf-8 -*-

"""Script to post tweet based on today's #100DaysOfCode log."""

from datetime import date, datetime, timedelta
import re

import requests
import bs4


URL = "https://log100days.lpld.io/log.md"

# TODO: Remove delta
TODAY = date.today() - timedelta(days=10)

DATE_FORMAT = "%B %d, %Y"


def is_today(day_heading_text: str) -> bool:
    """
    Check if given day heading represents today.

    Arguments:
        day_heading_text (str): Text content of the day's heading.

    Returns:
        bool: Expresses if the given day heading text represents today.

    """
    # Extract the date string
    date_string = re.sub(
        r"(.*: )(.*)(, .*day.*)",  # pattern to create groups
        r"\2",  # Return only second group
        day_heading_text,
    )
    # Convert to date object
    date_obj = datetime.strptime(date_string, DATE_FORMAT).date()
    # Check if today
    return date_obj == TODAY


if __name__ == "__main__":
    response = requests.get(URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    day_headings = soup.find_all("h2")

    for day in day_headings:
        if is_today(day.text):
            print(day)


