#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/29 17:06
# @Author  : Aries
# @Site    : 
# @File    : threadPool.py
# @Software: PyCharm

import threading


class _Worker(threading.Thread):
    def __init__(self, queue, func, *args, **kwargs):
        super(_Worker, self).__init__(*args, **kwargs)
        self.__queue = queue
        self.__func = func

    def __task(self):
        args = self.__queue.get()
        self.__func(args)
        self.__queue.task_done()

    def run(self):
        while True:
            self.__task()


class ReThreadPool(object):
    def __init__(self, queue, func, daemon=False, num=10):
        self.daemon = daemon
        self.num = num
        self.queue = queue
        self.func = func

    def execute(self):
        for _ in range(self.num):
            worker = _Worker(self.queue, self.func)
            if self.daemon:
                worker.setDaemon(True)
            worker.start()
        self.queue.join()


if __name__ == '__main__':
    import time
    import Queue

    start_time = time.time()
    q = Queue.Queue()
    for i in range(50):
        q.put(i)


    def test(num):
        time.sleep(1)
        print 'num:%d' % num
        return


    ReThreadPool(q, test).execute()
    # 队列加入新数据
    for i in range(50, 100):
        q.put(i)
    print time.time() - start_time
