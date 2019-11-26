# -*- coding: utf-8 -*-

"""Defines User model and typical query helper."""

import datetime
from typing import Optional

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Text,
    orm,
)
from sqlalchemy.orm import Session

from .meta import Base


class User(Base):
    __tablename__ = 'users'

    id_ = Column("id", Integer, primary_key=True)
    name = Column(Text, index=True)
    email = Column(Text, index=True, unique=True)
    password = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)

    accounts = orm.relation(
        "Account",
        back_populates="user",
        uselist=True,
    )


def get_by_id(session: Session, user_id: int) -> Optional[User]:
    """Return User object for given ID from DB."""
    return session.query(User).filter(User.id_ == user_id).first()
