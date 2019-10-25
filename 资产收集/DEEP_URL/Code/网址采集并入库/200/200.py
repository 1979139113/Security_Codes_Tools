# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 0016 16:46
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 200.py
# @Software: PyCharm
import sys
import requests
import threading
import pymysql
import os
from bs4 import BeautifulSoup as bs
import random
import time
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')


first_cule= ['.com.cn','.org.cn','.net.cn','.com','.cn','.cc','.net','.org','.info','.fun','.one','.xyz','.name','.io','.top','.me','.club','.tv']

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

print (unicode('开始检查运行环境状态......','utf-8'))
time.sleep(1)
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")
black = cfg.get("Config","black")
blackname=black.lstrip('|').rstrip('|').split('|')
print (unicode('数据库地址 : ','utf-8')) + str(host)
print (unicode('数据库账号 : ','utf-8')) + str(user)
print (unicode('数据库密码 : ','utf-8')) + str(passwd)
print (unicode('扫描线程数 : ','utf-8')) + str(thread_s)

try:
    coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, charset='utf8')
    cur_svn = coon_svn.cursor()
    cur_svn.close()
    coon_svn.close()
    print (unicode('数据库连接成功......','utf-8'))
    time.sleep(1)
    print (unicode('程序开始载入网址......', 'utf-8'))
    time.sleep(1)
except:
    print (unicode('无法连接到数据库.....','utf-8'))
    time.sleep(60)

url_list = list(set([x.replace('\n', '') if x.startswith('http')  else 'http://' + x.replace('\n', '') for x in open('url.txt', 'r').readlines()]))

print (unicode('种子网址总数 : ','utf-8')) +str(len(url_list))

