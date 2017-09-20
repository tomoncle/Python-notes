# -*- encoding:utf-8 -*-

import redis

redis_client = redis.Redis()
print redis_client


def add_str(k, v):
    """
    添加字符串
    :param k:键
    :param v:值
    :return:
    """
    redis_client.set(k, v)


def get_str(k):
    """
    获取字符串
    :param k:键
    :return:
    """
    return redis_client.get(k)


def add_llist(k, l):
    """lpush 倒序返回"""
    redis_client.lpush(k, l)


def add_rlist(k, l):
    """rpush 顺序返回"""
    redis_client.rpush(k, l)


def get_list(k, start=0, end=-1):
    """
    redis_client.lrange('list_descsort',0,-1)
    :param k:
    :param start:
    :param end:
    :return:
    """
    return redis_client.lrange(k, start, end)


def get_keys(pattern='*'):
    """
    :param pattern: 'list*'
    :return:
    """
    return redis_client.keys(pattern)


def delete_key(*keys):
    redis_client.delete(keys)


def redis_subscribe(chanel_name):
    """
    redis　订阅频道
    :param chanel_name:
    :return:
    """
    pub = redis_client.pubsub()
    pub.subscribe(chanel_name)
    if pub.parse_response():
        return pub
    else:
        return None


def redis_publish(chanel_name, **kwargs):
    """
    发布消息
    :param chanel_name:
    :param kwargs:
    :return:
    """
    redis_client.publish(chanel_name, kwargs)


# redis publish and subscribe
# publish message
'''
for i in range(10):
    redis_client.publish('fm101', 'hello i am %d' % i)
'''
# subscribe chanel
'''
pub = redis_client.pubsub()
pub.subscribe('fm101')
while True:
    print pub.parse_response()
'''

if __name__ == '__main__':
    import time

    for i in range(10):
        time.sleep(2)
        redis_publish('fm001', k='hello')
