# -*- coding: utf-8 -*-
# Python 3.6.3
"""
  prime(质数/素数)  可以优化
  1. 写一个函数is_prime(x),判断x是否为素数,如果为素数,返回True,否则返回False.

  2. 写一个函数prime_m2n(m, n) 返回从m开始,到n结束范围内的素数,返回这些质数的列表,并在主程序中打印
  如:
    L = prime_m2n(5, 10)
    print(L)  # [5, 7]

  3. 写一个函数primes(n), 返回指定范围内的全部素数的列表,并在主程序中打印这些素数
    L = primes(100)
    print(L)  # [2, 3, 5, 7, ....... 97]
"""
def is_prime(x):
    a=-2
    for i in range(2,x):
        a=i
        if x%i==0:
            break
    if a==x-1 or x==2:
        str=True
    else:
        str=False
    return str
print(is_prime(2))
#--------------------------------
def prime_m2n(m,n):
    l=[]
    for i in range(m,n+1):
        if is_prime(i):
            l.append(i)
    return l
L=prime_m2n(5,10)
print(L)
#--------------------------------
def primes(n):
    l=[]
    for i in range(2,n+1):
        if is_prime(i):
            l.append(i)
    return l

Y=primes(100)
print(Y)
print(__doc__) # 打印第一个注释