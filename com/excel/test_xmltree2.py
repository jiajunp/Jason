#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:59
# @Author  : Jason
# @Site    : 
# @File    : test_xmltree2.py
# @Software: PyCharm

import  xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
print(root)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
print('')
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)





for rank in root.iter('rank'):
    new_rank  = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated','yes')

tree.write('output.xml')