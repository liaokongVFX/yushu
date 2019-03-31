# -*- coding: utf-8 -*-
# Time    : 2019/3/31 14:23
# Author  : LiaoKong


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []

        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime("%Y-%m-%d")
        else:
            time = "未知"

        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
