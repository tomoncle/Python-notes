#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-23 下午9:31
# @Author  : tom.lee
# @Site    : 重写带退出方法的线程类
# @File    : rethread.py
# @Software: PyCharm


import threading


class ReThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ReThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    @property
    def is_running(self):
        """
        获取运行标志
        :return: True/False
        """
        return self.__running.isSet()

    def run(self):
        """
        使用while 循环,使用self.is_running 来获取运行标志位
        """
        pass

    def stop(self):
        """
        设置为False, 让线程阻塞
        """
        self.__flag.clear()

    def resume(self):
        """
        设置为True, 让线程停止阻塞
        """
        self.__flag.set()

    def exit(self):
        """
        暂停标志设置为True
        运行标志设置为False
        """
        self.__flag.set()
        self.__running.clear()

if __name__=="__main__":
    rt= ReThread()
    rt.start()
    print '111'
    # rt.join()
