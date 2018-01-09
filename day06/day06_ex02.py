# -*- coding: utf-8 -*-
# Python 3.6.3
"""
  写一个函数sum4(a,b,c,d) 来计算四个参数的和
  可以用如下方法调用：
  print(sum4(1, 2))
  print(sum4(1.1,2.2, 3.3))
  print(sum4(100, 200, 300, 400))
"""
def sum4(a,b,c=.0,d=.0):
    return a+b+c+d
print(sum4(1,2))
print(sum4(1.1,2.2,3.3))
print(sum4(100,200,300,400))
