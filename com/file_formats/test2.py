#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 16:12
# @Author  : Jason
# @Site    : 
# @File    : test2.py
# @Software: PyCharm

from multiprocessing import  Pool
from multiprocessing import  Process

def f2(nane):
    print("hello",nane)

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f,[1,2,3]))

    p = Process(target=f2,args=('bbb',))
    p.start()
    p.join()
