# -*- coding: utf-8 -*-

from rest_framework import generics

from api.serializers import QuoteSerializer
from quotes.models import Quote


class QuotesListView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
