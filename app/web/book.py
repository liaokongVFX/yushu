# -*- coding: utf-8 -*-
# Time    : 2019/3/20 23:36
# Author  : LiaoKong
from flask import jsonify, Blueprint

from YuShuBook import YuShuBook
from Helper import is_isbn_or_key

web = Blueprint("web", __name__)


@web.route("/book/search/<q>/<page>/")
def search(q, page):
    """
    q: 不同关键字 isbn
    page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == "isbn":
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    # return json.dumps(result), 200, {"content-type": "application/json"}
    return jsonify(result)
