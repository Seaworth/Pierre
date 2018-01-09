# -*- coding: utf-8 -*-
# Python 3.6.3
"""
　　写一个函数，在函数内部读取学生姓名，并存入列表中,通过两种方式返回学生姓名数据并打印出来
　　方式1，通过返回值返回数据
　　方式2，通过参数返回数据
"""
# class_list={"Benjen","Brandon","Sansa","Arya","Summer","Tyrion","Drogo","Jon","Bronn","Seaworh"}
import copy
def operator1():
    i=1
    L=[]
    while 1:
        name=input("请输入第{}个学生的姓名（输入0结束）：".format(i))
        if name=="0":
            break
        L.append(copy.deepcopy(name))
        i+=1
    return L

for i in operator1():
    print(i,end=",")
print("\b")  #倒退一格
print("------------------------------------")

class_list=[]
def operator2(L):
    i=1
    while 1:
        name=input("请输入第{}个学生的姓名（输入0结束）：".format(i))
        if name=="0":
            break
        L.append(copy.deepcopy(name))
        i+=1
    return None
operator2(class_list)
for i in class_list:
    print(i,end=",")
print("\b")  #倒退一格
