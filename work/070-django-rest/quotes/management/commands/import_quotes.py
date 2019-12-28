# -*- coding: utf-8 -*-

"""Command for manage.py to populate the database with quotes from a CSV. """

import csv
import sys

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import requests

from quotes.models import Quote

QUOTE_RESOURCE = (
    "https://raw.githubusercontent.com/bbelderbos/"
    + "inspirational-quotes/master/Quotes.csv"
)
DEFAULT_QUOTE_CREATOR = "tibor"
MAX_QUOTES = 20


class Command(BaseCommand):
    help = "Script to populate database with example quotes."

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            dest="username",
            default=DEFAULT_QUOTE_CREATOR,
            help="Username to associate the quotes with.",
        )
        parser.add_argument(
            "--limit",
            dest="limit",
            default=MAX_QUOTES,
            help=(
                "Limit the maximum number of quotes created."
                + f" (default: {MAX_QUOTES})"
            ),
        )

    def handle(self, *args, **options):
        if Quote.objects.count() > 0:
            sys.exit("Database is not empty. Aborting population.")

        username = options["username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            error = (
                f"User {username} does not exist in the DB. Create the user"
                "via `manage.py createsuperuser` or register on the page."
            )

        try:
            max_quotes = int(options["limit"])
        except ValueError:
            sys.exit("Limit has to be numeric!")

        response = requests.get(QUOTE_RESOURCE)
        lines = response.text.strip().splitlines()

        headers = "quote author genre".split()  # What a strange way to create a list.
        reader = csv.DictReader(lines, fieldnames=headers, delimiter=";")

        quotes = []
        first_content_row = 1
        last_content_row = first_content_row + max_quotes
        for row in list(reader)[first_content_row:last_content_row]:
            quote = Quote(
                quote=row["quote"],
                author=row["author"],
                user=user,
            )
            quotes.append(quote)

        Quote.objects.bulk_create(quotes)

        created_quotes_count = len(quotes)
        print(f"Done. {created_quotes_count} quotes created.")
