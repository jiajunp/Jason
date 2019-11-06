#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:21
# @Author  : Jason
# @Site    : 
# @File    : JCP011.py
# @Software: PyCharm

'''
将一个正整数分解质因数
'''

from sys import  stdout
n = int(input("input number:\n"))
print("n = %d" %n)

for i in range(2,n + 1):
    while n != i :
        if n % i == 0:
            stdout.write(str(i))
            stdout.write("*")
            n = n / i
        else:
            break

print("%d " %n)