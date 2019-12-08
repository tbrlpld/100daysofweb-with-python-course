# -*- coding: utf-8 -*-

"""Define DB setup for the app."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

project_dir = os.path.abspath(__file__)
# dbfile = os.path.join(project_dir, "db.sqlite3")
# dbstring = "sqlite:///{0}".format(dbfile)
dbstring = "sqlite:///:memory:"
dbengine = create_engine(dbstring, echo=True)

Session = sessionmaker(bind=dbengine)
