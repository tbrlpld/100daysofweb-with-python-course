# -*- coding: utf-8 -*-

"""Define the views that respond to the urls being requested."""

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    """Return the rendered index page."""
    return HttpResponse("Welcome to my first custom view.")
