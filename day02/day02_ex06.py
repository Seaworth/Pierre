# -*- coding: utf-8 -*-
# Python 2.7.14
# 练习6：
# 输入一个季度1~4的数字，输出这个季度有哪几个月份。
'''
而实际上严格的划分应该为：(按照中国的纬度)
第一季度：3－5 月（春季）
第二季度：6－8 月（夏季）
第三季度：9－11月（秋季）
第四季度：12－2月（冬季）
'''
num=int(input('please input 1~4 for every season:'))
if num==1:
    print '第一季度：3－5月（春季）'
elif num==2:
    print '第二季度：6－8月（夏季）'
elif num==3:
    print '第三季度：9－11月（秋季）'
elif num==4:
    print '第四季度：12－2月（冬季）'
else:
    print ' input error! please input 1 to 4.'

# 练习6 over


