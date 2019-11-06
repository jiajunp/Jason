#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 13:56
# @Author  : Jason
# @Site    : 
# @File    : JCP001.py
# @Software: PyCharm

'''判断闰月'''

import  sys

def leap_month():
    year = int(input('year:\n'))
    month = int(input('month:\n'))
    day = int(input('day:\n'))

    months = (0,31,59,90,120,151,181,212,243,273,304,334)

    if 0 <= month <= 12:
        sum = months[month - 1]
    else:
        print("data error")
    sum += day
    leap = 0

    if(year % 400 == 0) or ((year % 4 == 0) and (year %100 != 0)):
        leap = 1
    if(leap == 1) and (month >2):
        print('it is the %dth day.' % sum)


