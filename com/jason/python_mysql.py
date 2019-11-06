#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 10:55
# @Author  : Jason
# @Site    : 
# @File    : python_mysql.py
# @Software: PyCharm



import  paramiko

hostname = '192.168.100.21'
port = 22
username = 'root'
password = 'root@123'

t = paramiko.Transport((hostname,port))
t.connect(username=username,password=password)
sftp = paramiko.SFTPClient.from_transport(t)

sftp.put(r'E:\python\data\600508.csv','/home/jiajunp/data/')
sftp.close()
print('上传完成！')
