#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex05.py
@time: 2018/1/6 15:57
"""
# 1.用filter函数将1~100之间的所有素数prime放入到列表中并打印
l=list(range(1,101))
def is_prime(x):
    a=-2
    for i in range(2,x):
        a=i
        if x%i==0:
            break
    if a==x-1 or x==2:
        str=True
    else:
        str=False
    return str
prime_list=list(filter(is_prime,l))
print(prime_list)
