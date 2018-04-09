from flask import render_template, redirect, request, url_for

from app import app
from models import db, Category

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
        return redirect(url_for('homepage'))
    else:
        return render_template('category/create.html')

if __name__ == '__main__':
    app.run(debug=True)