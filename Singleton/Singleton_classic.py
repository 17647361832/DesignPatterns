# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: P♂boy
@License: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@Contact: 17647361832@163.com
@Software: Pycharm
@File: Singleton_classic.py
@Time: 2019/3/8 0:31
@Desc:单例模式
"""

class Singleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    s = Singleton()

    print("Singleton类创建的对象s的地址是：", s)
    s2 = Singleton()

    print("Singleton类创建的对象s2的地址是：", s2)