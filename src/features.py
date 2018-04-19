from flask import request, redirect, url_for, session, flash

from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Login first before do any process!')
            return redirect(url_for('login'))
    return wrap


def clear_session():
    '''
        Function for clear session
    '''
    session.clear()