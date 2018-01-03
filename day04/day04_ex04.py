# -*- coding: utf-8 -*-
# Python 3.6.3
"""----------------
version 1.0
coding by seaworth
----------------"""
# 练习4:
# 输入Unicode 的起始编码和终止编码,打印此范围内所有的字符。
start_num=int(input("请输入Unicode的起始编码："))
end_num=int(input("请输入Unicode的终止编码："))

while start_num<=end_num:
    print("十进制编码","十六进制编码","文字")
    print("%s%s%s" %(str(start_num).center(9," "),
                     oct(start_num).center(13," "),
                     chr(start_num).center(4," ")))
    start_num+=1



