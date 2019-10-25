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
import time
import requests
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
print '''
        txt is phpmy.txt
        and result is result.txt
        by lzyq

    '''
time.sleep(5)
list1 = []
with open('phpmy.txt','r')as f:
    for x in f:
        x1 = x.replace('\n','')
        list1.append(x1)
smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
def scan(urlx):
    url = urlx + '/phpmyadmin/index.php'
    try:
        r = requests.head(url)
        print url + '  ' + str(r.status_code)
        if r.status_code == 200:
            try:
                r1 = requests.get(url)
                if 'Documentation.html' in r1.content:
                    with open('result.txt','a+')as a:
                        a.write(url + '\n')
            except:
                pass
        else:
            pass
    except Exception,e:
        print e
        pass
listbp = list(set(list1))
pool = ThreadPool(processes=smxc)  #线程数量
result = pool.map(scan, listbp)
pool.close()
pool.join()
