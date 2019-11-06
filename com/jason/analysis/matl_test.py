#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 14:52
# @Author  : Jason
# @Site    : 
# @File    : matl_test.py
# @Software: PyCharm

import  numpy as np
import  matplotlib.pyplot as plt

x = np.linspace(0,10,1000) #作图的变量自变量
y = np.sin(x) + 1
z = np.cos(x**2) + 1

plt.figure(figsize = (8,4)) #设置图像大小
plt.plot(x,y,label = '$\sin x+1$',color='red',linewidth=2) #作图、设置标签、线条颜色、线条大小
plt.plot(x,z,'b--',label = '$\cos x^2+1$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Example')
#plt.legend() #显示图例
plt.show()