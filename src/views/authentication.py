from flask import request, redirect, render_template, url_for

from passlib.hash import pbkdf2_sha256

from src.models import db, User
from src.app import app


@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']

        # hassing password
        password_encrypt = pbkdf2_sha256.encrypt(password, rounds=2000, salt_size=16)

        user = User(username=username, password=password_encrypt, email=email, name=name)
        db.session.add(user)
        db.session.commit()
        
        return render_template('homepage.html')
    else:
        return render_template('authentication/register.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.get(username)

        # checking password in db
        password_verify = pbkdf2_sha256.verify(password, user.password)

        if password_verify:
            return render_template('homepage.html')
        else:
            return render_template('authentication/login.html')
    else:
        return render_template('authentication/login.html')