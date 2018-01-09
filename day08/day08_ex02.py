#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day08_ex02.py
@time: 2018/1/7 22:43
"""
# 自己定义一个类Human(人类)
#   有两个属性:
#     姓名(name)
#     年龄(age)
#   有三个方法:
#     设置姓名(setName)  # 添加和修改姓名
#     设置年龄(setAge)   # .....
#     显示信息(infos)    # 显示人的信息
# 用此类来创建两个对象:
#     张三,20岁
#     李四,21岁
# 调用方法设置和显示信息

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setName(self,new_Name):
        self.name=new_Name
    def setAge(self,new_age):
        self.age=new_age
    def infos(self):
        print("你好，我的名字是{}，今年{}岁！".format(self.name,self.age))
person1=Human("张三",20)
person2=Human("李好",21)
person1.infos()
person2.infos()

person1.setName("张三丰")
person1.setAge(100)
person1.infos()

person2.setName("李好帅")
person2.setAge(200)
person2.infos()