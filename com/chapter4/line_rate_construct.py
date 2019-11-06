#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 18:00
# @Author  : Jason
# @Site    : 
# @File    : line_rate_construct.py
# @Software: PyCharm


#线损率属性构造
import  pandas as pd

inputfile = 'data/electricity_data.xls'
outputfile = 'tmp/electricity_data.xls'

data = pd.read_excel(inputfile)

data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量']) / data[u'供入电量']

data.to_excel(outputfile,index= False)