
# Flask is already imported in the __init__.py
from program import app  # This is in the __init__.py
# Now I have the app


@app.route("/")
@app.route("/index")
def index():
    return "Hello Pythonistas"


@app.route("/hello/<string:name>")
def hello(name):
    return f"Hello {name}"
