# **coding: utf8**
import redis


REDIS_CACHE = {
    'host': '120.77.38.20',
    'port': 6379,
    'db': 0
}


def get_cache_redis():
    """
    redis 缓存
    """
    return redis.Redis(
        host=REDIS_CACHE['host'],
        port=REDIS_CACHE['port'],
        db=REDIS_CACHE['db']
    )

# get_cache_redis().set('name', 'mcc')
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
