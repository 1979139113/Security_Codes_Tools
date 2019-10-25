# -*- coding: utf-8 -*-
# @Time    : 2018/5/6 0006 10:47
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 爬行3-5.py
# @Software: PyCharm
import sys
import re
import random
import requests
import os
import threading
import time
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')

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



txt_ = str(raw_input(unicode('输入种子文件名称:(Example:url.txt):','utf-8').encode('gbk')))
smxc = int(input(unicode('设置扫描线程数(1-200):','utf-8').encode('gbk')))
timenow = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())+'.txt'
# f1 = open(timenow,'w')
# f1.close()
txt_name=list(set([i.replace("\n","") for i in open(txt_,"r").readlines()]))
def end_scan(url):
    liss = []
    #print unicode('开始深度连接爬行....', 'utf-8')
    uu = url.split('//')[1].split('/')[0]
    print 'Crawl: ' + uu
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r = requests.get(url=url,headers=headers,timeout=6).content
        r1 = re.findall('href="(.*?)"',r)
        r2 = re.findall(r'href=."/(.*?/.*?)"',r)
        r3 = re.findall('src="(.*?)" ', r)
        if r3:
            for x in r3:
                if uu in x:
                    diyi = x.split('://')[1].split('/')[1]
                    if uu in diyi:
                        pass
                    else:
                        dier = url + '/' + diyi + '/'
                        liss.append(dier)

        if r1:
            for x in r1:
                if uu in x and x.find('=')<0 and x.find('#')<0 and x.find('javascript')<0 :
                    if not '.' in x.split('/')[-1]:
                        if x.startswith('http://'):
                            if uu == x.split('//')[1].split('/')[0]:
                                #print x
                                liss.append(x)
                        else:
                            if uu == str('http://'+x.replace('//','')).split('//')[1].split('/')[0]:
                                xxxr = str('http://'+x.replace('//',''))
                                #print xxxr
                                liss.append(xxxr)

        if r2:
            for x in r2:
                #print x
                if x.find('.')>1 or x.find('www.')>0 or x.find('javascript')>0 or x.find('http')>0 or x.find(' ')>0:
                    pass
                else:
                    dd = x.split('/')[0]
                    liss.append(url+'/'+dd+'/')
                    dddd = x.split('/')[0:2]
                    e = '/'
                    for aa in dddd:
                        e+=aa+'/'
                    liss.append(url+e)
                    ddd = x.split('/')[0:3]
                    e = '/'
                    for aa in ddd:
                        e+=aa+'/'
                    liss.append(url+e)

    except Exception,e:
        print e

    for uiui in list(set(liss)):
        if 'http' in uiui:
            print uiui
            with open(timenow,'a+') as a:
                a.write(uiui + '\n')
    #             time.sleep(random.choice([0.1,0.2,0.4,0.5]))
# pool = ThreadPool(processes=int(smxc))
# pool.map(end_scan,txt_name)
# pool.close()
# pool.join()
for i in range(int(smxc)):
    for x in txt_name:
        t = threading.Thread(target=end_scan,args=(x,))
        t.start()
        t.join()