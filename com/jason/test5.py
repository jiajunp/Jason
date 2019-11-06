#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 8:25
# @Author  : Jason
# @Site    : 
# @File    : test5.py
# @Software: PyCharm
#更新最新版本库

import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions
for dist in get_installed_distributions():
    call("pip3 install --upgrade " + dist.project_name, shell=True)
