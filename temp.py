# -*- coding: utf-8 -*-
# Time    : 2019/3/23 18:57
# Author  : LiaoKong

import time
import threading

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)

print("a:" + str(my_stack.top))


def worker():
    print("b:" + str(my_stack.top))

    my_stack.push(2)

    print("c:" + str(my_stack.top))


new_t = threading.Thread(target=worker, name="qy")
new_t.start()
time.sleep(1)

print("d:" + str(my_stack.top))
