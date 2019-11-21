# -*- coding: utf-8 -*-

"""Configuration for the database connection."""

import os

_current_dir = os.path.dirname(os.path.abspath(__file__))

db_filename = "assem_mgmt.sqlite3"
db_path = os.path.join(_current_dir, db_filename)
