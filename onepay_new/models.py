# -*- coding: utf-8 -*-

from datetime import datetime

from flask_login import UserMixin
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    truename = db.Column(db.String(20))
    password = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))

class Onepay(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    paytime = db.Column(db.String(20))
    paytype = db.Column(db.String(2))
    paymoney = db.Column(db.String(20))