def first_get_url(url):
    result_list = []
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r = requests.get(url=url,headers=headers,timeout=7)
        print (unicode('原始网址采集友情链接:     ', 'utf-8')) + r.url  + '      ' + str(r.status_code)
        bp = bs(r.content, 'html.parser')
        for x in bp.select('li > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
        for x in bp.select('td > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
        for x in bp.select('p > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
        for x in bp.select('div > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
    except Exception,e:
        print url + (unicode('  该链接无法访问，已保存到数据库...', 'utf-8'))
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
        cur = coon.cursor()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql006 = "INSERT INTO die(url,datatime) select '%s','%s' from dual where '%s' not in (select url from die)" % (
            str(url), str(timenow), str(url))
        cur.execute(sql006)
        coon.commit()
        cur.close()
        coon.close()
    result_list=list(set(result_list))
    for _ in result_list:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            rr = requests.head(url=_,headers=headers,timeout=7)
            print (unicode('友链网址存活检测:     ','utf-8')) + rr.url + '     ' + str(rr.status_code)
            if rr.status_code == 200:
                coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                cur = coon.cursor()
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (
                str(_), '0', str(timenow), str(_))
                cur.execute(sql)
                coon.commit()
                sql001 = "INSERT INTO result(url,datatime) select '%s','%s' from dual where '%s' not in (select url from result)" % (
                str(_), str(timenow), str(_))
                cur.execute(sql001)
                coon.commit()
                if 'www' in _.split('http://')[1]:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sql003 = "INSERT INTO url_domain(url,datatime) select '%s','%s' from dual where '%s' not in (select url from url_domain)" % (
                        str(_), str(timenow), str(_))
                    cur.execute(sql003)
                    coon.commit()
                else:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sql005 = "INSERT INTO url_subdomain(url,datatime) select '%s','%s' from dual where '%s' not in (select url from url_subdomain)" % (
                        str(_), str(timenow), str(_))
                    cur.execute(sql005)
                    coon.commit()
                    cur.close()
                    coon.close()
            else:
                print _ + (unicode('    该链接无法访问，已保存到数据库...', 'utf-8'))
                coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                cur = coon.cursor()
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sql006 = "INSERT INTO die(url,datatime) select '%s','%s' from dual where '%s' not in (select url from die)" % (
                    str(_), str(timenow), str(_))
                cur.execute(sql006)
                coon.commit()
                cur.close()
                coon.close()
        except Exception,e:
            print _ + (unicode('    该链接无法访问，已保存到数据库...', 'utf-8'))
            coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
            cur = coon.cursor()
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sql006 = "INSERT INTO die(url,datatime) select '%s','%s' from dual where '%s' not in (select url from die)" % (
                str(_), str(timenow), str(_))
            cur.execute(sql006)
            coon.commit()
            cur.close()
            coon.close()

def scan(url):
    result_list = []
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r = requests.get(url=url,headers=headers,timeout=7)
        print (unicode('友情链接采集:     ', 'utf-8')) + r.url  + '      ' + str(r.status_code)
        bp = bs(r.content, 'html.parser')
        for x in bp.select('li > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
        for x in bp.select('p > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
        for x in bp.select('div > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for _ in blackname:
                        if _ not in ddd:
                            for x in first_cule:
                                if x in ddd:
                                    if 'http' in ddd:
                                    #print ddd.split(x)[0] + x
                                        result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    pass
            else:
                pass
    except Exception,e:
        print url + (unicode('  该链接无法访问，已保存到数据库...', 'utf-8'))
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
        cur = coon.cursor()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql006 = "INSERT INTO die(url,datatime) select '%s','%s' from dual where '%s' not in (select url from die)" % (
            str(url), str(timenow), str(url))
        cur.execute(sql006)
        coon.commit()
        cur.close()
        coon.close()
    result_list=list(set(result_list))
    for _ in result_list:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            rr = requests.head(url=_,headers=headers,timeout=7)
            print (unicode('友链网址存活检测:     ','utf-8')) + rr.url + '     ' + str(rr.status_code)
            if rr.status_code == 200:
                coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                cur = coon.cursor()
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (
                str(_), '0', str(timenow), str(_))
                cur.execute(sql)
                coon.commit()
                sql001 = "INSERT INTO result(url,datatime) select '%s','%s' from dual where '%s' not in (select url from result)" % (
                str(_), str(timenow), str(_))
                cur.execute(sql001)
                coon.commit()
                if 'www' in _.split('http://')[1]:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sql003 = "INSERT INTO url_domain(url,datatime) select '%s','%s' from dual where '%s' not in (select url from url_domain)" % (
                        str(_), str(timenow), str(_))
                    cur.execute(sql003)
                    coon.commit()
                else:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sql005 = "INSERT INTO url_subdomain(url,datatime) select '%s','%s' from dual where '%s' not in (select url from url_subdomain)" % (
                        str(_), str(timenow), str(_))
                    cur.execute(sql005)
                    coon.commit()
                    cur.close()
                    coon.close()
            else:
                print _ + (unicode('    该链接无法访问，已保存到数据库...', 'utf-8'))
                coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                cur = coon.cursor()
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                sql006 = "INSERT INTO die(url,datatime) select '%s','%s' from dual where '%s' not in (select url from die)" % (
                    str(_), str(timenow), str(_))
                cur.execute(sql006)
                coon.commit()
                cur.close()
                coon.close()
        except Exception,e:
            print _ + (unicode('    该链接无法访问，已保存到数据库...','utf-8'))
            coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
            cur = coon.cursor()
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sql006 = "INSERT INTO die(url,datatime) select '%s','%s' from dual where '%s' not in (select url from die)" % (
                str(_), str(timenow), str(_))
            cur.execute(sql006)
            coon.commit()
            cur.close()
            coon.close()

def zairu():
    try:
        time.sleep(random.randint(1,15))
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
            scan(xxx1aiji)
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print unicode('原始网址已经爬行完毕，请添加新的原始网址...', 'utf-8')
        time.sleep(150)
        #print (unicode('该网址无法访问... ','utf-8'))
def writein():
    while 1:
        try:
            print  (unicode('开始清理缓存文件', 'utf-8'))
            os.remove(('全部友链网址.txt').decode('utf-8'))
            os.remove(('主域名友链网址.txt').decode('utf-8'))
            os.remove(('二级域名友链网址.txt').decode('utf-8'))
            os.remove(('无法访问友链网址.txt').decode('utf-8'))
            print  (unicode('缓存清理完毕 ','utf-8'))
        except Exception,e:
            print e
        #time.sleep(500)
        try:
            coon = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
            cur = coon.cursor()
            sql1 = 'select url from result'
            sql2 = 'select url from url_domain'
            sql3 = 'select url from url_subdomain'
            sql4 = 'select url from die'
            cur.execute(sql1)
            coon.commit()
            res1 = cur.fetchall()
            for _ in res1:
                with open(('全部友链网址.txt').decode('utf-8'),'a+')as a:
                    d = str(_)
                    a.write(d.replace("('","").replace("',)","").replace(' ','') + '\n')
            cur.execute(sql2)
            coon.commit()
            res2 = cur.fetchall()
            for _ in res2:
                with open(('主域名友链网址.txt').decode('utf-8'),'a+')as a:
                    d = str(_)
                    a.write(d.replace("('","").replace("',)","").replace(' ','') + '\n')
            cur.execute(sql3)
            coon.commit()
            res3 = cur.fetchall()
            for _ in res3:
                with open(('二级域名友链网址.txt').decode('utf-8'),'a+')as a:
                    d = str(_)
                    a.write(d.replace("('","").replace("',)","").replace(' ','') + '\n')
            cur.execute(sql4)
            coon.commit()
            res4 = cur.fetchall()
            for _ in res4:
                with open(('无法访问友链网址.txt').decode('utf-8'),'a+')as a:
                    d = str(_)
                    a.write(d.replace("('", "").replace("',)", "").replace(' ', '') + '\n')
            cur.close()
            coon.close()
        except Exception,e:
            print e
            pass
        time.sleep(600)



def xc():
    while 1:
        zairu()

ifstart =input(unicode('是否导入种子文件并且开始扫描(1是[导入种子扫描]/2否[继续在上次数据库扫描]):','utf-8').encode('gbk'))

if ifstart == 1:
    for xaxa in url_list:
        first_get_url(xaxa)
else:
    print unicode('开始从数据库载入网址扫描...', 'utf-8')

t = threading.Thread(target=writein).start()
for i in range(int(thread_s)):
    t1 = threading.Thread(target=xc,name=str('[-] URL GET - %s - '%str(i))).start()