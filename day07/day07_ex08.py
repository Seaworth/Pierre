#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex08.py
@time: 2018/1/6 16:35
"""
# 改写之前学生信息的程序
#     每个人的信息有:
#       姓名:name
#       年龄:age
#       成绩:score
#     输入5个学生的信息.然后做如下操作:
#     1)按成绩从高至低打印学生信息
#     2)按年龄从高至低打印学生信息
#     3)按年龄从低至高打印学生信息
#     4)按原来输入顺序打印学生信息(要保持原列表不变)
import copy  # 使用copy模块进行深拷贝，拷贝对象及其子对象

d={"name":"zhangsan","age":"18","score":"0"}
max=8  # 学生姓名长度的最大值
l=[]   # 总的学生信息列表
for i in range(1,6): # 手动输入5位学生的名字和年龄
    str_1=input("请输入第{}位学生的名字：".format(i))
    d["name"]=str_1
    if len(str_1)>max:
        max=len(str_1)+2
    str_2=input("请输入第{}位学生的年龄：".format(i))
    d["age"]=str_2
    str_3 = input("请输入第{}位学生的成绩：".format(i))
    d["score"] = str_3
    l.append(copy.deepcopy(d))  # 需要拷贝对象，而不是只拷贝引用
    # print(l)

name_str="name"
age_str="age"
score_str="score"
# 格式化输出
print("1)按成绩从高至低打印学生信息")
l1=sorted(l,key=lambda x:int(x["score"]),reverse=True)
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
print("|"+name_str.center(max," ")+"|"+age_str.center(max," ")+"|"+score_str.center(max," ")+"|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
for i in range(len(l1)):
    print("|" + l1[i]["name"].center(max, " ") +
          "|" + l1[i]["age"].center(max, " ") +
          "|"+ l1[i]["score"].center(max, " ") + "|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")

print("2)按年龄从高至低打印学生信息")
l2=sorted(l,key=lambda x:int(x["age"]),reverse=True)
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
print("|"+name_str.center(max," ")+"|"+age_str.center(max," ")+"|"+score_str.center(max," ")+"|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
for i in range(len(l2)):
    print("|" + l2[i]["name"].center(max, " ") +
          "|" + l2[i]["age"].center(max, " ") +
          "|"+ l2[i]["score"].center(max, " ") + "|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")

print("3)按年龄从低至高打印学生信息")
l3=sorted(l,key=lambda x:int(x["age"]),reverse=False)
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
print("|"+name_str.center(max," ")+"|"+age_str.center(max," ")+"|"+score_str.center(max," ")+"|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
for i in range(len(l3)):
    print("|" + l3[i]["name"].center(max, " ") +
          "|" + l3[i]["age"].center(max, " ") +
          "|"+ l3[i]["score"].center(max, " ") + "|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")

print("4)按原来输入顺序打印学生信息")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
print("|"+name_str.center(max," ")+"|"+age_str.center(max," ")+"|"+score_str.center(max," ")+"|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")
for i in range(len(l)):
    print("|" + l[i]["name"].center(max, " ") +
          "|" + l[i]["age"].center(max, " ") +
          "|"+ l[i]["score"].center(max, " ") + "|")
print("+"+"-"*max+"+"+"-"*max+"+"+"-"*max+"+")

