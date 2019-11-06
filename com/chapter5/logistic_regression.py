#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 11:08
# @Author  : Jason
# @Site    : 
# @File    : logistic_regression.py
# @Software: PyCharm
#逻辑回归，自动建模

import  pandas as pd
from sklearn.linear_model import  LogisticRegression as LR
#from sklearn.linear_model import  RandomizedLogisticRegression as RLR
from stability_selection.randomized_lasso import  RandomizedLogisticRegression as RLR


filename = 'data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].as_matrix()
y = data.iloc[:,8].as_matrix()


rlr = RLR()
rlr.fit(x,y)
rlr.get_support()
print(u'通过随机逻辑回归模型筛选特征结束')
print(u'有效特征为:%s' % ','.join(data.columns[rlr.get_support()]))

x = data[data.columns[rlr.get_support()]].as_matrix()

lr = LR()
lr.fit()
print(u'逻辑回归模型训练结束。')
print(u'模型的平均正确率为:%s' % lr.score(x,y))
