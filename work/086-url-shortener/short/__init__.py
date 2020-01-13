from flask import Flask, redirect


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Lambda!"


@app.route("/x")
def exmple():
    return redirect("http://example.com")


@app.route("/<shortlink>")
def redirect_to_long(shortlink):
    return f"You requested the shortlink: {shortlink}"
