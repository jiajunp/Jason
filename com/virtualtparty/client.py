#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time : 2019/11/6 22:29
 @Author : Jason.Jia
 @contact: jiajunp@163.com
 @Version : 1.0
 @file :client.py
 @desc :
 
'''


import  socket
import  time

clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientsock.connect(('127.0.0.1',8888))

while True:
    time.sleep(2)
    clientsock.send(bytes('hello the5fire',encoding="utf8"))
    print(clientsock.recv(1024))

clientsock.close()
