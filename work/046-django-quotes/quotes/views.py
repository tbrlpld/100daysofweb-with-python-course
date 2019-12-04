# -*- coding: utf-8 -*-

"""Define the views that respond to the urls being requested."""

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


from quotes.models import Quote
from quotes.forms import QuoteForm

# def index(request: HttpRequest) -> HttpResponse:
#     """Return the rendered index page."""
#     return HttpResponse("Welcome to my first custom view.")


def quote_create(request: HttpRequest) -> HttpResponse:
    """Create a new quote."""  # noqa: 201
    form = QuoteForm(request.POST or None)
    print(form)

    if form.is_valid():
        print("Form is valid")
        form.save()
        messages.success(request, "Created quote.")
        return redirect("quotes:quote_list")

    return render(
        request,
        "quotes/quote_form.html",
        {"form": form},
    )


def quote_list(request: HttpRequest) -> HttpResponse:
    """Render a list of quotes."""  # noqa: 201
    quotes = Quote.objects.all()
    print(quotes)
    return render(
        request,
        "quotes/quotes_list.html",
        {"quotes": quotes},
    )


def quote_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Render a single quote."""  # noqa: 201
    pass


def quote_update(request: HttpRequest, pk: int) -> HttpResponse:
    """Update a quote."""  # noqa: 201
    pass


def quote_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Delete a quote."""  # noqa: 201
    pass



