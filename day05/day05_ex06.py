# -*- coding: utf-8 -*-
# Python 3.6.3
"""
2. 编写程序，获取一个数值，计算并打印其中每个数字出现个数
如：输入:2234524
打印如下：
  数字2出现3次
  数字3出现1次
  数字4出现2次
  数字5出现1次
"""
str=input("请输入一个数值：")
t=tuple(str)
for i in range(len(t)):
    if t[i] not in t[0:i]:  # 如果当前的数字不在以前遍历过的元组中，则打印
        print("数字%s出现%s次" %(t[i],t.count(t[i])))