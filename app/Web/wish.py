from flask import current_app, flash, redirect, url_for, render_template

from app import db
from app.Models.wish import Wish
from app.ViewModels.wish import MyWishes
from . import web

from flask_login import login_required, current_user


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_counts(isbn_list)

    view_model = MyWishes(wishes_of_mine, gift_count_list)
    return render_template("my_wish.html", wishes=view_model.wishes)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Wish()
            gift.isbn = isbn
            gift.uid = current_user.id

            current_user.beans += current_app.config["BEANS_UPLOAD_ONE_BOOK"]
            db.session.add(gift)
    else:
        flash("这本书已经添加到你的赠送清单或者已存在于你的心愿清单，请不要重复添加")

    return redirect(url_for("Web.book_detail", isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
