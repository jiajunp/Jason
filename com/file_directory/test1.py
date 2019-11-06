#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 15:44
# @Author  : Jason
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

from pathlib import  Path

p = Path('.')
print([x for x in p.iterdir() if x.is_dir() ])

print(list(p.glob('**/*.py')))
