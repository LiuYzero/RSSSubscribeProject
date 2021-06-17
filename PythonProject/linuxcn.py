# -*- coding:utf-8 -*-

import requests
from xmltodict3 import XmlTextToDict
import time

url = "https://linux.cn/rss.xml"

def get_rss_content_from_linuxcn(url):
    """
    从linux.cn网站的rss连接中解析订阅列表
    :param url: linux.cn rss link
    :return: rss_obj
    """
    try:
        response = requests.get(url, timeout=10)
        # print(response)
        if response.status_code != 200:
            return {}
        # print(response.text)
        json = XmlTextToDict(response.text, ignore_namespace=True).get_dict()
        # print(json)

        result = json["rss"]["channel"]

        author = result["title"]
        uri = result["link"][0]
        updated = result["pubDate"]

        entry_list = result["item"]
        articles = []
        for entry in entry_list:
            articles.append({
                "title": entry["title"],
                "summary": "too long, not show.",
                "url": entry["link"][0:entry["link"].find("?")],
                "updated": entry["pubDate"]
            })

        linuxcn_rss = {
            "author": author,
            "uri": uri,
            "updated": updated,
            "articles": articles
        }
    except Exception:
        pass
    # print(linuxcn_rss)
    return linuxcn_rss
get_rss_content_from_linuxcn(url)