# -*- coding: utf-8 -*-
# Python 3.6.3
"""
集合练习：
  经理有: 曹操 刘备 周瑜
  技术员有: 曹操 周瑜，张飞，赵云
  用集合求:
  1.即是经理也是技术员的人有谁？
  2.是经理，但不是技术员的人都有谁？
  3.是技术员，但不是经理的人有谁？
  4.张飞是经理吗？
  5.身兼一职的人都有谁？
  6.经理和技术员共有几个?
"""
manager={"曹操","刘备","周瑜"}
technician={"曹操","周瑜","张飞","赵云"}
print("1.即是经理也是技术员的人有谁？{}".format(manager&technician))
print("2.是经理，但不是技术员的人都有谁？{}".format(manager-technician))
print("3.是技术员，但不是经理的人有谁？{}".format(technician-manager))
print("4.张飞是经理吗？{}".format("张飞" in manager))
print("5.身兼一职的人都有谁？{}".format(manager^technician))
print("6.经理和技术员共有几个？{}".format(len(manager|technician)))