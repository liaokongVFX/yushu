# -*- coding: utf-8 -*-
# Time    : 2019/3/20 23:36
# Author  : LiaoKong
from flask import jsonify, request

from app.Forms.Book import SearchForm

from spider.YuShuBook import YuShuBook
from libs.Helper import is_isbn_or_key
from . import web


@web.route("/book/search")
def search():
    """
    q: 不同关键字 isbn
    page:
    :return:
    """
    # 验证层
    form = SearchForm(request.args)

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        # print(request.args.to_dict())
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        # return json.dumps(result), 200, {"content-type": "application/json"}
        return jsonify(result)
    else:
        return jsonify(form.errors)
