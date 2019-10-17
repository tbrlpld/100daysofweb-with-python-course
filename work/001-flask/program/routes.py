from flask import render_template

# Flask is already imported in the __init__.py
from program import app  # This is in the __init__.py
# Now I have the app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/100days")
def route100days():
    return render_template("100days.html")
