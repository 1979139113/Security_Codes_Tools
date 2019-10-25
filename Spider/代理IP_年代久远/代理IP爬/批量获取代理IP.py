# -*- coding:utf-8 -*-
import queue
import requests
import re
import random
import time
import threading
import os
def headerss():

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
    headers = {
        'User-Agent': random.choice(headerss),
        'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'referer': random.choice(REFERERS),
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    }
    return headers



q = queue.Queue()
def get_ip(page):
    url1='http://www.66ip.cn/mo.php?sxb=&tqsl=30&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='
    url2='http://www.xicidaili.com/nn/'
    for i in range(1,page):
        headers = headerss()
        url1_1=url1+str(i)
        url2_2=url2+str(i)
        try:
            r = requests.get(url=url1_1,headers=headers,timeout=5)
            encoding = requests.utils.get_encodings_from_content(r.text)[0]
            res = r.content.decode(encoding, 'replace')
            rr = re.findall('		(.*?)<br />',res)
            for x in rr:
                #print('抓到IP:{}'.format(x))
                q.put(x)
        except Exception as e:
            #print(e)
            pass
        try:
            time.sleep(20)
            r = requests.get(url=url2_2,headers=headers,timeout=5)
            rr = re.findall('/></td>(.*?)<a href',res,re.S)
            for x in rr:
                x1 = x.replace('\n','').replace('<td>','').replace("</td>",':').replace('      ','').replace(':  ','')
                #print('抓到IP:{}'.format(x1))
                q.put(x1)
        except Exception as e:
            #print(e)
            pass


def scan_ip():
    while 1:
        proxies={}
        ip = q.get()
        proxies['http'] = str(ip)
        headers = headerss()
        try:
            url = 'http://www.baidu.com'
            req2 = requests.get(url=url, proxies=proxies, headers=headers, timeout=5)
            if '百度一下，你就知道' in req2.content.decode():
                print('访问网址：{} 代理IP：{} 访问成功'.format(url,ip))
                with open('result_ip.txt','a+')as a:
                    a.write(ip+'\n')
        except Exception as e:
            pass

if __name__ == '__main__':
    try:
        os.remove('result.txt')
    except:
        pass
    print('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      
                               |___/       
                                           
                            批量获取代理IP
                            自动保存到文本
                            2019-3-22-21-30
            
    ''')
    time.sleep(3)
    threading.Thread(target=get_ip,args=(200,)).start()
    for i in range(10):
        threading.Thread(target=scan_ip).start()

