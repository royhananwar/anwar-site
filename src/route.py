from flask import render_template, redirect, request, url_for

from app import app
from models import db, Category, Post

# index
@app.route('/')
def homepage():
    return 'Hello, this is Royhan Anwar'

# get all category
@app.route('/category/')
def list_category():
    categories = Category.query.all()
    print(categories)
    return render_template('category/index.html', categories=categories)

# create new category
@app.route('/create_category/', methods=['POST', 'GET'])
def create_category():
    if request.method == 'POST':
        category_name = request.form['category_name']
        category = Category(name=category_name)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('list_category'))
    else:
        return render_template('category/create.html')

# update category
@app.route('/update_category/<int:id>', methods=['POST', 'GET'])
def update_category(id):
    if request.method == 'POST':
        category_name = request.form['category_name']
        category = Category.query.get(id)
        category.name = category_name
        db.session.commit()
        return redirect(url_for('list_category'))
    else:
        category = Category.query.get(id)
        return render_template('category/update.html', category=category)

# list all post
@app.route('/post/')
def list_post():
    posts = Post.query.all()
    if posts is None:
        return render_template('post/index.html', data="No post Available")
    return render_template('post/index.html', posts=posts)

# create new post
@app.route('/create_post/', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['post_title']
        body = request.form['post_body']
        category_id = request.form['category_id']

        post = Post(title=title, body=body, category_id=category_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('list_post'))
    else:
        categories = Category.query.all()
        return render_template('post/create.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)