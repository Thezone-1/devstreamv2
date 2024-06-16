from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello, world"


@app.get("/welcome")
def welcome_template():
    return render_template("base.html", title="devstream")
