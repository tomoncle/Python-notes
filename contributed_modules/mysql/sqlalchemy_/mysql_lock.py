#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-26 下午3:54
# @Author         : Tom.Lee
# @File           : mysql_lock2.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

"""
通过MySQL sqlalchemy 实现分布式锁服务
"""
import logging
import time
from sqlalchemy import create_engine

FORMAT_STR = '%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT_STR)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))


class MySqlLock(object):
    LOCK_SQL = "SELECT get_lock('{key}', {timeout}) FROM dual"
    UNLOCK_SQL = "SELECT release_lock('{key}') FROM dual"

    def __init__(self, lock_key=None, **kwargs):
        """
        :param lock_key:
        :param args:    参数与MySQLdb初始化参数一致.
        :param kwargs:  参数与MySQLdb初始化参数一致.
                    host='localhost'
                    user='test'
                    passwd='test'
                    db='test'
        """
        self.engine = create_engine('mysql+mysqldb://{user}:{pwd}@{host}:{port}/{db_name}?charset=utf8'.format(
            user=kwargs.pop('user', None),
            pwd=kwargs.pop('pwd', None),
            host=kwargs.pop('host', 'localhost'),
            port=kwargs.pop('pop', '3306'),
            db_name=kwargs.pop('db_name', None)
        ))
        self.lock_key = lock_key or '7ab18906739e4662ac01e69f5ebb7352'

    def _execute(self, sql):
        """
        MySQL数据库操作
        :param sql:
        :return: (1L,) --> tuple
        """
        res = -1
        try:
            e = self.engine.execute(sql)
            if e.rowcount <= 1:
                res = e.rowcount
        except Exception, ex:
            logging.error("执行SQL\"%s\" 失败! 异常信息: %s", sql, str(ex))
        finally:
            pass
        return res

    def lock(self, timeout):
        """
        MySQL数据库加锁
        :param timeout:  超时时间
        :return:
        """
        # 加锁操作
        lk = self._execute(self.LOCK_SQL.format(key=self.lock_key, timeout=timeout))

        if lk == 0:
            logging.debug("锁'%s'已经被创建.", self.lock_key)
            return False
        elif lk == 1:
            logging.debug("创建锁'%s'." % self.lock_key)
            return True
        else:
            logging.error("获取锁失败!")
            return None

    def unlock(self):
        """
        释放MySQL锁.
        :return:
        """
        # 释放操作
        uk = self._execute(self.UNLOCK_SQL.format(key=self.lock_key))

        if uk == 0:
            logging.debug("释放锁'%s'失败(该锁被其他进程持有)" % self.lock_key)
            return False
        elif uk == 1:
            logging.debug("释放锁'%s'." % self.lock_key)
            return True
        else:
            logging.error("锁'%s'不存在." % self.lock_key)
            return None


if __name__ == "__main__":
    l = MySqlLock(host='localhost', user='root', pwd='root', db_name='iaasms')
    ret = l.lock(15)
    if not ret:
        logging.error("获取锁失败,退出!")
        quit()

    time.sleep(5)  # 模拟跨进程的同步操作!
    # raise Exception('模拟操作异常,mysql会自动释放该进程持有的锁.')
    # TODO something
    print 'hello ok!'

    l.unlock()
