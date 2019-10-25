# -*- coding:utf-8 -*-
import re
import requests
import random
import time
from bs4 import BeautifulSoup
def writedata(x):
    with open('log.txt', 'a+')as aa:
        aa.write('-------------------------------------' + '\n')
        aa.write(str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + x + '\n')


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


def get_links(url):
    '''
    需要的有常规的注入点
        1. category.php?id=17
        2. https://www.yamibuy.com/cn/brand.php?id=566
    伪静态
        1. info/1024/4857.htm
        2. http://news.hnu.edu.cn/zhyw/2017-11-11/19605.html
    :param url:
    :return:
    '''
    if 'gov.cn' in url or 'edu.cn' in url:
        return 0
    domain = url.split('//')[1].strip('/').replace('www.', '')
    result = []
    id_links = []
    html_links = []
    result_links = {}
    html_links_s = []
    result_links['title'] = '网址标题获取失败'
    idid = []
    htht = []
    try:
        headers = {
            'User-Agent': random.choice(headerss),
            'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        }
        rxww = requests.get(url, headers=headers,verify=False, timeout=10).content
        soup = BeautifulSoup(rxww, 'html.parser')
        try:
            result_links['title'] = soup.title.text
        except Exception as e:
            writedata('[WARNING ERROR]' + str(e))
            try:
                result_links['title'] = re.search('<title>(.*?)</title>', rxww, re.I | re.S).group(1)
            except Exception as e:
                writedata('[WARNING ERROR]' + str(e))
                pass
        if result_links['title'] == '' or result_links['title'] == None:
            result_links['title'] = '网址标题获取失败'
        links = soup.findAll('a')
        for link in links:
            _url = link.get('href')
            res = re.search('(javascript|:;|#)', str(_url))
            res1 = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt)', str(_url))
            if res == None and res1 == None:
                result.append(str(_url))
            else:
                pass

        print('---------')
        print(result)
        time.sleep(10)


        if result != []:
            rst = list(set(result))
            for rurl in rst:
                if '//' in rurl and 'http' in rurl:
                    # https://www.yamibuy.com/cn/search.php?tags=163
                    # http://news.hnu.edu.cn/zhyw/2017-11-11/19605.html
                    if domain in rurl:
                        if '?' in rurl and '=' in rurl:
                            # result_links.append(rurl)
                            id_links.append(rurl)
                        if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                            if '?' not in rurl:
                                # result_links.append(rurl)
                                html_links.append(rurl)
                # //wmw.dbw.cn/system/2018/09/25/001298805.shtml
                elif 'http' not in rurl and domain in rurl:
                    if '?' in rurl and '=' in rurl:
                        id_links.append('http://' + rurl.lstrip('/'))
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        if '?' not in rurl:
                            html_links.append('http://' + rurl.lstrip('/'))

                else:
                    # search.php?tags=163
                    if '?' in rurl and '=' in rurl:
                        # result_links.append(url + '/' + rurl)
                        id_links.append(url + '/' + rurl)
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        # result_links.append(url + '/' + rurl)
                        if '?' not in rurl:
                            html_links.append(url + '/' + rurl)

            for x1 in html_links:
                try:
                    rx1 = requests.head(url=x1, headers=headers,verify=False, timeout=15).status_code
                    if rx1 == 200:
                        htht.append(x1)
                except Exception as e:
                    writedata('[WARNING ERROR]' + str(e))
                    pass
            for x2 in id_links:
                try:
                    rx2 = requests.head(url=x2, headers=headers, verify=False, timeout=15).status_code
                    if rx2 == 200:
                        idid.append(x2)
                except Exception as e:
                    writedata('[WARNING ERROR]' + str(e))
                    pass

            if htht == []:
                pass
            else:
                for x in htht:
                    if x.count('/') > 3:
                        ra = re.search('.*?/[0-9]\.', x)
                        if ra == None:
                            pass
                        else:
                            html_links_s.append(x)
                        if html_links_s == []:
                            html_links_s.append(random.choice(htht))

                if html_links_s == []:
                    result_links['html_links'] = random.choice(htht)
                else:
                    result_links['html_links'] = random.choice(html_links_s)

            if idid == []:
                pass
            else:
                result_links['id_links'] = random.choice(idid)
        if result_links == {}:
            return None
        else:
            return result_links

    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    return None

print(get_links('http://house.njhouse.com.cn/company/xylist/'))