# -*- coding: utf-8 -*-

"""Script to post tweet based on today's #100DaysOfCode log."""

from datetime import date, datetime, timedelta
import re
import sys

import requests
import bs4


URL = "https://log100days.lpld.io/log.md"

# TODO: Remove delta
TODAY = date.today() - timedelta(days=10)

DATE_FORMAT = "%B %d, %Y"

MAX_TWEET_LEN = 240


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

    # Get today's heading
    today_heading = None
    for day in day_headings:
        if is_today(day.text):
            today_heading = day
    if today_heading is None:
        print("No log for today found!")
        sys.exit(1)

    # Grab today's subheadings
    content_heading = None
    today_subheadings = day.find_next_siblings("h3")
    for subhead in today_subheadings:
        if subhead.text == "Today's Progress":
            content_heading = subhead
    if content_heading is None:
        print("No content found for today!")
        sys.exit(1)

    # Loop over the next siblings until you find something
    # that is not a paragraph.
    current_element = content_heading
    while True:
        print(current_element)
        # possible_content = content
        next_sibling = current_element.find_next_sibling()
        if next_sibling.name != "p":
            # Leave loop if not a paragraph.
            break
        current_element = next_sibling
        # possible_content += current_element.text

        # if len(possible_content) > MAX_TWEET_LEN:
        #     break
        # content = possible_content

    # print(content)




