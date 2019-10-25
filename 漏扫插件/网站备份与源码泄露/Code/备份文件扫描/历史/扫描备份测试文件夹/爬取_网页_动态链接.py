# -*- coding: utf-8 -*-
# @Time    : 2018/8/9 0009 13:36
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 爬取_网页_动态链接.py
# @Software: PyCharm
# coding:utf-8
import sys
import requests
import re
import threading
from multiprocessing.dummy import Pool as tp
from bs4 import BeautifulSoup as bs
import time
import random
reload(sys)
sys.setdefaultencoding('utf8')

print unicode('''

    你的网址放在url.txt里面

    带不带http都无所谓，算了你还是带上吧

    url.txt放在同一个目录

    双击启动

''', 'utf-8')

# time.sleep(5)

headerss = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

list_dir = list(set([x.replace('\n', '') if x.startswith('http')  else 'http://' + x.replace('\n', '') for x in open('url.txt', 'r').readlines()]))


def start(func):
    def inter(url):
        result = func(url)
        print unicode(('【当前线程:%s】 扫描网址 : ' + url) % threading.current_thread().name, 'utf-8')
        if result is None:
            pass
        else:
            with open('result.txt', 'a+')as a:
                for x in result:
                    a.write(str(x) + '\n')
        return result

    return inter


@start
def crawl_sql(urlx):
    if urlx.endswith('/'):
        url = urlx
    else:
        url = urlx+'/'
    dir_list=[]
    file_list=[]
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r = requests.get(url=url,headers=headers,timeout=10)
        bp = bs(r.content,'lxml')
        for _ in bp.find_all('a'):
            try:
                d = _['href']
            except Exception, e:
                #print e
                pass

            # 开始爬取目录
            if d and d!='':
                da = d.replace(url, '')
                if da.find('=') < 0 and da.find(':') < 0:
                    de = '/'+da
                    dex = de.split('/')[1]
                    #print de
                    #print 'url目录：'+dex
                    if dex.find('.')<0:
                        dir_list.append(dex)
                    else:
                        pass
            # 开始爬取链接
                if da.find('=') > 0 and da.find('?') > 0 and da.find('http:') < 0 and da.find('://') < 0 and da.find('javas') < 0 :
                    #print 'url网址：' + da
                    if da.startswith('/'):
                        url.strip('/')
                        file_list.append(url+da)
                    else:
                        file_list.append(url + da)
        if dir_list!=[]:
            dir_list=list(set(dir_list))
            for x in dir_list:
                try:
                    ra = requests.get(url=url+'/'+x+'/',headers=headers,timeout=10)
                    bp = bs(ra.content, 'lxml')
                    for _ in bp.find_all('a'):
                        try:
                            d = _['href']
                        except Exception, e:
                            #print e
                            pass
                        # 开始爬取链接.
                        if d and d!='':
                            da = d.replace(url, '')
                            if da.find('=') > 0 and da.find('?') > 0 and da.find('http:') < 0 and da.find('://') < 0 and da.find('javas') < 0 :
                                #print 'url网址：'+da
                                if da.startswith('/'):
                                    url.strip('/')
                                    file_list.append(url + da)
                                else:
                                    file_list.append(url + da)
                except Exception,e:
                    #print e
                    pass
    except Exception,e:
        #print e
        pass

    return list(set(file_list))



px = tp(processes=8)
# 开启8个线程池
px.map(crawl_sql, list_dir)
px.close()
px.join()




