# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 0004 12:08
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : webscancc.py
# @Software: PyCharm
import sys
import requests
import re
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.webscan.cc/?action=getip&domain=http://blog.webscan.cc'
r = requests.get(url)
ip = re.findall('{"ip":"(.*?)",',r.content)
print ip
ipp = str(ip).replace("'",'').replace('[','').replace(']','')
print ipp
url1 = 'http://www.webscan.cc/?action=query&ip='+''.join(ip)
print url1
r1 = requests.get(url1)
ip1 = re.findall('domain":"(.*?)",',r1.content)
for x in ip1:print x.replace('\\','')