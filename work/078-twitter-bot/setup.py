# -*- coding: utf-8 -*-

"""Setup script."""

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

requires = [
    "bs4",
    "requests",
    "tweepy",
]

setup(
    name="LogTweet",
    version="0.1.0",
    author="Tibor Leupold",
    author_email="tibor@lpld.io",
    description="Create a tweet based on the log message for today from https://log100days.lpld.io/log.md",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tbrlpld/100daysofweb-with-python-course/tree/master/work/078-twitter-bot",
    python_requires=">=3.6",
    install_requires=requires,
    packages=["logtweet"],
    entry_points={
        "console_scripts": [
            "logtweet = logtweet:main",
        ],
    },
    include_package_data=True,  # To copy the files listen in MANIFEST.in
)
