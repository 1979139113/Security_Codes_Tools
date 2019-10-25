# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
import re
from requests.packages import urllib3
urllib3.disable_warnings()
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote,urlparse
import configparser
import pymysql
import contextlib
import os

cfg = configparser.ConfigParser()
cfg.read('../Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server", "db")
port = int(cfg.get("Server", "port"))
keep_scan = int(cfg.get("Scan_Modules", "Keep_Scan"))

@contextlib.contextmanager
def connect_mysql():
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
    cursor = coon.cursor()
    try:
        yield cursor
    except Exception as e:
        print(e)
        pass
    finally:
        coon.commit()
        cursor.close()
        coon.close()

from bs4 import BeautifulSoup as bs
import random
requests.packages.urllib3.disable_warnings()
timeout = 5

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
first_cule = ['.com.cn', '.org.cn', '.net.cn', '.com', '.cn', '.cc', '.net', '.org', '.info', '.fun', '.one', '.xyz',
              '.name', '.io', '.top', '.me', '.club', '.tv']

def Get_Page_Url(url):
    '''

    根据传入网址
    获取该网址页面中的网址
    需要进一步的判断
    '''
    result_list = []
    result_set = []
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA, 'Connection': 'close'}
        r = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
        time.sleep(0.02)
        bp = bs(r.content, 'html.parser')
        for x in bp.select('li > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception as e:
                    print(e)
            else:
                pass
        for x in bp.select('td > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception as e:
                    print(e)
            else:
                pass
        for x in bp.select('p > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception as e:
                    print(e)
            else:
                pass
        for x in bp.select('div > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception as e:
                    print(e)
            else:
                pass
    except Exception as e:
        print(e)

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA, 'Connection': 'close'}
        r = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
        time.sleep(0.02)
        pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.I)
        encoding = requests.utils.get_encodings_from_content(r.text)[0]
        res = r.content.decode(encoding, 'replace')
        urls = re.findall(pattern, res)
        for x in urls:
            a1, a2 = x.split('//')[0], x.split('//')[1].split('/')[0]
            a3 = ''.join(a1) + '//' + ''.join(a2)
            result_list.append(a3.replace("'", "").replace('>', '').replace('<', ''))
    except:
        pass

    result_list = list(set(result_list))
    for u in result_list:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA, 'Connection': 'close'}
            r = requests.get(url=u, headers=headers, verify=False, timeout=timeout)
            time.sleep(0.02)
            if r.status_code == 200:
                real_url = r.url.rstrip('/')

                if '/' in real_url.split('//')[1]:
                    real_urls = real_url.split('//')[0]+'//'+real_url.split('//')[1].split('/')[0]
                    result_set.append(real_urls)
                else:
                    real_urls = real_url.split('//')[0]+'//'+real_url.split('//')[1]
                    result_set.append(real_urls)


        except:
            pass
    print(len(result_set))
    print(result_set)
    return result_set
    # 返回数据是完整的url，并且经过了存活性检测


domains = [x.split('.')[0] for x in open('domains.txt','r',encoding='utf-8').readlines()]


def Get_Linkss(sem):
    time.sleep(random.randint(1,20))
    while 1:
        try:
            sem.acquire()
            with connect_mysql() as coon:
                sql1 = 'select url from Sec_Index where subdomain=0 limit 0,1'
                sql2 = 'update Sec_Index set subdomain=1 where subdomain = 0 limit 1'
                coon.execute(sql1)
                min_res1 = coon.fetchone()
                if min_res1 == None:
                    sem.release()
                    return
                res_url1 = min_res1[0]
                coon.execute(sql2)
            sem.release()
            link = Get_Page_Url(res_url1)
            if link:
                for url in link:
                    with connect_mysql() as coon:
                        print('插入数据到网址表:' + url)
                        sql3 = "insert into Sec_Urls(url) values  ('{}')".format(url)
                        coon.execute(sql3)
                    for domain in domains:
                        if domain in url:
                            print('符合子域名规则，插入数据到主扫描表:'+url)
                            with connect_mysql() as coon:
                                sql4 = "insert into Sec_Index(url) values  ('{}')".format(url)
                                coon.execute(sql4)
                    if keep_scan == 1:
                        with connect_mysql() as coon:
                            print('插入数据到主扫描表:'+url)
                            sql5 = "insert into Sec_Index(url) values  ('{}')".format(url)
                            coon.execute(sql5)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    import threading
    sem = threading.BoundedSemaphore(1)
    p = ThreadPoolExecutor()
    for i in range(36):
        p.submit(Get_Linkss, sem)

