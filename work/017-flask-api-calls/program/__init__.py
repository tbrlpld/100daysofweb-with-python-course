from flask import Flask

# Creates the flask instance
app = Flask(__name__)

# This needs to be below the app instance!
from program import routes
# App is imported in the routes.py -- isn't this a circular dependency?
# The routes are registered with the app in the routes.py.
# Why do I need to include this here?
# This is apparently to make the decorators for the routes work.
# The circular import is directly addressed by the flask documentation:
# https://flask.palletsprojects.com/en/1.1.x/patterns/packages/?highlight=Circ
