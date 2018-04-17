from flask import Flask

import os

from src.models import db

app = Flask(__name__)

POSTGRES = {
    'user': 'MY USER',
    'pw': 'MY PASSWORD',
    'db': 'MY DB',
    'host': 'MY HOST',
    'port': '5432',
}

db_url = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(POSTGRES['user'], POSTGRES['pw'], POSTGRES['host'], POSTGRES['port'], POSTGRES['db'])

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "My Secret Key"

db.init_app(app)