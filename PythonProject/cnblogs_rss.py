# -*- coding:utf8 -*-

import requests
from xmltodict3 import XmlTextToDict


url = "https://feed.cnblogs.com/blog/u/408549/rss/"

def get_rss_content_from_url(url):
  """
  从cnblogs网站的rss链接中解析订阅列表
  :param url: cnblogs is rss link
  :return: rss_obj
  """
  response = requests.get(url=url)
  if response.status_code != 200:
    return {}
  json = XmlTextToDict(response.text, ignore_namespace=True).get_dict()
  # print(result)

  result = json["feed"]

  author = result["author"]["name"]
  uri = result["author"]["uri"]
  updated = result["updated"]

  entry_list = result["entry"]
  articles = []
  for entry in entry_list:
    articles.append({"title":entry["title"]["#text"], "summary":entry["summary"]["#text"], "url":entry["id"], "updated":entry["updated"]})

  cnblogs_rss = {
    "author":author,
    "uri":uri,
    "updated":updated,
    "articles":articles
  }

  return cnblogs_rss


article = get_rss_content_from_url(url)
print (article)

