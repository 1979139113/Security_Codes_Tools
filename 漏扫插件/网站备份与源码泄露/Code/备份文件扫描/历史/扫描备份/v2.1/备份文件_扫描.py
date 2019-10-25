# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 0008 10:56
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 备份文件_扫描.py
# @Software: PyCharm
import sys
import requests
import re,time
import os
import random
from multiprocessing.dummy import Pool as ThreadPool
import threading
reload(sys)
sys.setdefaultencoding('utf-8')

backup_name_A = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt','.tar.gz','.iso','.gz']
#要和域名组合在一起拼接的后缀
# backup_name_B = ['/a.zip','/web.zip','/web.rar','/1.rar','/bbs.rar','/www.root.rar','/123.rar','/data.rar','/bak.rar','/oa.rar','/admin.rar','/www.rar','/2014.rar','/2015.rar','/2016.rar','/2014.zip','/2015.zip','/2016.zip','/2017.zip','/1.zip','/1.gz','/1.tar.gz','/2.zip','/2.rar','/123.rar','/123.zip','/a.rar','/a.zip','/admin.rar','/back.rar','/backup.rar','/bak.rar','/bbs.rar','/bbs.zip','/beifen.rar','/beifen.zip','/beian.rar','/data.rar','/data.zip','/db.rar','/db.zip','/flashfxp.rar','/flashfxp.zip','/fdsa.rar','/ftp.rar','/gg.rar','/hdocs.rar','/hdocs.zip','/HYTop.mdb','/root.rar','/Release.rar','/Release.zip','/sql.rar','/test.rar','/template.rar','/template.zip','/upfile.rar','/vip.rar','/wangzhan.rar','/wangzhan.zip','/web.rar','/web.zip','/website.rar','/www.rar','/www.zip','/wwwroot.rar','/wwwroot.zip','/wz.rar']
#常见的后缀
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
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24" ]
# headers
list_url = list(set([x.replace('\n','') if x.startswith('http')  else 'http://'+x.replace('\n','') for x in open('url.txt','r').readlines()]))
backup_name_B = list(set([x.replace('\n','')  for x in open('rar.txt','r').readlines()]))
# 把文件导入
result_name = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())).replace(' ','')
os.system('color a')
print ('''

         _                           _ 
        | |                         (_)
        | |     __ _ _ __   __ _ _____ 
        | |    / _` | '_ \ / _` |_  / |
        | |___| (_| | | | | (_| |/ /| |
        |______\__,_|_| |_|\__, /___|_|
                            __/ |      
                           |___/       Version:2.1

''')
time.sleep(3)

