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
import pymysql
import random
import socket
import ConfigParser
import hashlib
import urllib2
import codecs
import requests
import re
import datetime
import time
import threading
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 5
socket.setdefaulttimeout(timeout)
cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
New_start=cfg.get("Config","new_start")
Rarscan=cfg.get("Config","rarscan")
St2scan=cfg.get("Config","st2scan")
Cmsscan=cfg.get("Config","cmsscan")
Urlcj= cfg.get("Config","urlcaiji")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")
print '''

        |    __   __   __  
        |_, (__( |  ) (__| 
                       __/ 
        QQ:982722261

'''
time.sleep(3)

global black
global coon
global list002
global list_zairu
global list_zairust
global list_zairucms
global list_zairurar
global waf
waf = ['"404"','404 Not Found','ERROR PAGE','miibeian.gov.cn','permission','500','huwei','404','ERR_CONNECTION_ABORTED','safedog','not found','yunsuo','360','anquan','Security','ChinaCache-CDN']
list_zairu=[]
list_zairurar=[]
list_zairucms=[]
list_zairust=[]
black = []
with open('black.txt','r')as f:
    for x in f:
        black.append(x.replace('\n',''))

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

list007 = []
#/'>




def urlcaiji007(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        req = requests.get(url=url,headers=headers,timeout=5,allow_redirects=False)
    except Exception,e:
        print e

    try:
        r1 = re.findall('http.*?cn">',req.content)
        r1s = re.findall("http.*?cn/'>", req.content)
        r1ss = re.findall('http.*?cn/"', req.content)
        try:
            for x in r1:
                x1 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
                if ' ' in x1:
                    pass
                else:
                    list007.append(x1)
                    print x1
        except:
            pass
        try:
            for xs in r1s:
                x1s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
                if ' ' in x1s:
                    pass
                else:
                    list007.append(x1s)
                    print x1s
        except:
            pass
        try:
            for xsss in r1ss:
                x1ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
                if ' ' in x1ss:
                    pass
                else:
                    list007.append(x1ss)
                    print x1ss
        except:
            pass
    except Exception,e:
        pass

    try:
        r2 = re.findall('http.*?com">',req.content)
        r2s = re.findall("http.*?com/'>", req.content)
        r2ss = re.findall('http.*?com/"', req.content)
        for x in r2:
            x2 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x2:
                pass
            else:
                list007.append(x2)
                print x2
        for xs in r2s:
            x2s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x2s:
                pass
            else:
                list007.append(x2s)
                print x2s
        for xsss in r2ss:
            x2ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x2ss:
                pass
            else:
                list007.append(x2ss)
                print x2ss
    except Exception,e:
        pass


    try:
        r3 = re.findall('http.*?org">',req.content)
        r3s = re.findall("http.*?org/'>", req.content)
        r3ss = re.findall('http.*?org/"', req.content)
        for x in r3:
            x3 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x3:
                pass
            else:
                list007.append(x3)
                print x3
        for xs in r3s:
            x3s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x3s:
                pass
            else:
                list007.append(x3s)
                print x3s
        for xsss in r3ss:
            x3ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x3ss:
                pass
            else:
                list007.append(x3ss)
                print x3ss
    except Exception,e:
        pass

    try:
        r4 = re.findall('http.*?cc">',req.content)
        r4s = re.findall("http.*?cc/'>", req.content)
        r4ss = re.findall('http.*?cc/"', req.content)
        for x in r4:
            x4 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x4:
                pass
            else:
                list007.append(x4)
                print x4
        for xs in r4s:
            x4s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x4s:
                pass
            else:
                list007.append(x4s)
                print x4s
        for xsss in r4ss:
            x4ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x4ss:
                pass
            else:
                list007.append(x4ss)
                print x4ss
    except Exception,e:
        pass

    try:
        r5 = re.findall('http.*?net">',req.content)
        r5s = re.findall("http.*?net/'>", req.content)
        r5ss = re.findall('http.*?net/"', req.content)
        for x in r5:
            x5 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x5:
                pass
            else:
                list007.append(x5)
                print x5
        for xs in r5s:
            x5s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x5s:
                pass
            else:
                list007.append(x5s)
                print x5s
        for xsss in r5ss:
            x5ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x5ss:
                pass
            else:
                list007.append(x5ss)
                print x5ss
    except Exception,e:
        pass


if int(New_start) == 1:
    wenbenzairu = str(raw_input(unicode('输入当前目录下要导入的原始网址文本名称:', 'utf-8').encode('gbk')))
    time.sleep(0.5)
    print unicode('\n***外部链接载入成功***', 'utf-8')
    time.sleep(1)
    yuanshilist = []
    with open(wenbenzairu,'r')as f:
        for f0 in f:
            yuanshilist.append(f0.replace('\n',''))
            #time.sleep(3)
    print unicode('正在提取外链，请稍等...', 'utf-8')
    for x in yuanshilist:
        urlcaiji007(x)
    list008 = list(set(list007))
    print unicode('***原始外链提取成功***', 'utf-8')
    time.sleep(1)
    for uxxx in list008:
        print str(uxxx) + '---Get'
    cfg.set("Config", "New_start",0)
    cfg.write(open('config.ini', 'w'))
    if len(list008) < 5:
        print unicode('提取原始外链数量小于5,可能会出现无限爬行重复,建议重启程序修改配置文件并更换新的外链', 'utf-8')
        time.sleep(6)
    else:
        pass
    try:
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        coon = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cur = coon.cursor(pymysql.cursors.SSCursor)
        #listzhao = []
        for x0x in black:
            for xxx8 in list008:
                xxx9 = xxx8.split('.')[-1]
                xxx10 = xxx8.split('.')[-2]
                xxx11 = xxx10 + '.' + xxx9
                print 'houzhui:' + xxx11
                print xxx11 + '   ' + x0x
                if str(xxx11) == str(x0x):
                    list008.remove(xxx8)
                else:
                    pass
        #listhan = list(set(list008))
        for xx in list008:
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                urlxieru = requests.head(url=str(xx),headers=headers,timeout=3)
                if urlxieru.status_code == 200:
                    print str(xx) + '  ' + str(urlxieru.status_code)
                    sql001 = "INSERT INTO url_2 (urllist,cmsscan,rarscan,st2,gettime) VALUES (%s,%s,%s,%s,%s)"
                    sql = "INSERT INTO url_1(urllist,urlget,urltime) VALUES ('" + str(xx) + "','" + str(0) + "','" + str(timenow) + "')"
                    cur.execute(sql)
                    coon.commit()
                    cur.execute(sql001,(str(xx),0,0,0,str(timenow)))
                    coon.commit()

                else:
                    print str(xx) + '  ' + str(urlxieru.status_code)
                    pass
            except:
                pass

        cur.close()
        coon.close()

    except:
        print unicode('无法写入数据库，请检查配置文件及系统环境', 'utf-8')
        time.sleep(300)
else:
    pass





#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

#开始无限采集url  可以使用单线程

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

def wuxiancaiji(url):
    list002=[]
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        req = requests.get(url=url,headers=headers,timeout=5,allow_redirects=False)
    except :
        pass
    try:
        r1 = re.findall('http.*?cn">',req.content)
        r1s = re.findall("http.*?cn/'>", req.content)
        r1ss = re.findall('http.*?cn/"', req.content)
        try:
            for x in r1:
                x1 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
                if ' ' in x1:
                    pass
                else:
                    list002.append(x1)
        except:
            pass
        try:
            for xs in r1s:
                x1s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
                if ' ' in x1s:
                    pass
                else:
                    list002.append(x1s)
        except:
            pass
        try:
            for xsss in r1ss:
                x1ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
                if ' ' in x1ss:
                    pass
                else:
                    list002.append(x1ss)
        except:
            pass
    except Exception,e:
        pass

    try:
        r2 = re.findall('http.*?com">',req.content)
        r2s = re.findall("http.*?com/'>", req.content)
        r2ss = re.findall('http.*?com/"', req.content)
        for x in r2:
            x2 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x2:
                pass
            else:
                list002.append(x2)
        for xs in r2s:
            x2s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x2s:
                pass
            else:
                list002.append(x2s)
        for xsss in r2ss:
            x2ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x2ss:
                pass
            else:
                list002.append(x2ss)
    except Exception,e:
        pass


    try:
        r3 = re.findall('http.*?org">',req.content)
        r3s = re.findall("http.*?org/'>", req.content)
        r3ss = re.findall('http.*?org/"', req.content)
        for x in r3:
            x3 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x3:
                pass
            else:
                list002.append(x3)
        for xs in r3s:
            x3s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x3s:
                pass
            else:
                list002.append(x3s)
        for xsss in r3ss:
            x3ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x3ss:
                pass
            else:
                list002.append(x3ss)
    except Exception,e:
        pass

    try:
        r4 = re.findall('http.*?cc">',req.content)
        r4s = re.findall("http.*?cc/'>", req.content)
        r4ss = re.findall('http.*?cc/"', req.content)
        for x in r4:
            x4 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x4:
                pass
            else:
                list002.append(x4)
        for xs in r4s:
            x4s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x4s:
                pass
            else:
                list002.append(x4s)
        for xsss in r4ss:
            x4ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x4ss:
                pass
            else:
                list002.append(x4ss)
    except Exception,e:
        pass

    try:
        r5 = re.findall('http.*?net">',req.content)
        r5s = re.findall("http.*?net/'>", req.content)
        r5ss = re.findall('http.*?net/"', req.content)
        for x in r5:
            x5 = x.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x5:
                pass
            else:
                list002.append(x5)
        for xs in r5s:
            x5s = xs.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x5s:
                pass
            else:
                list002.append(x5s)
        for xsss in r5ss:
            x5ss = xsss.replace('%3A%2F%2F','//').replace('\/\/','//').replace('">','').replace("/'>","").replace('/"','')
            if ' ' in x5ss:
                pass
            else:
                list002.append(x5ss)
    except Exception,e:
        pass

    list003 = list(set(list002))
    if len(list003) != 1:
        try:
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cooncaiji1 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
            curcaiji1 = cooncaiji1.cursor(pymysql.cursors.SSCursor)
            #listzhao = []
            #print unicode('正在筛选wangzhi')
            for x0x in black:
                for xxx8 in list003:
                    xxx9 = xxx8.split('.')[-1]
                    xxx10 = xxx8.split('.')[-2]
                    xxx11 = xxx10 + '.' + xxx9
                    if str(xxx11) == str(x0x):
                        list003.remove(xxx8)
                    else:
                        pass
            #listhan = list(set(list003))
            for xxx in list003:
                try:
                    UA = random.choice(headerss)
                    headers = {'User-Agent': UA}
                    xieru2 = requests.head(url=str(xxx),headers=headers,timeout=3)
                    if xieru2.status_code == 200:
                        print str(threading.current_thread().name) + ' ' + str(xxx) + '  ' + str(xieru2.status_code)
                        #sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                        sqlcaiji1 = "INSERT INTO url_2 (urllist,cmsscan,rarscan,st2,gettime) VALUES (%s,%s,%s,%s,%s)"
                        sqlcaiji1_1 = "INSERT INTO url_1 (urllist,urlget,urltime) VALUES (%s,%s,%s)"
                        curcaiji1.execute(sqlcaiji1,(str(xxx),0,0,0,str(timenow)))
                        cooncaiji1.commit()
                        curcaiji1.execute(sqlcaiji1_1,(str(xxx),0,str(timenow)))
                        cooncaiji1.commit()
                    else:
                        print str(threading.current_thread().name) + ' ' + str(xxx) + '  ' + str(xieru2.status_code)
                except:
                    pass
            curcaiji1.close()
            cooncaiji1.close()
        except Exception,e:
            print unicode('爬行到的网址无法存储数据库，请检查配置文件及系统环境', 'utf-8')
            print e
    else:
        pass

#从数据库中提取5个的外链载入无线采集当中
#载入无线采集函数
# def zairu():
#     list_zairu = []
#     try:
#         coon = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
#         cur = coon.cursor(pymysql.cursors.SSCursor)
#         sql = "select urllist from url_1 where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
#         sql1 = "update url_1 set urlget='1' where urlget = 0 limit 1"
#         cur.execute(sql)
#         coon.commit()
#         print unicode('[-]数据库激活，提取网址', 'utf-8')
#         curs = cur.fetchone()
#         for xx in curs:
#             print xx + '\n'
#             xxx1 = xx.replace("('","").replace("',)","")
#             print 'Url:' + str(xxx1)
#             list_zairu.append(xxx1)
#         cur.execute(sql1)
#         coon.commit()
#         print list_zairu
#         print '**--**--**--'
#         for xxxx in list_zairu:
#             # print 'test:' + str(xxxx)
#             wuxiancaiji(xxxx)
#         cur.close()
#         coon.close()
#     except Exception,e:
#         print e
#
# time.sleep(3)
def zairu():
    list_zairu = []
    try:
        cooncaiji2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcaiji2 = cooncaiji2.cursor()
        sqlcaiji2 = "select urllist from url_1 where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sqlcaiji2_1 = "update url_1 set urlget='1' where urlget = 0 limit 1"
        curcaiji2.execute(sqlcaiji2)
        cooncaiji2.commit()
        #print cur
        # print unicode('[-]数据库激活，提取网址', 'utf-8')
        curscaiji = curcaiji2.fetchone()
        for xx in curscaiji:
            xxx1aiji = xx.replace("('","").replace("',)","")
            #print 'Url:' + str(xxx1aiji)
            list_zairu.append(xxx1aiji)
        curcaiji2.execute(sqlcaiji2_1)
        cooncaiji2.commit()
        curcaiji2.close()
        cooncaiji2.close()
        for xxxx in list_zairu:
            # print 'test:' + str(xxxx)
            wuxiancaiji(xxxx)
    except Exception,e:
        print unicode('原始网址已经爬行完毕，请添加新的原始网址，使用方法详见帮助文档', 'utf-8')
        time.sleep(3)
        print e



#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

#扫描使用st2的网站

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
def scanst2(xxxxx):
    #print unicode('\n ***开始ST2扫描***', 'utf-8')
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        url = xxxxx
        for houzhui in st:
            urlx = url + '/' + str(houzhui)
            #print urlx
            req = requests.head(url=urlx,headers=headers,timeout=5,allow_redirects=False)
            if req.status_code == 200:
                reqst = requests.get(url=urlx,headers=headers,timeout=5,verify=False,allow_redirects=False)
                if reqst.status_code == 200 and str('.action') in reqst.content:
                    for x in waf:
                        #print x
                        if x not in reqst.content:
                            print  str(threading.current_thread().name) + ' ' + '[+]' + urlx + ' :ST2 found' + ' [' +str(reqst.status_code) + ']'
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coonst1 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
                                curst1 = coonst1.cursor(pymysql.cursors.SSCursor)
                                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                                sqlst1 = "INSERT INTO url_5 (urllist,st,st2time) VALUES (%s,%s,%s)"
                                curst1.execute(sqlst1, (str(urlx),str(reqst.status_code),str(timenow)))
                                coonst1.commit()
                                curst1.close()
                                coonst1.close()
                                break
                            except Exception,e:
                                print unicode('ST2数据无法写入数据库，请检查配置文件及系统环境', 'utf-8')
                                print e
                        else:
                            pass
                else:
                    pass
            else:
                 print str(threading.current_thread().name) + ' ' +  urlx + '  ' + str(req.status_code)
    except Exception,e:
        print e


def st2tiqu():
    list_zairust = []
    try:
        coonst2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curst2 = coonst2.cursor()
        sqlst2 = "select urllist from url_2 where st2=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sqlst2_1 = "update url_2 set st2='1' where st2 = 0 limit 1"
        curst2.execute(sqlst2)
        coonst2.commit()
        try:
            #print unicode('[-]数据库激活，提取网址', 'utf-8')
            cursst2 = curst2.fetchone()
            for xx in cursst2:
                xxx1st2 = xx.replace("('","").replace("',)","")
                #print 'Url:' + str(xxx1st2)
                list_zairust.append(xxx1st2)
            curst2.execute(sqlst2_1)
            coonst2.commit()
            curst2.close()
            coonst2.close()
            for xxxxx in list_zairust:
                # print 'test:' + str(xxxxx)
                scanst2(xxxxx)
        except Exception,e:
            print unicode('ST2网址已经爬行完毕，请添加新的原始网址，使用方法详见帮助文档', 'utf-8')
            print e

    except Exception,e:
        print unicode('当前数据库ST2扫描已经全部扫描完毕', 'utf-8')
        print e


#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

#扫描备份文件

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass

def scanrar(xxxxxx):       #开始构建扫描函数
    #print unicode('\n ***开始备份文件SVN扫描*** \n', 'utf-8')
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    with open('rar.txt','r')as f:
        for rarhouzhui in f:
            yumingrar = str(xxxxxx) + str(rarhouzhui)
            #print
            try:    #域名rarzip扫描
                openerrar = urllib2.build_opener(RedirectHandler)
                reqryumingrar = urllib2.Request(url=yumingrar,headers=headers)
                ryumingrar = openerrar.open(reqryumingrar)
                print str(threading.current_thread().name) + ' ' + str(yumingrar).replace('\n','  ') + str(ryumingrar.code)
                if ryumingrar.code == 200:
                    metarar = ryumingrar.info()
                    sizerar = str(metarar.getheaders("Content-Length")[0])  #文件大小
                    sizerar1 = int(metarar.getheaders("Content-Length")[0])
                    if sizerar1 > 1800000:
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coonrar1 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
                            currar1 = coonrar1.cursor(pymysql.cursors.SSCursor)
                            # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                            sql1rar1 = "INSERT INTO url_4 (urllist,rarsize,rartime) VALUES (%s,%s,%s)"
                            currar1.execute(sql1rar1, (str(yumingrar), str(sizerar),str(timenow)))
                            coonrar1.commit()
                            currar1.close()
                            coonrar1.close()
                        except Exception, e:
                            print e
                    else:
                        pass
                else:
                    #print str(yumingrar) + ': ' + str(sizerar)
                    pass
            except Exception,e:
                    print str(threading.current_thread().name) + ' ' +  str(yumingrar).replace('\n','   ') + str(e)
                    pass

    yumingsvn = str(xxxxxx) + '/.svn/entries'
    #print yumingsvn
    try:  # svn漏洞扫描
        openersvn = urllib2.build_opener(RedirectHandler)
        reqryumingsvn = urllib2.Request(url=yumingsvn, headers=headers)
        ryumingsvn = openersvn.open(reqryumingsvn)
        print str(threading.current_thread().name) + ' ' +  str(yumingsvn).replace('\n','  ') + str(ryumingsvn.code)
        if ryumingsvn.code == 200:
            metasvn = ryumingsvn.info()
            sizesvn = str(metasvn.getheaders("Content-Length")[0])
            sizesvn1 = int(metasvn.getheaders("Content-Length")[0])
            if 'dir' and 'svn' in ryumingsvn.read():
                if sizesvn1 != 3368 and sizesvn1 != 888 and sizesvn1 != 927 and sizesvn1 != 266 and sizesvn1 != 3383 and sizesvn1 != 522 and sizesvn1 != 915 and sizesvn1 != 264 and sizesvn1 != 417 and sizesvn1 != 960:
                    if 'found' and 'ERROR' and 'JumpSelf' in ryumingsvn.read():
                        print str(threading.current_thread().name) + ' ' +  str(yumingsvn) + ': ' + str(sizesvn)
                    else:
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coonrar11 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                            currar11 = coonrar11.cursor(pymysql.cursors.SSCursor)
                            # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                            sql1rar2 = "INSERT INTO url_4 (urllist,rarsize,rartime) VALUES (%s,%s,%s)"
                            currar11.execute(sql1rar2, (str(yumingsvn), str(sizesvn),str(timenow)))
                            coonrar11.commit()
                            currar11.close()
                            coonrar11.close()
                        except Exception,e:
                            print e
                else:
                    pass
            else:
                pass
    except Exception,e:
        print str(threading.current_thread().name) + ' ' +  str(yumingsvn).replace('\n','   ') + str(e)
    try:
        dutehouzhui = str(xxxxxx).split(".",2)[1]
        yumingrarzip = str(xxxxxx) + '/' + str(dutehouzhui) + '.rar'
        #print yumingrarzip
        try:  # 域名rarzip扫描
            openerrar = urllib2.build_opener(RedirectHandler)
            reqryumingrar = urllib2.Request(url=yumingrarzip, headers=headers)
            ryumingrar = openerrar.open(reqryumingrar)
            print str(threading.current_thread().name) + ' ' +  str(yumingrarzip).replace('\n','  ') + str(ryumingrar.code)
            if ryumingrar.code == 200:
                metarar = ryumingrar.info()
                sizerar = str(metarar.getheaders("Content-Length")[0])  # 文件大小
                sizerar1 = int(metarar.getheaders("Content-Length")[0])
                if sizerar1 > 1800000:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coonrar112 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
                        currar112 = coonrar112.cursor(pymysql.cursors.SSCursor)
                        # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                        sql1rar3 = "INSERT INTO url_4 (urllist,rarsize,rartime) VALUES (%s,%s,%s)"
                        currar112.execute(sql1rar3, (str(yumingrarzip), str(sizerar),str(timenow)))
                        coonrar112.commit()
                        currar112.close()
                        coonrar112.close()
                    except Exception, e:
                        print e
                else:
                    pass
            else:
                pass
        except Exception,e:
            print e
    except Exception, e:
        print str(threading.current_thread().name) + ' ' +  str(yumingrarzip).replace('\n','   ') + str(e)
        pass



def rartiqu():
    list_zairurar = []
    try:
        coonrar2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        currar2 = coonrar2.cursor()
        sql = "select urllist from url_2 where rarscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2 set rarscan='1' where rarscan = 0 limit 1"
        currar2.execute(sql)
        coonrar2.commit()
        try:
            #print unicode('[-]数据库激活，提取网址', 'utf-8')
            cursrar = currar2.fetchone()
            for xx in cursrar:
                xxx1rar = xx.replace("('","").replace("',)","")
                #print 'Url:' + str(xxx1rar)
                list_zairurar.append(xxx1rar)
            currar2.execute(sql1)
            coonrar2.commit()
            currar2.close()
            coonrar2.close()
            for xxxxxx in list_zairurar:
                scanrar(xxxxxx)
        except Exception,e:
            print e
    except Exception,e:
        print e




#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

#扫描CMS

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
def scancms(xxxxxxx):       #开始构建扫描函数
    #print unicode('\n ***开始CMS识别扫描*** \n', 'utf-8')
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    f = codecs.open('cms.txt', 'r', 'gbk')
    for cmsxx in f.readlines():
        cmshouzhui = cmsxx.split('|', 3)[0]
        cmsmd5 = cmsxx.split('|', 3)[2]
        cmsname = cmsxx.split('|', 3)[1]
        urlcms = str(xxxxxxx) + str(cmshouzhui)

        try:
            req1 = requests.head(url=urlcms,headers=headers,timeout=5,allow_redirects=False)
            print str(threading.current_thread().name) + ' ' +  str(urlcms) + '  ' + str(req1.status_code)
            if req1.status_code == 200:
                #print cmshouzhui + ' ' + cmsname + '  ' + cmsmd5
                req2 = requests.get(url=urlcms,headers=headers,timeout=5,allow_redirects=False)
                md5 = hashlib.md5()
                md5.update(req2.content)
                rmd5 = md5.hexdigest()
                #print rmd5
                #print str(urlcms) + ': ' + str(mmd)
                if rmd5 == cmsmd5:
                    print cmsname + 'Found'
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        cooncms1 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
                        curcms1  = cooncms1 .cursor(pymysql.cursors.SSCursor)
                        # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                        sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                        curcms1 .execute(sql1cms, (str(xxxxxxx),str(urlcms),str(cmsname),str(timenow)))
                        cooncms1.commit()
                        curcms1 .close()
                        cooncms1 .close()
                    except Exception, e:
                        print e
            else:
                pass
        except Exception,e:
            print e
    try:
        url = str(xxxxxxx) + '/robots.txt'
        req2 = requests.get(url=url,headers=headers,timeout=3,allow_redirects=False)
        #print url + '  ' + str(req2.status_code)
        if 'mlecms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('mlecms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'ecshop' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('ecshop'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'finecms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('finecms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'OurPhp' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('OurPhp'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'pageadmin' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('pageadmin'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'PHPWind' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('PHPWind'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Webnet' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Webnet'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'cutecms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('cutecms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Yidacms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Yidacms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Discuz' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Discuz'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'kingcms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('kingcms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'shopxp' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('shopxp'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'JeeCMS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('JeeCMS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'aspcms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('aspcms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif '86cms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('86cms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'dedecms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('dedecms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'metinfo' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('metinfo'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'joomla' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('joomla'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'AppCms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('AppCms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'PHPCMS v9' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('PHPCMS v9'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'emlog' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('emlog'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'DuomiCMS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('DuomiCMS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Trunkey' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Trunkey'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'phpmps' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('phpmps'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Zabbix' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Zabbix'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'expocms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('expocms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'EspCMS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('EspCMS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'wordpress' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('wordpress'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'dvbbs' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('dvbbs'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'EmpireCMS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('EmpireCMS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'FengCms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('FengCms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'phpweb' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('phpweb'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif '程氏舞曲CMS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('程氏舞曲CMS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'JBOOS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('JBOOS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'KesionCMS' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('KesionCMS'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Powereasy' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Powereasy'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif '74cms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('74cms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'qiboSoft' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('qiboSoft'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'siteserver' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('siteserver'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'maccms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('maccms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Yongyou' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Yongyou'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'actcms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('actcms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'maxcms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('maxcms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e

        ###########################################################
        elif 'DayuCms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('DayuCms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'PHP168' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('PHP168'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Z-Blog' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Z-Blog'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'Ecshop' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('Ecshop'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'SiteServer' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('SiteServer'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'WebMail' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('WebMail'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif '08cms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('08cms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'fengxun' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('fengxun'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        ###########################################################
        elif 'qianbocms' in req2.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                cooncms1_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                curcms1_1 = cooncms1_1.cursor()
                # sql = "INSERT INTO url_2(urllist,cmsscan,rarscan,st2) VALUES ('" + xxx + "','" + str(0) + "','" + str(0) + "','" + str(0) + "')"
                sql1cms = "INSERT INTO url_3 (urllist,urllujin,cms,cmstime) VALUES (%s,%s,%s,%s)"
                curcms1_1.execute(sql1cms, (str(xxxxxxx), str('robots.txt'),str('qianbocms'), str(timenow)))
                cooncms1_1.commit()
                curcms1_1.close()
                cooncms1_1.close()
                #break
            except Exception, e:
                print e
        else:
            pass

    except Exception,e:
         print e


def cmstiqu():
    list_zairucms = []
    try:
        cooncms2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcms2 = cooncms2.cursor()
        sql = "select urllist from url_2 where cmsscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2 set cmsscan='1' where cmsscan = 0 limit 1"
        curcms2.execute(sql)
        cooncms2.commit()
        try:
            #print unicode('[-]数据库激活，提取网址', 'utf-8')
            curscms = curcms2.fetchone()
            for xx in curscms:
                xxx1cms = xx.replace("('","").replace("',)","")
                #print 'Url:' + str(xxx1cms)
                list_zairucms.append(xxx1cms)
            curcms2.execute(sql1)
            cooncms2.commit()
            curcms2.close()
            cooncms2.close()
            for xxxxxxx in list_zairucms:
                scancms(xxxxxxx)
        except Exception,e:
            #print e
            pass
    except Exception,e:
        print e





def xc1():
    while 1: #最多保存10亿个网址
        #list_zairu = []
        zairu()   #这里已经从数据库的到了到了10个网址


def xc2():
    #time.sleep(30)
    while 1: #最多保存1亿个网址
        #list_zairurar = []
        rartiqu()   #这里已经从数据库的到了到了10个网址


def xc3():
    #time.sleep(30)
    while 1: #最多保存1亿个网址
        #list_zairucms = []
        cmstiqu()   #这里已经从数据库的到了到了10个网址



def xc4():
    #time.sleep(30)
    while 1: #最多保存1亿个网址
        #list_zairust = []
        st2tiqu()   #这里已经从数据库的到了到了10个网址
if int(thread_s) == 1:
    threads=[]

    # xc1 是 url无限采集  xc2是备份文件扫描 xc3是cms采集 xc4是st2扫描

    t1 = threading.Thread(target=xc1)#,name='当先现场:')
    t2 = threading.Thread(target=xc2)
    t3 = threading.Thread(target=xc3)
    t4 = threading.Thread(target=xc4)

    if int(Urlcj) == 1:
        print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t1)
    if int(Rarscan) == 1:
        print unicode('\n[+] 备份文件扫描进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t2)

    if int(Cmsscan) == 1:
        print unicode('\n[+] CMS扫描认证进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t3)
    if int(St2scan) == 1:
        print unicode('\n[+] ST2框架扫描进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t4)
    else:
        # print unicode('\n[+]  未加载任何扫描任务 ','utf-8')
        # time.sleep(100000)
        pass
    for x in threads:
        x.start()
    x.join()   #线程不堵塞  但是会出现不匀称的表现  并且会修改不同线程中的变量

# if int(thread_s) > 1:
#     for i in range(int(thread_s)):
#         t1 = threading.Thread(target=xc1, args=(), name='URL Scan Thread -' + str(i)).start()
#         t2 = threading.Thread(target=xc2, args=(), name='RAR Scan Thread -' + str(i)).start()
#         t3 = threading.Thread(target=xc3, args=(), name='CMS Scan Thread -' + str(i)).start()
#         t4 = threading.Thread(target=xc4, args=(), name='ST2 Scan Thread -' + str(i)).start()

if int(thread_s) > 1:
    for i in range(int(thread_s)):
        if int(Urlcj) == 1:
            print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
            time.sleep(1)
            t1 = threading.Thread(target=xc1, args=(), name='URL Scan Thread -' + str(i)).start()
        if int(Rarscan) == 1:
            print unicode('\n[+] 备份文件扫描进程加载成功...', 'utf-8')
            time.sleep(1)
            t2 = threading.Thread(target=xc2, args=(), name='RAR Scan Thread -' + str(i)).start()
        if int(Cmsscan) == 1:
            print unicode('\n[+] CMS扫描认证进程加载成功...', 'utf-8')
            time.sleep(1)
            t3 = threading.Thread(target=xc3, args=(), name='CMS Scan Thread -' + str(i)).start()
        if int(St2scan) == 1:
            print unicode('\n[+] ST2框架扫描进程加载成功...', 'utf-8')
            time.sleep(1)
            t4 = threading.Thread(target=xc4, args=(), name='ST2 Scan Thread -' + str(i)).start()