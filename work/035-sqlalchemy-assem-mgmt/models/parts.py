# -*- coding: utf-8 -*.

"""Defines Part class."""

import sqlalchemy as sa
from sqlalchemy import orm

from models.base import Base


class Part(Base):
    """Simple part class."""

    __tablename__ = "parts"

    id_ = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(30), unique=True)  # noqa: WPS432

    stock_part = orm.relation(
        "StockPart",
        back_populates="part",
        uselist=False,
    )

    def __repr__(self):
        """Representation string."""
        return "<Part {0}: '{1}'>".format(self.id_, self.name)


class StockPart(Base):
    """Part that is in stock. Can have 0 stock for out-of-stock."""

    __tablename__ = "inventory"

    id_ = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)

    part_id = sa.Column(sa.ForeignKey("parts.id"), nullable=False)
    part = orm.relation(
        "Part",
        back_populates="stock_part",
        uselist=False,
    )

    count = sa.Column(sa.Integer, default=0)

    def __repr__(self):
        """Representation string."""
        return "<StockPart {0}: '{1}', {2} pcs.>".format(
            self.id_,
            self.part.name,
            self.count,
        )
