# -*- coding: utf-8 -*-

"""Print all course titles from the talkpython.fm website."""

import bs4
import requests


URL = "https://training.talkpython.fm/courses/all"


def main():
    raw_page = requests.get(URL)
    raw_page.raise_for_status()

    soup = bs4.BeautifulSoup(raw_page.text, "html.parser")

    course_titles_html = soup.select("h3")
    course_titles = [title.get_text() for title in course_titles_html]
    for title in course_titles:
        print(title)


if __name__ == "__main__":
    main()
