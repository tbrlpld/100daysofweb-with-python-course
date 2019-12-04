# -*- coding: utf-8 -*-

"""Define the urls for the quotes app."""

from django.urls import path

from quotes import views


app_name = "quotes"

urlpatterns = [
    path("", views.quote_list, name="quote_list"),
    path("<int:pk>", views.quote_detail, name="quote_detail"),
    path("create", views.quote_create, name="quote_create"),
    path("update/<int:pk>", views.quote_update, name="quote_update"),
    path("delete/<int:pk>", views.quote_delete, name="quote_delete"),
]
