# -*- coding: utf-8 -*-
# Python 3.6.3
"""
练习3：
  输入三行文字 ,让这三行文字在一个方框内居中显示
  如输入(不要输入中文):
  hello tarena!
  my name is weimingze！
  good-bye
  显示结果如下：
+-----------------------+
|     hello tarena!     |
| my name is weimingze! |
|        good-bye       |
+-----------------------+
"""
my_string1=input("please input string1:")
my_string2=input("please input string2:")
my_string3=input("please input string3:")
str_len=0
if len(my_string1)>len(my_string2):
    if len(my_string3) > len(my_string1):
        str_len = len(my_string3)
    else:
        str_len = len(my_string1)
else:
    if len(my_string3) > len(my_string2):
        str_len = len(my_string3)
    else:
        str_len = len(my_string2)
str_len+=4
for raw_1 in range(str_len):  # 打印第一行
    if raw_1==0 or raw_1==(str_len-1):
        print("+",end="")
    else:
        print("-",end="")
print("")

for raw_2 in range(str_len):  # 打印第2行
    if raw_2==0 or raw_2==(str_len-1):
        print("|",end="")
        if raw_2==0:
            for i in my_string1.center(str_len-2," "):
                print(i,end="")
print("")

for raw_3 in range(str_len):  # 打印第3行
    if raw_3==0 or raw_3==(str_len-1):
        print("|",end="")
        if raw_3==0:
            for i in my_string2.center(str_len-2," "):
                print(i,end="")
print("")

for raw_4 in range(str_len):  # 打印第4行
    if raw_4==0 or raw_4==(str_len-1):
        print("|",end="")
        if raw_4==0:
            for i in my_string3.center(str_len-2," "):
                print(i,end="")
print("")

for raw_5 in range(str_len):  # 打印第5行
    if raw_5==0 or raw_5==(str_len-1):
        print("+",end="")
    else:
        print("-",end="")
print("")
