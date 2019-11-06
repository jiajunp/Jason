#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:38
# @Author  : Jason
# @Site    : 
# @File    : test_xmletree.py
# @Software: PyCharm


import  xml.etree.ElementTree as ET

import  os
import  sys

#遍历xml文件

def traveseXml(element):
    if len(element)>0:
        for child in element:
            print(child.tag,"---" ,child.attrib)
            traveseXml(child)


if __name__ == "__main__":
    xmlFilePath = os.path.abspath("test.xml")

    print(xmlFilePath)

    try:
        tree = ET.parse(xmlFilePath)
        print("tree type:",type(tree))

        #获得根节点
        root = tree.getroot()

    except Exception as e:
        print("parse test.xml fail")
        sys.exit()

    print("root type:",type(root))
    print(root.tag,"---",root.attrib)

    #遍历root的下一层

    for child in root:
        print("遍历root的下一层", child.tag, "----", child.attrib)

    #使用下标访问
    print(root[0].text)
    print(root[1][1][0].text)

    print(20 * "*")

    #遍历xml文件
    traveseXml(root)
    print(20 * "*")

    #根据标签名查找root下所有标签
    captionList = root.findall("item")
    print(len(captionList))
    for caption in captionList:
        print(caption.tag, "----", caption.attrib, "----", caption.text)

    # 修改xml文件，将passwd修改为999999
    login = root.find("login")
    passwdValue = login.get("passwd")
    print("not modify passwd:", passwdValue)
    login.set("passwd", "999999")  # 修改，若修改text则表示为login.text
    print("modify passwd:", login.get("passwd"))