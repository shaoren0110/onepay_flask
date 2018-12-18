# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for, render_template ,jsonify ,request ,current_app ,Blueprint

from onepay_new.forms import LoginForm, RegisterForm
from onepay_new.models import Admin, Onepay
from onepay_new.commands import redirect_back
from onepay_new.models import db
import logging

pay_flag = 0

import json
from flask_login import login_user

view_bp = Blueprint('view', __name__)

@view_bp.route('/')
def index():
    return render_template('index.html')

@view_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            if username == admin.username and password == admin.password :
                flash('Welcome back.', 'info')
            else:
                flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('login.html', form=form)

@view_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    html = 'register.html'
    if form.validate_on_submit():
        username = form.username.data
        truename = form.truename.data
        password = form.password.data
        password_again = form.password_again.data
        phone_number = form.phone_number.data
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            flash('用户名已经被注册....', 'warning')
            return render_template(html, form=form)
        if password == password_again:
            admin = Admin(username=username, truename=truename, password=password, phone_number=phone_number)
            db.session.add(admin)
            db.session.commit()
            flash('register success....', 'info')
            return redirect_back('view.login')
    return render_template(html, form=form)


@view_bp.route('/pay', methods=['GET', 'POST'])
def pay():
    return render_template('pay.html')

@view_bp.route('/pay/test', methods=['GET', 'POST'])
def test():
    global pay_flag
    logging.debug("set pay_flag is %d " % pay_flag)
    if pay_flag == 0:
        return jsonify({'error': 0})
    else:
        return jsonify({'error': 1})

@view_bp.route('/pay/clear', methods=['GET', 'POST'])
def clear():
    global pay_flag
    pay_flag = 0
    logging.debug("clear pay_flag ")
    return jsonify({'error': 0})


@view_bp.route('/paysuccess', methods=['GET', 'POST'])
def paysuccess():
    return render_template('paysuccess.html')

@view_bp.route('/api/login', methods=['POST'])
def check_login():
    onepayname = request.json['name']
    onepaypass = request.json['password']
    check = Admin.query.filter_by(username=onepayname).first()
    if check:
        if  onepaypass == check.password:
            return jsonify({'error': 0})
        else:
            return jsonify({'error': 2})
    else:
        return jsonify({'error': 1})


@view_bp.route('/api/onepay', methods=['POST'])
def update_onepay_info():
    global pay_flag
    onepay_time = request.json['time']
    onepay_type = request.json['type']
    onepay_money = request.json['money']
    logging.debug("set onepay_time is %d " % onepay_time)
    logging.debug("set onepay_type is %d " % onepay_type)
    logging.debug("set onepay_money is %d " % onepay_money)
    if onepay_type == '1' or onepay_type == '2':
        onepay = Onepay(paytime=onepay_time, paytype=onepay_type, paymoney=onepay_money)
        db.session.add(onepay)
        db.session.commit()
        pay_flag = 1
        return jsonify({'error': 0})
    else:
        return jsonify({'error': 1})