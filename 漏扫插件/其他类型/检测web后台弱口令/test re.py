# -*- coding:utf-8 -*-
import re
import requests


url = 'http://www.jsamzs.com/newsssd.php?nid=215'
#url = 'http://www.kjxc.cc/'
r = requests.get(url).content

res = re.search(b'<title>(.*?)</title>', r, re.I | re.S).group(1)
print(res.decode())
# _url = '//wmw.dbw.cn/system/2012/04/06/000491494.shtml'
# pat = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt)', str(_url))
# print(pat)
#
# domain = 'http://wmw.dbw.cn/'
# print(domain.split('//')[1].strip('/').replace('www.', ''))