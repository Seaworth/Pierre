# -*- coding: utf-8 -*-
# Python 3.6.3
import copy
class_list={"Benjen","Brandon","Sansa","Arya","Summer","Tyrion","Drogo","Jon","Bronn","Seaworh"}
absent_list=set()
for i in class_list:
    x=input("{:^8}到了么？输入'y'代表已到,输入'n'代表未到：".format(i))
    if x=='n':
        absent_list.add(copy.deepcopy(i))
print("未到课的同学有：")
for j in absent_list:
    print(j,end=" ")

