#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 11:38
# @Author  : Jason
# @Site    : 
# @File    : decision_tree.py
# @Software: PyCharm

import  pandas as pd
from sklearn.tree import  DecisionTreeClassifier as DTC
from sklearn.tree import  export_graphviz
from sklearn.externals.six import  StringIO

filename = 'data/sales_data.xls'
data = pd.read_excel(filename,index_col=u'序号')

data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1

x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)


dtc = DTC(criterion='entropy')
dtc.fit(x,y) #训练模型

with open("tree.dot",'w') as f:
    f = export_graphviz(dtc,feature_names=x.columns,out_file=f)