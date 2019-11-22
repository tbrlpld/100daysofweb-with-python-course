# -*- coding: utf8 -*-

"""Define services to interact with data through function calls."""

from typing import List

from db.session import Session
from models.parts import Part, StockPart


def get_inventory() -> List[StockPart]:
    """Return list of all parts in the inventory."""
    session: Session = Session()
    return session.query(StockPart).all()


def create_new_stock_part(name: str, count: int) -> None:
    """Create new part in stock."""
    session: Session = Session()
    new_part: StockPart = StockPart(
        part=Part(name=name),
        count=count,
    )
    session.add(new_part)
    session.commit()
