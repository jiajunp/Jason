#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 14:47
# @Author  : Jason
# @Site    : 
# @File    : xmlparse.py
# @Software: PyCharm

import xml.etree.ElementTree as ET
import sys
import os.path


class XmlParse:
    def __init__(self, file_path):
        self.tree = None
        self.root = None
        self.xml_file_path = file_path

    def ReadXml(self):
        try:
            print("xmlfile:", self.xml_file_path)
            self.tree = ET.parse(self.xml_file_path)
            self.root = self.tree.getroot()
        except Exception as e:
            print("parse xml faild!")
            sys.exit()
        else:
            print("parse xml success!")
        finally:
            return self.tree

    def CreateNode(self, tag, attrib, text):
        element = ET.Element(tag, attrib)
        element.text = text
        print("tag:%s;attrib:%s;text:%s" % (tag, attrib, text))
        return element

    def AddNode(self, Parent, tag, attrib, text):
        element = self.CreateNode(tag, attrib, text)
        if Parent:
            Parent.append(element)
            el = self.root.find("lizhi")
            print(el.tag, "----", el.attrib, "----", el.text)
        else:
            print("parent is none")

    def WriteXml(self, destfile):
        dest_xml_file = os.path.abspath(destfile)
        self.tree.write(dest_xml_file, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    xml_file = os.path.abspath("test.xml")
    parse = XmlParse(xml_file)
    tree = parse.ReadXml()
    root = tree.getroot()
    print(root)
    parse.AddNode(root, "Python", {"age": "22", "hello": "world"}, "YES")

    parse.WriteXml("testtest.xml")
