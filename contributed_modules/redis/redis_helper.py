# -*- encoding:utf-8 -*-


import redis


class RedisHelper(object):
    def __init__(self, port=6379, host='127.0.0.1'):
        self.port = port
        self.host = host
        self.__conn = redis.Redis(host=self.host, port=self.port)

    def set(self, key, value):
        assert key
        self.__conn.set(key, value)
        return True

    def get(self, key):
        assert key
        return self.__conn.get(key)

    def keys(self, pattern='*'):
        return self.__conn.keys(pattern)

    def delete(self, *keys):
        return self.delete(keys)

    def subscribe(self, chanel):
        assert chanel
        pub = self.__conn.pubsub()
        pub.subscribe(chanel)
        if pub.parse_response():  # first validate connection
            # return chanel
            return pub
        return None

    def publish(self, chanel, message):
        assert chanel and message
        self.__conn.publish(chanel, message)
        return True


"""
TEST
"""
if __name__ == '__main__':
    r = RedisHelper()
    r.publish('fm001', 1)
    pub = r.subscribe('fm001')
    print pub
    while True:
        result = pub.parse_response()
        print result[2]
