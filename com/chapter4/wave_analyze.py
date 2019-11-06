#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 18:24
# @Author  : Jason
# @Site    : 
# @File    : wave_analyze.py
# @Software: PyCharm


from scipy.io import  loadmat
import pywt

inputfile = 'data/leleccum.mat'
mat = loadmat(inputfile)
signal = mat['leleccum'][0]

coeffs = pywt.wavedec(signal,'bior3.7',level = 5)

print(coeffs)


