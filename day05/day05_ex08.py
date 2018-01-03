# -*- coding: utf-8 -*-
# Python 3.6.3
"""
　　输入5个学生的姓名和年龄，每个学生的信息形成字典后存入列表，内部存储格式如下：
  [{"name":"aaa", "age": 20}, {"name":"bbb", "age": 30}, ...]
  输入完成后，打印所有学生信息如下：
  +-------------+-------------+
  |    name     |     age     |
  +-------------+-------------+
  |     aaa     |    20       |
  |     bbb     |    30       |
  |     ...     |    ...      |
  +-------------+-------------+
"""
# st_1={"name":"lizhijun","age":"22"}
# st_2={"name":"liwei","age":"21"}
# st_3={"name":"liyejue","age":"23"}
# st_4={"name":"hecangpeng","age":"24"}
# st_5={"name":"liangpei","age":"26"}
import copy  # 使用copy模块进行深拷贝，拷贝对象及其子对象

d={"name":"zhangsan","age":"18"}
max=8  # 学生姓名长度的最大值
l=[]   # 总的学生信息列表
for i in range(1,6): # 输入5位学生的名字和年龄
    str_1=input("请输入第{}位学生的名字：".format(i))
    d["name"]=str_1
    if len(str_1)>max:
        max=len(str_1)+2
    str_2=input("请输入第{}位学生的年龄：".format(i))
    d["age"]=str_2
    l.append(copy.deepcopy(d))  # 需要拷贝对象，而不是只拷贝引用
    # print(l)

name_str="name"
age_str="age"
# 格式化输出
print("+"+"-"*max+"+"+"-"*max+"+")
print("|"+name_str.center(max," ")+"|"+age_str.center(max," ")+"|")
print("+"+"-"*max+"+"+"-"*max+"+")
for i in range(len(l)):
    print("|" + l[i]["name"].center(max, " ") + "|" + l[i]["age"].center(max, " ") + "|")
print("+"+"-"*max+"+"+"-"*max+"+")

"""
输入学生年龄，把低于此年龄的学生信息打印出来
知识点:
  列表和字典组合使用
"""
in_age=input("请输入学生年龄，并打印低于此年龄的学生信息打印出来：")
for i in range(len(l)):
    if l[i]["age"]<in_age:
        print("name={:^8},age={:^4}".format(l[i]["name"],l[i]["age"]))


