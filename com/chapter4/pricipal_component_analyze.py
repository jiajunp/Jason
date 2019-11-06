#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 10:43
# @Author  : Jason
# @Site    : 
# @File    : pricipal_component_analyze.py
# @Software: PyCharm

import pandas as pd
from sklearn.decomposition import  PCA

inputfile = 'data/principal_component.xls'
outputfile = 'tmp/dimention_reducted.xls'

data = pd.read_excel(inputfile,header=None)

pca = PCA(3)
pca.fit(data)
#pca.components_ #返回模型的各个特征向量

#pca.explained_variance_ratio_ #返回各个成分各自的方差百分比

low_d = pca.transform(data) #用来降低维度
pd.DataFrame(low_d).to_excel(outputfile)

pca.inverse_transform(low_d)

