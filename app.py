from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello, world"


@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})


@app.get("/welcome")
def welcome_template():
    return render_template("base.html", title="devstream")
