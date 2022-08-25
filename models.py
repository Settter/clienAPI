from flask_sqlalchemy import SQLAlchemy
from flask import Flask


App = Flask(__name__)

App.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rEtyuol44@localhost/t_db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(App)
db.create_all()


class mailing_list(db.Model):
    id_send = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    date_time_start = db.Column(db.DATE, nullable=False)
    phone_n = db.Column(db.Integer, nullable=False)
    date_time_close = db.Column(db.DATE, nullable=False)
    id_message = db.Column(db.Integer, nullable=False)

class client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    phone_n = db.Column(db.Integer, nullable=False, unique=True)
    timezone = db.Column(db.Integer, nullable=False)

class message(db.Model):
    id_message = db.Column(db.Integer, primary_key=True)
    date_time_create = db.Column(db.DATE, nullable=False)
    status = db.Column(db.String, nullable=False)
    id_send = db.Column(db.Integer, nullable=False)
    id_client = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String, nullable=False)


