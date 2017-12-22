# -*- coding: utf-8 -*-
# Python 2.7.14
# 练习5：
#   分三次输入当前的小时，分钟和秒数
#   打印此时距离0:0:0已过了多少秒
hour_num=int(input('please input hour now:'))
minute_num=int(input('please input minute now:'))
second_num=int(input('please input second now:'))
second_total=hour_num*3600+minute_num*60+second_num
print '此时距离0:0:0已过了{}秒'.format(second_total)
# 练习5 over


