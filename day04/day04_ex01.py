# -*- coding: utf-8 -*-
# Python 3.6.3
"""
练习2：
	1，完成一个函数，判断字符串中单词个数。
	2，把该字符串中的单词顺序逆序。
		例如：a="This is a pig"
		逆序：a="pig a is This"
"""
def count_words(s):
    flag=0
    if s[len(s) - 1].isalpha(): # 如果最后一个字符是字母num=1，不是字母则为0
        num = 1
    else:
        num=0
    for i in range(len(s)):  # 循环整个字符串，从出现字母到空格num加1
        if s[i].isalpha():
            flag=1
        elif s[i].isspace() and flag==1:
            num+=1
            flag=0
    return num
my_string=input("请输入一段字符串：")
print("%s 中有 %d" %(my_string,count_words(my_string)))




