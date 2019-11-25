import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    orm,
)

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
