#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 14:27
# @Author  : Jason
# @Site    : 
# @File    : structure.py
# @Software: PyCharm

def sqrt(x):
    y = 1.0
    while abs(y * y -x) > 1e-6:
        y = (y + x/y) /2
    return x







if __name__=='__main__':
    print(sqrt(5))
