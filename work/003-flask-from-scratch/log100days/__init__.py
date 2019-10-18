from flask import Flask

app = Flask(__name__)

from log100days import routes
