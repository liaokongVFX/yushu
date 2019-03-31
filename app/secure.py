# -*- coding: utf-8 -*-
# Time    : 2019/3/20 22:20
# Author  : LiaoKong

DEBUG = True

SECRET_KEY = "fhklfgjhlfg"

# database
SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:root@127.0.0.1:3306/fisher1"

MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_USE_SSL : default False
MAIL_USERNAME = "568250549@qq.com"
MAIL_PASSWORD = "zwd6666666666fcb"
MAIL_DEFAULT_SENDER = "568250549@qq.com"
