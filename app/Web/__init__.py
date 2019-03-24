# -*- coding: utf-8 -*-
# Time    : 2019/3/21 0:04
# Author  : LiaoKong
from flask import Blueprint

web = Blueprint("Web", __name__)

from app.Web import book
from app.Web import user
from app.Web import auth
from app.Web import drift
from app.Web import gift
from app.Web import main
from app.Web import wish
