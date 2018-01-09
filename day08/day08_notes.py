#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day08_notes.py
@time: 2018/1/6 19:49
"""
class Dog:
    """
    这是一种小动物的定义
    这种动物属于犬类
    """
    def __init__(self,k,c,a):
        self.kinds=k
        self.color=c
        self.age=1
dog1=Dog("京巴","灰色",2)
print(dog1.kinds,dog1.color,dog1.age)
