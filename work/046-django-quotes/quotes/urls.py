# -*- coding: utf-8 -*-

"""Define the urls for the quotes app."""

from django.urls import path

from quotes import views


app_name = "quotes"

urlpatterns = [
    path("", views.index, name="index"),
]
