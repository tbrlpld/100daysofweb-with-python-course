# -*- coding: utf-8 -*-

"""Define simple user model."""

import sqlalchemy as sa

from models.base import Base


class User(Base):
    """Simple User model."""

    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)  # noqa: A103
    username = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    phone_number = sa.Column(sa.String)
