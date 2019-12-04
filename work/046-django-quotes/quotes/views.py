# -*- coding: utf-8 -*-

"""Define the views that respond to the urls being requested."""

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


from quotes.models import Quote

# def index(request: HttpRequest) -> HttpResponse:
#     """Return the rendered index page."""
#     return HttpResponse("Welcome to my first custom view.")


def quote_list(request: HttpRequest) -> HttpResponse:
    """Render a list of quotes."""  # noqa: 201
    quotes = Quote.objects.all()
    return render(
        request,
        "quotes/quotes_list.html",
        {"quotes": quotes},
    )


def quote_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Render a single quote."""  # noqa: 201
    pass


def quote_create(request: HttpRequest) -> HttpResponse:
    """Create a new quote."""  # noqa: 201
    pass


def quote_update(request: HttpRequest, pk: int) -> HttpResponse:
    """Update a quote."""  # noqa: 201
    pass


def quote_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Delete a quote."""  # noqa: 201
    pass



