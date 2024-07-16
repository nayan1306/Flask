from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("index.html",person=name)