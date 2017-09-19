#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-3-27 下午4:29
# @Author         : Tom.Lee
# @Description    : mysql 操作
# @File           : study_mysql.py
# @Product        : PyCharm
import MySQLdb
import logging
from contextlib import closing

"""
# # １．创建数据库的连接
# conn = MySQLdb.connect(host='localhost', port=3306, user='root',
#                        passwd='root', db='iaasms_dev', )
#
# # ２．创建游标
# cur = conn.cursor(MySQLdb.cursors.DictCursor)
#
# # ３．通过游标cur 操作execute()方法可以写入纯sql语句对数据进行操作
# sql = '''
# SELECT a.name AS snapshot_name, b.name AS volume_name
# FROM snapshot a INNER JOIN volume b
# ON a.volume_id=b.volume_id
# '''
# count = cur.execute(sql)  # 返回总条数
# # result = cur.fetchmany(count)  # 返回指定条目的结果集
# result = cur.fetchall()
# # ４．关闭游标
# cur.close()
#
# # ５．提交事务，必须要有这个方法，否则数据不会被真正的插入。
# conn.commit()
#
# # ６．关闭连接
# conn.close()
#
# # ************打印***********
# print result

# 一次插入多条记录,,返回值为受影响的行数。
# sql="insert into student values(%s,%s,%s,%s)"
# cur.executemany(sql,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','rick','2 year 2 class','7'),
#     ])

# *******************close conn***************************
from contextlib import closing
import MySQLdb

''' At the beginning you open a DB connection. Particular moment when
  you open connection depends from your approach:
  - it can be inside the same function where you work with cursors
  - in the class constructor
  - etc
'''
db = MySQLdb.connect("host", "user", "pass", "database")
with closing(db.cursor()) as cur:
    cur.execute("somestuff")
    results = cur.fetchall()
    # do stuff with results

    cur.execute("insert operation")
    # call commit if you do INSERT, UPDATE or DELETE operations
    db.commit()

    cur.execute("someotherstuff")
    results2 = cur.fetchone()
    # do stuff with results2

# at some point when you decided that you do not need
# the open connection anymore you close it
db.close()

"""

# 创建名为MySQL的日志
logger = logging.getLogger('MySQL')
# 设置logger的level为DEBUG
logger.setLevel(logging.DEBUG)
# 创建一个输出日志到控制台的StreamHandler
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
handler.setFormatter(formatter)
# 给logger添加上handler
logger.addHandler(handler)


class _Closing(closing):
    def __exit__(self, *exc_info):
        if self.thing:
            self.thing.close()


class MySQLUtils(object):
    def __init__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

        self.__args = args
        self.__kwargs = kwargs
        self.__connection = None
        self.__cursor = None

    def __enter__(self):
        """
        打开资源,支持with语法
        :return: MySQLUtils instance
        """
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        关闭资源,支持with语法
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.close()
        if exc_tb:
            # 默认返回None,　返回None或False 发生异常交由外部调用程序捕获（建议）
            # 如果返回True,则由该函数内部处理，外部调用会继续执行
            logger.error('[%s]%s' % (exc_type, exc_val))

    def open(self):
        """
        打开连接
        :return:
        """
        if self.__connection:
            raise MySQLdb.MySQLError("connection already connected.")
        self.__connection = MySQLdb.connect(*self.__args, **self.__kwargs)
        if self.__cursor:
            raise MySQLdb.MySQLError("cursor already opened.")
        self.__cursor = self.__connection.cursor(MySQLdb.cursors.DictCursor)
        logger.info("connection opened.")

    def close(self):
        """
        关闭连接
        :return:
        """
        with _Closing(self.__cursor) as _:
            pass
        with _Closing(self.__connection) as _:
            pass
        self.__cursor = None
        self.__connection = None

        logger.info("connection close success.")

    def __execute(self, sql, commit=False):
        """
        执行SQL
        :param sql:
        :param commit:
        :return:tuple result or row numbers
        """
        if not (self.__connection and self.__cursor):
            raise MySQLdb.MySQLError("connection already closed.")
        count = self.__cursor.execute(sql)  # 返回总条数
        result = self.__cursor.fetchall()
        self.__connection.commit() if commit else None
        return count if commit else result

    def select(self, sql, formatter_func=None):
        """
        查询函数
        :param sql:
        :param formatter_func:格式化函数
        :return:
        """
        if formatter_func:
            return map(formatter_func, self.__execute(sql))
        return self.__execute(sql)

    def save_or_update(self, sql):
        """
        编辑或修改
        :param sql:
        :return:row numbers
        """
        return self.__execute(sql, True)

    def delete(self, sql):
        """
        删除资源
        :param sql:
        :return: row numbers
        """
        return self.__execute(sql, True)


if __name__ == '__main__':
    mu = MySQLUtils(host='localhost', port=3306, user='root',
                    passwd='root', db='iaasms_dev')
    import datetime


    def formatter_datetime(dic):
        for k, v in dic.iteritems():
            if isinstance(v, datetime.datetime):
                dic[k] = str(v)
        return dic


    # 1. try-finally
    # try:
    #     mu.open()
    #     # raise Exception('异常')
    #     print mu.select('SELECT * FROM flavor', formatter_datetime)
    #     print mu.delete('DELETE FROM flavor WHERE id=42')
    # finally:
    #     mu.close()

    # 2. with
    with mu as mu:
        mu.close()
        # raise Exception('异常')
        print mu.select('SELECT * FROM flavor', formatter_datetime)
        print mu.delete('DELETE FROM flavor WHERE id=42')

    print getattr(mu, 'host'), getattr(mu, 'port'), getattr(mu, 'no', None)

