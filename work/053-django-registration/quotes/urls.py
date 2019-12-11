# -*- coding: utf-8 -*-

"""Define the urls for the quotes app."""

from django.urls import path

from quotes import views


app_name = "quotes"

# Function based
urlpatterns = [
    path("", views.quotes_list, name="quotes_list"),
    path("<int:pk>", views.quote_detail, name="quote_detail"),
    path("create", views.quote_create, name="quote_create"),
    path("update/<int:pk>", views.quote_update, name="quote_update"),
    path("delete/<int:pk>", views.quote_delete, name="quote_delete"),
]

# # Class based
# urlpatterns = [
#     path("", views_cb.QuotesList.as_view(), name="quotes_list"),
#     path("<int:pk>", views_cb.QuoteDetail.as_view(), name="quote_detail"),
#     path("create", views_cb.QuoteCreate.as_view(), name="quote_create"),
#     path("update/<int:pk>", views_cb.QuoteUpdate.as_view(), name="quote_update"),
#     path("delete/<int:pk>", views_cb.QuoteDelete.as_view(), name="quote_delete"),
# ]
