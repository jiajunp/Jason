#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 18:37
# @Author  : Jason
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

import  matplotlib.pyplot as plt

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [15,30,45,10]
colors = ['yellowgreen','gold','lightskyblue','lightcoral']
explode = (0,0.1,0,0)

plt.pie(sizes,explode = explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=True,startangle=90)

plt.axis('equal')
plt.show()

