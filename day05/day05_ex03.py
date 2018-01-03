# -*- coding: utf-8 -*-
# Python 3.6.3
"""
2. 完全数:
  完全数是指除自身以外的所有的因数相加之和等于自身的数
  例：
    1 + 2 + 3 = 6
    1,2,3都为6的因数(能被一个数x整除的数为y,则y为x的因数)
    求4~5个完全数并打印出来.
  答案（前三个)
  6
  28
  496
"""
x=2  # 从自然数2开始遍历
sum=0
perfect_num=[]
for i in range(4):
    while 1:
        sum = 0
        for j in range(1,x):
            if x%j==0:
                sum=sum+j
        if sum==x:
            perfect_num.append(x)
            x=x+1
            break
        else:
            x=x+1

print("前4个完全数为：")
for k in perfect_num:
    print(k)
