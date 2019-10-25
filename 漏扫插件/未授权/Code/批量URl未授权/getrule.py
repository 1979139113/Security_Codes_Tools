# coding:utf-8
import base64
import random
import socket
import sys
import time
import urllib2
import multiprocessing
import requests
requests.packages.urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 3
socket.setdefaulttimeout(timeout)

#user_list = ['root', 'sa', 'system', 'Administrtor', 'ubuntu']
user_list = ['root', 'admin']

password_list = ['root', 'sa', 'admin', 'test', 'mysql', '123456', 'admin1234','admin12345', '000000', '987654321', '1234', '12345']

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


def get_url_vlun(url):
    print 'is running......waiting........'
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
        r8_0 = url + '/p.asp'
        r4_0_0 = url + '/aspcheck.asp'
        r_.append(r1)
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
                if 'upload_max_filesize' in rxr.content or 'SoftArtisans.FileManager' in rxr.content:
                    with open('result.txt', 'a+')as aaa:
                        aaa.write('服务器探针信息泄露:' + r_r + '\n')
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
            with open('result.txt', 'a+')as aaa:
                aaa.write('CouchDB未授权访问漏洞:' + rr.url.strip('/') + '\n')
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
                    with open('result.txt', 'a+')as aaa:
                        aaa.write('Jenkins未授权访问漏洞:' + rxr.url.strip('/') + '\n')
            except:
                pass
    except:
        pass

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        rrr = requests.get(url=str(url + '/servlets-examples/'), headers=headers, timeout=5)
        if 'servlet/RequestParamExample' in rrr.content:
            with open('result.txt', 'a+')as aaa:
                aaa.write('Tomcat example 应用信息泄漏漏洞:' + rrr.url.strip('/')+ '\n')
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
                    with open('result.txt', 'a+')as aaa:
                        aaa.write('Resin viewfile远程文件读取漏洞:' + r_r+ '\n')
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
                    with open('result.txt', 'a+')as aaa:
                        aaa.write('JBoss后台上传漏洞:' + r_r + '\n')
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
                            with open('result.txt', 'a+')as aaa:
                                aaa.write('Weblogic弱口令漏洞:' + r_r + ':' + uuser + '|' + ppass + '\n')
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
                                    with open('result.txt', 'a+')as aaa:
                                        aaa.write('Tomcat远程部署弱口令:' + r_r + ':' + uuser + '|' + ppass + '\n')
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
                                    with open('result.txt', 'a+')as aaa:
                                        aaa.write('Tomcat后台管理弱口令:' + r_r + ':' + uuser + '|' + ppass + '\n')
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
                            with open('result.txt', 'a+')as aaa:
                                aaa.write('Wordpress弱口令:' + url + login_path + ':' + uuser + '|' + ppass + '\n')
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
                                    with open('result.txt', 'a+')as aaa:
                                        aaa.write('PHPmyadmin弱口令:' + r_r + ':' + uuser + '|' + ppass+ '\n')
                            except:
                                pass
                else:
                    pass
            except:
                pass
    except:
        pass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print ('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_Unauthorized_Vlun_URL
                               |___/       Version:1.0
                                           Datetime:2018-11-22-15:11:36

    ''')
    print unicode('             URL未授权漏洞集成自动化识别', 'utf-8')


    New_start = raw_input(unicode('待需验证URL文本拖拽进来:', 'utf-8').encode('gbk'))
    smxc = int(input(unicode('设置线程池数量(2-128):', 'utf-8').encode('gbk')))
    list_ = list(set(
                [x.replace('\n', '') if x.startswith('http') else 'http://' + x.replace('\n', '') for x in
                 open(New_start, 'r').readlines()]))
    p = multiprocessing.Pool(smxc)
    for _ in list_:
        p.apply_async(get_url_vlun, args=(_,))
    p.close()
    p.join()

