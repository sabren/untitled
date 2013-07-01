"""
A small database designer for the web.
"""
from contextlib import closing
import sqlite3
from flask import Flask, g, render_template

app = Flask(__name__)
app.config.from_object(__name__)

DATABASE = 'untitled.sdb'
DEBUG = True


def connect_db():
    """
    Connect to the database.
    """
    return sqlite3.connect(app.config["DATABASE"])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/')
def main():
    """
    Main entry point for flask.
    """
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
