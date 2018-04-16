from flask import request, redirect, render_template, url_for, session, flash

from passlib.hash import pbkdf2_sha256

from src.models import db, User
from src.app import app
from src.features import login_required
from src.forms.authentication import RegisterForm


@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        if form.validate_on_submit():
            # hassing password
            password_encrypt = pbkdf2_sha256.encrypt(password, rounds=2000, salt_size=16)
            try:
                user = User(username=username, password=password_encrypt, email=email, name=name)
                db.session.add(user)
                db.session.commit()
            except:
                flash("Username has been selected, try another username")
                return render_template('authentication/register.html', form=form)
                
            flash("Register complete, you can login right now!")
            return redirect(url_for('login'))
        else:
            return render_template('authentication/register.html', form=form)
    else:
        return render_template('authentication/register.html', form=form)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.get(username)

        # checking password in db
        password_verify = pbkdf2_sha256.verify(password, user.password)

        if password_verify:
            session['logged_in'] = True
            session['username'] = username
            flash("Login Success {0}".format(username))
            return render_template('homepage.html')
        else:
            flash("Login failed because password is not match")
            return render_template('authentication/login.html')
    else:
        return render_template('authentication/login.html')

@app.route('/logout/')
@login_required
def logout():
    session.clear()
    flash("Success Logout")
    return render_template('authentication/login.html')