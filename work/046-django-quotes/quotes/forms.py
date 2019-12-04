# -*- coding: utf-8 -*-

"""Define the forms for the Quotes app."""

from django.forms import ModelForm


from quotes.models import Quote


class QuoteForm(ModelForm):
    """Define form for the quote model."""

    class Meta(object):
        """Define Meta attributes."""

        model = Quote
        fields = ["quote", "author", "source", "cover"]
