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
import random
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
list_rar=list(set([i.replace("\n","") for i in open("rar.txt","r").readlines()]))
houzui = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt']
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
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24" ]
def scan(urlx):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    url1 = urlx + '/.svn/entries'
    try:
        r = requests.head(url=url1,headers=headers,timeout=5)
        print r.url + " : " + str(r.status_code)
        if r.status_code == 200:
            try:
                r1 = requests.get(url=url1,headers=headers,timeout=5)
                print r1.content
                print '#####################################'
                if 'dir' and 'svn' in r1.content:
                    if r1.status_code != 3368 and r1.status_code != 888 and r1.status_code != 927 and r1.status_code != 266 and r1.status_code != 3383 and r1.status_code != 522 and r1.status_code != 915 and r1.status_code != 264 and r1.status_code != 417 and r1.status_code != 960:
                        if 'found' and 'ERROR' and 'JumpSelf' in r1.content:
                            pass
                        else:
                            with open('svn.txt','a+')as a:
                                a.write(url1 + '\n')
                    else:
                        pass

                else:
                    pass
            except Exception,e:
                print e
        else:
            pass
    except Exception,e:
        print e
    url2 = urlx + '/.git/config'
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r3 = requests.head(url=url2,headers=headers,timeout=5)
        print r3.url + " : " + str(r3.status_code)
        if r3.status_code == 200:
            try:
                r4 = requests.get(url=url2,headers=headers,timeout=5)
                print r4.content
                print '#####################################'
                if 'repositoryformatversion' in r4.content:
                    with open('git.txt','a+')as aa:
                        aa.write(url2 + '\n')
                else:
                    pass
            except Exception,e:
                print e
        else:
            pass
    except Exception,e:
        print e

########################################################
    url_3 = urlx + '/' + urlx.split(".",2)[1]
    for x in houzui:
        url3 = url_3 + str(x)
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r5 = requests.head(url=url3,headers=headers,timeout=5)
            print r5.url + ' : ' + str(r5.status_code) + ' : ' + str(r5.headers["Content-Length"])
            try:
                if int(r5.headers["Content-Length"]) > 18888:
                    with open('bf.txt','a+')as aaa:
                        aaa.write(url3 + '\n')
                else:
                    pass
            except Exception,e:
                print e
        except Exception,e:
            print e
#########################################################
    for x in list_rar:
        url4 = urlx + x.replace('\n','')
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r6 = requests.head(url=url4,headers=headers,timeout=5)
            print r6.url + " : " + str(r6.status_code) + ' : ' + str(r6.headers["Content-Length"])
            try:
                if int(r6.headers["Content-Length"]) > 18888:
                    with open('bf.txt','a+')as aaa:
                        aaa.write(url4 + '\n')
                else:
                    pass
            except Exception,e:
                print e
        except Exception,e:
            print e
    url5 = urlx + '/WEB-INF/web.xml'
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r7 = requests.head(url=url5,headers=headers,timeout=5)
        print r7.url + " : " + str(r7.status_code)
        if r7.status_code == 200:
            try:
                r8 = requests.get(url=url5,headers=headers,timeout=5)
                print r8.content
                print '#####################################'
                if '<web-app' in r8.content:
                    with open('webinf.txt','a+')as aa:
                        aa.write(url5 + '\n')
                else:
                    pass
            except Exception,e:
                print e
        else:
            pass
    except Exception,e:
        print e

smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
url_list=list(set([i.replace("\n","") for i in open("url.txt","r").readlines()]))
pool = ThreadPool(processes=smxc)  #线程数量
result = pool.map(scan, url_list)
pool.close()
pool.join()