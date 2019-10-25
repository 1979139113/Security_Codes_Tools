# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun

# coding:utf-8
from string import whitespace
import urllib
import requests
requests.packages.urllib3.disable_warnings()
import re
from urllib.parse import urlparse,urlencode,parse_qs,parse_qsl,quote_plus
from urllib.request import urlopen
import mechanize
import http.client
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import random
import sys
import os
import time
from docx import Document
from docx.shared import Pt
from docx.shared import RGBColor
from docx.oxml.ns import qn
from docx.shared import Inches
import multiprocessing
import re
import random
import requests
from concurrent.futures import ProcessPoolExecutor
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab
# 输入屏幕左上角和右下角的坐标
from urllib.parse import urlparse
import contextlib
import configparser
import pymysql
import datetime
import requests
import time
import aiohttp
import aiofiles
import aiomultiprocess
import multiprocessing
import asyncio
import re
import time
import asyncio
import aiohttp
import aiomultiprocess
import aiofiles
import multiprocessing





cfg = configparser.ConfigParser()
cfg.read('../Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server", "db")
port = int(cfg.get("Server", "port"))

thread_s = int(cfg.get("Common_Config", "threads"))



@contextlib.contextmanager
def connect_mysql():
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
    cursor = coon.cursor()
    try:
        yield cursor
    except Exception as e:
        print(e)
        pass
    finally:
        coon.commit()
        cursor.close()
        coon.close()


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

def writedata(x):
    with open('log.txt', 'a+')as aa:
        aa.write('***********************************' + '\n')
        aa.write(str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + str(x) + '\n')


class Get_Info:
    def __init__(self,url):
        self.url=url
        self.title_parrten = 'class="w61-0"><div class="ball">(.*?)</div></td>'  # group(1) 正常
        self.ip_parrten = '>IP：(.*?)</a></div>'  # group(1) 正常
        self.ages = '" target="_blank">(.*?)</a></div></div>'  # group(1)
        self.whois_id = '备案号：</span><a href=.*?" target="_blank">(.*?)</a></div>'  # 需group(1)
        self.whois_type = '<span>性质：</span><strong>(.*?)</strong></div>'  # 需group(1)
        self.whois_name = '<span>名称：</span><strong>(.*?)</strong></div>'  # 需group(1)
        self.whois_time = '<span>审核时间：</span><strong>(.*?)</strong></div>'  # 需group(1)
        self.include_baidu = '<div class="Ma01LiRow w12-1 ">(.*?)</div>'  # group(1)
        self.infos = '<div class="MaLi03Row w180">(.*?)</div>'  # 要findall 0，1，2，3
        self.result={'百度权重':'',
                    '网站主页':'',
                     '网站描述':'',
                   '网站标题':'',
                   'IP__坐标':'',
                   '所属__IP':'',
                   '网站年龄':'',
                   '备案编号':'',
                   '备案性质':'',
                   '备案名称':'',
                   '备案时间':'',
                   '百度收录':'',
                   '协议类型':'',
                   '页面类型':'',
                   '服务类型':'',
                   '程序语言':''}

    def get_baidu_weight(self):
        time.sleep(random.randint(1, 5))
        x = str(random.randint(1, 9))
        data = {
            't': 'rankall',
            'on': 1,
            'type': 'baidupc',
            'callback': 'jQuery111303146901980779846_154444474116%s' % (x),
            'host': self.url
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
            urls = 'http://rank.chinaz.com/ajaxseo.aspx?t=rankall&on=1&type=undefined&callback=jQuery111303146901980779846_154444474116%s' % (
                x)

            r = requests.post(url=urls, headers=headers, data=data)
            try:
                res = re.search(b',"br":(\d),"beforBr', r.content).group(1)
            except:
                pass
            if res:
                return res.decode()
            else:
                return '0'
        except:
            return '获取失败'


    def get_info_from_pattren(self,pattren, result):
        try:
            res = re.search(pattren, result).group(1)
            return res
        # return str(res.encode('utf-8'))
        except:
            return '暂无信息'

    def scan_seo(self):
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        domain_url = self.url.replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0]
        urls = 'http://seo.chinaz.com/' + domain_url
        # url,title,weights,ip,ages,whois_id,whois_type,whois_name,whois_time
        # 网址，标题，百度权重，ip信息，年龄，备案号，备案性质，备案名称，备案时间
        # include_baidu,request,text,service,language
        # 百度收录，，协议类型，页面类型，服务器类型，程序语言
        try:
            req = requests.get(urls, headers, verify=False, timeout=20)
            encoding = requests.utils.get_encodings_from_content(req.text)[0]
            r = req.content.decode(encoding, 'replace')
        except Exception as e:
            writedata(str(e))

        try:
            req = requests.get(self.url, headers, verify=False, timeout=20)
            encoding = requests.utils.get_encodings_from_content(req.text)[0]
            rss = req.content.decode(encoding, 'replace')
        except Exception as e:
            writedata(str(e))


        self.result['网站描述'] = '暂无信息'
        try:
            description = re.search('description.*?content=(.*?)>',rss,re.S).group(1)
            self.result['网站描述'] = description.strip()
        except:
            pass

        self.result['百度权重'] = str(self.get_baidu_weight())

        self.result['网站主页'] = self.url.split('//')[0] + '//' + self.url.split('//')[1].split('/')[0]

        try:
            req1 = requests.get(url=self.url, headers=headers, verify=False, timeout=10)
            encoding = requests.utils.get_encodings_from_content(req1.text)[0]
            rress = req1.content.decode(encoding, 'replace')
            title_pattern = '<title>(.*?)</title>'
            title = re.search(title_pattern, rress, re.S | re.I)
            self.result['网站标题'] = str(title.group(1))
        except:
            self.result['网站标题'] = self.url.split('//')[0] + '//' + self.url.split('//')[1].split('/')[0]


        ip_infos = self.get_info_from_pattren(self.ip_parrten, r)
        if '[' in ip_infos:
            ip, address = ip_infos.split('[')[0], ip_infos.split('[')[1]
            self.result['IP__坐标'] = address.replace(']', '')
            self.result['所属__IP'] = ip
        else:
            self.result['IP__坐标'] = '获取失败'
            self.result['所属__IP'] = '获取失败'

        self.result['网站年龄'] = self.get_info_from_pattren(self.ages, r)
        self.result['备案编号'] = self.get_info_from_pattren(self.whois_id, r)
        self.result['备案性质'] = self.get_info_from_pattren(self.whois_type, r)
        self.result['备案名称'] = self.get_info_from_pattren(self.whois_name, r)
        self.result['备案时间'] = self.get_info_from_pattren(self.whois_time, r)
        self.result['百度收录'] = self.get_info_from_pattren(self.include_baidu, r)

        dd = re.findall(self.infos, r, re.S)
        resu = ['暂无信息' if x.replace(' ', '') is '' else x for x in dd]
        try:
            self.result['协议类型'] = resu[0]
        except:
            self.result['协议类型'] = '获取失败'

        try:
            self.result['页面类型'] = resu[1]
        except:
            self.result['页面类型'] = '获取失败'

        try:
            self.result['服务类型'] = resu[2]
        except:
            self.result['服务类型'] = '获取失败'

        try:
            self.result['程序语言'] = resu[3]
        except:
            self.result['程序语言'] = '获取失败'
        return self.result

def Get_Title(url):
    title = '获取失败'
    try:
        r = requests.get(url)
        titles = re.search(b'<title>(.*?)</title>',r.content,re.S).group(1)
        title = titles.decode()
    except:
        pass
    finally:
        return title

def Get_Resp_EN(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    try:
        r = requests.get(url,headers=headers,timeout=20,verify=False)
        return r.content
    except:
        return None



def Get_Resp_CN(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    }
    try:
        r = requests.get(url,headers=headers,timeout=20,verify=False)
        encoding = requests.utils.get_encodings_from_content(r.text)[0]
        res = r.content.decode(encoding,'replace')
        return res
    except:
        return None


back_lists = ['/404/search_children.js',"访问的页面不存在",'当前页面不存在或已删除','qzone.qq.com/gy/404/data.js','404 Not Found','<p>The server encountered an internal error or','http://www.qq.com/babygohome/?pgv_ref=404','<h1>410 Gone</h1>','<title>404 Page Not Found</title>','You do not have permission to get URL','<title>403 Forbidden</title>','<h1>Whoops, looks like something went wrong.</h1>','invalid service url:','have permission to access this page','No direct script access allowed','args not correct','Controller Not Found','url error','Bad Request','http://appmedia.qq.com/media/flcdn/404.png']
white_lists = ['<title>Index of','<title>phpMyAdmin</title>','allow_url_fopen','MemAdmin','This is the default start page for the Resin server','Apache Tomcat','request_uri','<title>Login to Cacti</title>','<title>Zabbix</title>','Dashboard [Jenkins]','Graphite Browser','http://www.atlassian.com/software/jira','Internal Server Error','Fatal error','Exception caught','Incorrect syntax','You have an error in your SQL syntax','</b> on line <b>','The proxy server could not handle the request']
file_dict = {'/WEB-INF/classes/conf/datasource.xml': '<?xml', '/editor/ckeditor/samples/': '<title>CKEditor Samples</title>', '/WEB-INF/applicationContext.xml': '<?xml', '/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd': 'root:x:', '/.ssh/id_dsa': 'PRIVATE KEY-', '/aa/../../cc/../../bb/../../dd/../../aa/../../cc/../../bb/../../dd/../../bb/../../dd/../../bb/../../dd/../../bb/../../dd/../../ee/../../etc/profile': '/etc/profile.d/*.sh', '/configs/application.ini': '[', '/ckeditor/samples/sample_posteddata.php': 'http://ckeditor.com</a>', '/login.php': 'type="password"', '/settings.ini': '[', '/WEB-INF/classes/hibernate.cfg.xml': '<?xml', '/ueditor/ueditor.config.js': 'window.UEDITOR_HOME_URL', '/id_rsa': 'PRIVATE KEY-', '/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd': 'root:x:', '/WEB-INF/config/dbconfig': 'passw', '/.idea/workspace.xml': '<project version=', '/.database.php.swp': '<?php', '/configprops': 'serverProperties', '/sftp-config.json\t': 'password', '//././././././././././././././././././././././././../../../../../../../../etc/profile': '/etc/profile.d/*.sh', '#': 'text string to find', '/fck/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php': 'init_spell()', '/WEB-INF/applicationContext-slave.xml': '<?xml', '/solr/': '<title>Solr Admin</title>', '/etc/profile': '/etc/profile.d/*.sh', '/..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd': 'root:x:', '/WEB-INF/spring.xml': '<?xml', '/jenkins/script\t\t{status=200}': 'Type in an arbitrary', '/.config.php.swp': '<?php', '/static/f3a41d2f/css/style.css': 'jenkins-home-link', '/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellcheckder.php': 'init_spell()', '/configuration.ini': '[', '/application.ini': '[', '/_phpmyadmin/index.php': '<title>phpMyAdmin', '/php.ini': '[', '/config/.config.php.swp': '<?php', '/id_dsa': 'PRIVATE KEY-', '/config/config.ini': '[', '/WEB-INF/dwr.xml': '<?xml', '/conf.ini': '[', '/apc.php': '<title>APC INFO', '/etc/passwd': 'root:x:', '/../../../../../../../../../../../../../etc/passwd': 'root:x:', '/server-status': '<title>Apache Status</title>', '/examples/servlets/servlet/SessionExample': '<title>Sessions Example</title>', '/.ssh/id_rsa': 'PRIVATE KEY-', '/WEB-INF/classes/data.xml': '<?xml', '/application/configs/application.ini': '[', '/config/database.yml': 'password', '/.ssh/authorized_keys': 'ssh-rsa', '/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd': 'root:x:', '/cacti/': '<title>Login to Cacti</title>', '/WEB-INF/conf/activemq.xml': '<?xml', '/ckeditor/samples/': '<title>CKEditor Samples</title>', '/WEB-INF/struts/struts-config.xml': '<?xml', '/app.ini': '[', '/.settings.php.swp': '<?php', '/memadmin/index.php': '<title>Login - MemAdmin', '/editor/ckeditor/samples/sample_posteddata.php': 'http://ckeditor.com</a>', '/db.ini': '[', '/WEB-INF/spring-cfg/applicationContext.xml': '<?xml', '/WEB-INF/classes/conf/spring/applicationContext-datasource.xml': '<?xml', '/jmx-console/HtmlAdaptor': 'JBoss Management Console', '/.config.inc.php.swp': '<?php', '/.ssh/id_rsa.pub': 'ssh-rsa', '/index.php.bak': '<?php', '/WEB-INF/classes/applicationContext.xml': '<?xml', '/upload.do': 'type="file"', '/core': 'ELF', '/info.php': 'allow_url_fopen', '/resin-admin/\t': '<title>Resin Admin Login for', '/proc/meminfo': 'MemTotal', '/resin-doc/viewfile/?contextpath=/&servletpath=&file=index.jsp': 'This is the default start page for the Resin server', '/WEB-INF/struts-config.xml': '<?xml', '/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/profile': '/etc/profile.d/*.sh', '/server.xml': '<?xml', '/../../../../../../../../../../../../../etc/profile': '/etc/profile.d/*.sh', '/WEB-INF/struts-front-config.xml': '<?xml', '/WEB-INF/classes/config/applicationContext.xml': '<?xml', '/WEB-INF/config.xml': '<?xml', '/WEB-INF/classes/struts_manager.xml': '<?xml', '/upload.html': 'type="file"', '/script\t\t': 'Type in an arbitrary', '/config.ini': '[', '/phpinfo.php': 'allow_url_fopen', '/conf/config.ini': '[', '/WEB-INF/config/db/dataSource.xml': '<?xml', '/.svn/entries': '-props', '/ganglia/': '<title>Ganglia', '/crossdomain.xml': '<allow-access-from domain="*"', '/.mysql.php.swp': '<?php', '/ueditor/php/getRemoteImage.php': "'tip':'", '/file:///etc/passwd': 'root:x:', '/fckeditor/_samples/default.html': '<title>FCKeditor', '/WEB-INF/web.xml': '<?xml', '/examples/': '<TITLE>Apache Tomcat Examples</TITLE>', '/.git/index': 'DIRC', '/.git/config': '[core]', '/../{hostname_or_folder}.ini': '[', '/{hostname_or_folder}.ini': '[', '/zabbix/': '<title>Zabbix</title>', '/pi.php': 'allow_url_fopen', '/phpmyadmin/index.php': '<title>phpMyAdmin', '/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/profile': '/etc/profile.d/*.sh', '/.ssh/id_dsa.pub': 'ssh-dss', '/upload.php': 'type="file"', '/upfile.php': 'type="file"', '/WEB-INF/web.xml.bak': '<?xml', '/.db.php.swp': '<?php', '/.index.php.swp': '<?php', '/WEB-INF/classes/struts.xml': '<?xml', '/config.inc.php.bak': '<?php', '/exit': '<title>POST required</title>', '/upload.jsp': 'type="file"', '/.idea/modules.xml': 'ProjectModuleManager', '/login.do': 'type="password"', '/pma/index.php': '<title>phpMyAdmin', '/WEB-INF/classes/rabbitmq.xml': '<?xml', '/.git/HEAD\t': 'refs/heads/', '/phpMyAdmin/index.php': '<title>phpMyAdmin', '/WEB-INF/classes/spring.xml': '<?xml', '/jenkins/static/f3a41d2f/css/style.css\t': 'jenkins-home-link'}


def Start_Scan(url):
    print('Check : {}'.format(url))
    print('开始存活检测........')
    check_alive = Get_Resp_EN(url)
    if check_alive == None:
        time.sleep(random.randint(5,10))
        check_alive = Get_Resp_EN(url)
        if check_alive == None:
            with connect_mysql() as coon:
                print('网址无法访问，保存到相对表中....')
                sql1 = 'insert into Sec_Fail_Links(url) values ("{}")'.format(url)
                coon.execute(sql1)
            return None

    domain = urlparse(url).netloc
    try:
        filename = url.split('//')[1].split('/')[0].replace(':', '_').replace('/', '_') + '__敏感目录文件报表.html'
    except:
        pass
    try:
        filename = domain.replace(':', '_').replace('/', '_') + '__敏感目录文件报表.html'
    except:
        pass
    finally:
        filename = filename.replace('__', '_' + str(random.randint(1, 2000)) + '_')
        filename = '../result/' + filename

    print('开始扫描敏感目录信息')

