from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from app.Models.base import db
from app.Forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.Models.user import User

from libs.email import send_mail

from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST":
        if form.validate():
            with db.auto_commit():
                user = User()
                user.set_attrs(form.data)
                db.session.add(user)

            return redirect(url_for("Web.login"))

    return render_template("auth/register.html", form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=True)

                next = request.args.get("next")
                if not next or not next.startswith("/"):
                    next = url_for("Web.index")

                return redirect(next)
            else:
                flash("账号不存在或者密码错误")
    return render_template("auth/login.html", form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == "POST":
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()

            send_mail(account_email, "重置你的密码", "email/reset_password.html", user=user, token=user.generate_token())
            flash("一封邮件已经发送到邮箱" + account_email + "，请及时查收")
            # return redirect(url_for("Web.login"))

    return render_template("auth/forget_password_request.html", form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        success = User.reset_password(token, form.password1.data)

        if success:
            flash("你的密码已更新，请使用新密码登录")
            return redirect(url_for("Web.login"))
        else:
            flash("密码重置失败")

    return render_template("auth/forget_password.html", form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("Web.index"))
