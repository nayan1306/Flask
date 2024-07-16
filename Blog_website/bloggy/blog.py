from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from bloggy.auth import login_required
from bloggy.db import get_db

bp = Blueprint('blog', __name__)