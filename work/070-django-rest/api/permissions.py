# -*- coding: utf-8 -*-

"""Define custom permission schema for Quotes API."""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow only a quotes owner to edit/delete it."""

    def has_object_permission(self, request, view, obj):
        """Check if user has permission to edit the object."""
        if request.method in permissions.SAFE_METHODS:
            # For safe methods like GET (which do not change the data)
            # always allow access.
            return True
        # Check if request user is user of the requested object.
        # The object is probably passed in from the class based view.
        return request.user == obj.user
