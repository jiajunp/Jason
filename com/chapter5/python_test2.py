#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 8:16
# @Author  : Jason
# @Site    : 
# @File    : python_test2.py
# @Software: PyCharm

import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt


ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2019'),periods=1000)

ts = ts.cumsum()
ts.plot()
plt.figure()
plt.show()