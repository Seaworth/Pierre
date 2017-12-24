# -*- coding: utf-8 -*-
# Python 2.7.14
'''
练习:
1.北京出租车计价器:
  收费标准:
      3公里以内收费13元
      基本单价 2.3元公里(超出3公里以外)
      空驶费: 超过15公里后，每公里加收单价的50%
  　　　　(部分算法)
  要求：输入公里数，打印出费用金额
'''
distance=float(input('please input your ride distance(km):'))
if distance<=3:  # 3公里以内收费13元
    print 'your ride distance is %.1f km' %distance
    print 'your ride costs is 13 yuan'
elif 3<distance<=15:  # 基本单价 2.3元公里(超出3公里以外)
    print 'your ride distance is %.1f km' % distance
    print 'your ride costs is %.1f yuan' %(13+(distance-3)*2.3)
else:  # 超过15公里后，每公里加收单价的50%
    print 'your ride distance is %.1f km' % distance
    print 'your ride cost is %.1f yuan' %(13+12*2.3+1.5*2.3*(distance-15))





