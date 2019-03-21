# -*- coding: utf-8 -*-
# Time    : 2019/3/20 23:02
# Author  : LiaoKong

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ""

        return r.json() if return_json else r.text
