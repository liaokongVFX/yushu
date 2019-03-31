from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.Models.gift import Gift
from . import web

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)

    if current_gift.is_yourself_gift(current_user.id):
        flash("这本书是你自己的，不能自己和自己索取")
        return redirect(url_for("Web.book_detail", isbn=current_gift.isbn))

    can = current_user.can_send_gift()

    if not can:
        return render_template("not_enough_beans.html", beans=current_user.beans)

    gifter = current_gift.user.summary
    return render_template("drift.html", gifter=gifter, user_beans=current_user.beans)


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
