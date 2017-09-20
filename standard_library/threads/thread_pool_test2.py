#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/29 16:50
# @Author  : Aries
# @Site    : 
# @File    : thread_pool_test2.py
# @Software: PyCharm


import Queue
import threading
import urllib2
import time


class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # 从队列抓取主机
            # print self.queue
            # print self.queue.qsize()
            host = self.queue.get()
            print host,'**************************'
            # 抓取主机的URL和打印第一个1024字节的页面
            url = urllib2.urlopen(host)
            # print url.read(10)
            # 队列工作的信号完成
            self.queue.task_done()


hosts = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
]


def main():
    start = time.time()
    # 创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
    queue = Queue.Queue()
    # 生成线程池，并传递队列实例
    for i in range(4):
        t = ThreadUrl(queue)
        # 通过将守护线程设置为 true，
        # 将允许主线程或者程序仅在守护线程处于活动状态时才能够退出。
        t.setDaemon(True)
        t.start()
    # 用数据填充队列
    for host in hosts:
        queue.put(host)
    # 等待队列，直到一切都被处理
    queue.join()
    print "Elapsed Time: %s" % (time.time() - start)


main()

