# -*- coding: utf-8 -*-
# Time    : 2019/3/31 17:42
# Author  : LiaoKong
from threading import Thread

from flask_mail import Message
from flask import current_app, render_template

from app import mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except:
            pass


def send_mail(to, subject, template, **kwargs):
    msg = Message("[鱼书]" + " " + subject,
                  sender=current_app.config["MAIL_DEFAULT_SENDER"], recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
