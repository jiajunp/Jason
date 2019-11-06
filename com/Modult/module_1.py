#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24
# @Author  : Jason.Jia

import os, sys
from scipy.optimize import  fsolve
import torch

def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 -1,x1**2 - x2 - 2]

result = fsolve(f,[1,1])
print(result)

from scipy import  integrate



from PIL import  Image


from statsmodels.tsa.stattools import  adfuller


import  django





