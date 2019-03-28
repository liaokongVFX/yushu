# -*- coding: utf-8 -*-
# Time    : 2019/3/21 0:03
# Author  : LiaoKong

from flask import Flask
from flask_login import LoginManager

from app.Models.base import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")

    create_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = "Web.login"
    login_manager.login_message = "请先登录或注册"

    db.init_app(app)
    db.create_all(app=app)

    return app


def create_blueprint(app):
    from app.Web.book import web
    app.register_blueprint(web)
