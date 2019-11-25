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


class Record(Base):
    __tablename__ = 'records'

    id_ = Column("id", Integer, primary_key=True)

    type_ = Column("type", Text, index=True)
    category = Column(Text, index=True)
    description = Column(Text, nullable=True)

    amount = Column(Float, default=0.0)
    created = Column(DateTime, default=datetime.datetime.now)

    account_id = Column(ForeignKey("accounts.id"), nullable=False)
    account = orm.relation(
        "Account",
        uselist=False,
        back_populates="records",
    )
