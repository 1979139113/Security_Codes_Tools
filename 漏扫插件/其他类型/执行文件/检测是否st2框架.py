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
import random
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
waf = ['"404"','404 Not Found','ERROR PAGE','miibeian.gov.cn','permission','500','huwei','404','ERR_CONNECTION_ABORTED','safedog','not found','yunsuo','360','anquan','Security','ChinaCache-CDN']
st = ['VloginUser.action','Mail.action','code.action','reg.action','Address.action','!Index.action','login.action','Add.action','pageslist.action','.Action','Message.action','getMul.action','shouye.action','logout.action','Valid.action','search.action','Magazine.action','news.action','init.action','create.action','index2.action','default.action','welcome.action','Name.action','single.action','updateForm.action','SysStart.action','adminlogin.action','Offportal.action','Buying.action','Success.action','exchange.action','menu.action','airport.action','Email.action','On.action','show.action','tain.action','randomPicture.action','news.do']
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



def scanst2(xxxxx):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        url = xxxxx
        for houzhui in st:
            urlx = url + '/' + str(houzhui)
            #print urlx
            req = requests.head(url=urlx,headers=headers,timeout=5,allow_redirects=False)
            print urlx + " : " + str(req.status_code)
            if req.status_code == 200:
                reqst = requests.get(url=urlx,headers=headers,timeout=5,verify=False,allow_redirects=False)
                if reqst.status_code == 200 and str('.action') in reqst.content:
                    for x in waf:
                        #print x
                        if x not in reqst.content:
                            with open('st2.txt','a+')as aa:
                                aa.write(urlx + '\n')
                        else:
                            pass
                else:
                    pass
            else:
                 pass
    except Exception,e:
        print e
smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
url_list=list(set([i.replace("\n","") for i in open("url.txt","r").readlines()]))
pool = ThreadPool(processes=smxc)  #线程数量
result = pool.map(scanst2, url_list)
pool.close()
pool.join()