# -*- coding: utf-8 -*-

"""Define package wide components."""

from flask import Flask


app = Flask(__name__)

from awesome import routes
