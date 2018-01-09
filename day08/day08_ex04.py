#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day08_ex04.py
@time: 2018/1/8 20:44
"""
# 1. 写一个正方形类:
# 有三个属性:
# 边长length
# 周长circumference
# 面积area
# 用此类生成对象, 此三个属性其中一个变量, 所有属性同步变化
# 注: 用特殊属性 @ property实现
import math
class Square:  # 正方形类
    def __init__(self,length):  # 边长
        self.length=length

    @property
    def circumference(self):  # 周长
        return self.length*4.0

    @circumference.setter
    def circumference(self,cir):
        self.length=cir*0.25
    #
    @property
    def area(self):  # 面积
        return self.length**2
    @area.setter
    def area(self,a):
        self.length=math.sqrt(a)

s1=Square(2)
print("s1.length={:^4}".format(s1.length),end="  ")
print("s1.circumference={:^4}".format(s1.circumference),end="  ")
print("s1.area={:^4}".format(s1.area))

s1.length=3 # 改变边长
print("s1.length={:^4}".format(s1.length),end="  ")
print("s1.circumference={:^4}".format(s1.circumference),end="  ")
print("s1.area={:^4}".format(s1.area))

s1.circumference=16  #改变周长
print("s1.length={:^4}".format(s1.length),end="  ")
print("s1.circumference={:^4}".format(s1.circumference),end="  ")
print("s1.area={:^4}".format(s1.area))

s1.area=25  # 改变面积
print("s1.length={:^4}".format(s1.length),end="  ")
print("s1.circumference={:^4}".format(s1.circumference),end="  ")
print("s1.area={:^4}".format(s1.area))


