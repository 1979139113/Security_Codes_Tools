# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 0008 14:56
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 判断字符串相似度.py
# @Software: PyCharm
import difflib
import requests
url_0 = 'http://www.langzi.fun/56454'
url_1 = 'http://www.langzi.fun/admin/666'
url_2 = 'http://www.langzi.fun/'

def content(url):
    return requests.get(url).content
url_0_ = content(url_0)
url_1_ = content(url_1)
url_2_ = content(url_2)

print(difflib.SequenceMatcher(None, url_1_, url_0_).quick_ratio())
print(difflib.SequenceMatcher(None, url_1_, url_2_).quick_ratio())

