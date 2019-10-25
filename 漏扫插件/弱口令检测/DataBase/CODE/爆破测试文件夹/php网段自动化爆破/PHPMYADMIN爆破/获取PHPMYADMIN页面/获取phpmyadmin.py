# -*- coding:utf-8 -*-

#__author__:langzi
#__blog__:www.langzi.fun

import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def run(url):
    try:
        r = requests.get(url,timeout=20)
        print('{} : {}'.format(r.url,r.status_code))
        if b'Documentation.html' in r.content:
            print('网址:{} 发现PHPMYADMIN后台地址'.format(url))
            with open('urls.txt', 'a+')as a:
                a.write(r.url + '\n')
    except:
        pass

if __name__ == '__main__':
    urls = [x.strip() + '/phpmyadmin/index.php' for x in open('all_url.txt', 'r').readlines()]
    with ThreadPoolExecutor(100)as p:
        p.map(run,urls)