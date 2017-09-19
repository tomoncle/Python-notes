#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-6-13 下午12:56
# @Author         : Tom.Lee
# @Docs           : http://www.cnblogs.com/hhh5460/p/5838516.html
# @File           : mongodb.py
# @Product        : PyCharm
import pymongo


class _Mongodb(object):
    def __init__(self,
                 host=None,
                 port=None,
                 document_class=dict,
                 tz_aware=None,
                 connect=None,
                 **kwargs):
        self.__mongodb = pymongo.MongoClient(
            host, port, document_class, tz_aware, connect, **kwargs)

    @property
    def mongodb_client(self):
        return self.__mongodb


class MongodbUtils(object):
    def __init__(self,
                 host=None,
                 port=None,
                 document_class=dict,
                 tz_aware=None,
                 connect=None,
                 **kwargs):
        self.__mongodb_client = _Mongodb(
            host=host,
            port=port,
            document_class=document_class,
            tz_aware=tz_aware,
            connect=connect,
            **kwargs).mongodb_client
        self.__database = None
        self.__collection = None

    @property
    def mongodb_client(self):
        return self.__mongodb_client

    @property
    def mongodb_database(self):
        assert self.__database
        return self.__database

    @property
    def mongodb_collection(self):
        assert self.__collection
        return self.__collection

    def use_db(self, db):
        """
        切换数据库 > use tom_db

        :param db:
        :return:
        """
        self.__database = self.db_create_or_get(db)
        return self

    def use_collection(self, collection, db=None):
        """
        使用表操作 > db.tom_table

        :param collection:
        :param db:
        :return:
        """
        if db:
            self.__database = self.db_create_or_get(db)
        self.__collection = self.mongodb_database[collection]
        return self

    def db_list(self):
        """
        数据库列表 show dbs

        :return: ['db1','db2']
        """
        return self.mongodb_client.database_names()

    def db_exists(self, db_name):
        """
        :param db_name:
        :return: True/False
        """
        return db_name in self.db_list()

    def db_create_or_get(self, db_name):
        """
        创建或使用
        > use tom_db
        > db.createCollection('table1') # 第二步开始创建数据库

        :param db_name:
        :return: __mongodb.get_database(db_name)
        """
        # self.mongodb_client.get_database(db_name)

        return self.mongodb_client[db_name]

    def db_delete(self, db_name):
        """
        删除
        > use tom_db
        > db.dropDatabase()

        :param db_name:
        :return:
            error  :  {u'code': 26, u'ok': 0.0, u'errmsg': u'ns not found'}
            success:  {u'ns': u'tom_db.tom_table', u'ok': 1.0, u'nIndexesWas': 1}
        """
        return self.mongodb_client.drop_database(db_name)

    def collection_list(self):
        """
        表(文档)列表 > show tables
        :return:
        """
        return self.mongodb_database.collection_names()

    def collection_create_or_get(self, collection_name):
        """
        创建或获取表 createCollection('table1')

        :param collection_name:
        :return:
        """
        return self.mongodb_database[collection_name]

    def collection_exists(self, collection_name):
        """
        集合是否存在
        :param collection_name:
        :return:
        """
        return collection_name in self.collection_list()

    def collection_delete(self, collection_name):
        """
        删除集合 db.tom_table2.drop()

        :param collection_name:
        :return:
        """
        return self.mongodb_database.drop_collection(collection_name)

    def document_count(self, filter_=None):
        """
        db.tom_table.count()

        :param filter_:{'name':'zs'}
        :return:
        """
        return self.mongodb_collection.count(filter=filter_)

    def document_find(self, *args, **kwargs):
        """
        db.tom_table.find({'seq':'_seq_7'})

        :param args:
        :param kwargs:{'seq':'_seq_7'}
        :return:
        """
        return self.mongodb_collection.find(*args, **kwargs)

    def document_insert(self, dict_item):
        """
        db.tom_table.insert({'name':'jack'})

        :param dict_item: {'name':'jack'}
        :return:
        """
        return self.mongodb_collection.insert(dict_item)

    def document_drop(self):
        """
        删除全部文档
        :return:
        """
        return self.mongodb_collection.drop()

    def document_delete(self, filter_, collation=None):
        """
        db.tom_table.deleteOne({'seq':'_seq_7'})

        :param filter_: {'name':'jack'}
        :param collation:
        :return:
        """
        result = self.mongodb_collection.delete_one(filter_, collation)
        return result.delete_count > 0

    def document_delete_list(self, filter_, collation=None):
        """
        db.tom_table.deleteMany({'seq':'_seq_7'})

        :param filter_: {'seq':'_seq_7'}
        :param collation:
        :return:
        """
        self.mongodb_collection.delete_many(filter_, collation)
        return self.document_count(filter_) == 0
