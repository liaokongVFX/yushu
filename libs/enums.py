# -*- coding: utf-8 -*-
# Time    : 2019/3/31 19:09
# Author  : LiaoKong

from enum import Enum


class PendingStatus(Enum):
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
