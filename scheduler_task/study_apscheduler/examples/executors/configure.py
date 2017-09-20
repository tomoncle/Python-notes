#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-9 上午9:56
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017
# @File           : job_configure.py
# @Product        : PyCharm


from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

job_stores = {
    'default': SQLAlchemyJobStore(
        url='mysql+mysqldb://root:root@localhost:3306/djangoapp?charset=utf8')
}


executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}


job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

# UTC as the scheduler’s timezone
scheduler = BackgroundScheduler(
    jobstores=job_stores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc,
    daemon=False
)


def current_time():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def job1():
    print 'job1 is running, Now is %s' % current_time()


def job2():
    print 'job2 is running, Now is %s' % current_time()


# 每隔5秒运行一次job1,replace_existing=True防止添加重复，启动失败
scheduler.add_job(job1, 'interval', seconds=5, id='job1', replace_existing=True)
# 每隔5秒运行一次job2
scheduler.add_job(job2, 'cron', second='*/5', id='job2', replace_existing=True)
scheduler.start()
print scheduler.get_jobs()
