# -*- coding: utf-8 -*-
# Time    : 2019/3/20 23:36
# Author  : LiaoKong

import json

from flask import jsonify, request, flash, render_template
from flask_login import current_user

from app.Forms.Book import SearchForm
from app.Models.gift import Gift
from app.Models.wish import Wish
from app.ViewModels.trade import TradeInfo

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
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True

        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template("book_detail.html", book=book, wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)
