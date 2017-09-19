#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-26 下午2:48
# @Author         : Tom.Lee
# @File           : study_sqlalchemy.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : sqlalchemy.sql.selectable.py
import time
from sqlalchemy import (
    Table, Column, MetaData, create_engine)
from sqlalchemy.engine.result import ResultProxy
from sqlalchemy.sql.sqltypes import (
    Unicode, INTEGER)

url = 'mysql+mysqldb://{user}:{pwd}@{host}:{port}/{db_name}?charset=utf8'.format(
    user='root',
    pwd='root',
    host='localhost',
    port='3306',
    db_name='iaasms'
)
# pool_recycle=3600 连接超时参数
engine = create_engine(url)

table = Table(
    'tom_test', MetaData(),
    Column('id', INTEGER, primary_key=True),
    Column('start_time', INTEGER, index=False),
    Column('last_time', INTEGER, nullable=False),
    Column('count', INTEGER, nullable=False),
    Column('region', Unicode(20, _warn_on_bytestring=False))
)

# 创建表
table.create(engine, True)


def _formatter_data(res):
    """
    sqlalchemy.engine.result.ResultProxy 对象数据提取

    res.cursor._rows   # 数据
    res._metadata.keys 或 res.cursor.description # 数据库表字段名
    :param res:
    :return: list
    """
    assert isinstance(res, ResultProxy)
    assert res.returns_rows
    rows = []
    for _row in res.cursor._rows:
        row = {}
        for index, column in enumerate(res._metadata.keys):
            row[column] = _row[index]
        rows.append(row)
    return rows


def _execute_success(res):
    """
    sqlalchemy.engine.result.ResultProxy 数据库修改状态

    res.returns_rows   # 是否返回数据
    res.rowcount 是否执行成功 1 success,0 error
    :param res:
    :return: boolean
    """
    assert isinstance(res, ResultProxy)
    return res.rowcount > 0


def insert():
    # 插入
    # sqlalchemy.exc.IntegrityError 主键冲突异常
    sql = table.insert().values(**{
        'id': 2,
        'start_time': time.time(),
        'last_time': time.time(),
        'count': 1,
        'region': 'test'
    })
    res = engine.execute(sql)
    print _execute_success(res)


def select():
    # 查询
    sql = table.select().where(table.c.id == 2)
    res = engine.execute(sql)
    print _formatter_data(res)


def update():
    # 修改
    sql = table.update().where(table.c.id == 1).values(count=9)
    res = engine.execute(sql)
    print _execute_success(res)


def delete():
    sql = table.delete().where(table.c.id == 2)
    res = engine.execute(sql)
    print _execute_success(res)
