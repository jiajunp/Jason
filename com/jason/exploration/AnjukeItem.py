#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 13:46
# @Author  : Jason
# @Site    : 
# @File    : AnjukeItem.py
# @Software: PyCharm


import  scrapy

class AnjukeItem(scrapy.Item):
    price = scrapy.Field()
    mode = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    age = scrapy.Field()
    location = scrapy.Field()
    district = scrapy.Field()
    pass



