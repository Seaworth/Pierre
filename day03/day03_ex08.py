# -*- coding: utf-8 -*-
# Python 2.7.14
"""
打印一颗圣诞树~~~
3. 输入一个整数(代表树干的高度) 打印如下一棵树,如输入
输入:2
 *
***
 *
 *
"""
print "Please enter the height of the Christmas tree:",  # 提示用户输入圣诞树的高度
height=int(raw_input())  # 用户输入字符数
space_num=height-1  # 打印的空格数量
star_num=1  # *的初始值
# ================打印树枝======================
for i in range(1,height+1):  # 打印height行
    for j in range(space_num):  # 先打印每一行的空格
        print " ",
    space_num -= 1  # 下一行的空格减1
    for k in range(star_num):   # 再打印每一行的*号
        print "*",
    star_num+=2  # 下一行的*号加2
    print ""  #每打印完一行，换行
space_num=height-1
star_num=1
# ================打印树干======================
for i1 in range(1,height+1):
    for j1 in range(space_num):  # 先打印每一行的空格
        print " ",
    for k1 in range(star_num):   # 再打印每一行的*号
        print "*",
    print ""  #每打印完一行，换行