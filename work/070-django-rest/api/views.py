# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        if not request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        new_quote = Quote(
            quote=request.POST["quote"],
            author=request.POST["author"],
            cover=request.POST["cover"],
            source=request.POST["source"],
            user=request.user,
        )
        try:
            new_quote.full_clean()
        except ValidationError as e:
            return Response(
                data=e,
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            new_quote.save()
            serialized_new_quote = QuoteSerializer(new_quote)
            return Response(
                data=serialized_new_quote.data,
                status=status.HTTP_201_CREATED,
            )

class QuoteRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsOwnerOrReadOnly,)


documentation_view = get_swagger_view(title="Quotes API")
