#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex04.py
@time: 2018/1/6 15:24
"""
# 练习:求:1**9+2**8+3**7+.....+9**1的和 11377
# 用函数式编程来求:
# pow, sum, map, range
# lambda
"""
def my_op():
    L1 = list(range(1, 10))
    L2 = list(range(9, 0, -1))
    L3 = list(map(pow, L1, L2))
    return sum(L3)
print(my_op())
"""
L1=list(range(1,10))
L2=list(range(9,0,-1))
print("1**9+2**8+3**7+...+9**1=",end="")
print(sum(list(map(pow, L1, L2))))

