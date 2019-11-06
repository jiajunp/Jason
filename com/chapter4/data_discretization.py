#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 16:50
# @Author  : Jason
# @Site    : 
# @File    : data_discretization.py
# @Software: PyCharm


import pandas as pd
import  matplotlib.pyplot as plt
import  numpy as np

datafile = 'data/discretization_data.xls'
data = pd.read_excel(datafile)

data = data[u'肝气郁结证型系数'].copy()
k = 4
d1 = pd.cut(data,k,labels=range(k))

#等频率离散化

w = [1.0 * i/k for i in range(k+1)]
w = data.describe(percentiles = w) [4:4+k+1]
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(data,w,labels=range(k))

from sklearn.cluster import  KMeans

kmodel = KMeans(n_clusters=k,n_jobs= 4 )
kmodel.fit(data.values.reshape((len(data),1)))
c = pd.DataFrame(kmodel.cluster_centers_).sort(0)
#plt.plot(data)
#ts_log = np.log(c)
#w = ts_log.rolling(c,2).mean()
w = pd.rolling_mean(c,2).ilco[1:]

w = [0] + list(w[0]) + [data.max()]

d3 = pd.cut(data,w,labels=range(k))


def cluster_plot(d,k):

    plt.rcParams['font-sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus']  =False

    plt.figure(figsize=(8,3))

    for j in range(0,k):
        plt.plot(data[d==j],[j for i in d[d==j]],'o')

    plt.ylim(-0.5,k-0.5)
    return plt


cluster_plot(d1,k).show()
cluster_plot(d2,k).show()
cluster_plot(d3,k).show()