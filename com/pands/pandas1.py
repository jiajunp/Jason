#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 14:14
# @Author  : Jason
# @Site    : 
# @File    : pandas1.py
# @Software: PyCharm

import  pandas as  pd
import  numpy as np


frame = pd.DataFrame(np.random.randn(10000,5),
                     columns=['a','b','c','d','e'])

frame.iloc[::2] = np.nan

print(frame.describe())

s = pd.Series(['a','a','b','b','a','a',np.nan,'c','d','a'])

print(s.describe())