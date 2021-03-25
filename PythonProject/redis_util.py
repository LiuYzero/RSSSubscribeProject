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

# redis = StrictRedis(host='localhost', port=6379, db=0, password='redispass')

# redis_tab = "RSSSubscribeLink"
# rss_link = {"author": "古明地", "url": "https://feed.cnblogs.com/blog/u/408549/rss/"}
# redis.hset(redis_tab, rss_link["author"], json.dumps(rss_link))
# keys = [bytes2string(item) for item in redis.hkeys(string2bytes(redis_tab))]
# print(keys)
# redis.close()

host = "localhost"
port = 6379
db=0
password="redispass"
rss_link_db = "RSSSubscribeLink"

def insert_rss_link(name, url):
    """
    向RSSSubscribeLink插入标注和rss链接
    :param name: rss标注
    :param url: rss链接
    :return: True / False
    """
    try:
        redis = StrictRedis(host=host, port=port, db=db, password=password)
        rss_link = {"author":name, "url":url}
        redis.hset(rss_link_db, rss_link["author"], json.dumps(rss_link))
        redis.close()
        return True
    except :
        print ("insert_rss_link %s %s throw exception, please check it." % (name, url))
        if redis:
            redis.close()
        return False

def get_rss_link_db_key():
    """
    获取RSSSubscribeLink下的所有rss标注，即keys
    :return: [rss_name...]
    """
    try:
        redis = StrictRedis(host=host, port=port, db=db, password=password)
        keys = [bytes2string(item) for item in redis.hkeys(string2bytes(rss_link_db))]
        redis.close()
        return keys
    except :
        print ("get_rss_link_db_key throw exception, please check it." )
        if redis:
            redis.close()
        return []

def get_rss_link(key):
    """
    获取RSSSubscribeLink下具体rss_link
    :param key: rss的作者，即key
    :return: key对应的rss_link
    """
    try:
        redis = StrictRedis(host=host, port=port, db=db, password=password)
        obj = bytes2string(redis.hget(rss_link_db, string2bytes(key)))
        obj = json.loads(obj)
        # rss_link = {
        #     "author":key,
        #     "url":obj['url']
        # }
        return obj
    except :
        print ("get_rss_link_db_key throw exception, please check it." )
        if redis:
            redis.close()
        return {}
