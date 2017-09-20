#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-4-19 上午10:58
# @Author         : Tom.Lee
# @Description    : 
# @File           : socket.py
# @Product        : PyCharm
import socket
import threading
import time


class Server(object):
    NUMBER = 0

    def __init__(self, ip, port, message='hello'):
        self.__ip = ip
        self.__port = port
        self.__message = message

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.__ip, self.__port))
        s.listen(0)

        def run(**kwargs):
            num = self.NUMBER
            client = kwargs.get('client')
            print self.NUMBER, client, client.recv(1024)
            time.sleep(10)
            client.sendall('%s:%d' % (self.__message, num))
            client.close()

        while True:
            client, addr = s.accept()
            if client:
                self.NUMBER += 1
                threading.Thread(target=run, name='T%d' % self.NUMBER,
                                 kwargs={'client': client}).start()


class Client(object):
    def __init__(self, ip, port, message='hi'):
        self.__ip = ip
        self.__port = port
        self.__message = message

    def start(self):
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((self.__ip, self.__port))
        c.send(self.__message)
        print c.recv(1024)
        c.close()


if __name__ == '__main__':
    server = Server('127.0.0.1', 1000)
    server.start()
