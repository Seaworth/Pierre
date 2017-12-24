# -*- coding: utf-8 -*-
# Python 2.7.14
"""
  用字符串 * 运算符打印三角形
    要求输入一个整数，此整数代表此三角形离左侧的字符数
  $ python3 tri_angle.py
  请输入离左侧的距离: 3
      *
     ***
    *****
   *******
"""
print "please input the number of characters to the left of the triangle:",  # 提示用户输入三角形离左侧的字符数
num=int(raw_input())  # 用户输入字符数
raw=num+1  # 打印的行数
space_num=num  # 打印的空格数量
star_num=1  # *的初始值
for i in range(1,raw+1):  # 打印raw行
    for j in range(space_num):  # 先打印每一行的空格
        print " ",
    space_num -= 1  # 下一行的空格减1
    for k in range(star_num):   # 再打印每一行的*号
        print "*",
    star_num+=2  # 下一行的*号加2
    print ""  #每打印完一行，换行




