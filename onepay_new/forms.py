# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 20)])
    remember = BooleanField('记住密码')
    submit = SubmitField('登陆')

class RegisterForm(FlaskForm):
    username = StringField('用户名(邮箱地址)', validators=[DataRequired(), Length(1, 20)])
    truename = StringField('真实姓名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 20)])
    password_again = PasswordField('重复密码', validators=[DataRequired(), Length(1, 20)])
    phone_number = PasswordField('手机号', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('注册')