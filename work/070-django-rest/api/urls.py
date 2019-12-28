# -*- coding: utf-8 -*-

"""URLs for the Quotes API."""


from django.urls import path, include

from api.views import (
    QuotesListView,
    QuoteRUDView,
    documentation_view,
)


urlpatterns = [
    path("", QuotesListView.as_view()),
    path("<int:pk>", QuoteRUDView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("docs/", documentation_view),
]
