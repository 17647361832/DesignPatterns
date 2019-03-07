# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: Python_hasattr.py
@Time: 2019/3/8 0:51
@Desc:hasattr方法测试
"""


class Boy():
    def __init__(self):
        self.JJ = 'Crude_Long_Black'


if __name__ == '__main__':
    Tom = Boy()

    if hasattr(Tom, 'JJ'):
        print('Tom has JJ and his JJ is', Tom.JJ)

    else:
        print("It's a sad story! Tom is a girl!")