#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:16
# @Author  : Jason
# @Site    : 
# @File    : JCP010.py
# @Software: PyCharm

import  sys

sys.stdout.write(chr(1))
sys.stdout.write(chr(1))

print('')

for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print('')
