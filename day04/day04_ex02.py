# -*- coding: utf-8 -*-
# Python 3.6.3
"""
	2，把该字符串中的单词顺序逆序。
		例如：a="This is a pig"
		逆序：a="pig a is This"
"""
my_string1="This is a pig"
my_string2=my_string1.split()  # 分解为一个个单词
new_string=""
for i in my_string2[::-1]:  # 将一个个单词反向连接
    new_string=new_string+i+" "
new_string=new_string[:-1]  # 删掉末尾的一个空格
print(my_string1+"\n"+new_string)

