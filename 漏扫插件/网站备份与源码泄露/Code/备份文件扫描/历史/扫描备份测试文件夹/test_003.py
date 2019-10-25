# -*- coding: utf-8 -*-
import requests
def scan(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    try:
        r = requests.head(url=url,headers=headers,allow_redirects=True)
        print r.status_code
        print r.headers
    except Exception,e:
        print e

scan('http://www.wanmei2.net/web.rar')