# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 0009 13:37
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : test_002.py
# @Software: PyCharm
import sys
import requests
import re
from bs4 import BeautifulSoup as bs
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://www.php-factory.net'

def crawl_sql(urlx):
    if urlx.endswith('/'):
        url = urlx
    else:
        url = urlx+'/'
    print url
    dir_list=[]
    file_list=[]
    try:
        r = requests.get(url=url,timeout=10)
        print r.status_code
        bp = bs(r.content,'lxml')
        for _ in bp.find_all('a'):
            try:
                d = _['href']
            except Exception, e:
                print e
            # 开始爬取目录
            if d and d!='':
                da = d.replace(url, '')
                if da.find('=') < 0 and da.find(':') < 0:
                    de = '/' + da
                    de = de.split('/')[1]
                    #print de
                    print 'url目录：'+de
                    dir_list.append(de)
            # 开始爬取链接
                if da.find('=') > 0 and da.find('?') > 0 and da.find('http:') < 0 and da.find('://') < 0 and da.find('javas') < 0 :
                    print 'url网址：' + da
                    file_list.append(url+da)
        if dir_list!=[]:
            dir_list=list(set(dir_list))
            for x in dir_list:
                try:
                    ra = requests.get(url=url+'/'+x+'/',timeout=10)
                    bp = bs(ra.content, 'lxml')
                    for _ in bp.find_all('a'):
                        try:
                            d = _['href']
                        except Exception, e:
                            print e
                        # 开始爬取链接.
                        if d and d!='':
                            da = d.replace(url, '')
                            if da.find('=') > 0 and da.find('?') > 0 and da.find('http:') < 0 and da.find('://') < 0 and da.find('javas') < 0 :
                                print 'url网址：'+da
                                file_list.append(url + da)
                except Exception,e:
                    print e
    except Exception,e:
        print e
    return list(set(file_list))

crawl_sql(url)