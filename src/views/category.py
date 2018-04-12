from flask import redirect, render_template, url_for, request

from src.app import app
from src.models import db, Category, Post


# get all category
@app.route('/category/')
def list_category():
    categories = Category.query.all()
    print(categories)
    return render_template('category/index.html', categories=categories)

# get detail category
@app.route('/detail_category/<int:id>')
def detail_category(id):
    category = Category.query.get(id)
    if category is None:
        message = "Error 404, Category not found!"
        return render_template('category/detail.html', message=message)
    return render_template('category/detail.html', category=category)

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
        if category is None:
            message = "Error 404, Category not found!"
            return render_template('category/update.html', message=message)
        return render_template('category/update.html', category=category)
