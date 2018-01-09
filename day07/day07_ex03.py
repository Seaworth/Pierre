#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex03.py
@time: 2018/1/6 15:00
"""
# 练习： 给出一个数n,写一个函数计算1+2**2+3**3+...+n**n的和
# 注意：n给个小点的数
def my_op(n):
    L1 = list(range(1, n + 1))  # 得到1,2,3,...,n的列表
    L2 = list(map(pow,L1,L1))   # 得到1**1,2**2,3**3,...,n**n的列表
    return sum(L2)              # 对L2求和并返回

print("计算1+2**2+3**3+...+n**n的和")
n=int(input("请输入一个数n："))
print("结果是{}".format(my_op(n)))



