# -*- coding: utf-8 -*-
# Python 2.7.14
"""
  1. 打印 1~20的偶数
  2. 打印 1~20的奇数
  3. 打印 1~10的数,打印在一行显示，每个数字用空格分隔
      1 2 3 4 5 6 7 8 9 10
      提示: 用print函数的end参数

  4. 用while循环生成如下字符串:
    "ABCD.....XYZ"
  5. 用while循环生成如下字符串
    "AaBbCcDd....XxYyZz"
"""
print "打印 1~20的偶数:",
a=2
while a<=20:
    print "%2d" %a,
    a+=2
print ""

print "打印 1~20的奇数:",
b=1
while b<=20:
    print "%2d" %b,
    b+=2
print ""

print "打印 1~10的数:  ",
c=1
while c<=10:
    print "%2d" %c,
    c+=1
print ""

print "打印 A~Z的26个字母:  ",
letter=65
while letter<=90:
    print "%-2c" %chr(letter),
    letter+=1
print ""

print "打印 Aa~Zz的52个字母:",
upper_letter=65  # A的ASCII码
lower_letter=97  # a的ASCII码
while upper_letter<=90:  # Z的ASCII码:90
    print "%c%c" %(chr(upper_letter),chr(lower_letter)),
    upper_letter+=1
    lower_letter+=1
