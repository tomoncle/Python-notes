# coding:utf-8
import random
from time import sleep
import sys
import multiprocessing
import os

lock = multiprocessing.Lock()  # 一个锁


def a(x):
    lock.acquire()
    print '开始进程：', os.getpid(), '模拟进程时间:', x
    lock.release()
    sleep(x)  # 模拟执行操作
    lock.acquire()
    print '结束进程：', os.getpid(), '预测下一个进程启动会使用该进程号'
    lock.release()


list = []
for i in range(10):
    list.append(random.randint(1, 10))
pool = multiprocessing.Pool(processes=3)  # 限制并行进程数为3
pool.map(a, list)
