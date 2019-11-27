# -*- coding: utf-8 -*-

"""Define Account model and utility functions."""

from typing import List
import datetime

from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    DateTime,
    ForeignKey,
    orm,
)
from sqlalchemy.orm import Session

from Heath.models.meta import Base
from Heath.models.user import User


class Account(Base):
    """Define Account model."""

    __tablename__ = "accounts"

    id_ = Column("id", Integer, primary_key=True)
    name = Column(Text, index=True)
    balance_actual = Column(Float, default=0.0)
    created = Column(DateTime, default=datetime.datetime.now)

    user_id = Column(ForeignKey("users.id"), nullable=False)
    user = orm.relation(
        "User",
        back_populates="accounts",
        uselist=False,
    )

    records = orm.relation(
        "Record",
        uselist=True,
        back_populates="account",
    )


def get_accounts_by_user(session: Session, user: User) -> List[Account]:
    """Return accounts for a given user."""
    return session.query(Account).filter(Account.user == user).all()
