#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day08_ex03.py
@time: 2018/1/7 22:54
"""
# 练习：
# 　　创建一个车类(Car)类
#   车有属性:
#     品牌 brand
#     型号 model
#     颜色　color
#   车的方法有:
#     run(speed)       # 以多少公里的速度行驶
#     infos()          # 显示信息
#     change_color(c)  #改变颜色
class Car:
    def __init__(self,color,brand,model):
        self.color=color
        self.brand=brand
        self.model=model
    def run(self,speed):
        self.speed=speed
        print("{}{}{}正在以{}km/h的速度行驶".format(self.color,self.brand,self.model,self.speed))
    def infos(self):
        print("{}{}{}正在以{}km/h的速度行驶".format(self.color, self.brand, self.model, self.speed))
    def change_color(self,new_color):
        self.color=new_color
a4 = Car("红色", "奥迪", "A4")
a4.run(199)  # 红色奥迪A4正在以199km/h的速度行驶
a4.change_color("黑色")
a4.run(230)  # 黑色奥迪A4正在以230km/h的速度行驶


