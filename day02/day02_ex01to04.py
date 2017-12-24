# -*- coding: utf-8 -*-
# Python 2.7.14

# 练习1：输入一个五位数，把每一位的数求出
print '------------------------------------'
print '输入一个五位数，把每一位的数求出'

num=12345
num1=num%10
num2=(num//10)%10
num3=(num//100)%10
num4=(num//1000)%10
num5=(num//10000)%10
print 'num=%d' %num
print '个:',num1,'十:',num2,'百:',num3,'千:',num4,'万:',num5
# 练习1：输入一个五位数，把每一位的数求出over

print '------------------------------------'
# 练习2:改写圆的周长和面积的计算用变量代替某些值
radius=4
pi=3.14
print 'the radius of circle is %d' %radius  # 半径
print 'the circumference of circle is %.2f' %(2*pi*radius)  # 周长
print 'the area of circle is %.2f' %(pi*radius*radius)  # 面积
# 练习2：改写圆的周长和面积的计算用变量代替某些值over

print '------------------------------------'
# 练习3：
# 从凌晨0:0:0　计时，到现在已经过了63320秒
# 请问，现在是几时,几分，几秒,写程序打印出来
total_time=63320
second_num=63320%60
minute_num=(63320//60)%60
hour_num=(63320//60)//60
print 'now is {}hour:{}minute:{}second'.format(hour_num,minute_num,second_num)
# 练习3 over

print '------------------------------------'
'''
练习4：在终端输出图形:
   *
  ***
 *****
*******
'''
print 'Merry Christmas!'
print '   *'
print '  ***'
print ' *****'
print '*******'
print '   *'
# 练习4 over


