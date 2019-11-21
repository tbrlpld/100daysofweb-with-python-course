# -*- coding: utf-8 -*-

"""
Create database session factory.

Also holds functionality to initialize the database in the first place.
"""

import os

import sqlalchemy as sa
from sqlalchemy import orm

from models.base import Base
from db.db_config import db_path


class _Factory(object):

    def __init__(self):
        self.factory = None

    def init_db(self):
        # Delete if exists (no migrations yet)
        if os.path.exists(db_path):
            os.remove(db_path)
        connection_string = "".join(["sqlite:///", db_path])

        # DB engine
        engine = sa.create_engine(connection_string)

        # Create DB tables (and thus the DB file)
        from models import _all
        Base.metadata.create_all(bind=engine)

        self.factory = orm.sessionmaker(bind=engine)

    def create(self):
        if self.factory is None:
            raise Exception(
                "Database not initialized!"
                + " Run `_SessionFactory.init_db()`",
            )
        return self.factory


Session = _Factory()
