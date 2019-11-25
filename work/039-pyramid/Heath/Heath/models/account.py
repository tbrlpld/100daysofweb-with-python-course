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

from .meta import Base


class Account(Base):
    __tablename__ = 'accounts'

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
