#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 17:10
# @Author  : Jason
# @Site    :
# @File    : data_exploration.py
# @Software: PyCharm


import pandas as pd
import  numpy as np
import  seaborn as sns
import  matplotlib as mpl

import  matplotlib.pyplot as plt
from IPython.display import  display


plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Jason']})

from sys import  version_info
if version_info.major != 3:
    raise  Exception('请使用Python 3 来完成此项目')


lian_df = pd.read_csv('600508.csv', encoding = 'gb2312')
lian_df.info()
display(lian_df.head(n=3))

df = lian_df.copy()

df['PerPrice'] = lian_df['收盘价']-lian_df['开盘价']
columns = ['日期', '股票代码', '名称', '收盘价', '最高价', '最低价', '开盘价', '前收盘', '涨跌额', '涨跌幅', '换手率', '成交量','成交金额','总市值','流通市值','PerPrice']
df = pd.DataFrame(df, columns = columns)

display(df.head(n=2))




