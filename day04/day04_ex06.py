# -*- coding: utf-8 -*-
# Python 3.6.3
"""----------------
version 1.0
coding by seaworth
----------------"""
# 练习6：
# 	查找两个字符串的最长公共子串。
# 	a="123456789"
# 	b="123312345612345678"
# 	“12345678”
# 	逻辑里一定用到三层循环！！！
str_1="123456789"
str_2="123123456123456784657985138123456789"
print("str_1=%s" %str_1)
print("str_2=%s" %str_2)
begin=[]  # 记录每次开始比较的下标
end=[]    # 记录每次结束比较的下标
for i in range(len(str_1)):  # str_1不动，用str_2逐个比较str_1
    for j in range(len(str_2)):
        begin.append(i)      # 将开始比较的下标放在列表begin
        i1=i
        j1=j
        while i1<len(str_1) and j1<len(str_2) and str_1[i1]==str_2[j1]:  # 如果i1和j1下标对应的字符相等，继续循环比较下一个字符，
                                                                         # 直到不相等或遍历到str_1,str_2的字符串的末尾
            i1+=1
            j1+=1
        end.append(i1)      # 将结束比较的下标放在end列表中
L=[]  #用来存放公共子串的长度
for i in range(0,len(end)):
    sub=end[i]-begin[i]
    L.append(sub)

max=max(L)  # 找出最大的公共子串，存放在max中
for k in range(len(L)):
    if L[k]==max:
        print("最大公共子串：%s" %str_1[begin[k]:end[k]])
        break

