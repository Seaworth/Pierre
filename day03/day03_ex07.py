# -*- coding: utf-8 -*-
# Python 2.7.14
"""
  1. 打印1~10奇数
  2. 打印1~10偶数
  用for 语句
  3. 算出 100 ~1000之间的水仙花数(Narcissistic number)
     水仙花是指百位的立方+ 十位的立方 + 个位的立方等于原数的数字
     例:
        153 等于 1**3 + 5**3 + 3**3
     答案: 153 370 371 407
"""
print "打印1~10奇数:",
for i in range(1,11,2):
    print i,
print ""

print "打印1~10偶数:",
for i in range(2,11,2):
    print i,
print ""

print "打印100~1000的水仙花数:",
for i in range(100,1000):
    ge=i%10  # 获得个位
    shi=(i//10)%10  # 获得十位
    bai=i//100  # 获得百位
    if i==ge**3+shi**3+bai**3:
        print i,
print ""
"""
  1.打印1~20之间的整数,打印在一行显示，每个数字之间用一个空格分隔
    1 2 3 4 5 6 7 8 9 ... 18 19 20
  2. 打印1~20之间的整数,每行打印5个数字，打印四行,如：
    1 2 3 4 5
    6 7 8 9 10
    11 12 ...
    .....
"""

print "打印1~20之间的整数:",
for i in range(1,21):
    print i,
print ""

print "打印1~20之间的整数，每行打印5个数字:"
for i in range(1,21):
    print "%2d" %i,
    if i%5==0:
        print ""