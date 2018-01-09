#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex10.py
@time: 2018/1/9 11:20
"""
# 3. 写函数打印杨辉三角(只打印6层)
import copy
def Triangles(n=6):
    total_list=[[1]]
    for i in range(1,n): # 打印第2层到第n层
        total_list.append([(0 if j==0 else total_list[i-1][j-1])+(0 if j==i else total_list[i-1][j]) for j in range(i+1)])
    return total_list
l=Triangles(6)
for i in range(6):
    for j in range(i+1):
        print(l[i][j],end=" ")
    print()

