# -*- coding: utf-8 -*-

"""URLs for the Quotes API."""


from django.urls import path

from api.views import QuotesListView


urlpatterns = [
    path("", QuotesListView.as_view()),
]
