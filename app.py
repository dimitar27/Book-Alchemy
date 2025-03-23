from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'library.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
os.makedirs(os.path.dirname(db_path), exist_ok=True)
db.init_app(app)

with app.app_context():
    db.create_all()