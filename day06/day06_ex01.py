# -*- coding: utf-8 -*-
# Python 3.6.3
def hello():
    print("hello python")

def hellon(n):
    while n:
        print("hello world")
        n-=1
def add(a,b):
    return a+b

hello()
hellon(3)
x=add(10,5)
print(x)

"""
定义两个函数:
   sum3(a, b, c) 用于返回三个数的和
   pow3(x)    用于返回x的三次方(立方)
   用以上两个函数计算：
   　1. 计算1的立方＋２的立方＋３的立方的和
     2. 计算1+2+3的和的立方
"""
def sum3(a,b,c):
    return a+b+c

def pow3(x):
    return x*x*x

y1=pow3(1)+pow3(2)+pow3(3)
y2=pow3(sum3(1,2,3))
print("1^3+2^3+3^3={}".format(y1))
print("(1+2+3)^3={}".format(y2))