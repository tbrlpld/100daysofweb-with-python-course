from flask import Flask

# Creates the flask instance
app = Flask(__name__)

# This needs to be below the app instance!
from program import routes

