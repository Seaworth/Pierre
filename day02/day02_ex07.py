# -*- coding: utf-8 -*-
# Python 2.7.14
'''
if语句嵌套练习：
  季节嵌套:
  输入1~12个月,超出此范围提示不合法:
  1-3 春季
  4-6 夏季
  ....
  要求：输入月份打印季节(用if语句嵌套实现)
'''
month_num=int(input('please input 1~12 for every month:'))
if 1<=month_num<=12:
    if 1 <= month_num <= 3:
        print '1-3 春季'
    elif 4 <= month_num <= 6:
        print '4-6 夏季'
    elif 7 <= month_num <= 9:
        print '7-9 秋季'
    elif 10 <= month_num <= 12:
        print '10-12 冬季'
else:
   print 'input error!'




