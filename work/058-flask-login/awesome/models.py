# -*- coding: utf-8 -*-

"""Define ORM models for the app."""

from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from sqlalchemy.ext.hybrid import hybrid_property

from awesome import db


class User(UserMixin, db.Model):
    """User model to enable authorization."""

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String,
        unique=True,
        nullable=False,
    )
    _password_hash = db.Column(
        "password_hash",
        db.String,
        unique=False,
        nullable=False,
    )

    @hybrid_property
    def password_hash(self) -> str:
        """Return the saved password hash."""
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password: str) -> None:
        """Set `password_hash property` to a hash of the given password."""
        self._password_hash = pbkdf2_sha256(password)

    def verify_password(self, password: str) -> bool:
        """Check if the given password matches the stored (and hashed) one."""
        return pbkdf2_sha256.verify(password, self._password_hash)

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
