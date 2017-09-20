#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 下午1:31
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017
# @File           : demo.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import rpyc
from rpyc.utils.server import ThreadedServer


class MyService(rpyc.Service):
    data = []

    def exposed_save_data(self, d):
        self.data.append(d)

    def exposed_get_data(self):
        return self.data


class MyClient(object):
    @classmethod
    def conn(cls):
        connections = rpyc.connect('localhost', 15111)
        connections.root.save_data(123)
        print connections.root.get_data()


if __name__ == '__main__':
    import threading
    import time

    server = ThreadedServer(MyService, port=15111)
    client = MyClient()


    def start():
        print '*************************************'
        print '*************************************'
        print '*****************RpyC****************'
        print '************           **************'
        print '*************************************'
        print '***************start server**********'
        print '*************************************'
        print '*************************************\n\n'
        server.start()

    threading.Thread(target=start).start()

    client.conn()
    time.sleep(5)

    server.close()
    print 'service stop.'
