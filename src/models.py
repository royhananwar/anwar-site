from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
            default=datetime.utcnow)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))

    owner_id = db.Column(db.String, db.ForeignKey('user.username'), nullable=True)
    owner = db.relationship('User', backref=db.backref('posts', lazy=True))
    
    def __repr__(self):
        return 'Post: {0}'.format(self.title)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'Category: {0}'.format(self.name)


class User(db.Model):
    username = db.Column(db.String(32), primary_key=True)
    password = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return '{0}'.format(self.username)

