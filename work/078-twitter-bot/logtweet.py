# -*- coding: utf-8 -*-

"""Script to post tweet based on today's #100DaysOfCode log."""

from datetime import date, datetime, timedelta
import re
import sys
from typing import Optional, List

import requests
import bs4
from bs4.element import Tag


URL = "https://log100days.lpld.io/log.md"

# TODO: Remove delta
TODAY = date.today() - timedelta(days=15)

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


def get_today_heading(day_headings: List[Tag]) -> Optional[Tag]:
    """
    Return today's heading element or None.

    Arguments:
        day_headings (List[Tag]): List of heading elements for the
            different day in the log.

    Returns:
        bs4.element.Tag: Heading element representing today.
        None: If no heading element for today was found.

    """
    for day in day_headings[::]:
        if is_today(day.text):
            return day
    return None


def get_tweet_message(content_heading: Tag) -> str:
    """
    Extract the tweet content from the paragraphs after content heading.

    Arguments:
        content_heading (Tag): Heading tag element preceeding
            the content paragraphs.

    Returns:
        str: Tweet message with a maximum length of MAX_TWEET_LEN

    """
    # Loop over the next siblings until you find something
    # that is not a paragraph. Extract content from the paragraphs until
    # maximum tweet length is reached.
    current_element = content_heading
    tweet_message = ""
    while True:
        possible_content = tweet_message
        next_sibling = current_element.find_next_sibling()
        if next_sibling.name != "p":
            # Leave loop if not a paragraph.
            break
        current_element = next_sibling

        possible_content = "{existing_content}\n\n{new_content}".format(
            existing_content=possible_content,
            new_content=current_element.text,
        ).strip()
        if len(possible_content) > MAX_TWEET_LEN:
            break
        tweet_message = possible_content

    return tweet_message


if __name__ == "__main__":
    response = requests.get(URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    day_headings = soup.find_all("h2")

    # Get today's heading
    today_heading = get_today_heading(day_headings)
    if today_heading is None:
        print("No log for today found!")
        sys.exit(1)

    # Grab today's content heading
    content_heading = today_heading.find_next_sibling(
        "h3",
        string="Today's Progress",
    )
    if content_heading is None:
        print("No content found for today!")
        sys.exit(1)

    # Get content
    tweet_message = get_tweet_message(content_heading)
    print(tweet_message)




