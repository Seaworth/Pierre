# -*- coding: utf-8 -*-
# Python 2.7.14
"""
 5. 打印九九乘法表(循环嵌套):
   1x1=1
   1x2=2 2x2=4
   1x3=3 2x3=6 3x3=9
   .....
   1x9=9 ............
"""
print "九九乘法表"
x=1
y=1
for x in range(1,10):
    for y in range(1,x+1):
        print "{}x{}={: <2}".format(x,y,x*y),
    y+=1
    print ""


