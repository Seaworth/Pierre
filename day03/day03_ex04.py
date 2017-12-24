# -*- coding: utf-8 -*-
# Python 2.7.14
"""
输入一个数，求这个数的绝对值
"""
print "请输入一个数：",
x=input()
x = x if x>0 else -x  # 等同于 x=abs(x)
print "x={}".format(x)


