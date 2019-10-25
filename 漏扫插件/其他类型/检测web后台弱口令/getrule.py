# coding:utf-8
import random
import sys
import time
import re
import requests
import os
import multiprocessing
requests.packages.urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 3

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
        refer=random.choice(REFERERS)
    headers = {
        'User-Agent': random.choice(headerss),
        'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'referer': refer,
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    }
    return headers

def get_data(content):
    pattern = ''

def scan_admin(urls,manage_way):
    url = urls + manage_way
    refer = urls
    try:
        r = requests.get(url=url,headers=headers(refer),timeout=timeout,verify=False)
        if 'user' in r.content and 'pass' in r.content:
            return r.url
        if '用户名' in r.content and '密码' in r.content:
            return r.url
        if '管理员登陆' in r.content:
            return r.url
        if '后台管理登陆' in r.content:
            return r.url
        if '管理员' in r.content and '密码' in r.content:
            return r.url
        if '登录密码' in r.content:
            return r.url
        if '账号' in r.content and '密码' in r.content:
            return r.url
        if '帳號' in r.content and '密碼' in r.content:
            return r.url
    except Exception,e:
        print e

def post_data(url,)
if __name__ == '__main__':
    multiprocessing.freeze_support()
    print ('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_Unauthorized_Vlun_IP
                               |___/       Version:1.0
                                           Datetime:2018-11-22-14:55:36

    ''')
    print unicode('             IP未授权漏洞集成自动化识别', 'utf-8')

    New_start = raw_input(unicode('待需验证IP文本拖拽进来:', 'utf-8').encode('gbk'))
    smxc = int(input(unicode('设置线程池数量(2-128):', 'utf-8').encode('gbk')))
    list_ = list(set(
        [x.replace('\n', '') for x in open(New_start, 'r').readlines()]))

    p = multiprocessing.Pool(smxc)
    for _ in list_:
        p.apply_async(get_ip_vlun, args=(_,))
    p.close()
    p.join()
