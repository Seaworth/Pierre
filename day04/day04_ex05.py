# -*- coding: utf-8 -*-
# Python 3.6.3
"""----------------
version 1.0
coding by seaworth
----------------"""
# 练习5：
# 	判断一个字符串是否回文？
# 	a="123456789987654321"
a="123456789987654321"
len_a=len(a)
i=0
j=len_a-1
while i<len_a and a[i]==a[j]:
    i+=1
    j-=1
if i<j:
    print("%s不是回文" %a)
else:
    print("%s是回文" %a)


