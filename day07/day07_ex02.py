#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@version: Python 3.6.3
@author: Seaworth
@software: PyCharm Community Edition
@file: day07_ex02.py
@time: 2018/1/6 12:29
"""
# 练习:
#   写一个函数，此函数有一个参数op,如下：
#       def get_op(op):
#           ...
#   此函数在传入字符串"加"，　返回加操作的函数
#     def myadd(x, y): return x + y
#   此函数在传入字符串"乘"，　返回乘操作的函数
#     def mymul(x, y): return x * y
# 　　在主函数中程序如下：
#   a = int(input("输入第一个数:"))
#   b = int(input("输入第二个数:"))
#   operator = input("请输入操作方式：")
#   fn = get_op(operator)
#   print("结果是:", fn(a, b))
#   测试用例：
#   　3
#     2
#     +<回车>
#     结果是:5
#   　
#   	3
#     2
#     *<回车>
#     结果是:6
def get_op(op):
    def my_add(x,y):
        return x+y
    def my_mul(x,y):
        return x*y
    if op=="+":
        return my_add
    elif op=="*":
        return my_mul
    else:
        print("输入错误！")


a = int(input("输入第一个数:"))
b = int(input("输入第二个数:"))
operator = input("请输入操作方式:")
fn = get_op(operator)
print("结果是{}{}{}={}".format(a,operator,b,fn(a,b)))
