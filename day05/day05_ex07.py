# -*- coding: utf-8 -*-
# Python 3.6.3
"""
练习：
　已知两个等长的列表list1和list2
  以list1中的元素为键，以list2中的元素为值，生成相应字典
  如:
    list1 = ["a", "b", "c"]
    list2 = [1,2,3]
    生成字典为:
      {'a':1, 'b':2, 'c' : 3}
"""
list_1=["a","b","c"]
list_2=["1","2","3"]
d={list_1[i]:list_2[i] for i in range(3)}
print("生成相应的字典为；")
for k,v in d.items():
    print("键%s--->%s" %(k,v))