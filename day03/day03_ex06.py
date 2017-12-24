# -*- coding: utf-8 -*-
# Python 2.7.14
"""
  任意输入一个字符串,计算要输入的字符'a'的个数，并打印出来
  例如:
  请输入: abcdabcabazzzzzz
  打印 4
"""
print "请任意输入一个字符串：",
my_str=raw_input()
count=0
for i in my_str:
    if i == 'a':
        count+=1
print "'%s'中有%d个'a'" %(my_str,count)


