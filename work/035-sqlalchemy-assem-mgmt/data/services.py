# -*- coding: utf8 -*-

"""Define services to interact with data through function calls."""

from db.session import Session
from models.parts import Part, StockPart


def create_new_stock_part(name: str, count: int):
    """Create new part in stock."""
    session = Session()
    new_part = StockPart(
        part=Part(name=name),
        count=count,
    )
    session.add(new_part)
    session.commit()
