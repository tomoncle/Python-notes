#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-19 下午10:49
# @Author  : tom.lee
# @Site    : 
# @File    : tools.py
# @Software: PyCharm
import logging
import os
import threading
import time


class Decorator(object):
    @staticmethod
    def time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            logging.warning(
                '*******方法[%s]消耗时间%d s' %
                (func.__name__, time.time() - start))
            return result

        return wrapper


class Constants(object):
    parser = 'html.parser'
    encoding = 'utf-8'
    url_filed = 'href'


class Dir(object):
    @staticmethod
    def create_dir(path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception, e:
                print u'文件夹%s　创建失败;\n %s' % (path, e)
        else:
            print u'文件夹%s　已经存在' % path

    @staticmethod
    def parent_dir(path):
        path = path.rstrip('/')
        return '/'.join(path.split('/')[0:-1])

    @staticmethod
    def del_dir(path):
        assert os.path.exists(path) and os.path.isdir(path)
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(path)

    @staticmethod
    def create_file(name, mode='r', data=""):
        try:
            parent_path = Dir.parent_dir(name)
            if parent_path and not os.path.exists(parent_path):
                Dir.create_dir(parent_path)
            with open(name, mode)as f:
                f.write(data)
        except Exception, e:
            print u'%s 创建失败\n异常：%s' % (name, e)


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
