from flask import request, redirect, render_template, url_for, session

from src.app import app
from src.models import db, Post, Category
from src.features import login_required


# list all post
@app.route('/post/')
def list_post():
    posts = Post.query.all()
    if posts is None:
        return render_template('post/index.html', data="No post Available")
    return render_template('post/index.html', posts=posts)

# get detail post
@app.route('/detail_post/<int:id>')
def detail_post(id):
    post = Post.query.get(id)
    if post is None:
        message = "Error 404, Post is not Found"
        return render_template('post/detail.html', message=message)
    return render_template('post/detail.html', post=post)

# create new post
@app.route('/create_post/', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['post_title']
        body = request.form['post_body']
        category_id = request.form['category_id']
        owner_id = session['username']

        post = Post(title=title, body=body, category_id=category_id, owner_id=owner_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('list_post'))
    else:
        categories = Category.query.all()
        return render_template('post/create.html', categories=categories)

# update post
@app.route('/update_post/<int:id>', methods=['POST', 'GET'])
@login_required
def update_post(id):
    if request.method == 'POST':
        title = request.form['post_title']
        body = request.form['post_body']
        category_id = request.form['category_id']
        owner_id = session['username']

        post = Post.query.get(id)
        post.title = title
        post.body = body
        post.category_id = category_id
        post.owner_id = owner_id

        db.session.commit()
        return redirect(url_for('list_post'))
    else:
        post = Post.query.get(id)
        category = Category.query.get(post.category_id)
        categories = Category.query.all()

        if post is None:
            message = "Error 404, Post is not Found"
            return render_template('post/detail.html', message=message)

        return render_template('post/update.html', post=post, category=category, categories=categories)
