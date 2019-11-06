#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 16:44
# @Author  : Jason
# @Site    : 
# @File    : lagrange_newton_interp.py
# @Software: PyCharm

#拉格朗日插值

import  pandas as pd

from scipy.interpolate import  lagrange #导入拉格朗日函数

inputfile = 'data/catering_sale.xls'
outputfile = 'tmp/sales.xls'


data = pd.read_excel(inputfile)
print(data)
#data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None #过滤异常值，将其变为空值
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None

def ployinterp_column(s,n,k=5):
    y = s[list(range(n - k,n)) + list(range(n+1,n+1+k))]
    y = y[y.notnull()] #剔除空值

    return lagrange(y.index,list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: #如果为空即插值
            data[i][j] = ployinterp_column(data[i],j)

data.to_excel(outputfile) #输出结果，写入文件