# -*- coding: utf-8 -*-

"""Defines the django ORM models of the quotes app."""

from django.db import models


class Quote(models.Model):
    """Quote model."""

    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.URLField()
    cover = models.URLField()
    # Only set once when creating
    added = models.DateTimeField(auto_now_add=True)
    # Updated on every save.
    edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Return a string to represent the model with its type.

        Returns:
            str: String that represents the model.

        """
        return "{quote} - {author}".format(
            quote=self.quote,
            author=self.author,
        )

    class Meta(object):
        """Add additional settings."""

        # Order quotes by descending "added" date.
        ordering = ["-added"]
