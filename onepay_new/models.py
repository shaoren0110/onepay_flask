# -*- coding: utf-8 -*-

from datetime import datetime

from onepay_new import db
from flask_login import UserMixin

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    truename = db.Column(db.String(20))
    password = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))