with open(str(result_name)+'.html','a+')as a:
    a.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Lang_BackUp_备份文件扫描2.1</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap-theme.css">
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.css">
    </head>
    <body>
    <div class="container">
    <div class="navbar navbar-default">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">LangZi</a>
    </div>
    <DIV class="nav navbar-nav navbar-right">
        <div class="navbar-header">
        <a class="navbar-brand" href="http://www.langzi.fun:9827">看妹子</a>
    </div> 
    </DIV>
        </div>
    </div>
    <div class="container">

    ''')

def start(func):
    def inter(url_backup):
        result = func(url_backup)
        if result == []:
            pass
        else:
            print (unicode(('【该网站存在备份文件泄露:%s】 : ' + url_backup) % threading.current_thread().name, 'utf-8'))
            with open(str(result_name)+'.html','a+')as a:
                for _ in result:
                    a.write('<div class="col-md-10 font-weight-bold"><br>')
                    a.write(str(_.decode('utf-8')))
                    a.write('</div><br>')
        return result
    return inter


@start
def scan(url):
    list_result=[]
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        web_title = '获取网站标题失败'
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info_top = requests.get(url=url, headers=headers, timeout=5)
        if r_info_top.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'GB2312':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'gb2312':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'GBK':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'gbk':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        else:
            web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                '</title>', '')
    except:
        try:
            web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                '</title>', '')
        except:
            web_title = '暂时无法获取网站标题'
            
    # 开始扫描
    url_svn = url + '/.svn/entries'
    # print 'Cheaking>>>' + url_svn
    # 扫描svn源码泄露  组合成链接
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_svn = requests.head(url=url_svn, headers=headers, timeout=5)
        # 访问这个链接  超时设置5秒
        # print r_svn.url + " : " + str(r_svn.status_code)
        # 打印出这个网址 和 访问状态码
        print (str(threading.current_thread().name) + ' ' + str(url_svn) + '  ' + str(r_svn.status_code))
        if r_svn.status_code == 200:
            # 如果状态码是200  表示访问成功
            try:
                r_svn_1 = requests.get(url=url_svn, headers=headers, timeout=5)
                if 'dir' in r_svn_1.content and 'svn://' in r_svn_1.content:
                    list_result.append(str(r_svn_1.url + '  ' + str('SVN源码泄露') + '  ' + str(web_title)))
            except Exception as e:
                print e
                pass
        else:
            pass
    except Exception as e:
        pass

        # print e
        ######################################
        # svn源码泄露扫描完毕
        ######################################
    url_git = url + '/.git/config'
    # print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        # print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(url_git) + '  ' + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'repositoryformatversion' in r_git_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    list_result.append(str(r_git_1.url + '  ' + str('GIT源码泄露') + '  ' + str(web_title)))
                else:
                    pass
            except Exception as e:
                print e
                pass
    except Exception as e:
        print e
        pass
        ######################################
        # git源码泄露扫描完毕
        ######################################
    url_git = url + '/.git/index'
    # print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        # print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(url_git) + '  ' + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'DIRC' in r_git_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    list_result.append(str(r_git_1.url + '  ' + str('GIT源码泄露') + '  ' + str(web_title)))
                else:
                    pass
            except Exception as e:
                print e
                pass
    except Exception as e:
        print e
        pass
    url_git = url + '/.git/HEAD'
    # print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        # print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(url_git) + '  ' + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'refs/heads/' in r_git_1.content:
                    list_result.append(str(r_git_1.url + '  ' + str('GIT源码泄露') + '  ' + str(web_title)))
                else:
                    pass
            except Exception as e:
                print e
                pass
    except Exception as e:
        # print e
        pass
    url_info = url + '/WEB-INF/web.xml'
    # print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info = requests.head(url=url_info, headers=headers, timeout=5)
        # print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(r_info.url) + '  ' + str(r_info.status_code)
        if r_info.status_code == 200:
            try:
                r_info_1 = requests.get(url=url_info, headers=headers, timeout=5)
                if '<web-app' in r_info_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    list_result.append(str(r_info_1.url + '  ' + str('WEBinfo信息泄露') + '  ' + str(web_title)))
                else:
                    pass
            except Exception as e:
                print e
                pass
    except Exception as e:
        print e
        pass
        ######################################
        # webinfo源码泄露扫描完毕
        ######################################

    url_domain = url + '/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            print e
            ######################################
            # 域名加常见后缀组合扫描完毕-+-+-+-+-9
            ######################################
    url_domain_0 = url + '/' + url.split('//', 2)[1]
    # http://www.baidu.com/www.baidu.com

    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_0 = requests.head(url=str(url_domain_0 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_0.url) + '  ' + str(
                r_domain_0.status_code)
            if r_domain_0.status_code == 200:
                try:
                    if int(r_domain_0.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_0.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_0.url) + '    ' + str(rar_size) + '   ' +str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_1 = url + '/' + str(url.split('//', 2)[1]).replace('.', '').replace('/', '')
    # http://www.baidu.com/wwwbaiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_1 = requests.head(url=str(url_domain_1 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_1.url) + '  ' + str(
                r_domain_1.status_code)
            if r_domain_1.status_code == 200:
                try:
                    if int(r_domain_1.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_1.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_1.url) + '    ' + str(rar_size) + '   ' +str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_3 = url + '/' + url.split('.', 1)[1].replace('/', '')
    # http://www.baidu.com/baidu.com
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_3 = requests.head(url=str(url_domain_3 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_3.url) + '  ' + str(
                r_domain_3.status_code)
            if r_domain_3.status_code == 200:
                try:
                    if int(r_domain_3.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_3.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_3.url) + '    ' + str(rar_size) + '   ' +str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_2 = url + '/' + url.split('.', 1)[1].replace('.', '').replace('/', '')
    # http://www.baidu.com/baiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_2 = requests.head(url=str(url_domain_2 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_2.url) + '  ' + str(
                r_domain_2.status_code)
            if r_domain_2.status_code == 200:
                try:
                    if int(r_domain_2.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_2.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_2.url) + '    ' + str(rar_size) + '   ' +str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_4 = url + '/' + str(url.split(".", 2)[1]) + '2016'
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_4 = requests.head(url=str(url_domain_4 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_4.url) + '  ' + str(
                r_domain_4.status_code)
            if r_domain_4.status_code == 200:
                try:
                    if int(r_domain_4.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_4.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_4.url) + '    ' + str(rar_size) + '   ' +str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_5 = url + '/' + str(url.split(".", 2)[1]) + '2017'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(
                r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_5.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            pass
            print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_5 = url + '/' + str(url.split(".", 2)[1]) + '2018'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(
                r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_5.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    print e
            else:
                pass
        except Exception as e:
            print e
            pass
    url_domain_5 = url + '/' + url.replace('.com', '').replace('.cn', '').replace('.org', '').replace('.net',
                                                                                                      '').replace(
        '.org', '')
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(
                r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_5.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
    url_domain_8 = url + '/' + str(url.replace('www.', ''))
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_8 = requests.head(url=str(url_domain_8 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_8.url) + '  ' + str(
                r_domain_8.status_code)
            if r_domain_8.status_code == 200:
                try:
                    if int(r_domain_8.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_8.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_8.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
    url_domain_6 = url + '/' + str(url.split(".", 2)[1]) + '2015'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_6 = requests.head(url=str(url_domain_6 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_6.url) + '  ' + str(
                r_domain_6.status_code)
            if r_domain_6.status_code == 200:
                try:
                    if int(r_domain_6.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_6.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_6.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    for back_B in backup_name_B:
        url_rar = url + back_B
        # http://www.baidu.com/root.rar
        # print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            # print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_rar.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ##################zhaohanloveyou
    url_domain = url + '/data/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
    url_domain = url + '/www/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
    for back_B in backup_name_B:
        url_rar = url + '/www' + back_B
        # http://www.baidu.com/root.rar
        # print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            # print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_rar.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
        except:
            pass
    for back_B in backup_name_B:
        url_rar = url + '/data' + back_B
        # http://www.baidu.com/root.rar
        # print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            # print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_rar.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
        except:
            pass
    url_domain = url + '/backup/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕-+-+-+-+-9
            ######################################
    url_domain_0 = url + '/backup/' + url.split('//', 2)[1]
    # http://www.baidu.com/www.baidu.com
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_0 = requests.head(url=str(url_domain_0 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_0.url) + '  ' + str(
                r_domain_0.status_code)
            if r_domain_0.status_code == 200:
                try:
                    if int(r_domain_0.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_0.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_0.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_1 = url + '/backup/' + str(url.split('//', 2)[1]).replace('.', '').replace('/', '')
    # http://www.baidu.com/wwwbaiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_1 = requests.head(url=str(url_domain_1 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_1.url) + '  ' + str(
                r_domain_1.status_code)
            if r_domain_1.status_code == 200:
                try:
                    if int(r_domain_1.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_1.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_1.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_3 = url + '/backup/' + url.split('.', 1)[1].replace('/', '')
    # http://www.baidu.com/baidu.com
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_3 = requests.head(url=str(url_domain_3 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_3.url) + '  ' + str(
                r_domain_3.status_code)
            if r_domain_3.status_code == 200:
                try:
                    if int(r_domain_3.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_3.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_3.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_2 = url + '/backup/' + url.split('.', 1)[1].replace('.', '').replace('/', '')
    # http://www.baidu.com/baiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_2 = requests.head(url=str(url_domain_2 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_2.url) + '  ' + str(
                r_domain_2.status_code)
            if r_domain_2.status_code == 200:
                try:
                    if int(r_domain_2.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_2.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_2.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_4 = url + '/backup/' + str(url.split(".", 2)[1]) + '2016'
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_4 = requests.head(url=str(url_domain_4 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_4.url) + '  ' + str(
                r_domain_4.status_code)
            if r_domain_4.status_code == 200:
                try:
                    if int(r_domain_4.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_4.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_4.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_5 = url + '/backup/' + str(url.split(".", 2)[1]) + '2017'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(
                r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_5.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_6 = url + '/backup/' + str(url.split(".", 2)[1]) + '2015'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_6 = requests.head(url=str(url_domain_6 + back_A), headers=headers, timeout=5)
            # print 'Cheaking>>>' + r_domain.url
            # print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_6.url) + '  ' + str(
                r_domain_6.status_code)
            if r_domain_6.status_code == 200:
                try:
                    if int(r_domain_6.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_6.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_domain_6.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
            # print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    for back_B in backup_name_B:
        url_rar = url + '/backup' + back_B
        # http://www.baidu.com/root.rar
        # print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            # print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        list_result.append(str(r_rar.url) + '    ' + str(rar_size) + '   ' + str(web_title))
                    else:
                        pass
                except Exception as e:
                    pass
                    # print e
            else:
                pass
        except Exception as e:
            pass
    return list_result

    


smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
pool = ThreadPool(processes=smxc)  #线程数量
result = pool.map(scan, list_url)
pool.close()
pool.join()

os.system('pause')