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
print 'Start.....'



def first_scan(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    print unicode('开始IP获取....', 'utf-8')
    url_first = 'http://www.webscan.cc/?action=getip&domain='+url
    print url_first
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        first_url_scan = requests.get(url=url_first,headers=headers,timeout=20)
        first_rr = re.findall('{"ip":"(.*?)",',first_url_scan.content)
        first_ip = str(first_rr).replace("'",'').replace('[','').replace(']','')
        first_ip1 = first_ip.replace(first_ip.split('.',)[3],'')
        print 'IP:'+first_ip
        for ii in range(1,254):
            first_ipp = first_ip1 +str(ii)
            try:
                time.sleep(5)
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                #time.sleep(5)
                url_secend = 'http://www.webscan.cc/?action=query&ip='+''.join(first_ipp)
                print unicode('开始C段旁站链接爬行....', 'utf-8')
                print url_secend
                secend_url_scan=requests.get(url=url_secend,headers=headers,timeout=20)
                print secend_url_scan.content
                secend_rr = re.findall('domain":"(.*?)",',secend_url_scan.content)
                for uur in secend_rr:
                    uux = uur.replace('\\','')
                    print 'C Found: ' + str(uux)
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_svn = coon_svn.cursor()
                        sql_svn = "INSERT INTO url_index (url,urlip,urlget,datatime) VALUES (%s,%s,%s,%s)"
                        cur_svn.execute(sql_svn, (str(uux), str(str(first_ipp)), str('0'), str(timenow)))
                        coon_svn.commit()
                        cur_svn.close()
                        coon_svn.close()
                        time.sleep(random.randint(1, 3))
                    except:
                        pass
            except Exception,e:
                print e
    except Exception,e:
        print e


list_001=[]
def scan_url(url):
    print unicode('开始友情链接爬行....','utf-8')
    list_001=[]
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        first_r = requests.get(url=url,headers=headers,timeout=10)
        for first_url in first_cule:
            patt = re.compile(str('http' +'.*?' + str(first_url)))
            try:
                first_re = re.findall(patt, first_r.content)
                for first_u_url in first_re:
                    first_u_url_1 = first_u_url.replace('%3A%2F%2F', '//').replace('\/\/', '//').replace('">','').replace("/'>", "").replace('/"', '')
                    if ' ' in first_u_url_1:
                        pass
                    if 'www' in first_u_url_1.split('http://')[1] and len(first_u_url_1) < 52:
                        list_001.append(first_u_url_1)
            except Exception, e:
                pass
        for xxu in list(set(list_001)):
            print xxu
            try:
                xxux=requests.get(url=xxu,headers=headers,timeout=5)
                if isinstance(xxux.content, unicode):
                    pass
                else:
                    codesty = chardet.detect(xxux.content)
                    a = xxux.content.decode(codesty['encoding'])
                try:
                    dd = re.search(u'[\u4e00-\u9fa5]', a)
                    if dd.group():
                        print 'IS CHina WEB'
                except:
                    print 'NO chinese WEB'
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_sql_2 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_sql_2 = coon_sql_2.cursor()
                        sql_sql_2="INSERT INTO url_result(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_result)"%(str(xxu),'0', str(timenow),str(xxu))
                        cur_sql_2.execute(sql_sql_2)
                        coon_sql_2.commit()
                        cur_sql_2.close()
                        coon_sql_2.close()
                        time.sleep(random.randint(1, 3))
                    except:
                        pass
            except Exception,e:
                print e
    except Exception,e:
        pass




def end_scan(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    liss = []
    print unicode('开始深度连接爬行....', 'utf-8')
    uu = url.split('//')[1].split('/')[0]
    print 'Crawl: ' + uu
    try:
        r = requests.get(url).content
        r1 = re.findall('href="(.*?)"',r)
        r2 = re.findall(r'href=."/(.*?/.*?)"',r)
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
        for x in list(set(liss)):
            print x
    except Exception,e:
        print e
    for uiui in list(set(liss)):
        try:
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            coon_sql_2 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
            cur_sql_2 = coon_sql_2.cursor()
            sql_sql_2 = "INSERT INTO result(url,datatime) VALUES (%s,%s)"
            cur_sql_2.execute(sql_sql_2, (str(uiui), str(timenow)))
            coon_sql_2.commit()
            cur_sql_2.close()
            coon_sql_2.close()
            time.sleep(random.randint(1, 3))
        except:
            pass

ifstart =input(unicode('是否导入种子文件并且开始扫描(1是[导入种子扫描]/2否[继续在上次数据库扫描]):','utf-8').encode('gbk'))
if ifstart == 1:
    first_input = raw_input("Input ULR TXT NAME:")
    first_url_txt = list(set([i.replace("\n", "") for i in open(first_input, "r").readlines()]))
    for xxx in first_url_txt:
        first_scan(xxx)
else:
    pass


def cmstiqu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        cooncms2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcms2 = cooncms2.cursor()
        sql = "select url from url_index where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_index set urlget='1' where urlget = 0 limit 1"
        curcms2.execute(sql)
        cooncms2.commit()
        curscms = curcms2.fetchone()
        curcms2.execute(sql1)
        cooncms2.commit()
        curcms2.close()
        cooncms2.close()
        lock.release()
        try:
            for xx in curscms:
                xxx1cms = xx.replace("('","").replace("',)","")
                scan_url(xxx1cms)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        print unicode('C段与旁站数据库无数据....', 'utf-8')
        print unicode('C段与旁站数据库无数据....', 'utf-8')
        print unicode('C段与旁站数据库无数据....', 'utf-8')
        print unicode('C段与旁站数据库无数据....', 'utf-8')
        print unicode('C段与旁站数据库无数据....', 'utf-8')
        time.sleep(150)
        pass

def cmstiqu2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        cooncms2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcms2 = cooncms2.cursor()
        sql = "select url from url_result where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_result set urlget='1' where urlget = 0 limit 1"
        curcms2.execute(sql)
        cooncms2.commit()
        curscms = curcms2.fetchone()
        curcms2.execute(sql1)
        cooncms2.commit()
        curcms2.close()
        cooncms2.close()
        lock.release()
        try:
            for xx in curscms:
                xxx1cms = xx.replace("('","").replace("',)","")
                end_scan(xxx1cms)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        print unicode('外链数据库无数据....', 'utf-8')
        print unicode('外链数据库无数据....', 'utf-8')
        print unicode('外链数据库无数据....', 'utf-8')
        print unicode('外链数据库无数据....', 'utf-8')
        print unicode('外链数据库无数据....', 'utf-8')

        time.sleep(150)
        pass

def xc():
    while 1:
        cmstiqu()
def xc2():
    while 1:
        cmstiqu2()
lock = threading.Lock()
for i in range(int(thread_s)):

    t1 = threading.Thread(target=xc, args=(), name='URL Scan Thread -' + str(i)).start()
    t2 = threading.Thread(target=xc2, args=(), name='RAR Scan Thread -' + str(i)).start()
