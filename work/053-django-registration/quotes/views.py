# -*- coding: utf-8 -*-

"""Define the views that respond to the urls being requested."""

from django.contrib import messages
from django.core import mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest


from quotes.models import Quote
from quotes.forms import QuoteForm


def quote_create(request: HttpRequest) -> HttpResponse:
    """Create a new quote."""  # noqa: 201
    form = QuoteForm(request.POST or None)

    if form.is_valid():
        # Create form instance, like it was saved, but without committing it
        # to the database.
        form = form.save(commit=False)
        form.user = request.user
        form.save()

        messages.success(request, "Created quote.")
        return redirect("quotes:quotes_list")

    return render(
        request,
        "quotes/quote_form.html",
        {"form": form},
    )


def quotes_list(request: HttpRequest) -> HttpResponse:
    """Render a list of quotes."""  # noqa: 201
    quotes = Quote.objects.all()
    return render(
        request,
        "quotes/quotes_list.html",
        {"quotes": quotes},
    )


def quote_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Render a single quote."""  # noqa: 201
    quote = get_object_or_404(Quote, pk=pk)
    return render(
        request,
        "quotes/quote_detail.html",
        {"quote": quote},
    )


def quote_update(request: HttpRequest, pk: int) -> HttpResponse:
    """Update a quote."""  # noqa: 201
    quote = get_object_or_404(Quote, pk=pk)
    form = QuoteForm(request.POST or None, instance=quote)

    if form.is_valid():
        form.save()
        messages.success(request, "Quote updated.")
        return redirect("quotes:quotes_list")

    return render(
        request,
        "quotes/quote_form.html",
        {
            "quote": quote,
            "form": form,
        },
    )


def quote_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Delete a quote."""  # noqa: 201
    quote = get_object_or_404(Quote, pk=pk)
    print(request.POST)
    if request.POST:
        quote.delete()
        messages.success(request, "Quote delete.")
        return redirect("quotes:quotes_list")

    return render(
        request,
        "quotes/quote_delete.html",
        {
            "quote": quote,
        },
    )
