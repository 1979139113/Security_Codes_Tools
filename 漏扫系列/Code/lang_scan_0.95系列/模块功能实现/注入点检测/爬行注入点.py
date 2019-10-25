# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# coding : utf-8
import requests
import re
url = 'http://www.sbzl.cn/'
def crawl_sql(sql):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        r_crawl = requests.get(url=sql,headers=headers,timeout=5).content
    except Exception,e:
        print e
    try:
        rx = re.search('(.*?)(.php\?|.asp\?|.apsx\?|.jsp\?)(.*?)=\d',r).group()
        print rx
        print '\n'
        print  url + rx.split('href="')[1]
    except Exception,e:
        print e