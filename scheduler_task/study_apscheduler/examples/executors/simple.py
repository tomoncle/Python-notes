#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-22 上午10:29
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017
# @File           : t.py
# @Product        : PyCharm


import datetime

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ###################使用add_job运行任务#################

def job1():
    print 'job1 is running, Now is %s' % current_time()


def job2():
    print 'job2 is running, Now is %s' % current_time()


# 每隔5秒运行一次job1
scheduler.add_job(job1, 'interval', seconds=5, id='job1')
# 每隔5秒运行一次job2
scheduler.add_job(job2, 'cron', second='*/5', id='job2')


# ###################使用装饰器添加任务#################

# 每隔5秒运行一次job3
@scheduler.scheduled_job('interval', seconds=5, id='job3')
def job3():
    print 'job3 is running, Now is %s' % current_time()


# 每隔5秒运行一次job4
@scheduler.scheduled_job('cron', second='*/5', id='job4')
def job4():
    print 'job4 is running, Now is %s' % current_time()


executors = {
    'processpool': ProcessPoolExecutor(5),
    'default': ThreadPoolExecutor(20)

}
job_defaults = {
    'coalesce': False,
    'max_instances': 5
}
scheduler.configure(executors=executors, job_defaults=job_defaults)
scheduler.start()
