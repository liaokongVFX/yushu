# -*- coding: utf-8 -*-
# Time    : 2019/3/25 22:37
# Author  : LiaoKong

from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, Integer, String, SmallInteger


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            # 回滚
            self.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    # 使Base类不生成表
    __abstract__ = True

    create_time = Column("create_time", Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
