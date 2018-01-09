#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day08_ex01.py
@time: 2018/1/7 22:06
"""
# 1. 自己写一个类Student, 此类的对象有属性name,age,score 用来保存学生的姓名,年龄,成绩,
# 用input读入5个学生关相信息,用对象来存储这些信息(不用字典), 打印五个学生信息
class Student:
    """
    这是一个学生的定义
    """
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
s1=Student("s1_name",0,0)
s2=Student("s2_name",0,0)
s3=Student("s3_name",0,0)
s4=Student("s4_name",0,0)
s5=Student("s5_name",0,0)
class_list=[s1,s2,s3,s4,s5]
for i in range(5):
    numi=i+1
    class_list[i].name = input("请输入第{}个学生的姓名：".format(numi))
    class_list[i].age = int(input("请输入第{}个学生的年龄：".format(numi)))
    class_list[i].score = int(input("请输入第{}个学生的分数：".format(numi)))
print("打印学生信息：")
for j in range(5):
    numj=j+1
    print("第{}个学生的姓名是{}".format(numj,class_list[j].name),end=",")
    print("第{}个学生的年龄是{}".format(numj,class_list[j].age),end=",")
    print("第{}个学生的分数是{}".format(numj,class_list[j].score))

