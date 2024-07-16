from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
from flask import abort, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()