# -*- coding: utf-8 -*-
# Time    : 2019/3/20 23:36
# Author  : LiaoKong

import json

from flask import jsonify, request, flash, render_template

from app.Forms.Book import SearchForm

from spider.YuShuBook import YuShuBook
from libs.Helper import is_isbn_or_key
from . import web
from app.ViewModels.book import BookViewModel, BookCollection


@web.route("/book/search")
def search():
    """
    q: 不同关键字 isbn
    page:
    :return:
    """
    # 验证层
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        # print(request.args.to_dict())
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)

        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)

    else:
        flash("搜索关键字不符合要求，请重新输入关键字")
        # return jsonify(form.errors)

    return render_template("search_result.html", books=books)


@web.route("/book/<isbn>/detail/")
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template("book_detail.html", book=book, wishes=[], gifts=[])
