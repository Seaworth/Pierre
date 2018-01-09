#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex09.py
@time: 2018/1/6 19:16
"""
# 写一个lambda表达式,求两个变量的最大值
# 三元运算是if-else 语句的快捷操作，也被称为条件运算
# [on_true] if [expression] else [on_false]
my_max2=lambda x,y:x if x>y else y
print(my_max2(100,200))

