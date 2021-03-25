# -*- coding:utf-8 -*-

from redis_util import get_rss_link_db_key
from redis_util import get_rss_link


db_keys = get_rss_link_db_key()
for key in db_keys:
    print (get_rss_link(key))