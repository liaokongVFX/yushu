# -*- coding: utf-8 -*-
# Time    : 2019/3/28 22:10
# Author  : LiaoKong

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.Models.base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)

    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(15), nullable=False)

    # book = relationship("Book")
    # bid = Column(Integer, ForeignKey("book.id"))

    launched = Column(Boolean, default=False)
