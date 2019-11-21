# -*- coding: utf8 -*-

"""Functions to populate the database with some example data."""


from db.session import Session
from models.parts import Part, StockPart


def add_parts():
    """Add parts to DB."""
    session = Session.create()

    stock_part = StockPart(
        part=Part(name='32" Valve Body'),
        count=100,
    )

    session.add(stock_part)
    session.commit()
