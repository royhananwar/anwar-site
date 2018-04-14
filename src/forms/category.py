from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField
from wtforms import ValidationError, validators


class CategoryForm(FlaskForm):
    category_name = StringField('Category Name', [validators.Required(message="Please Input this field!")])