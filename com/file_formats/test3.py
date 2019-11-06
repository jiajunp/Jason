#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 16:18
# @Author  : Jason
# @Site    : 
# @File    : test3.py
# @Software: PyCharm


from multiprocessing  import  Process,Lock
from multiprocessing.sharedctypes import  Value,Array
from ctypes import  Structure,c_double

class Point(Structure):
    _fields_ = [('x',c_double),('y',c_double)]



if __name__ == '__main__':
    lock = Lock()
    n = Value('i',7)
    x = Value(c_double,1.0/3.0,lock = False)
    s = Array('c',b'hello world' ,lock = lock)
    A = Array(Point,[(1.875,-6.25),(-5.75,2.0)])
