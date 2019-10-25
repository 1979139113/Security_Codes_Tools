# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 0004 8:55
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : get urls.py
# @Software: PyCharm
import sys
import chardet
import re
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://stackoverflow.com'
d1 = requests.get(url)
print d1.content
if isinstance(d1.content,unicode):
    pass
else:
    codesty = chardet.detect(d1.content)
    a = d1.content.decode(codesty['encoding'])
try:
    dd = re.search(u'[\u4e00-\u9fa5]',a)
    if dd.group():
        print dd.group()
except:
    print 'NO chinese'