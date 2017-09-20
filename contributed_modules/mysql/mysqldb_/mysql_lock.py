#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/25 22:42
# @Author  : Tom.lee
# @Site    : 
# @File    : mysql_lock.py
# @Software: PyCharm


"""
通过MySQL实现分布式锁服务
"""
import MySQLdb
import logging
import time

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

    def __init__(self, lock_key=None, *args, **kwargs):
        """
        :param lock_key:
        :param args:    参数与MySQLdb初始化参数一致.
        :param kwargs:  参数与MySQLdb初始化参数一致.
                    host='localhost'
                    user='test'
                    passwd='test'
                    db='test'
        """
        self.__db = MySQLdb.connect(*args, **kwargs)
        self.lock_key = lock_key or '7ab18906739e4662ac01e69f5ebb7352'

    def _execute(self, sql):
        """
        MySQL数据库操作
        :param sql:
        :return: (1L,) --> tuple
        """
        res = (-1,)
        cursor = self.__db.cursor()
        try:
            cursor.execute(sql)
            if cursor.rowcount != 1:
                logging.error("Multiple rows returned in mysql lock function.")
            else:
                res = cursor.fetchone()
        except Exception, ex:
            logging.error("执行SQL\"%s\" 失败! 异常信息: %s", sql, str(ex))
        finally:
            cursor.close()
        return res

    def lock(self, timeout):
        """
        MySQL数据库加锁
        :param timeout:  超时时间
        :return:
        """
        # 加锁操作
        lk = self._execute(self.LOCK_SQL.format(key=self.lock_key, timeout=timeout))

        if lk[0] == 0:
            logging.debug("锁'%s'已经被创建.", self.lock_key)
            return False
        elif lk[0] == 1:
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

        if uk[0] == 0:
            logging.debug("释放锁'%s'失败(该锁被其他进程持有)" % self.lock_key)
            return False
        elif uk[0] == 1:
            logging.debug("释放锁'%s'." % self.lock_key)
            return True
        else:
            logging.error("锁'%s'不存在." % self.lock_key)
            return None


if __name__ == "__main__":
    l = MySqlLock(host='localhost', user='root', passwd='root', db='iaasms')
    ret = l.lock(15)
    if not ret:
        logging.error("获取锁失败,退出!")
        quit()

    time.sleep(15)  # 模拟跨进程的同步操作!
    # raise Exception('模拟操作异常,mysql会自动释放该进程持有的锁.')
    # TODO something
    print 'hello ok!'

    l.unlock()
