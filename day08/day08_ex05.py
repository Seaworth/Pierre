#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day08_ex05.py
@time: 2018/1/8 22:13
"""
# 2.修改学生管理程序, 用来对象存储学生信息.
#     每个学生有infos()方法, 用于显示学生信息
class Student:
    """
    这是一个学生的定义
    """
    class_list=[]
    def __init__(self,name="Tom",age=18,score=0):
        self.name=name
        self.age=age
        self.score=score
        self.max=len(name)+2
        self.str1="name"
        self.str2="age"
        self.str3="score"
    def infos(self):
        # 格式化输出
        print("+" + "-" * self.max + "+" + "-" * self.max + "+" + "-" * self.max + "+")
        print("|" + self.str1.center(self.max, " ") +
              "|" + self.str2.center(self.max, " ") +
              "|" + self.str3.center(self.max, " ") + "|")
        print("+" + "-" * self.max + "+" + "-" * self.max + "+" + "-" * self.max + "+")
        print("|" + self.name.center(self.max, " ") +
              "|" + str(self.age).center(self.max, " ") +
              "|"+  str(self.score).center(self.max, " ") + "|")
        print("+" + "-" * self.max + "+" + "-" * self.max + "+" + "-" * self.max + "+")
L = []
for i in range(5):
    n = "Alice"
    a = 20
    s = 95
    stu = Student(n, a, s)
    L.append(stu)

for j in range(5):
    L[j].infos()




