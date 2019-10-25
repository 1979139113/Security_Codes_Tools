# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import requests
import time
import random
from urllib import parse
requests.packages.urllib3.disable_warnings()

def get_domain(url):
    try:
        if 'www' not in url:
            if url.count('.') == 1:
                return url.split('.')[0]
            if url.count('.') == 2:
                return url.split('.')[1]
            if url.count('.') == 3:
                return url.split('.')[1]
            if url.count('.') == 4:
                return url.split('.')[2]
        else:
            if url.count('.') == 2:
                return url.split('.')[1]
            if url.count('.') == 3:
                return url.split('.')[1]
            if url.count('.') == 4:
                return url.split('.')[2]
            else:
                return url.split('.')[3]
    except:
        return url.split('/')[1].split('.')[1]

def headers(refer):
    REFERERS = [
        "https://www.baidu.com",
        "http://www.baidu.com",
        "https://www.google.com.hk",
        "http://www.so.com",
        "http://www.sogou.com",
        "http://www.soso.com",
        "http://www.bing.com",
    ]

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
    if refer:
        pass
    else:
        refer = random.choice(REFERERS)
    headers = {
        'User-Agent': random.choice(headerss),
        'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'referer': refer,
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    }
    return headers

def check(r):
    if 'username' in r and 'password' in r:
        return True
    if 'type="password"' in r:
        return True
    if '用户名' in r and '密码' in r:
        return True
    if '登陆' in r and '密码' in r:
        return True
    if '账号' in r and '密码' in r:
        return True
    if '管理员登陆' in r:
        return True
    if '后台管理登陆' in r:
        return True
    if '管理员' in r and '密码' in r:
        return True
    if '登录密码' in  r and '用户名' in r:
        return True
    if '账号' in r and '密码' in r:
        return True
    if '帳號' in r and '密碼' in r:
        return True

def scan(url,ways):
    urlsss = parse.urljoin(url.strip('/'),get_domain(url))
    print('SCAN:{}'.format(urlsss))
    try:
        res = requests.get(url=urlsss, headers=headers(url), timeout=5)
        encoding = requests.utils.get_encodings_from_content(res.text)[0]
        r = res.content.decode(encoding, 'replace')
        if check(r):
            with open('后台列表.txt', 'a+')as a:
                a.write(urlsss+'\n')
            return urlsss
    except Exception as e:
        pass

    for way in ways:
        urls = parse.urljoin(url.strip('/'),way.lstrip('/'))
        print('SCAN:{}'.format(urls))

        urlss = parse.urljoin(url.strip('/'),get_domain(url)+'/'+way.lstrip('/'))
        print('SCAN:{}'.format(urlss))

        try:
            res = requests.get(url=urls, headers=headers(url), timeout=5)
            encoding = requests.utils.get_encodings_from_content(res.text)[0]
            r = res.content.decode(encoding, 'replace')
            if check(r):
                with open('后台列表.txt', 'a+')as a:
                    a.write(urls+'\n')
                return urls
        except Exception as e:
            pass
        try:
            res = requests.get(url=urlss, headers=headers(url), timeout=5)
            encoding = requests.utils.get_encodings_from_content(res.text)[0]
            r = res.content.decode(encoding, 'replace')
            if check(r):
                with open('后台列表.txt', 'a+')as a:
                    a.write(urlss+'\n')
                return urlss
        except Exception as e:
            pass



if __name__ == '__main__':
    print ('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Scan manager url
                               |___/       Version:0.5
                                           Datetime:2019-03-09-14:55:36

    ''')
    urls = input('Input urls:')
    url_ways = input('Input Dict:')
    urls = list([x.strip() for x in open(urls,'r').readlines()])
    url_ways = list([x.strip() for x in open(url_ways,'r').readlines()])
    p = ThreadPoolExecutor()
    all_tasks = [p.submit(scan,url,url_ways) for url in urls]

    res = [x.result() for x in all_tasks]
    p.shutdown()

    # for x in as_completed(all_tasks):



