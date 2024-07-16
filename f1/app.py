from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/boost")
def hello():
    return "Let\'s make it crazy"