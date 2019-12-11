# -*- coding: utf-8 -*-

"""Defines the django ORM models of the quotes app."""

from django.contrib.auth.models import User
from django.db import models


class Quote(models.Model):
    """Quote model."""

    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.URLField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)  # Set once when creating.
    edited = models.DateTimeField(auto_now=True)  # Updated on every save.

    user = models.ForeignKey(
        User,
        # Delete the users quotes when the user is deleted.
        on_delete=models.CASCADE,
        # blank and null should be true, because there are already quotes in
        # the DB that do not have a user associated with them.
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        """
        Return a string to represent the model with its type.

        Returns:
            str: String that represents the model.

        """
        return "{quote} - {author} added by {user}".format(
            quote=self.quote,
            author=self.author,
            user=self.user,
        )

    class Meta(object):
        """Add additional settings."""

        # Order quotes by descending "added" date.
        ordering = ["-added"]
