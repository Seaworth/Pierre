# -*- coding: utf-8 -*-
# Python 3.6.3
"""
练习：
  输入任意整数,先判断你输入的数是否为质数(只能被1和自身整除的数),
  如果为质数，则加入到列表中.再次输入任意整数，再判断.......
  直至输入的数小于等于0为止。
  最后打印您输入的质数。
  (所用知识点：输入输出，死循环，求余，for, range,列表...)
"""
prime_num=[]
while 1:
    str_1=input("请输入任意整数（输入0停止）：")
    num=int(str_1)
    if num==0:
        break
    else:
        a=1
        for i in range(2,num):  # 用2到num-1的数去除，如果能够被整除就跳出循环
            a=i
            if num%i==0:
                break
        if a==num-1:  # 如果跳出循环后的值时等于num-1的则是质数
            if num!=1:
                prime_num.append(num)
print("输入的质数有：")
for i in prime_num:
    print(i," ",end='')


