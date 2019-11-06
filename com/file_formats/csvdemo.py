#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 16:02
# @Author  : Jason
# @Site    : 
# @File    : csvdemo.py
# @Software: PyCharm

import  csv
print(dir(csv))

with open('eggs.csv','w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
