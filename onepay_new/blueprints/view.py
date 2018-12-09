# -*- coding: utf-8 -*-

from flask import flash, redirect, url_for, render_template ,jsonify ,request ,current_app ,Blueprint

from onepay_new.forms import LoginForm, RegisterForm
from onepay_new.models import Admin
from onepay_new.commands import redirect_back
from onepay_new.models import db

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
        current_app.logger.info(username)
        current_app.logger.info(truename)
        current_app.logger.info(password)
        current_app.logger.info(password_again)
        current_app.logger.info(phone_number)
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            flash('用户名已经被注册....', 'warning')
            return render_template(html, form=form)
        if password == password_again:
            admin = Admin(username=username, truename=truename, password=password, phone_number=phone_number)
            db.session.add(admin)
            db.session.commit()
            flash('register success....', 'info')
            return redirect_back()
    return render_template(html, form=form)

@view_bp.route('/onepay', methods=['POST',])
def update_onepay_info():
    onepay_time = request.json['time']
    current_app.logger.info(onepay_time)
    onepay_message = request.json['message']
    current_app.logger.info(onepay_message)
    return jsonify({'error': 0})