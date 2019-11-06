#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 16:21
# @Author  : Jason
# @Site    : 
# @File    : test1.py
# @Software: PyCharm


import  matplotlib.pyplot as plt
import  numpy as np
import pandas as pd

x = np.random.randn(1000)
D = pd.DataFrame([x,x+1]).T
D.plot(kind='box')
plt.show()


