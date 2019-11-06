#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 16:27
# @Author  : Jason
# @Site    : 
# @File    : test2.py
# @Software: PyCharm

import  matplotlib.pyplot as plt
import  numpy as np
import  pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

error = np.random.randn(10)
y = pd.Series(np.sin(np.arange(10)))
y.plot(yerr = error)
plt.show()