# -*- coding: utf-8 -*-
# Time    : 2019/3/21 0:03
# Author  : LiaoKong

from flask import Flask

import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    create_blueprint(app)

    return app


def create_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
