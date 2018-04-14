from flask import redirect, render_template, url_for, request

from src.app import app
from src.models import db, Category, Post
from src.features import login_required
from src.forms.category import CategoryForm

# get all category
@app.route('/category/')
def list_category():
    categories = Category.query.all()
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
@login_required
def create_category():
    form = CategoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            category_name = request.form['category_name']
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('list_category'))
        else:
            return render_template('category/create.html', form=form)
    else:
        return render_template('category/create.html', form=form)

# update category
@app.route('/update_category/<int:id>', methods=['POST', 'GET'])
@login_required
def update_category(id):
    category = Category.query.get(id)
    form = CategoryForm()
    if request.method == 'POST':
        if form.validate_on_submit():   
            category_name = request.form['category_name']
            category = Category.query.get(id)
            category.name = category_name
            db.session.commit()
            return redirect(url_for('list_category'))
        else:
            return render_template('category/update.html', form=form)
    else:
        if category is None:
            message = "Error 404, Category not found!"
            return render_template('category/index.html', message=message)
        return render_template('category/update.html', category=category, form=form)
