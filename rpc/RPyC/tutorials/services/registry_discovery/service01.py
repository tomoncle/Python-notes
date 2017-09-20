#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-15 下午1:35
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : service.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import rpyc
from rpyc.utils.server import ThreadedServer



class MyService(rpyc.Service):

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    @classmethod
    def exposed_get_answer(cls):
        return 66

    @classmethod
    def get_question(cls):
        return "what is the airspeed velocity of an unladen swallow?"


if __name__ == "__main__":
    t = ThreadedServer(MyService, port=18861)
    print """
    service start ok! port {port}
    """.format(port=18861)
    t.start()
