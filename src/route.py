from flask import render_template, redirect, request, url_for

from src.app import app
from src.models import db, Category, Post
from src.views import category, post, authentication

# index
@app.route('/')
def homepage():
    return 'Hello, this is Royhan Anwar'


if __name__ == '__main__':
    app.run(debug=True)