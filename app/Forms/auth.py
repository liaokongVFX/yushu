# -*- coding: utf-8 -*-
# Time    : 2019/3/25 23:16
# Author  : LiaoKong

from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, ValidationError, Email, EqualTo

from app.Models.user import User


class RegisterForm(Form):
    nickname = StringField('昵称', validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email(message='电子邮箱不符合规范')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class EmailForm(Form):
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email(message='电子邮箱不符合规范')])


class LoginForm(EmailForm):
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[DataRequired(),
                                          Length(6, 32, message="密码长度至少需要在6-32个字符之间"),
                                          EqualTo("password2", message="两次输入的密码不同")])

    password2 = PasswordField(validators=[DataRequired(), Length(6, 32)])
