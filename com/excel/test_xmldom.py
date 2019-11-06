#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:28
# @Author  : Jason
# @Site    : 
# @File    : test_xmldom.py
# @Software: PyCharm

import  xml.dom.minidom as xmldom
import  os

xmlfilepath = os.path.abspath("test.xml")

#print("xml文件路径：" ,xmlfilepath)

#得到问而当对象

domobj = xmldom.parse(xmlfilepath)
print("xmldom.parse:" ,type(domobj))

#得到元素对象

elementobj = domobj.documentElement
print("domobj.documnetElement:",type(elementobj))

#获得子标签

subElementObj = elementobj.getElementsByTagName("login")
print("getElementsByTagName:",type(subElementObj))

print(len(subElementObj))

#获取标签属性值

print(subElementObj[0].getAttribute("username"))
print(subElementObj[0].getAttribute("passwd"))

#区分相同标签名的标签

subElementObj1 = elementobj.getElementsByTagName("caption")
for i in range(len(subElementObj1)):
    print("subElementObj1[i]:" ,type(subElementObj1[i]))
    print(subElementObj1[i].firstChild.data) #显示标签之间的数据
