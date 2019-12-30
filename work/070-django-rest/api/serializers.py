# -*- conding: utf-8 -*-

"""Serializer to turn Quote model into JSON."""

from rest_framework import serializers

from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Quote
        fields = (
            "quote",
            "author",
            "source",
            "cover",
            "user",
        )
