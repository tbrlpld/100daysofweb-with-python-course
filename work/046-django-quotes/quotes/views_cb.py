# -*- coding: utf-8 -*-

"""Define the views that respond to the urls being requested."""

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from quotes.models import Quote
from quotes.forms import QuoteForm


class QuoteCreate(CreateView):
    """Create view for a Quote."""

    model = Quote
    form_class = QuoteForm
    success_url = reverse_lazy("quotes:quotes_list")


class QuotesList(ListView):
    """List all quotes."""

    model = Quote
    template_name = "quotes/quotes_list.html"
    context_object_name = "quotes"


class QuoteDetail(DetailView):
    """Show one quote in detail."""

    model = Quote


class QuoteUpdate(UpdateView):
    """Show update form for a quote."""

    model = Quote
    form_class = QuoteForm
    success_url = reverse_lazy("quotes:quotes_list")


class QuoteDelete(DeleteView):
    """Delete a quote after getting confirmation."""

    model = Quote
    success_url = reverse_lazy("quotes:quotes_list")
    template_name = "quotes/quote_delete.html"
