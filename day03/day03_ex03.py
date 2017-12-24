# -*- coding: utf-8 -*-
# Python 2.7.14
"""
练习：
  分三次输入当前的小时，分钟和秒数
  打印此时距离0:0:0已过了多少秒
"""
print "the hour now:",
hour=int(raw_input())
print "the minute now:",
minute=int(raw_input())
print "the second now:",
second=int(raw_input())
second_total=hour*3600+minute*60+second
print "此时距离0:0:0已过了%ds" %second_total
