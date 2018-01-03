# -*- coding: utf-8 -*-
# Python 3.6.3
"""
1.输入任意一个字符串或数字，判断是否为回文
  12321    回文数
  ABCDCBA  回文
  GEAEG    回文
  abeeba   回文
"""

str=input("判断是否为回文（输入0结束）？\n任意输入一个字符串或数字：")
begin=0
end=len(str)-1
for i in range(len(str)):
    begin=i
    if str[begin]==str[end]:
        end-=1
    else:
        break
if begin<end:
    print("%s不是回文" %str)
else:
    print("%s是回文" %str)



