# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework_swagger.views import get_swagger_view

from api.serializers import QuoteSerializer
from api.permissions import IsOwnerOrReadOnly
from quotes.models import Quote


class QuotesListView(generics.ListCreateAPIView):
    """
    get:
        Retrieve a list of all available quotes.

    post:
        Create new quotes.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsOwnerOrReadOnly,)


documentation_view = get_swagger_view(title="Quotes API")
