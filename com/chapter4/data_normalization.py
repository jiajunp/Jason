#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 16:45
# @Author  : Jason
# @Site    : 
# @File    : data_normalization.py
# @Software: PyCharm

import  pandas as pd
import  numpy as np

datafile = 'data/normalization_data.xls'

data = pd.read_excel(datafile,header = None)

(data - data.min()) / (data.max() - data.min())
(data - data.mean()) / data.std()

data/10**np.ceil(np.log10(data.abs().max()))

print(data)