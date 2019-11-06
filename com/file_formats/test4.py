#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 16:40
# @Author  : Jason
# @Site    : 
# @File    : test4.py
# @Software: PyCharm

import  selectors
import socket


sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr = sock.accept()
    print('accepted',conn,' from ',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)


def read(conn,mask):
    data = conn.recv(1000)
    if data:
        print('echoing',repr(data),'to',conn)
        conn.send(data)
    else:
        print('closing',conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('192.168.100.21',1234))
sock.listen(100)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    for key,mask in events:
        callback = key.data
        callback(key.fileobj,mask)


