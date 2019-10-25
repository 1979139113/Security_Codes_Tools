# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 0004 11:57
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 主程序.py
# @Software: PyCharm
import sys
import re
import chardet
import pymysql
import requests
import time
import threading
import random
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')
headerss = [
'Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)',
'Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)',
'Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)',
'Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)'
]
first_cule= ["com/'>","cn/'>","cc/'>","net/'>","org/'>",".com/",".cn/",".cc/",".net/",".org/",'com">','com/"','cn">','cn/"','net">','net/"','cc">','cc/"','org">','org/"']


# UA = random.choice(headerss)
# headers = {'User-Agent': UA}

cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")
black = cfg.get("Config","black")
blackname=black.lstrip('|').rstrip('|').split('|')
list_001 = []
print 'Start.....'
try:
    coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, charset='utf8')
    cur_svn = coon_svn.cursor()
    cur_svn.close()
    coon_svn.close()
    print (unicode('数据库连接成功......','utf-8'))
except:
    print (unicode('无法连接到数据库.....','utf-8'))
    time.sleep(60)
def first_scan(url):
    UA = random.choice(headerss)
    headers = {'百度': UA}
    try:
        first_r = requests.get(url=url,headers=headers,timeout=6)
        for first_url in first_cule:
            patt = re.compile(str('http' +'.*?' + str(first_url)))
            try:
                first_re = re.findall(patt, first_r.content)
                for first_u_url in first_re:
                    first_u_url_1 = first_u_url.replace('%3A%2F%2F', '//').replace('\/\/', '//').replace('">','').replace("/'>", "").replace('/"', '')
                    if ' ' in first_u_url_1:
                        pass
                    if 'www' in first_u_url_1.split('http://')[1] and len(first_u_url_1) < 52:
                        print '[*] GET : ' + first_u_url_1
                        list_001.append(first_u_url_1)
            except Exception, e:
                pass
                #print e
    except Exception,e:
       print e
    return list_001

ifstart =input(unicode('是否导入种子文件并且开始扫描(1是[导入种子扫描]/2否[继续在上次数据库扫描]):','utf-8').encode('gbk'))
if ifstart == 1:
    first_input = raw_input("Input ULR TXT NAME:")
    first_url_txt = list(set([i.replace("\n", "") for i in open(first_input, "r").readlines()]))
    for xxx in first_url_txt:
        first_scan(xxx)
    list_001 = list(set(list_001))
    print unicode('种子文件扫描成功，正在写入初始数据库....', 'utf-8')
    for xx in list_001:
        for yy in blackname:
            if yy in xx:
                list_001.remove(xx)
    try:
        coon = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        #cur = coon.cursor(pymysql.cursors.SSCursor)
        cur = coon.cursor()
        print unicode('数据库连接成功', 'utf-8')
        for xx_0 in list_001:
            xx = xx_0.strip('/')
            try:
                UA = random.choice(headerss)
                headers = {'百度': UA}
                urlxieru = requests.head(url=str(xx), headers=headers, timeout=3)
                print str(threading.current_thread().name) + ' ' + str(urlxieru.url).strip('/') + '  ' + str(urlxieru.status_code)
                if urlxieru.status_code == 200:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # sql001 = "INSERT INTO url_2 (urllist,cmsscan,rarscan,st2,gettime) VALUES (%s,%s,%s,%s,%s)"
                    sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (str(xx), '0', str(timenow), str(xx))
                    cur.execute(sql)
                    coon.commit()
                    sql001 = "INSERT INTO result(url,datatime) select '%s','%s' from dual where '%s' not in (select url from result)" % (str(xx),str(timenow), str(xx))
                    cur.execute(sql001)
                    coon.commit()
                else:
                    pass
            except Exception, e:
                print e
    except Exception,e:
        print e
else:
    pass



