# -*- coding: utf-8 -*-

"""Makes SQLAlchemy base class available with a shorter name."""

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
