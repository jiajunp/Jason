#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 7:44
# @Author  : Jason
# @Site    : 
# @File    : python_test.py
# @Software: PyCharm


import  pandas as pd
import  numpy as np


data = [
    {'name': 'Joe', 'state': 'NY', 'age': 18},
    {'name': 'Jane', 'state': 'KY', 'age': 19, 'hobby': 'Minecraft'},
    {'name': 'Jean', 'state': 'OK', 'age': 20, 'finances': 'good'}
]

df = pd.DataFrame(data)
#print(df)

#df = pd.SparseDataFrame({"A": [0, 0, 1, 2]})
#df.dtypes


#s = pd.Series([1,3,5,np.nan],(6,8))
#print(s)

dates = pd.date_range('20190927',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)

print(df.head())


s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
print(2)


print('\n')
print(df.sub(s,axis='index'))



df3 = pd.DataFrame(np.random.randn(10,4))
print(df3)