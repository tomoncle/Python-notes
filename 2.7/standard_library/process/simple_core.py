#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-5-7 下午11:16
# @Author  : tom.lee
# @Site    : 
# @File    : simple_core.py
# @Software: PyCharm


from multiprocessing import Process
import time
import os


def worker_1(interval):
    print("worker_1,父进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_1,执行时间为'%0.2f'秒" % (t_end - t_start))


def worker_2(interval):
    print("worker_2,父进程(%s),当前进程(%s)" % (os.getppid(), os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_2,执行时间为'%0.2f'秒" % (t_end - t_start))


if __name__ == "__main__":
    print("进程ID：%s" % os.getpid())
    # 如果不指定name参数，默认的进程对象名称为Process-N，N为一个递增的整数
    p1 = Process(target=worker_1, args=(20,))
    p1.start()
    # p1.join() # 阻塞，禁止并发
    p2 = Process(target=worker_2, name="dongGe", args=(10,))

    p2.start()
    print("p2.is_alive=%s" % p2.is_alive())
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    # p1.join()　# 然而没什么卵用
    print("p1.is_alive=%s" % p1.is_alive())
