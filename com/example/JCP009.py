#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:04
# @Author  : Jason
# @Site    : 
# @File    : JCP009.py
# @Software: PyCharm

import  sys
for  i in range(1,10):
    for j in range(1,i):
        result = i * j
        print('%d * %d = % -3d' % (i,j,result))
    print('')