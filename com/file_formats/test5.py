#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 16:52
# @Author  : Jason
# @Site    : 
# @File    : test5.py
# @Software: PyCharm

import  asyncio

class EchoClientProtocol(asyncio.Protocol):
    def __int__(self,message,loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent:{!r}'.format(self.message))

    def data_received(self,data):
        print('Data received:{!r}'.format(data.decode()))

        def connection_lost(self, exc):
            print('The server closed the connection')
            print('Stop the event loop')
            self.loop.stop()

    loop = asyncio.get_event_loop()
    message = 'Hello World!'
    coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                                  '192.168.100.21', 8888)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
