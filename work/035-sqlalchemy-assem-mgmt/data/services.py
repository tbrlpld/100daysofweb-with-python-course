# -*- coding: utf-8 -*-

"""Define services to interact with data through function calls."""

from typing import List, Tuple

from db.session import Session
from models.parts import Part, StockPart


def get_inventory() -> List[StockPart]:
    """Return list of all parts in the inventory."""
    session: Session = Session()
    return session.query(StockPart).all()


def get_part_ids_from_inventory() -> List[int]:
    """Return list of part ids."""
    session: Session = Session()
    rows = session.query(StockPart.id_).all()
    return [row.id_ for row in rows]


def create_new_stock_part(name: str, count: int) -> None:
    """Create new part in stock."""
    session: Session = Session()
    new_part: StockPart = StockPart(
        part=Part(name=name),
        count=count,
    )
    session.add(new_part)
    session.commit()


def increase_count_of_stock_part(part_id: int, increase: int) -> None:
    """Increase count of a part in stock."""
    session: Session = Session()
    part = session.query(StockPart).filter(StockPart.id_ == part_id).one()
    part.count += increase
    session.commit()


def reduce_count_of_stock_part(part_id: int, reduction: int) -> None:
    """Increase count of a part in stock."""
    session: Session = Session()
    part = session.query(StockPart).filter(StockPart.id_ == part_id).one()
    part.count -= reduction
    session.commit()
