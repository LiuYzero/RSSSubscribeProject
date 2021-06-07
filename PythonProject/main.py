# -*- coding:utf-8 -*-

from redis_util import get_rss_link_db_key
from redis_util import get_rss_link
from linuxcn import get_rss_content_from_linuxcn
from cnblogs_rss import get_rss_content_from_cnblogs
from redis_util import set_rss_content
from redis_util import get_rss_content
import time

db_keys = get_rss_link_db_key()
for key in db_keys:
    rssLink = get_rss_link(key)
    print (rssLink)
    # print(type(rssLink['url']))
    author = rssLink['author']
    url = rssLink['url']
    # url = ""
    content = {}
    if url.find("linux.cn") != -1:
        content = get_rss_content_from_linuxcn(url)
        set_rss_content(author, content)
    if url.find("feed.cnblogs.com") != -1:
        content = get_rss_content_from_cnblogs(url)
        set_rss_content(author, content)

    # set_rss_content(author, content)
    # print(get_rss_content(author)['articles'])
    time.sleep(2)