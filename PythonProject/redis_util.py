# -*- coding:utf8 -*-

"""
Redis 工具类
"""

from redis import StrictRedis
import json


def string2bytes(str):
    return bytes(str, encoding="utf-8")

def bytes2string(bytes):
    return str(bytes, encoding="utf-8")

redis = StrictRedis(host='localhost', port=6379, db=0, password='redispass')

redis_tab = "RSSSubscribeLink"
rss_link = {"author": "古明地", "url": "https://feed.cnblogs.com/blog/u/408549/rss/"}
redis.hset(redis_tab, rss_link["author"], json.dumps(rss_link))
keys = [bytes2string(item) for item in redis.hkeys(string2bytes(redis_tab))]
redis.close()