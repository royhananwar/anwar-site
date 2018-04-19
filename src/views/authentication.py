from flask import request, redirect, render_template, url_for, session, flash

from passlib.hash import pbkdf2_sha256

from src.models import db, User
from src.app import app
from src.features import login_required, clear_session
from src.forms.authentication import RegisterForm, LoginForm, ChangePasswordForm


@app.route('/register/', methods=['POST', 'GET'])
def register():
    '''
        Function for register
    '''

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
                flash("Username or email has been selected, try another username or email")
                return render_template('authentication/register.html', form=form)
                
            flash("Register complete, you can login right now!")
            return redirect(url_for('login'))
        else:
            return render_template('authentication/register.html', form=form)
    else:
        return render_template('authentication/register.html', form=form)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    ''' 
        Function for login in blog 
    '''

    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.get(username)
        if user is None: #check if user is none
            flash("This user is not exist")
            return render_template('authentication/login.html', form=form)
        if form.validate_on_submit():
            # checking password in db
            password_verify = pbkdf2_sha256.verify(password, user.password)
            if password_verify:
                session['logged_in'] = True #set logged_in in session True, so can use login_required
                session['username'] = username
                flash("Login Success {0}".format(username))
                return render_template('homepage.html')
            else:
                flash("Login failed because password is not match")
                return render_template('authentication/login.html', form=form)
        else:
            return render_template('authentication/login.html', form=form)
    else:
        return render_template('authentication/login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    '''
        Function for logout and clear session
    ''' 

    clear_session()
    flash("Success Logout")
    return redirect(url_for('login'))


@app.route('/change_password/', methods=['POST', 'GET'])
@login_required
def change_password():
    '''
        Function for change password
    '''

    form = ChangePasswordForm()
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        if form.validate_on_submit():
            username = session['username']
            user = User.query.get(username)
            password_verify = pbkdf2_sha256.verify(old_password, user.password)
            if password_verify:
                new_password_hash = pbkdf2_sha256.encrypt(new_password, rounds=2000, salt_size=16)
                user.password = new_password_hash
                db.session.commit() #save new password to db 
                clear_session() #clear session before logout
                flash("Password is changed")
                return redirect(url_for('login'))
            else:
                flash("Old password is not correct")
                return render_template('authentication/change_password.html', form=form)
        else:
            return render_template('authentication/change_password.html', form=form)
    else:
        return render_template('authentication/change_password.html', form=form)
