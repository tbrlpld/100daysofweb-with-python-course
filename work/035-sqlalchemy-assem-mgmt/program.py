# -*- coding: utf-8 -*-

"""Main program to run the assembly management."""

import os

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


def main():
    # Config DB
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_filename = "assem_mgmt.sqlite"
    db_path = os.path.join(current_dir, db_filename)
    if os.exists(db_path):
        os.remove(db_path)
    connection_string = "sqlite:///" + db_path

    # DB engine
    engine = sa.create_engine(connection_string)

    # DB tables
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)



if __name__ == "__main__":
    main()
