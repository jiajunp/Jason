#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 18:09
# @Author  : Jason
# @Site    : 
# @File    : statistics_analyze.py
# @Software: PyCharm

from __future__ import  print_function

import  pandas as pd

catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale,index_col=u'日期')
data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)]
statistics = data.describe() #保存基本统计量

statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%'] #四分位数间距

print(statistics)