# -*- coding: utf-8 -*-

"""Script to post tweet based on today's #100DaysOfCode log."""

from configparser import ConfigParser
from datetime import date, datetime, timedelta
import re
import sys

from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import tweepy


config = ConfigParser()
config.read("config.ini")
URL = "https://log100days.lpld.io/log.md"
TODAY = date.today() - timedelta(days=10)  # TODO: Remove delta
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


def get_today_heading(soup: BeautifulSoup) -> Tag:
    """
    Return today's heading element or None.

    Arguments:
        soup (BeautifulSoup): Soup object of log page parsed with
            BeautifulSoup.

    Returns:
        bs4.element.Tag: Heading element representing today.
        None: If no heading element for today was found.

    Raises:
        LookupError: Raised if no heading element for today was found.

    """
    day_headings = soup.find_all("h2")
    for day in day_headings[::]:
        if is_today(day.text):
            return day
    raise LookupError("No heading for found for today!")


def build_preamble(today_heading: Tag) -> str:
    """
    Build preamble for tweet.

    The preamble for e.g. day 77 would look like: "77/#100DaysOfCode".

    Arguments:
        today_heading (Tag): Today's log header from which the day can be
            extracted.

    Returns:
        str: Preamble for the tweet message.

    """
    day = re.sub(r"(.*)(.[0-9])(:.*)", r"\2", today_heading.text)
    # TODO: Use correct hashtag
    return f"{day}/#100DaysOfLode"


def get_first_link(today_heading: Tag) -> str:
    """
    Extract the first link  URL from the list of the day's links.

    Arguments:
        today_heading (Tag): Today's log header from which the day can be
            extracted.

    Returns:
        str: First link found in the list of links or empty if no links found.

    """
    # Go over the next siblings until the next day heading is found

    link_heading = None
    current_element = today_heading
    while True:
        next_sibling = current_element.next_sibling
        if next_sibling.name == "h2":
            break
        if next_sibling.name == "h3" and next_sibling.text == "Links(s)":
            link_heading = next_sibling
            break
        current_element = next_sibling

    if not link_heading:
        return ""
    return link_heading.find_next_sibling("ol").li.a["href"]


def get_short_link(long_link: str, bitly_api_key: str) -> str:
    """
    Create short link using the Bit.ly service.

    Arguments:
        long_link (str): Long link to shorten.
        bitly_api_key (str): API key for the Bit.ly service.
            See the `Bitly API documentation`_ on how to retrieve an API key.

    Returns:
        str: Shortened link pointing to the same resource as the long link.

    .. _Bitly API documentation:
        https://dev.bitly.com/v4/#section/Application-using-a-single-account

    """
    shortener_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {"Authorization": f"Bearer {bitly_api_key}"}
    payload = {"long_url": long_link}
    response = requests.post(shortener_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["link"]


def get_tweet_message(today_heading: Tag, max_len: int) -> str:
    """
    Extract the tweet content from the paragraphs after content heading.

    Arguments:
        today_heading (Tag): Heading tag element for today.
        max_len (int): Maximum length of tweet message.

    Returns:
        str: Tweet message with a maximum length of MAX_TWEET_LEN

    Raises:
        LookupError: This error is raised if no content heading is found or the
            message is empty.

    """
    # Grab today's content heading
    content_heading = today_heading.find_next_sibling(
        "h3",
        string="Today's Progress",
    )
    if content_heading is None:
        raise LookupError("No content heading found for today!")

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

        if len(possible_content) > max_len:
            break
        tweet_message = possible_content

    if not tweet_message:
        raise LookupError("No message found that could be tweeted!")
    return tweet_message


def twitter_authenticate(config: ConfigParser) -> tweepy.API:
    """
    Create authenticated Tweepy API.

    Arguments:
        config (ConfigParser): Config object containing the authentication
            detail for a twitter app. Requires a "Twitter" section and
            key-value-pairs for "api_key", "api_secret", "access_token" and
            "access_secret".

    Returns:
        tweepy.API: Authenticated tweepy API object.

    """
    auth = tweepy.OAuthHandler(
        config["Twitter"]["api_key"],
        config["Twitter"]["api_secret"],
    )
    auth.set_access_token(
        config["Twitter"]["access_token"],
        config["Twitter"]["access_secret"],
    )
    return tweepy.API(auth)


def send_tweet(tweet_content: str) -> None:
    """
    Send tweet with given content.

    For this to work, the config needs to contain valid Twitter API key and
    access token.

    Arguments:
        tweet_content (str): Content of the tweet.

    """
    # TODO: Log tweet and check log before sending tweet to prevent duplication.
    # TODO: Reactivate sending of tweet
    tweepy_api = twitter_authenticate(config)
    print(tweet_content)
    # tweepy_api.update_status(tweet_content)


if __name__ == "__main__":
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Get today's heading
    today_heading = get_today_heading(soup)

    # Generate tweet preamble (E.g. 77/#100DaysOfCode)
    preamble = build_preamble(today_heading)

    # Extract first link from list of links for the day.
    link = get_first_link(today_heading)
    # Create shortened link to first link of the day.
    if link:
        link = get_short_link(link, config["Bitly"]["api_key"])

    # Get content
    # TODO: Calculate max message length. This needs to be the maximum tweet
    # length, reduced by the preamble and the link.
    tweet_content_template = "{preamble} {tweet_message}\n\n{link}"
    tweet_length_wo_message = len(tweet_content_template.format(
        preamble=preamble,
        tweet_message="",
        link=link,
    ))
    max_length = MAX_TWEET_LEN - tweet_length_wo_message
    tweet_message = get_tweet_message(today_heading, max_len=max_length)

    # TODO: Build content from preamble, message and link
    tweet_content = tweet_content_template.format(
        preamble=preamble,
        tweet_message=tweet_message,
        link=link,
    )

    send_tweet(tweet_content)
