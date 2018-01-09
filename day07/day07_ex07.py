#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex07.py
@time: 2018/1/6 16:28
"""
# 用函数式编程,算出 1~20的阶乘的和
#      1!+2!+3!+4!+5!+6!+7!+....20!
def my_factorial():
    def recursion(n): # 递归求n的阶乘
        if n == 1:
            return 1
        return n * recursion(n-1)
    L1=list(range(1,21))
    L2=sum(list(map(recursion,L1)))
    return L2
print("1!+2!+3!+4!+5!+6!+7!+...+20!={}".format(my_factorial()))
