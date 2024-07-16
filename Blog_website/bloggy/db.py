import sqlite3

import click  # click is used for creating command-line interfaces in Flask
from flask import current_app, g  # current_app gives access to the current Flask application and g is a global object for holding data

# Function to get a database connection
def get_db():
    if 'db' not in g:
        # If 'db' is not already in the global object 'g', connect to the SQLite database
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],  # Use the DATABASE configuration from the current app
            detect_types=sqlite3.PARSE_DECLTYPES  # Allow SQLite to detect types of columns
        )
        g.db.row_factory = sqlite3.Row  # Configure the connection to return rows that behave like dictionaries

    return g.db  # Return the database connection

# Function to close the database connection
def close_db(e=None):
    db = g.pop('db', None)  # Remove 'db' from the global object 'g' and get its value. If 'db' is not in 'g', return None.

    if db is not None:
        db.close()  # If a database connection exists, close it
