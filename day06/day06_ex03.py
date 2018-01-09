# -*- coding: utf-8 -*-
# Python 3.6.3
"""
  写一个函数min_max有不定长个参数,返回这些参数的最大值和最小值(形成元组,最小在前,最大值在后)
  调用此函数,得到最大值和最小值并打印出来
"""

def min_max(*args):
    print("实参的个数是{}".format(len(args)))
    print(tuple(sorted(args,reverse=True)))
    print("最大值是{}，最小值是{}".format(sorted(args,reverse=True)[0],sorted(args,reverse=True)[-1]))
    return None
min_max(5,2,10,4,60,7,34)

