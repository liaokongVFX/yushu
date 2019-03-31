# -*- coding: utf-8 -*-
# Time    : 2019/3/28 22:10
# Author  : LiaoKong

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.Models.base import Base, db
from spider.YuShuBook import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)

    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(15), nullable=False)

    # book = relationship("Book")
    # bid = Column(Integer, ForeignKey("book.id"))

    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)

        return yushu_book.first


    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()

        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        # 根据传入的一组isbn,到wish表中计算出某个礼物的wish心愿数量
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(Gift.isbn).all()

        count_dict = [{"count": w[0], "isbn": w[1]} for w in count_list]
        return count_dict


from app.Models.gift import Gift