# -*- coding: utf-8 -*-
# Python 3.6.3
"""
练习：
  有字符串"hello",
  生成新字符串"h e l l o" 和"h-e-l-l-o"
"""
str_1="hello"
str_2=" "
str_3="-"

seq_1=str_2.join(list(str_1))  # str_1中间用str_2空格拼接
seq_2=str_3.join(list(str_1))  # str_1中间用str_3短划线拼接
print("字符串:%s" %str_1)
print("生成新的字符串:")
for j in seq_1:
    print(j,end="")
print()
for k in seq_2:
    print(k,end="")
