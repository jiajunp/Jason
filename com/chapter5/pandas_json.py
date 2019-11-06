#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 14:07
# @Author  : Jason
# @Site    : 
# @File    : pandas_json.py
# @Software: PyCharm

from pandas.io.json import  json_normalize
import  pandas as pd

data = [{
    'CreatedBy': {'Name': 'User001'},
    'Lookup': {'TextField': 'Some text',
    'UserField': {'Id': 'ID001', 'Name': 'Name001'}},
    'Image': {'a': 'b'}
}]

json_normalize(data,max_level=1)

print(data)
print(json_normalize(data,max_level=1))

df = pd.DataFrame([{'var1': 'a,b,c', 'var2': 1},
                   {'var1': 'd,e,f', 'var2': 2}])

df = pd.DataFrame([0], index=pd.DatetimeIndex(['2019-01-01'], tz='US/Pacific'))
print(df)

import  numpy as np


s = pd.Series(np.array(['a', 'ba', 'cba'], 'S'),dtype=object)
print(s)

print(s.str.startswith(b'a'))
