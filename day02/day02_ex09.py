# -*- coding: utf-8 -*-
# Python 2.7.14
'''
2. 输入语文，数学，英文的三科成绩,打印出最高是多少，最低分是多少,平均分是多少
'''
Chinese_score=float(input('please input your chinese scores:'))
Math_score=float(input('please input your math scores:'))
English_score=float(input('please input your english scores:'))
highest_score=max(Chinese_score,Math_score,English_score)
lowest_score=min(Chinese_score,Math_score,English_score)
average_score=(Chinese_score+Math_score+English_score)/3
print 'the highest score is %.1f' %highest_score
print 'the lowest  score is %.1f' %lowest_score
print 'the average score is %.1f' %average_score
