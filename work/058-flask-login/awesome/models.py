# -*- coding: utf-8 -*-

"""Define ORM models for the app."""

from awesome import db


class User(db.Model):
    """User model to enable authorization."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self) -> str:
        """
        Return User representation.

        Returns:
            str: User representation string.

        """
        return "<User {id}: {username} at {location}>".format(
            id=self.id,
            username=self.username,
            location=hex(id(self)),
        )
