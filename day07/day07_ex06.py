#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex06.py
@time: 2018/1/6 16:18
"""
# 用递归方式计算1+2+3+....+n的和
def recursion(n):
    if n==1:
        return 1
    return n + recursion(n-1)
print("1+2+3+....+n的和")
n=int(input("请输入n:"))
print("1+2+3...+{}={}".format(n,recursion(n)))

