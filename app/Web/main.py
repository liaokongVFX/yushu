from flask import render_template

from app.Models.gift import Gift
from app.ViewModels.book import BookViewModel
from . import web

__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template("index.html", recent=books)


@web.route('/personal')
def personal_center():
    pass