def wuxiancaiji(url):
    list_002 = []
    UA = random.choice(headerss)
    headers = {'百度': UA}
    try:
        wuxiancaiji_r = requests.get(url=url, headers=headers, timeout=5, allow_redirects=False)
        try:
            for wuxiancaiji_url in first_cule:
                patt_wuxiancaiji = re.compile('http' + '.*?' + str(wuxiancaiji_url))
                wuxiancaiji_re = re.findall(patt_wuxiancaiji, wuxiancaiji_r.content)
                for wuxiancaiji_u_url in wuxiancaiji_re:
                    wuxiancaiji_u_url_1 = wuxiancaiji_u_url.replace('%3A%2F%2F', '//').replace('\/\/','//').replace('">','').replace("/'>", "").replace('/"', '')
                    if ' ' in wuxiancaiji_u_url_1:
                        pass
                    if len(wuxiancaiji_u_url_1) > 52:
                        pass
                    else:
                        list_002.append(wuxiancaiji_u_url_1)
            list_002_1 = list(set(list_002))
            for xx in list_002_1:
                for yy in blackname:
                    if yy in xx:
                        list_002_1.remove(xx)
            try:
                coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                cur = coon.cursor()
                for xx_x0 in list_002_1:
                    xx = xx_x0.strip('/')
                    try:
                        UA = random.choice(headerss)
                        headers = {'User-Agent': UA}
                        urlxieru = requests.head(url=str(xx), headers=headers, timeout=3)
                        print str(threading.current_thread().name) + ' ' + str(urlxieru.url).strip('/') + '  ' + str(urlxieru.status_code)
                        if urlxieru.status_code == 200:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            # sql001 = "INSERT INTO url_2 (urllist,cmsscan,rarscan,st2,gettime) VALUES (%s,%s,%s,%s,%s)"
                            sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (str(xx), '0', str(timenow), str(xx))
                            cur.execute(sql)
                            coon.commit()
                            sql1 = "INSERT INTO result(url,datatime) select '%s','%s' from dual where '%s' not in (select url from result)" % (str(xx), str(timenow), str(xx))
                            cur.execute(sql1)
                            coon.commit()
                        else:
                            pass
                    except:
                        pass
                    try:
                        if 'www' in xx.split('http://')[1]:
                            UA = random.choice(headerss)
                            headers = {'User-Agent': UA}
                            urlxieru = requests.head(url=str(xx), headers=headers, timeout=3)
                            print str(threading.current_thread().name) + ' ' + str(urlxieru.url).strip('/') + '  ' + str(urlxieru.status_code)
                            if urlxieru.status_code == 200:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                sql001 = "INSERT INTO url_domain(url,datatime) select '%s','%s' from dual where '%s' not in (select url from url_domain)" % (str(xx),str(timenow), str(xx))
                                cur.execute(sql001)
                                coon.commit()
                            else:
                                pass
                        else:
                            UA = random.choice(headerss)
                            headers = {'User-Agent': UA}
                            urlxieru = requests.head(url=str(xx), headers=headers, timeout=3)
                            print str(threading.current_thread().name) + ' ' + str(urlxieru.url).strip('/') + '  ' + str(urlxieru.status_code)
                            if urlxieru.status_code == 200:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                # sql001 = "INSERT INTO url_2 (urllist,cmsscan,rarscan,st2,gettime) VALUES (%s,%s,%s,%s,%s)"
                                sql001 = "INSERT INTO url_subdomain(url,datatime) select '%s','%s' from dual where '%s' not in (select url from url_subdomain)" % (str(xx),str(timenow), str(xx))
                                cur.execute(sql001)
                                coon.commit()
                            else:
                                pass
                    except Exception, e:
                        print e
            except Exception, e:
                print unicode('爬行到的网址无法存储数据库，请检查配置文件及系统环境', 'utf-8')
                print e
        except Exception, e:
            print e
    except Exception, e:
        print e

def zairu():
    try:
        time.sleep(random.randint(2, 6))
        #lock.acquire()
        cooncaiji2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcaiji2 = cooncaiji2.cursor()
        sqlcaiji2 = "select url from url_index where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sqlcaiji2_1 = "update url_index set urlget='1' where urlget = 0 limit 1"
        curcaiji2.execute(sqlcaiji2)
        cooncaiji2.commit()
        curscaiji = curcaiji2.fetchone()
        curcaiji2.execute(sqlcaiji2_1)
        cooncaiji2.commit()
        curcaiji2.close()
        cooncaiji2.close()
        for xx in curscaiji:
            xxx1aiji = xx.replace("('","").replace("',)","")
            wuxiancaiji(xxx1aiji)
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print unicode('原始网址已经爬行完毕，请添加新的原始网址，使用方法详见帮助文档', 'utf-8')
        time.sleep(150)
        print e
def xc():
    while 1:
        zairu()
for i in range(int(thread_s)):
    t1 = threading.Thread(target=xc,name=str('[-] URL GET - %s - '%str(i))).start()
