from flask import render_template, request

from app.Models.base import db
from app.Forms.auth import RegisterForm
from app.Models.user import User

from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST":
        if form.validate():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            db.session.commit()

    else:
        return render_template("auth/register.html", form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
