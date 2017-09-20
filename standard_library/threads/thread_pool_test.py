#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/29 14:46
# @Author  : TOM
# @Site    : 模拟线程池
# @File    : thread_pool_test.py
# @Software: PyCharm


import time
import threading
import Queue
import urllib2


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            content = self._queue.get()
            print content
            response = urllib2.urlopen(content)
            self._queue.task_done()
            print content,'_______________ok'


def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        # 通过setDaemon(true)来设置线程为“守护线程”
        # 在没有用户线程可服务时会自动离开
        worker.setDaemon(True)
        worker.start()
        workers.append(worker)
    return workers


def Producer():
    urls = [
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
        # etc..
    ]
    start_time = time.time()
    queue = Queue.Queue()
    build_worker_pool(queue, 4)
    for url in urls:
        queue.put(url)

    queue.join()
    print 'time use :', time.time() - start_time




if __name__ == "__main__":
    Producer()
