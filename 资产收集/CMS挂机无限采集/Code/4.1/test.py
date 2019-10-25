# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun

import requests
import re
import random
import time
import contextlib
import pymysql
from concurrent.futures import ThreadPoolExecutor
import configparser
requests.packages.urllib3.disable_warnings()

import threading
@contextlib.contextmanager
def connect_mysql():
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
    cursor = coon.cursor()

    try:
        yield cursor
    except Exception as e:
        print(e)
    finally:
        coon.commit()
        cursor.close()
        coon.close()

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

def get_url_title(url):
    info = {'title':None,'power':None,'server':None}
    try:
        headers = {
            'User-Agent': random.choice(headerss),
            'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3'}
        r = requests.get(url=url, headers=headers, verify=False, timeout=5)
        encoding = requests.utils.get_encodings_from_content(r.text)[0]
        res = r.content.decode(encoding, 'replace')
        title_pattern = '<title>(.*?)</title>'
        title = re.search(title_pattern, res, re.S | re.I).group(1)
        info['title']=title.replace('\n', '').strip()
        info['power'] = r.headers.get('X-Powered-By')
        info['server']= r.headers.get('Server')
    except:
        title = url.split('//')[1].replace('www.', '')
        if '/' in title:
            info['title']=title.split('/')[0].replace('\n', '').strip()
            info['power'] = 'None'
            info['server'] = 'None'
        else:
            info['title']=title.replace('\n', '').strip()
            info['power'] = 'None'
            info['server']= 'None'
    return info

def run(s):
    while True:
        s.acquire()
        with connect_mysql() as cursor:
            select_url_sql = 'SELECT url FROM url_index WHERE urlget=0 LIMIT 0,1;'
            update_url_sql = 'UPDATE url_index set urlget=1 WHERE urlget=0 limit 1'
            cursor.execute(select_url_sql)
            url = cursor.fetchone()[0]
            cursor.execute(update_url_sql)
        s.release()
        infos = get_url_title(url)
        print(infos)
        sqls = 'UPDATE url_index set title="{}",power="{}",server="{}"where url = "{}"'.format(infos['title'],infos['power'],infos['server'],url)
        with connect_mysql() as cursor:
            cursor.execute(sqls)

if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    cfg.read('Config.ini')
    user = cfg.get("Server", "username")
    passwd = cfg.get("Server", "password")
    host = cfg.get("Server", "host")
    Dbname = cfg.get("Server", "db")
    port = int(cfg.get("Server", "port"))
    semaphore = threading.BoundedSemaphore(1)
    with ThreadPoolExecutor() as p:
        for i in range(100):
            p.submit(run(semaphore))
