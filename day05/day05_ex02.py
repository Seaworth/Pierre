# -*- coding: utf-8 -*-
# Python 3.6.3
"""
1. 生成前40个斐波那契数
  1 1 2 3 5 8 ......
  要求将这些数保存在列表中。最后打印这些数
  提示：用 while,for , 序列
"""
fib_num=[1,1]
i=2
while i<40:
    i_num=fib_num[i-1]+fib_num[i-2]  # 生成前40个斐波那契数列
    fib_num.append(i_num)
    i=i+1
print("前40个斐波那契数：")
for x in range(0,len(fib_num)):  # 打印前40个斐波那契数列
    print("%9d" %fib_num[x],end=",")
    if (x+1)%10==0:
        print()