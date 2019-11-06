#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 14:45
# @Author  : Jason
# @Site    : 
# @File    : analysis_test1.py
# @Software: PyCharm

from scipy.optimize import  fsolve
#导入求解方程组的函数

def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2-1,x1**2 - x2 - 2]

result = fsolve(f,[1,1]) #求解1，1

print(result)

from scipy import  integrate #导入积分函数

def g(x):
    return (1 - x**2)**0.5

pi_2,err = integrate.quad(g,-1,1) #积分结果和误差
print(pi_2*2) #由微积分知识知道积分结果为圆周率pi的一半



