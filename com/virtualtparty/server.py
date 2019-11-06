#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time : 2019/11/6 22:27
 @Author : Jason.Jia
 @contact: jiajunp@163.com
 @Version : 1.0
 @file :server.py
 @desc :
 
'''

import  socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysocket.bind(('127.0.0.1',8888))
mysocket.listen(5)

while True:
    connection,addr = mysocket.accept()
    revStr = connection.recv(1024)

    connection.send('Server:' + str(revStr))
    connection.close()
