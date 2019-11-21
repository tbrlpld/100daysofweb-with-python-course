# -*- coding: utf8 -*-

"""Functions to populate the database with some example data."""


from db.session import Session
from models.parts import Part, StockPart


def add_iventory():
    """Add parts to DB."""
    session = Session()

    inventory = (
        StockPart(
            part=Part(name='Valve Body 32"'),
            count=100,
        ),
        StockPart(
            part=Part(name='Valve Body 12"'),
            count=50,
        ),
        StockPart(
            part=Part(name='Valve Slip 32"'),
            count=90,
        ),
        StockPart(
            part=Part(name='Valve Slip 12"'),
            count=50,
        ),
        StockPart(
            part=Part(name='Screw 14 x 2 1/2"'),
            count=1000,
        ),
    )

    session.add_all(inventory)
    session.commit()
