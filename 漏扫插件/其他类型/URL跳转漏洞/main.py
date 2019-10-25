# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun

from urllib.parse import urlparse,parse_qs,parse_qsl,urlencode,urljoin
import copy
import requests
payloads = ['http://www.langzi.fun',
            '//www.langzi.fun',
            '\\\www.langzi.fun',
            '.langzi.fun',
            '@www.langzi.fun',
            'http://118.24.11.235',
            '118.24.11.235',
            '///www.langzi.fun//..'
            '{}@www.langzi.fun',
            '{}?www.langzi.fun',
            '{}#www.langzi.fun',
            '{}\\\www.langzi.fun',]


def scan_get(url,headers):
    print(url)
    try:
        r = requests.get(url,headers=headers,timeout=10,verify=False)
        if b'Never Setter' in r.content:
            print('存在URL跳转漏洞！！！')
            return 'GET:'+url
    except Exception as e:
        print(e)
def scan_post(url,data,headers):
    print(url,str(data))
    try:
        r = requests.post(url,data=data,headers=headers,timeout=10,verify=False)
        if b'Never Setter' in r.content:
            print('存在URL跳转漏洞！！！')
            return 'POST:'+url+str(urlencode(data))
    except Exception as e:
        print(e)

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
                dix = scan_get(path+'?' + urlencode(paramvlues),headers)
                if dix:
                    return dix
                dix = scan_post(path,paramvlues,headers)
                if dix:
                    return dix

    except Exception as e:
        print(e)


url = 'http://127.0.0.1/pik/vul/urlredirect/urlredirect.php?url=i&id=1'
print(Get_Paylpad(url))