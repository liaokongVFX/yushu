# -*- coding: utf-8 -*-
# Time    : 2019/3/20 21:53
# Author  : LiaoKong

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
