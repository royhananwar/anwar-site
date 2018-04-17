from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators, ValidationError


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Required('Please input your Username')])
    password = PasswordField('Password', [
        validators.length(min=1, max=20),
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Password is not match!'),
        ])
    password_confirm = PasswordField('Confirm Password')
    email = StringField('Email', [validators.Required('Please input your email')])
    name = StringField('Full Name', [validators.Required('Input your Full Name')])


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Required('Please input your Username')])
    password = PasswordField('Password', [validators.Required("Passowrd can't be null")])


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password')
    new_password = PasswordField('New Password', [
        validators.length(min=1, max=20),
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Password is not match!'),
        ])
    password_confirm = PasswordField('Confirm New Password')
