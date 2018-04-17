from flask import render_template, redirect, request, url_for

from src.app import app
from src.models import db, Category, Post
from src.views import category, post, authentication
from src.seed_data import seed_data

# index
@app.route('/')
def homepage():
    seed_data()
    return 'Hello, this is Royhan Anwar'


if __name__ == '__main__':
    app.run(debug=True)